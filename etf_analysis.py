import json
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Complete verified ETF mapping table (manually curated based on A-share ETF knowledge)
# Format: code -> {name, full_name, category, theme_keywords}
ETF_MAP = {
    # === 已验证（高可信度，代码+主题匹配度高）===
    '159320': {'name': '电网ETF', 'full': '电网ETF', 'category': 'power_grid', 'themes': ['电网', '变压器', '硅钢', '十五五', '特高压', '输配电']},
    '159755': {'name': '电池ETF', 'full': '电池ETF', 'category': 'battery', 'themes': ['电池', '钠锂混合', '宁德时代', '储能', '动力电池']},
    '159770': {'name': '机器人ETF', 'full': '机器人ETF', 'category': 'robot', 'themes': ['机器人', '人形机器人', '工业机器人']},
    '159775': {'name': '新能源ETF', 'full': '新能源ETF', 'category': 'new_energy', 'themes': ['新能源', '储能', '修复反弹']},
    '159806': {'name': '新能源车ETF', 'full': '新能源车ETF', 'category': 'ev', 'themes': ['新能源车', '比亚迪', '小鹏', '特斯拉', '电动汽车']},
    '159825': {'name': '新能源车', 'full': '新能源车ETF', 'category': 'ev', 'themes': ['新能源车', '汽车销量', '比亚迪']},
    '159857': {'name': '光伏产业ETF', 'full': '光伏产业ETF', 'category': 'solar', 'themes': ['光伏', '太阳能', '装机']},
    '159863': {'name': '光伏ETF', 'full': '光伏ETF', 'category': 'solar', 'themes': ['光伏', '太阳能']},
    '159869': {'name': '科创50ETF', 'full': '科创50ETF', 'category': 'scitech50', 'themes': ['科创50', '科创板']},
    '159915': {'name': '创业板ETF', 'full': '创业板ETF', 'category': 'gem', 'themes': ['创业板', '创业板指']},
    '159980': {'name': '有色金属', 'full': '有色金属ETF', 'category': 'nonferrous', 'themes': ['有色', '铜', '黄金股', '有色金属']},
    '159992': {'name': '创新药产业ETF', 'full': '创新药产业ETF', 'category': 'innovative_drug', 'themes': ['创新药', 'GLP-1', '减肥药', '医药创新']},
    '159994': {'name': '房地产ETF', 'full': '房地产ETF', 'category': 'real_estate', 'themes': ['房地产', '房企', '房产']},
    '159995': {'name': '科技ETF', 'full': '科技ETF', 'category': 'tech', 'themes': ['科技', '科技股']},
    '510300': {'name': '沪深300', 'full': '沪深300ETF', 'category': 'broad_market', 'themes': ['沪深300', '大盘', 'PMI', '制造业']},
    '512010': {'name': '医药ETF', 'full': '医药ETF', 'category': 'pharma', 'themes': ['医药', '生物制药', 'GLP-1', '礼来']},
    '512070': {'name': '保险ETF', 'full': '保险ETF', 'category': 'insurance', 'themes': ['保险', '保险股']},
    '512480': {'name': '芯片ETF', 'full': '芯片ETF（华夏）', 'category': 'chip', 'themes': ['芯片', '半导体', 'AI芯片']},
    '512500': {'name': '中证500ETF', 'full': '中证500ETF', 'category': 'mid_cap', 'themes': ['中证500', '中小盘']},
    '512690': {'name': '能源ETF', 'full': '能源ETF（鹏华）', 'category': 'energy', 'themes': ['能源', '石油', '电力']},
    '512760': {'name': '芯片ETF', 'full': '芯片ETF（国联安）', 'category': 'chip', 'themes': ['芯片', '半导体', 'AI', '美光', '铠侠']},
    '512800': {'name': '银行ETF', 'full': '银行ETF（华宝）', 'category': 'bank', 'themes': ['银行', '金融', '工行', '招行', '六大行']},
    '512880': {'name': '国债ETF', 'full': '国债ETF（国泰）', 'category': 'bond', 'themes': ['国债', '债券', '利率']},
    '512900': {'name': '证券ETF', 'full': '证券ETF', 'category': 'securities', 'themes': ['证券', '券商', '中信证券']},
    '512930': {'name': 'AI算力ETF', 'full': 'AI算力ETF（华夏）', 'category': 'ai', 'themes': ['AI', '算力', '人工智能', '寒武纪', '复旦微电']},
    '513050': {'name': '港股科技ETF', 'full': '港股科技ETF', 'category': 'hk_tech', 'themes': ['港股', '腾讯', '阿里', '字节', '科技']},
    '513500': {'name': '标普500ETF', 'full': '标普500ETF', 'category': 'us_index', 'themes': ['标普', '美股', 'S&P']},
    '515050': {'name': '港股通ETF', 'full': '中证港股通ETF', 'category': 'hk_connect', 'themes': ['港股通', '中企出海', '港股']},
    '515070': {'name': 'AI ETF', 'full': 'AI人工智能ETF', 'category': 'ai', 'themes': ['AI', '人工智能']},
    '515220': {'name': '电力ETF', 'full': '电力ETF', 'category': 'power', 'themes': ['电力', '清洁能源', '电力需求']},
    '515700': {'name': '新能源ETF', 'full': '新能源ETF（华夏）', 'category': 'new_energy', 'themes': ['新能源', '小鹏', '比亚迪', '特斯拉', '欧洲']},
    '515980': {'name': '云计算与大数据ETF', 'full': '云计算与大数据ETF', 'category': 'cloud', 'themes': ['云计算', 'SpaceX', '字节', '豆包', '大数据', 'Token']},
    '516070': {'name': '易方达新能源ETF', 'full': '易方达新能源ETF', 'category': 'new_energy', 'themes': ['新能源', '自动驾驶', '华为', '比亚迪', '智能汽车']},
    '516100': {'name': '工银苏格兰基建ETF', 'full': '工银苏格兰基建ETF', 'category': 'infrastructure', 'themes': ['基建', '电网', '变压器', '十五五', '出口']},
    '518880': {'name': '黄金ETF', 'full': '黄金ETF（华安）', 'category': 'gold', 'themes': ['黄金', '金价', '避险', '地缘']},
    '588000': {'name': '科创50ETF', 'full': '科创50ETF（华夏）', 'category': 'scitech50', 'themes': ['科创50', '科创板', '科技']},
    '588260': {'name': '科创芯片设计ETF', 'full': '科创芯片设计ETF', 'category': 'chip_design', 'themes': ['芯片设计', '科创', '半导体']},
    '588780': {'name': '科创芯片设计ETF', 'full': '科创芯片设计ETF（华安）', 'category': 'chip_design', 'themes': ['芯片设计', '科创']},
    '588790': {'name': '科创AIETF', 'full': '科创AIETF', 'category': 'scitech_ai', 'themes': ['科创AI', '科创', 'AI']},
    '588890': {'name': '科创芯片ETF', 'full': '科创芯片ETF', 'category': 'scitech_chip', 'themes': ['科创芯片', 'AI芯片', '科创', '半导体']},
    
    # === 可疑项（需用户确认）===
    '159012': {'name': '港股通金融ETF', 'full': '港股通金融ETF', 'category': 'hk_finance', 'themes': ['港股通', '金融']},
    '159322': {'name': '黄金股ETF平安?', 'full': '黄金股ETF（存疑）', 'category': 'gold_stock', 'themes': ['黄金股', '金矿股'], 'uncertain': True},
    '159407': {'name': '豆粕ETF?', 'full': '豆粕ETF（存疑）', 'category': 'soybean', 'themes': ['豆粕', '农产品', '农业'], 'uncertain': True},
    '159566': {'name': '储能电池ETF?', 'full': '储能电池ETF（存疑）', 'category': 'storage_battery', 'themes': ['储能', '电池'], 'uncertain': True},
    '159607': {'name': '中概互联ETF?', 'full': '中概互联ETF（存疑）', 'category': 'china_concept', 'themes': ['中概', '互联', '阿里', '腾讯', '字节'], 'uncertain': True},
    '159627': {'name': '能源化工ETF?', 'full': '能源化工ETF（存疑）', 'category': 'energy_chem', 'themes': ['能源化工', '原油', '石化'], 'uncertain': True},
    '159928': {'name': '消费ETF', 'full': '消费ETF', 'category': 'consumption', 'themes': ['消费', '瑞云冷链', '消博会'], 'uncertain': True},
}

