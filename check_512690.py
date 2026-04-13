import json
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

news_dir = 'news_data'

# Check ALL files for 512690 and 515220 issues
for fname in sorted(os.listdir(news_dir)):
    if not fname.endswith('.json'):
        continue
    with open(os.path.join(news_dir, fname), encoding='utf-8') as f:
        d = json.load(f)
    for key in ['s_level', 'a_level']:
        for item in d.get(key, []):
            if not isinstance(item, dict):
                continue
            for e in item.get('etfs', []):
                if not isinstance(e, dict):
                    continue
                name = e.get('name', '')
                if '512690' in name or '515220' in name:
                    print(f'[{fname}] {key}: {name} ({e.get("sentiment")})')
                    title = item.get('title', '')
                    print(f'  Title: {title}')
