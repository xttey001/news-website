import json
import os
import sys
sys.stdout.reconfigure(encoding='utf-8')

# All paths relative to news-server/ directory
MAP_FILE = 'etf_map.json'
INS_FILE = 'insights.json'
NEWS_DIR = 'news_data'

with open(MAP_FILE, encoding='utf-8') as f:
    m = json.load(f)

merged = m['merged']

# ============================================================
# USER CORRECTIONS (2026-04-12 12:24)
# ============================================================
fixes = {
    # Remove 159012 (doesn't exist)
    '159012': {
        'name': '不存在（非ETF）',
        'category': 'wrong',
        'source': 'user_verify',
        'status': 'wrong',
        'note': '用户确认：159012不是ETF'
    },
    # Add 513190 as correct code
    '513190': {
        'name': '港股通金融ETF',
        'category': 'hk_finance',
        'source': 'user_verify',
        'status': 'verified',
        'note': '用户核实确认'
    },
    # 515700 = 新能源车ETF
    '515700': {
        'name': '新能源车ETF',
        'category': 'ev',
        'source': 'user_verify',
        'status': 'verified',
        'note': '用户核实确认：新能源车ETF（与515030为同类不同发行商）'
    },
    # 159805 = 传媒ETF (not 医疗ETF)
    '159805': {
        'name': '传媒ETF',
        'category': 'media',
        'source': 'user_verify',
        'status': 'verified',
        'note': '用户核实确认：159805是传媒ETF，不是医疗ETF'
    },
    # 159828 = 医疗ETF (correct medical ETF)
    '159828': {
        'name': '医疗ETF',
        'category': 'medical',
        'source': 'user_verify',
        'status': 'verified',
        'note': '用户核实确认'
    },
    # 159322 = 黄金股ETF (verified!)
    '159322': {
        'name': '黄金股ETF',
        'category': 'gold_stock',
        'source': 'user_verify',
        'status': 'verified',
        'note': '用户核实确认：159322是黄金股ETF（真实存在）'
    },
}

for code, info in fixes.items():
    merged[code] = info

# Remove 512900 (not confirmed by user, user confirmed 512880=证券ETF)
if '512900' in merged:
    del merged['512900']

m['merged'] = merged
m['version'] = '3.1'
m['date'] = '2026-04-12'

with open(MAP_FILE, 'w', encoding='utf-8') as f:
    json.dump(m, f, ensure_ascii=False, indent=2)
print(f'etf_map.json updated. Total codes: {len(merged)}')

# ============================================================
# Update insights.json ETF knowledge entries
# ============================================================
with open(INS_FILE, encoding='utf-8') as f:
    ins = json.load(f)

corrections = {
    'ETF-KW-005': {
        'correct_code': '159322',
        'correct_name': '黄金股ETF',
        'root_cause': '用户核实：159322是黄金股ETF（真实存在，金矿股），不是未知代码'
    },
    'ETF-KW-006': {
        'correct_code': '561700',
        'correct_name': '电力ETF博时',
        'root_cause': '用户核实：电力ETF是561700，煤炭ETF是515220，切勿混淆'
    },
    'ETF-KW-007': {
        'wrong_name': '金融ETF',
        'correct_code': '512800',
        'correct_name': '银行ETF',
        'root_cause': '512800=银行ETF（工行/招行/六大行），金融综合=512800银行+512880证券+512070保险，不要混用'
    }
}

for ek in ins.get('etf_knowledge', []):
    cid = ek.get('id', '')
    if cid in corrections:
        ek.update(corrections[cid])
        print(f'Updated: {cid}')

ins['last_updated'] = '2026-04-12'
with open(INS_FILE, 'w', encoding='utf-8') as f:
    json.dump(ins, f, ensure_ascii=False, indent=2)
print('insights.json updated.')

# ============================================================
# Fix news files that used wrong codes
# ============================================================
news_fixes = [
    # (wrong_name, correct_name)
    ('159012', '513190 港股通金融ETF'),
    ('159805 医疗ETF', '159805 传媒ETF'),
]

total_fixes = 0
for fname in sorted(os.listdir(NEWS_DIR)):
    if not fname.endswith('.json'):
        continue
    fpath = os.path.join(NEWS_DIR, fname)
    with open(fpath, encoding='utf-8') as f:
        d = json.load(f)
    
    fc = []
    for key in ['s_level', 'a_level']:
        for item in d.get(key, []):
            if not isinstance(item, dict):
                continue
            for e in item.get('etfs', []):
                if not isinstance(e, dict):
                    continue
                name = e.get('name', '')
                if '159012' in name:
                    fc.append(f'  [{key}] {name} -> 513190 港股通金融ETF')
                    e['name'] = '513190 港股通金融ETF'
                elif '159805' in name and ('医疗ETF' in name or '医疗' in name):
                    fc.append(f'  [{key}] {name} -> 159805 传媒ETF')
                    e['name'] = name.replace('医疗ETF', '传媒ETF').replace('医疗', '传媒')

    if fc:
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
        print(f'\nFixed: {fname}')
        for c in fc:
            print(c)
        total_fixes += len(fc)

print(f'\nTotal news fixes: {total_fixes}')
print('Done.')