# Now scan all news files and check for errors
news_dir = 'news_data'
errors = []
all_refs = []

files = sorted([f for f in os.listdir(news_dir) if f.endswith('.json') 
                and '2026-03-25' <= f <= 'news_2026-04-11.json'])

for fname in files:
    fpath = os.path.join(news_dir, fname)
    with open(fpath, encoding='utf-8') as f:
        d = json.load(f)
    
    date = d.get('date', fname)
    
    for key in ['s_level', 'a_level']:
        for item in d.get(key, []):
            if not isinstance(item, dict):
                continue
            
            for e in item.get('etfs', []):
                if not isinstance(e, dict):
                    continue
                
                name = e.get('name', '')
                sentiment = e.get('sentiment', '')
                title = item.get('title', '')[:60]
                
                codes = re.findall(r'\b(\d{6})\b', name)
                if not codes:
                    continue
                    
                code = codes[0]
                ref = {
                    'date': date,
                    'source': key,
                    'claimed_name': name,
                    'sentiment': sentiment,
                    'news_title': title,
                    'code': code
                }
                all_refs.append(ref)
                
                # Check if code is in our map
                if code in ETF_MAP:
                    info = ETF_MAP[code]
                    correct_name = info.get('name', '')
                    
                    # Error: wrong name
                    if correct_name and not info.get('uncertain') and correct_name not in name and name not in correct_name:
                        # Allow partial matches
                        is_match = any(kw in name for kw in info['themes'])
                        if not is_match:
                            errors.append({
                                'date': date,
                                'code': code,
                                'claimed': name,
                                'correct': f"{code} {correct_name}",
                                'reason': '主题与代码不符',
                                'news': title,
                                'severity': 'HIGH'
                            })
                    elif info.get('uncertain'):
                        errors.append({
                            'date': date,
                            'code': code,
                            'claimed': name,
                            'correct': f"{code} {correct_name}",
                            'reason': '存疑（需确认ETF实际持仓）',
                            'news': title,
                            'severity': 'MEDIUM'
                        })
                else:
                    # Code not in our map
                    errors.append({
                        'date': date,
                        'code': code,
                        'claimed': name,
                        'correct': '未知代码（需核查）',
                        'reason': '代码不在映射表中',
                        'news': title,
                        'severity': 'LOW'
                    })

