import json
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

news_dir = 'news_data'

# ============================================================
# STEP 1: Fix HIGH severity errors in news data files
# ============================================================
# 512880 = 国债ETF (正确) -> 被错误写成"银行ETF"或"证券ETF"
# 512690 = 能源ETF (正确) -> 被错误写成"金融ETF"

fixes = {}

files = sorted([f for f in os.listdir(news_dir) if f.endswith('.json') 
                and '2026-03-25' <= f <= 'news_2026-04-11.json'])

for fname in files:
    fpath = os.path.join(news_dir, fname)
    with open(fpath, encoding='utf-8') as f:
        d = json.load(f)
    
    file_changes = []
    for key in ['s_level', 'a_level']:
        for item in d.get(key, []):
            if not isinstance(item, dict):
                continue
            for e in item.get('etfs', []):
                if not isinstance(e, dict):
                    continue
                name = e.get('name', '')
                
                # Fix 512880: 银行ETF / 证券ETF -> 国债ETF
                if '512880' in name:
                    if '银行ETF' in name:
                        old = name
                        e['name'] = name.replace('银行ETF', '国债ETF')
                        file_changes.append(f'  [{key}] {old} -> {e["name"]}')
                    elif '证券ETF' in name:
                        old = name
                        e['name'] = name.replace('证券ETF', '国债ETF')
                        file_changes.append(f'  [{key}] {old} -> {e["name"]}')
                
                # Fix 512690: 金融ETF -> 能源ETF
                if '512690' in name and '金融ETF' in name:
                    old = name
                    e['name'] = name.replace('金融ETF', '能源ETF')
                    file_changes.append(f'  [{key}] {old} -> {e["name"]}')
    
    if file_changes:
        fixes[fname] = file_changes
        with open(fpath, 'w', encoding='utf-8') as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
        print(f'Fixed: {fname}')
        for c in file_changes:
            print(c)
        print()

# ============================================================
# STEP 2: Build complete ETF mapping table
# ============================================================
print('=' * 80)
print('COMPLETE ETF MAPPING TABLE')
print('=' * 80)

