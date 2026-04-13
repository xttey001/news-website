import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('news_data/news_2026-04-11.json', encoding='utf-8') as f:
    d = json.load(f)

for key in ['s_level', 'a_level']:
    for item in d.get(key, []):
        etfs = item.get('etfs', [])
        for e in etfs:
            name = e.get('name', '')
            if '159542' in name or '159871' in name or '电网' in name or '电池' in name:
                print(f'=== Found in [{key}] ===')
                print(f'Title: {item["title"]}')
                print(f'ETF: {e}')
                print()