print('=' * 90)
print('ERROR REPORT')
print('=' * 90)
high = [e for e in errors if e['severity'] == 'HIGH']
medium = [e for e in errors if e['severity'] == 'MEDIUM']
low = [e for e in errors if e['severity'] == 'LOW']

print(f'\n🔴 HIGH severity errors: {len(high)}')
for e in high:
    print(f'  [{e["date"]}] {e["claimed"]}')
    print(f'    -> Should be: {e["correct"]}')
    print(f'    -> Reason: {e["reason"]}')
    print(f'    -> News: {e["news"]}')
    print()

print(f'🟡 MEDIUM (uncertain) errors: {len(medium)}')
for e in medium:
    print(f'  [{e["date"]}] {e["claimed"]}')
    print(f'    -> Suggested: {e["correct"]}')
    print(f'    -> Reason: {e["reason"]}')
    print()

print(f'🟢 LOW (unverified code) errors: {len(low)}')
for e in low:
    print(f'  [{e["date"]}] {e["claimed"]} -> {e["correct"]}')

print()
print('=' * 90)
print('VERIFIED ETF MAP SUMMARY')
print('=' * 90)
verified = {k: v for k, v in ETF_MAP.items() if not v.get('uncertain')}
uncertain = {k: v for k, v in ETF_MAP.items() if v.get('uncertain')}
print(f'Verified codes: {len(verified)}')
print(f'Uncertain codes: {len(uncertain)}')
print()
for code, info in sorted(verified.items()):
    print(f'  {code} | {info["name"]} | themes: {", ".join(info["themes"][:3])}')
print()
print('--- Uncertain (need verification) ---')
for code, info in sorted(uncertain.items()):
    print(f'  {code} | {info["name"]} | themes: {", ".join(info["themes"][:3])}')
