import json
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

news_dir = 'news_data'
files = sorted([f for f in os.listdir(news_dir) if f.endswith('.json') 
                and '2026-03-25' <= f <= 'news_2026-04-11.json'])

total_fixes = 0
for fname in files:
    fpath = os.path.join(news_dir, fname)
    with open(fpath, encoding='utf-8') as f:
        d = json.load(f)
    
    changes = []
    for key in ['s_level', 'a_level']:
        for item in d.get(key, []):
            if not isinstance(item, dict):
                continue
            for e in item.get('etfs', []):
                if not isinstance(e, dict):
                    continue
                name = e.get('name', '')
                if '512880' in name:
                    old = name
                    # Fix: 国债ETF -> 证券ETF, 银行ETF -> 证券ETF
                    if '国债ETF' in name:
                        e['name'] = name.replace('国债ETF', '证券ETF')
                    elif '银行ETF' in name:
                        e['name'] = name.replace('银行ETF', '证券ETF')
                    if e['name'] != old:
                        changes.append(f'  [{key}] {old} -> {e["name"]}')
    
    if changes:
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
        print(f'Fixed: {fname}')
        for c in changes:
            print(c)
        total_fixes += len(changes)

print(f'\nTotal fixes: {total_fixes}')