# Format: code -> {name, category, themes}
complete_etf_map = {
    # ===== 指数/宽基 ETF =====
    '159915': {'name': '创业板ETF', 'full': '创业板ETF', 'category': 'broad', 'themes': ['创业板', '创业板指']},
    '510300': {'name': '沪深300ETF', 'full': '沪深300ETF', 'category': 'broad', 'themes': ['沪深300', '大盘', 'PMI', '制造业', '经济']},
    '512500': {'name': '中证500ETF', 'full': '中证500ETF', 'category': 'broad', 'themes': ['中证500', '中小盘']},
    '159869': {'name': '科创50ETF', 'full': '科创50ETF', 'category': 'scitech', 'themes': ['科创50', '科创板']},
    '588000': {'name': '科创50ETF', 'full': '科创50ETF（华夏）', 'category': 'scitech', 'themes': ['科创50', '科创板']},
    '513500': {'name': '标普500ETF', 'full': '标普500ETF', 'category': 'us', 'themes': ['标普', '美股', 'S&P500']},

    # ===== 芯片/半导体 =====
    '512480': {'name': '芯片ETF', 'full': '芯片ETF（华夏）', 'category': 'chip', 'themes': ['芯片', '半导体', 'AI芯片', '设备']},
    '512760': {'name': '芯片ETF', 'full': '芯片ETF（国联安）', 'category': 'chip', 'themes': ['芯片', '半导体', 'AI', '美光', '铠侠', '存储']},
    '588890': {'name': '科创芯片ETF', 'full': '科创芯片ETF', 'category': 'chip', 'themes': ['科创芯片', 'AI芯片', '科创']},
    '588260': {'name': '科创芯片设计ETF', 'full': '科创芯片设计ETF', 'category': 'chip', 'themes': ['芯片设计', '科创']},
    '588780': {'name': '科创芯片设计ETF', 'full': '科创芯片设计ETF（华安）', 'category': 'chip', 'themes': ['芯片设计', '科创']},

    # ===== AI / 算力 / 云计算 =====
    '512930': {'name': 'AI算力ETF', 'full': 'AI算力ETF（华夏）', 'category': 'ai', 'themes': ['AI', '算力', '人工智能', '寒武纪', '复旦微电']},
    '515070': {'name': 'AI人工智能ETF', 'full': 'AI人工智能ETF', 'category': 'ai', 'themes': ['AI', '人工智能']},
    '515980': {'name': '云计算与大数据ETF', 'full': '云计算与大数据ETF', 'category': 'cloud', 'themes': ['云计算', 'SpaceX', '字节', '豆包', '大数据', 'Token', 'SaaS']},
    '588790': {'name': '科创AIETF', 'full': '科创AIETF', 'category': 'ai', 'themes': ['科创AI', 'AI', '科创']},
    '159819': {'name': '人工智能ETF', 'full': '人工智能ETF（需确认）', 'category': 'ai', 'themes': ['AI', '人工智能', '科技龙头'], 'verify': True},

    # ===== 新能源 / 光伏 / 电池 =====
    '159320': {'name': '电网ETF', 'full': '电网ETF', 'category': 'grid', 'themes': ['电网', '变压器', '硅钢', '十五五', '特高压', '输配电', '出口']},
    '159755': {'name': '电池ETF', 'full': '电池ETF', 'category': 'battery', 'themes': ['电池', '钠锂混合', '宁德时代', '储能', '动力电池']},
    '159775': {'name': '新能源ETF', 'full': '新能源ETF', 'category': 'new_energy', 'themes': ['新能源', '储能', '修复反弹']},
    '159806': {'name': '新能源车ETF', 'full': '新能源车ETF', 'category': 'ev', 'themes': ['新能源车', '比亚迪', '小鹏', '特斯拉', '电动汽车']},
    '159825': {'name': '新能源车ETF', 'full': '新能源车ETF', 'category': 'ev', 'themes': ['新能源车', '汽车销量', '比亚迪']},
    '159857': {'name': '光伏产业ETF', 'full': '光伏产业ETF', 'category': 'solar', 'themes': ['光伏', '太阳能', '装机']},
    '159863': {'name': '光伏ETF', 'full': '光伏ETF', 'category': 'solar', 'themes': ['光伏', '太阳能']},
    '515700': {'name': '新能源ETF', 'full': '新能源ETF（华夏）', 'category': 'new_energy', 'themes': ['新能源', '小鹏', '比亚迪', '特斯拉', '欧洲']},
    '516070': {'name': '易方达新能源ETF', 'full': '易方达新能源ETF', 'category': 'new_energy', 'themes': ['新能源', '自动驾驶', '华为', '比亚迪', '智能汽车', '光伏', '锂电']},
    '159566': {'name': '储能电池ETF', 'full': '储能电池ETF（需确认）', 'category': 'storage', 'themes': ['储能', '电池'], 'verify': True},

    # ===== 机器人 / 医疗 =====
    '159770': {'name': '机器人ETF', 'full': '机器人ETF', 'category': 'robot', 'themes': ['机器人', '人形机器人', '工业机器人', 'OpenAI']},
    '512010': {'name': '医药ETF', 'full': '医药ETF（易方达）', 'category': 'pharma', 'themes': ['医药', '生物制药', 'GLP-1', '礼来', '减肥药']},
    '159992': {'name': '创新药产业ETF', 'full': '创新药产业ETF', 'category': 'pharma', 'themes': ['创新药', 'GLP-1', '减肥药', '医药创新']},
    '159805': {'name': '医疗ETF', 'full': '医疗ETF（需确认）', 'category': 'medical', 'themes': ['医疗'], 'verify': True},

    # ===== 金融 / 银行 / 证券 / 保险 =====
    '512800': {'name': '银行ETF', 'full': '银行ETF（华宝）', 'category': 'bank', 'themes': ['银行', '工行', '招行', '六大行', '净息差']},
    '512900': {'name': '证券ETF', 'full': '证券ETF', 'category': 'securities', 'themes': ['证券', '券商', '中信证券']},
    '512070': {'name': '保险ETF', 'full': '保险ETF', 'category': 'insurance', 'themes': ['保险', '保险股']},
    '512880': {'name': '国债ETF', 'full': '国债ETF（国泰）', 'category': 'bond', 'themes': ['国债', '债券', '利率', '避险']},
    '512690': {'name': '能源ETF', 'full': '能源ETF（鹏华）', 'category': 'energy', 'themes': ['能源', '石油', '电力', '中石油', '中石化']},
    '159012': {'name': '港股通金融ETF', 'full': '港股通金融ETF', 'category': 'hk_finance', 'themes': ['港股通', '金融', '港股']},

    # ===== 黄金 / 有色 / 能源化工 =====
    '518880': {'name': '黄金ETF', 'full': '黄金ETF（华安）', 'category': 'gold', 'themes': ['黄金', '金价', '避险', '地缘', '霍尔木兹']},
    '159980': {'name': '有色金属ETF', 'full': '有色金属ETF', 'category': 'nonferrous', 'themes': ['有色', '铜', '黄金股', '有色金属', '金矿']},
    '159322': {'name': '黄金股ETF', 'full': '黄金股ETF（需确认，平安）', 'category': 'gold_stock', 'themes': ['黄金股', '金矿股'], 'verify': True},
    '159627': {'name': '能源化工ETF', 'full': '能源化工ETF（需确认）', 'category': 'energy_chem', 'themes': ['能源化工', '原油', '石化', '化工'], 'verify': True},

    # ===== 港股 / 海外 =====
    '513050': {'name': '港股科技ETF', 'full': '港股科技ETF', 'category': 'hk_tech', 'themes': ['港股', '腾讯', '阿里', '字节', '科技']},
    '515050': {'name': '中证港股通ETF', 'full': '中证港股通ETF', 'category': 'hk_connect', 'themes': ['港股通', '中企出海', '港股']},
    '159607': {'name': '中概互联ETF', 'full': '中概互联ETF（需确认）', 'category': 'china_concept', 'themes': ['中概', '互联', '阿里', '腾讯', '字节'], 'verify': True},

    # ===== 消费 / 农业 / 房地产 / 电力 =====
    '159928': {'name': '消费ETF', 'full': '消费ETF（需确认）', 'category': 'consumption', 'themes': ['消费', '零售', '食品'], 'verify': True},
    '159407': {'name': '豆粕ETF', 'full': '豆粕ETF（需确认）', 'category': 'agriculture', 'themes': ['豆粕', '农产品', '农业', '期货'], 'verify': True},
    '159994': {'name': '房地产ETF', 'full': '房地产ETF', 'category': 'real_estate', 'themes': ['房地产', '房企', '房产']},
    '515220': {'name': '电力ETF', 'full': '电力ETF', 'category': 'power', 'themes': ['电力', '清洁能源', '电力需求']},
    '159995': {'name': '科技ETF', 'full': '科技ETF', 'category': 'tech', 'themes': ['科技', '科技股']},
}

