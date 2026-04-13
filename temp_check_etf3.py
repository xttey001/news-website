import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('news_data/news_2026-04-11.json', encoding='utf-8') as f:
    d = json.load(f)

# Print full item structure
for key in ['all_news', 's_level', 'a_level']:
    items = d.get(key, [])
    print(f'=== {key} ===')
    for i, item in enumerate(items):
        print(json.dumps(item, ensure_ascii=False, indent=2)[:1000])
        print('---')
    print()
