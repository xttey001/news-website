import json
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

news_dir = 'news_data'
files = sorted([f for f in os.listdir(news_dir) if f.endswith('.json') 
                and '2026-03-25' <= f <= 'news_2026-04-11.json'])

# Codes we know are wrong (based on past errors)
wrong_codes = {
    '512880': {'wrong_names': ['银行ETF', '证券ETF'], 'correct': '国债ETF'},
    '512690': {'wrong_names': ['金融ETF'], 'correct': '能源ETF'},
    '159542': {'wrong_names': ['电网ETF'], 'correct': '电网ETF(159320)'},
    '159871': {'wrong_names': ['新能源电池ETF', '新能源ETF'], 'correct': '易方达新能源ETF(516070)'},
}

all_errors = []
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
                for code, info in wrong_codes.items():
                    if code in name:
                        for wn in info['wrong_names']:
                            if wn in name:
                                all_errors.append(f'  [{date}][{key}] STILL WRONG: {name} (should be {info["correct"]})')

if all_errors:
    print('REMAINING ERRORS:')
    for e in all_errors:
        print(e)
else:
    print('ALL PREVIOUS ERRORS FIXED - No known wrong codes found!')

print()
# Show all ETF refs in 2026-03-30 and 2026-03-31 and 2026-04-10 to confirm
for fname in ['news_2026-03-30.json', 'news_2026-03-31.json', 'news_2026-04-10.json']:
    print(f'=== {fname} ETF references ===')
    with open(os.path.join(news_dir, fname), encoding='utf-8') as f:
        d = json.load(f)
    for key in ['s_level', 'a_level']:
        for item in d.get(key, []):
            if not isinstance(item, dict):
                continue
            for e in item.get('etfs', []):
                if isinstance(e, dict) and '512880' in e.get('name', ''):
                    print(f'  [{key}] {e.get("name")} ({e.get("sentiment")})')
    print()

# Verify etf_map.json
print('=== etf_map.json check ===')
with open('etf_map.json', encoding='utf-8') as f:
    m = json.load(f)
print(f'Verified: {len(m["verified"])} codes')
print(f'To verify: {len(m["to_verify"])} codes')
print('Sample verified entries:')
for code in ['159320', '159755', '512880', '512800', '512900', '516070', '518880']:
    if code in m['verified']:
        print(f'  {code}: {m["verified"][code]["name"]} ({m["verified"][code]["category"]})')

# Verify insights.json
print()
print('=== insights.json check ===')
with open('insights.json', encoding='utf-8') as f:
    ins = json.load(f)
etf_pats = [p for p in ins['patterns'] if 'ETF' in p.get('id', '')]
etf_know = ins.get('etf_knowledge', [])
print(f'ETF patterns: {[p["id"] for p in etf_pats]}')
print(f'ETF knowledge entries: {len(etf_know)}')
for ek in etf_know:
    print(f'  {ek["id"]}: wrong={ek["wrong_code"]}/{ek["wrong_name"]} -> correct={ek["correct_code"]}/{ek["correct_name"]}')
