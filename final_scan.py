import json
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Load ETF map
with open('etf_map.json', encoding='utf-8') as f:
    etf_map = json.load(f)

verified = etf_map['verified']
all_etf_codes = set(verified.keys())

# Known wrong codes to check
known_wrong = {
    '159542': '应为159320电网ETF或不在列表中',
    '159871': '应为516070易方达新能源ETF',
    '159322': '不在官方ETF列表中',
}

news_dir = 'news_data'
files = sorted([f for f in os.listdir(news_dir) if f.endswith('.json') 
                and '2026-03-25' <= f <= 'news_2026-04-11.json'])

print(f'Scanning {len(files)} files...')
print()

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
                codes = re.findall(r'\b(\d{6})\b', name)
                for code in codes:
                    if code in known_wrong:
                        all_errors.append(f'  [{date}] STILL WRONG: {name} ({known_wrong[code]})')
                    elif code not in all_etf_codes:
                        # Unknown code - flag it
                        all_errors.append(f'  [{date}] UNKNOWN CODE: {name} (code {code} not in map)')

if all_errors:
    print('ERRORS FOUND:')
    for e in all_errors:
        print(e)
else:
    print('ALL CLEAR - No known wrong codes or unknown codes found!')

print()
print('=== Final ETF Reference Summary ===')
ref_count = {}
for fname in files:
    with open(os.path.join(news_dir, fname), encoding='utf-8') as f:
        d = json.load(f)
    for key in ['s_level', 'a_level']:
        for item in d.get(key, []):
            if not isinstance(item, dict):
                continue
            for e in item.get('etfs', []):
                if isinstance(e, dict):
                    name = e.get('name', '')
                    codes = re.findall(r'\b(\d{6})\b', name)
                    for code in codes:
                        ref_count[code] = ref_count.get(code, 0) + 1

for code, count in sorted(ref_count.items(), key=lambda x: -x[1]):
    name = verified.get(code, {}).get('name', 'UNKNOWN')
    print(f'  {code} {name}: {count} refs')

print(f'\nTotal unique ETFs: {len(ref_count)}')
print(f'Total references: {sum(ref_count.values())}')
