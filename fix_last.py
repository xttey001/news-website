import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('news_data/news_2026-04-03.json', encoding='utf-8') as f:
    d = json.load(f)

for key in ['s_level', 'a_level']:
    for item in d.get(key, []):
        if not isinstance(item, dict):
            continue
        for e in item.get('etfs', []):
            if isinstance(e, dict) and '159805' in e.get('name', ''):
                print(f'Before: {repr(e["name"])}')
                e['name'] = '512010 医药ETF易方达'
                print(f'After: {repr(e["name"])}')
                print(f'Context: {item.get("title")}')

with open('news_data/news_2026-04-03.json', 'w', encoding='utf-8') as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print('Saved.')
