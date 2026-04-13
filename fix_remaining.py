import json
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

news_dir = 'news_data'
changes = []

# Fix 512880 in banking context -> should be 512800
# Fix 512690 -> should be 512800 (banking context, not 酒ETF)
# Fix 515220 name -> 煤炭ETF

fixes = {
    'news_2026-03-30.json': [
        ('512880 证券ETF', '512800 银行ETF', '银行新闻，512880=证券ETF不适合'),
        ('512690 能源ETF', '512800 银行ETF', '银行新闻，酒ETF/能源ETF均不适合，应为银行ETF'),
    ],
    'news_2026-03-25.json': [
        ('515220 电力ETF', '515220 煤炭ETF', '515220跟踪煤炭指数，非电力ETF'),
    ],
    'news_2026-03-27.json': [
        ('515220 电力ETF', '515220 煤炭ETF', '515220跟踪煤炭指数，非电力ETF'),
    ],
}

for fname, file_fixes in fixes.items():
    fpath = os.path.join(news_dir, fname)
    with open(fpath, encoding='utf-8') as f:
        d = json.load(f)
    
    fc = []
    for old_name, new_name, reason in file_fixes:
        for key in ['s_level', 'a_level']:
            for item in d.get(key, []):
                if not isinstance(item, dict):
                    continue
                for e in item.get('etfs', []):
                    if not isinstance(e, dict):
                        continue
                    if e.get('name') == old_name:
                        e['name'] = new_name
                        fc.append(f'  [{key}] {old_name} -> {new_name}')
                        fc.append(f'       Reason: {reason}')
    
    if fc:
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
        print(f'Fixed: {fname}')
        for c in fc:
            print(c)
        print()

print('Done.')
