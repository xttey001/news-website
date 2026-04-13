import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

news_dir = 'news_data'
problem_codes = ['159542', '159871']

print('=== Checking all news files for ETF code errors ===')
for fname in sorted(os.listdir(news_dir)):
    if not fname.endswith('.json'):
        continue
    fpath = os.path.join(news_dir, fname)
    with open(fpath, encoding='utf-8') as f:
        d = json.load(f)
    
    for key in ['s_level', 'a_level', 'wukong_judgment', 'bajie_conclusion', 'all_news']:
        items = d.get(key, [])
        if not isinstance(items, list):
            continue
        for item in items:
            etfs = item.get('etfs', [])
            if not isinstance(etfs, list):
                continue
            for e in etfs:
                if not isinstance(e, dict):
                    continue
                name = e.get('name', '')
                for code in problem_codes:
                    if code in name:
                        print(f'{fname} [{key}]: {e}')
                        print(f'  Title: {item.get("title", "")[:80]}')
                        print()