# Categorize
verified = {k: v for k, v in complete_etf_map.items() if not v.get('verify')}
to_verify = {k: v for k, v in complete_etf_map.items() if v.get('verify')}

print(f'VERIFIED ETF codes: {len(verified)}')
print()
categories = {}
for code, info in sorted(verified.items()):
    cat = info['category']
    if cat not in categories:
        categories[cat] = []
    categories[cat].append((code, info))

for cat, items in sorted(categories.items()):
    print(f'  [{cat}]')
    for code, info in items:
        print(f'    {code} | {info["name"]} | {", ".join(info["themes"][:4])}')
    print()

print(f'NEEDS USER VERIFICATION: {len(to_verify)}')
for code, info in sorted(to_verify.items()):
    print(f'  {code} | {info["name"]} | {", ".join(info["themes"])}')

print()
print(f'Total ETF codes in map: {len(complete_etf_map)}')

# Save to etf_map.json
etf_map_data = {
    'version': '1.0',
    'date': '2026-04-12',
    'verified': verified,
    'to_verify': to_verify,
}

with open('etf_map.json', 'w', encoding='utf-8') as f:
    json.dump(etf_map_data, f, ensure_ascii=False, indent=2)
print('\netf_map.json saved.')

# ============================================================
# STEP 3: Update insights.json ETF patterns
# ============================================================
with open('insights.json', encoding='utf-8') as f:
    insights = json.load(f)

# Remove old ETF entries
old_etf_knowledge = insights.get('etf_knowledge', [])
old_etf_pat = [p for p in insights['patterns'] if p['id'] == 'ETF-001']
if old_etf_pat:
    insights['patterns'].remove(old_etf_pat[0])

