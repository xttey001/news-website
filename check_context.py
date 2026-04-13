import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Check 3.30 full context
with open('news_data/news_2026-03-30.json', encoding='utf-8') as f:
    d = json.load(f)

print('=== news_2026-03-30.json FULL ===')
for key in ['s_level', 'a_level']:
    for item in d.get(key, []):
        if not isinstance(item, dict):
            continue
        etfs = item.get('etfs', [])
        if etfs:
            print(f'\n[{key}] Title: {item.get("title")}')
            for e in etfs:
                if isinstance(e, dict):
                    print(f'  ETF: {e.get("name")} ({e.get("sentiment")})')

print()
print('=== news_2026-03-25.json ETF context ===')
with open('news_data/news_2026-03-25.json', encoding='utf-8') as f:
    d = json.load(f)
for key in ['s_level', 'a_level']:
    for item in d.get(key, []):
        if not isinstance(item, dict):
            continue
        for e in item.get('etfs', []):
            if isinstance(e, dict) and '515220' in e.get('name', ''):
                print(f'[{key}] {e.get("name")} ({e.get("sentiment")})')
                print(f'  Title: {item.get("title")}')
