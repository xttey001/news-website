import json
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Key ETF codes that need to be verified
CRITICAL = {
    '512880': '证券ETF',
    '512690': '酒ETF',
    '512800': '银行ETF',
    '512900': '证券ETF',
    '515220': '煤炭ETF',
    '561700': '电力ETF博时',
    '561360': '石油ETF',
    '159320': '电网ETF',
    '159755': '电池ETF',
    '516070': '易方达新能源ETF',
    '518880': '黄金ETF',
    '159985': '豆粕ETF',
    '512480': '半导体ETF',
    '512760': '芯片ETF',
    '515070': '人工智能AIETF',
    '515980': '人工智能ETF',
    '159819': '人工智能ETF易方达',
}

news_dir = 'news_data'
files = sorted([f for f in os.listdir(news_dir) if f.endswith('.json') 
                and '2026-03-25' <= f <= 'news_2026-04-11.json'])

print('=== ETF Reference Check (3.25-4.11) ===')
print()

issues = []
for fname in files:
    with open(os.path.join(news_dir, fname), encoding='utf-8') as f:
        d = json.load(f)
    date = d.get('date', fname)
    for key in ['s_level', 'a_level']:
        for item in d.get(key, []):
            if not isinstance(item, dict):
                continue
            for e in item.get('etfs', []):
                if not isinstance(e, dict):
                    continue
                name = e.get('name', '')
                codes = re.findall(r'\b(\d{6})\b', name)
                for code in codes:
                    if code in CRITICAL:
                        correct = CRITICAL[code]
                        if correct not in name:
                            issues.append(f'  [{date}][{key}] {name} -> should be: {code} {correct}')
                            print(f'  [!] [{date}] {name}')
                    else:
                        # Code not in critical list - might be fine or might be wrong
                        if code not in ['512880', '512690', '512800', '512900']:
                            pass  # skip non-critical

print()
print(f'Total potential issues with critical ETFs: {len(issues)}')

# Also check 512690 specifically
print()
print('=== 512690 context in all files ===')
for fname in sorted(os.listdir(news_dir)):
    if not fname.endswith('.json'):
        continue
    with open(os.path.join(news_dir, fname), encoding='utf-8') as f:
        d = json.load(f)
    for key in ['s_level', 'a_level']:
        for item in d.get(key, []):
            if not isinstance(item, dict):
                continue
            for e in item.get('etfs', []):
                if not isinstance(e, dict):
                    continue
                if '512690' in e.get('name', ''):
                    print(f'  [{fname}] {e.get("name")}')
                    title = item.get('title', '')[:50]
                    print(f'    News: {title}')

print()
print('=== insights.json ETF entries ===')
with open('insights.json', encoding='utf-8') as f:
    ins = json.load(f)
for ek in ins.get('etf_knowledge', []):
    print(f'  {ek["id"]}: {ek["wrong_code"]}/{ek["wrong_name"]} -> {ek["correct_code"]}/{ek["correct_name"]}')
print()
pats = [p for p in ins['patterns'] if 'ETF' in p.get('id','')]
print(f'ETF patterns: {[p["id"] for p in pats]}')

print()
print('=== etf_map.json ===')
with open('etf_map.json', encoding='utf-8') as f:
    mp = json.load(f)
print(f'Verified codes: {len(mp["verified"])}')
print(f'To verify: {len(mp["to_verify"])}')

# Check if key codes are correctly mapped
for code, expected_name in [('512880','证券ETF'), ('512690','酒ETF'), ('561700','电力ETF博时')]:
    if code in mp['verified']:
        print(f'  {code}: {mp["verified"][code]["name"]} (expected: {expected_name}) {"OK" if mp["verified"][code]["name"] == expected_name else "WRONG"}')
