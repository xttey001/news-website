import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('news_data/news_2026-04-11.json', encoding='utf-8') as f:
    d = json.load(f)

for key in ['all_news', 's_level', 'a_level']:
    items = d.get(key, [])
    print(f'=== {key} ({len(items)} items) ===')
    for i, item in enumerate(items):
        title = item.get('title', '')
        content = str(item.get('content', ''))
        print(f'[{i}] Title: {title}')
        print(f'    Content: {content[:800]}')
        print()
