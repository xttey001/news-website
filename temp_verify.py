import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Verify news files fixed
for fname in ['news_2026-04-10.json', 'news_2026-04-11.json']:
    with open('news_data/' + fname, encoding='utf-8') as f:
        d = json.load(f)
    print(f'=== {fname} ETF check ===')
    found_error = False
    for key in ['s_level', 'a_level']:
        for item in d.get(key, []):
            for e in item.get('etfs', []):
                name = e.get('name', '')
                if '159542' in name or '159871' in name:
                    print(f'  ERROR still present: {name}')
                    found_error = True
    if not found_error:
        print('  OK - no wrong codes')
    print()

# Verify insights.json
with open('insights.json', encoding='utf-8') as f:
    data = json.load(f)

patterns = data.get('patterns', [])
etf_knowledge = data.get('etf_knowledge', [])
etf_pat = [p for p in patterns if p.get('id') == 'ETF-001']

print(f'patterns count: {len(patterns)}')
print(f'etf_knowledge entries: {len(etf_knowledge)}')
print(f'ETF-001 added: {len(etf_pat) > 0}')
print(f'meta: {data.get("meta")}')