# Update etf_knowledge
insights['etf_knowledge'] = [
    {
        'id': 'ETF-KW-001',
        'wrong_code': '159542',
        'wrong_name': '电网ETF',
        'correct_code': '159320',
        'correct_name': '电网ETF',
        'category': 'power_grid',
        'confirmed_date': '2026-04-11',
        'root_cause': '159542是机械ETF，159320才是电网ETF（特高压/变压器/硅钢/十五五）'
    },
    {
        'id': 'ETF-KW-002', 
        'wrong_code': '159871',
        'wrong_name': '新能源电池ETF',
        'correct_code': '159755',
        'correct_name': '电池ETF',
        'category': 'battery',
        'confirmed_date': '2026-04-10',
        'root_cause': '159871是某有色ETF，非电池ETF；电池相关主题正确代码是159755（电池ETF）'
    },
    {
        'id': 'ETF-KW-003',
        'wrong_code': '512880',
        'wrong_name': '银行ETF / 证券ETF',
        'correct_code': '512880',
        'correct_name': '国债ETF',
        'category': 'bond',
        'confirmed_date': '2026-04-12',
        'root_cause': '512880是国债ETF（国债/债券/利率），银行相关新闻应映射512800（银行ETF），证券相关新闻应映射512900（证券ETF）'
    },
    {
        'id': 'ETF-KW-004',
        'wrong_code': '512690',
        'wrong_name': '金融ETF',
        'correct_code': '512690',
        'correct_name': '能源ETF',
        'category': 'energy',
        'confirmed_date': '2026-04-12',
        'root_cause': '512690是能源ETF（石油/电力），银行相关新闻应映射512800（银行ETF）'
    }
]

# Add new ETF-001 pattern
insights['patterns'].append({
    'id': 'ETF-001',
    'name': 'ETF code/name mapping — must verify before citing',
    'category': 'etf_knowledge',
    'confidence': 95,
    'status': 'active',
    'verified_count': 4,
    'source': '2026-04-12 comprehensive audit (3.25-4.11)',
    'formula': 'News theme -> check ETF table -> use verified code',
    'scope': 'All A-share ETF references in financial news analysis',
    'boundaries': 'Always use this table when ANY news mentions ETF code or theme',
    'key_signal': 'ETF name in analysis contains: 电网/银行/金融/证券/电池/新能源',
    'trading_rules': [
        '512880 = 国债ETF（国债/债券/利率/避险）≠ 银行ETF(512800) ≠ 证券ETF(512900)',
        '512690 = 能源ETF（石油/电力）≠ 金融ETF(512800银行)',
        '159320 = 电网ETF（特高压/变压器/十五五）≠ 159542机械ETF',
        '159755 = 电池ETF（储能/钠锂/动力电池）≠ 159871（有色ETF）',
        '516070 = 易方达新能源ETF（光伏+锂电+智能汽车全产业链）',
        '512800 = 银行ETF（工行/招行/六大行/净息差）',
        '512900 = 证券ETF（券商/中信证券）',
        '512480 vs 512760: 均为芯片ETF，但持仓略有不同（512760含存储/美光/铠侠，512480偏设备）',
        '159819 = 人工智能ETF（需确认持仓是否含AI龙头）',
        'When news says 银行+券商+保险: use 512800银行ETF + 512900证券ETF + 512070保险ETF separately',
        'Never use ETF code from thematic keyword alone — always cross-reference with this table'
    ],
    'etf_reference_table': {code: info['name'] + ' | ' + ', '.join(info['themes'][:3]) 
                             for code, info in sorted(verified.items())},
    'failure_lessons': [
        'Root cause: 512880 wrong = 国债ETF被误认为银行ETF because news mentioned 银行/金融',
        'Root cause: 512690 wrong = 能源ETF被误认为金融ETF because same confusion',
        'Root cause: 159542 wrong = 159320电网ETF was replaced with similar-looking code 159542',
        'Root cause: 159871 wrong = 电池ETF theme triggered wrong code from similar digits',
        'Prevention: Always lookup actual ETF name AND holdings, never infer from news keywords'
    ]
})

insights['meta']['total_patterns'] = len(insights['patterns'])
insights['last_updated'] = '2026-04-12'

with open('insights.json', 'w', encoding='utf-8') as f:
    json.dump(insights, f, ensure_ascii=False, indent=2)
print('insights.json updated.')
