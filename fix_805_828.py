import json
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

NEWS_DIR = 'news_data'

# Find all 159805 references and check context
print('=== All 159805 references in news files ===')
for fname in sorted(os.listdir(NEWS_DIR)):
    if not fname.endswith('.json'):
        continue
    with open(os.path.join(NEWS_DIR, fname), encoding='utf-8') as f:
        d = json.load(f)
    for key in ['s_level', 'a_level']:
        for item in d.get(key, []):
            if not isinstance(item, dict):
                continue
            for e in item.get('etfs', []):
                if isinstance(e, dict) and '159805' in e.get('name', ''):
                    print(f'[{fname}] [{key}] {e.get("name")}')
                    print(f'  Title: {item.get("title")}')
                    print()
