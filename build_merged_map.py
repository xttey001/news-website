import json
import os
import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

# ====================================================================
# PART 1: User-provided codes (from 1386-ETF document)
# All these are AUTHORITATIVE - use as-is
# ====================================================================
user_codes = {
    # 宽基
    '510050': {'name': '上证50ETF', 'category': 'broad'},
    '510100': {'name': '上证50ETF易方达', 'category': 'broad'},
    '510300': {'name': '沪深300ETF华泰柏瑞', 'category': 'broad'},
    '510310': {'name': '沪深300ETF易方达', 'category': 'broad'},
    '510330': {'name': '沪深300ETF华夏', 'category': 'broad'},
    '510500': {'name': '中证500ETF', 'category': 'broad'},
    '512100': {'name': '中证1000ETF', 'category': 'broad'},
    '159915': {'name': '创业板ETF易方达', 'category': 'broad'},
    '159949': {'name': '创业板50ETF', 'category': 'broad'},
    '588000': {'name': '科创50ETF', 'category': 'scitech'},
    '588080': {'name': '科创50ETF易方达', 'category': 'scitech'},
    '159901': {'name': '深证100ETF易方达', 'category': 'broad'},
    # 金融
    '512880': {'name': '证券ETF', 'category': 'securities'},
    '512800': {'name': '银行ETF', 'category': 'bank'},
    '512690': {'name': '酒ETF', 'category': 'liquor'},
    '512070': {'name': '保险ETF', 'category': 'insurance'},
    # 新能源/光伏/电池
    '515790': {'name': '光伏ETF', 'category': 'solar'},
    '515030': {'name': '新能源车ETF', 'category': 'ev'},
    '516160': {'name': '新能源ETF', 'category': 'new_energy'},
    '159755': {'name': '电池ETF', 'category': 'battery'},
    '561160': {'name': '锂电池ETF', 'category': 'battery'},
    '159824': {'name': '新能源车ETF博时', 'category': 'ev'},
    '516660': {'name': '新能源车ETF基金', 'category': 'ev'},
    '159625': {'name': '绿色电力ETF嘉实', 'category': 'green_power'},
    '562550': {'name': '绿电ETF', 'category': 'green_power'},
    # 科技/芯片/AI
    '512480': {'name': '半导体ETF', 'category': 'chip'},
    '512760': {'name': '芯片ETF', 'category': 'chip'},
    '588200': {'name': '科创芯片ETF', 'category': 'scitech_chip'},
    '159995': {'name': '芯片ETF', 'category': 'chip'},
    '516350': {'name': '芯片ETF易方达', 'category': 'chip'},
    '515070': {'name': '人工智能AIETF', 'category': 'ai'},
    '512930': {'name': 'AI人工智能ETF', 'category': 'ai'},
    '159819': {'name': '人工智能ETF易方达', 'category': 'ai'},
    '515980': {'name': '人工智能ETF', 'category': 'ai'},
    '516010': {'name': '游戏ETF', 'category': 'gaming'},
    '512980': {'name': '传媒ETF', 'category': 'media'},
    '512720': {'name': '计算机ETF', 'category': 'computer'},
    # 医药/医疗
    '512010': {'name': '医药ETF易方达', 'category': 'pharma'},
    '512170': {'name': '医疗ETF', 'category': 'medical'},
    '159859': {'name': '生物医药ETF', 'category': 'biotech'},
    '515120': {'name': '创新药ETF', 'category': 'innovative_drug'},
    '159647': {'name': '中药ETF', 'category': 'tcm'},
    '512290': {'name': '生物医药ETF', 'category': 'biotech'},
    '159883': {'name': '医疗器械ETF', 'category': 'medical_device'},
    '562600': {'name': '医疗器械ETF', 'category': 'medical_device'},
    # 行业
    '512710': {'name': '军工龙头ETF', 'category': 'military'},
    '512660': {'name': '军工ETF', 'category': 'military'},
    '512200': {'name': '房地产ETF', 'category': 'real_estate'},
    '515220': {'name': '煤炭ETF', 'category': 'coal'},
    '561360': {'name': '石油ETF', 'category': 'oil'},
    '159690': {'name': '有色矿业ETF招商', 'category': 'nonferrous'},
    '512400': {'name': '有色金属ETF', 'category': 'nonferrous'},
    '516020': {'name': '化工ETF', 'category': 'chemical'},
    '159865': {'name': '养殖ETF', 'category': 'agriculture'},
    '512680': {'name': '军工ETF广发', 'category': 'military'},
    '561700': {'name': '电力ETF博时', 'category': 'power'},
    '159619': {'name': '基建ETF', 'category': 'infrastructure'},
    '159512': {'name': '汽车ETF', 'category': 'auto'},
    '561120': {'name': '家电ETF', 'category': 'appliance'},
    # 港股/海外
    '159920': {'name': '恒生ETF', 'category': 'hk'},
    '513130': {'name': '恒生科技ETF', 'category': 'hk_tech'},
    '513050': {'name': '中概互联网ETF易方达', 'category': 'china_concept'},
    '159605': {'name': '中概互联ETF', 'category': 'china_concept'},
    '513100': {'name': '纳指ETF', 'category': 'us'},
    '513500': {'name': '标普500ETF博时', 'category': 'us'},
    '513520': {'name': '日经ETF', 'category': 'us'},
    '159941': {'name': '纳指ETF', 'category': 'us'},
    '513110': {'name': '纳斯达克100ETF', 'category': 'us'},
    '159612': {'name': '标普500ETF', 'category': 'us'},
    # 红利/价值
    '510880': {'name': '红利ETF华泰柏瑞', 'category': 'dividend'},
    '515180': {'name': '红利ETF易方达', 'category': 'dividend'},
    '515080': {'name': '中证红利ETF', 'category': 'dividend'},
    '512890': {'name': '红利低波ETF华泰柏瑞', 'category': 'dividend'},
    '515100': {'name': '红利低波100ETF', 'category': 'dividend'},
    '563180': {'name': '高股息ETF', 'category': 'dividend'},
    # 商品/货币
    '518880': {'name': '黄金ETF', 'category': 'gold'},
    '159934': {'name': '黄金ETF易方达', 'category': 'gold'},
    '159937': {'name': '黄金ETF博时', 'category': 'gold'},
    '159985': {'name': '豆粕ETF', 'category': 'agriculture'},
    '511880': {'name': '银华日利ETF', 'category': 'money'},
    '511990': {'name': '华宝添益ETF', 'category': 'money'},
    '511800': {'name': '易方达货币ETF', 'category': 'money'},
    '511810': {'name': '货币ETF南方', 'category': 'money'},
    # 其他
    '515050': {'name': '中证港股通ETF', 'category': 'hk_connect'},
}

# ====================================================================
# PART 2: News-derived codes NOT in user's document
# These come from news files 3.25-4.11 - status varies
# ====================================================================
news_codes = {
    # In user's doc under different name/code
    '159825': {'name': '新能源车ETF（新闻代码）', 'category': 'ev', 
               'status': 'alt_code', 'note': '同名不同代码，用户列表515030为同主题ETF'},
    '159994': {'name': '房地产ETF（新闻代码）', 'category': 'real_estate',
               'status': 'alt_code', 'note': '同名不同代码，用户列表512200为同主题ETF'},
    '159407': {'name': '豆粕ETF（新闻代码）', 'category': 'agriculture',
               'status': 'alt_code', 'note': '同名不同代码，用户列表159985为同主题ETF'},
    '512500': {'name': '中证500ETF（新闻代码）', 'category': 'broad',
               'status': 'alt_code', 'note': '同名不同代码，用户列表510500为同主题ETF'},
    # Not found in user's doc at all - may exist in 1386 but not in provided excerpt
    '159928': {'name': '消费ETF（新闻数据）', 'category': 'consumption', 'status': 'in_news'},
    '159770': {'name': '机器人ETF（新闻数据）', 'category': 'robot', 'status': 'in_news'},
    '159863': {'name': '光伏ETF（新闻代码）', 'category': 'solar', 'status': 'alt_code',
               'note': '同名不同代码，用户列表515790为同主题光伏ETF'},
    '512900': {'name': '证券ETF（新闻数据）', 'category': 'securities', 'status': 'in_news',
               'note': '新闻中多次出现，需确认是否在1386列表中（512880已确认=证券ETF）'},
    '159607': {'name': '中概互联ETF（新闻数据）', 'category': 'china_concept', 'status': 'in_news',
               'note': '新闻中用于中概股主题，用户列表513050/159605为同类ETF'},
    '159566': {'name': '储能电池ETF（新闻数据）', 'category': 'storage', 'status': 'in_news'},
    '159775': {'name': '新能源ETF（新闻代码）', 'category': 'new_energy', 'status': 'alt_code',
               'note': '同名不同代码，用户列表516160为同主题ETF'},
    '159857': {'name': '光伏产业ETF（新闻数据）', 'category': 'solar', 'status': 'in_news'},
    '159992': {'name': '创新药产业ETF（新闻代码）', 'category': 'innovative_drug', 'status': 'alt_code',
               'note': '同名不同代码，用户列表515120为创新药ETF'},
    '515700': {'name': '新能源ETF（新闻数据）', 'category': 'new_energy', 'status': 'in_news'},
    '159869': {'name': '科创50ETF（新闻代码）', 'category': 'scitech', 'status': 'alt_code',
               'note': '同名不同代码，用户列表588000/588080为科创50ETF'},
    '159805': {'name': '医疗ETF（新闻数据）', 'category': 'medical', 'status': 'in_news'},
    '588890': {'name': '科创芯片ETF（新闻代码）', 'category': 'scitech_chip', 'status': 'alt_code',
               'note': '同名不同代码，用户列表588200为科创芯片ETF'},
    '588790': {'name': '科创AIETF（新闻数据）', 'category': 'scitech_ai', 'status': 'in_news'},
    '588780': {'name': '科创芯片设计ETF（新闻代码）', 'category': 'scitech_chip', 'status': 'alt_code',
               'note': '同名不同代码，用户列表588200为科创芯片ETF'},
    '588260': {'name': '科创芯片设计ETF（新闻代码）', 'category': 'scitech_chip', 'status': 'alt_code',
               'note': '同名不同代码，用户列表588200为科创芯片ETF'},
    '159806': {'name': '新能源车ETF（新闻代码）', 'category': 'ev', 'status': 'alt_code',
               'note': '同名不同代码，用户列表515030为新能源车ETF'},
    '516070': {'name': '易方达新能源ETF（新闻数据）', 'category': 'new_energy', 'status': 'in_news'},
    '159012': {'name': '港股通金融ETF（新闻数据）', 'category': 'hk_finance', 'status': 'in_news'},
    '516100': {'name': '工银苏格兰基建ETF（新闻数据）', 'category': 'infrastructure', 'status': 'in_news',
               'note': '新闻中用于电网投资主题'},
    '159980': {'name': '有色金属ETF（新闻代码）', 'category': 'nonferrous', 'status': 'alt_code',
               'note': '同名不同代码，用户列表512400/159690为有色金属ETF'},
    # Known wrong codes
    '159320': {'name': '电网ETF（待核查）', 'category': 'grid', 'status': 'to_verify',
               'note': '用户确认是电网ETF，但不在1386列表中'},
    '159322': {'name': '未知/黄金股ETF', 'category': 'unknown', 'status': 'wrong',
               'note': '不在1386列表中，历史新闻错误引用'},
    '159542': {'name': '机械ETF（错误代码）', 'category': 'wrong', 'status': 'wrong',
               'note': '电网投资主题错误引用为机械ETF'},
    '159871': {'name': '有色ETF（错误代码）', 'category': 'wrong', 'status': 'wrong',
               'note': '新能源电池主题错误引用为有色ETF'},
}

# ====================================================================
# PART 3: Build merged map and output
# ====================================================================
merged = {}
for code, info in user_codes.items():
    merged[code] = {
        'name': info['name'],
        'category': info['category'],
        'source': 'user_doc',
        'status': 'verified'
    }
for code, info in news_codes.items():
    merged[code] = {
        'name': info['name'],
        'category': info['category'],
        'source': 'news',
        'status': info['status'],
        'note': info.get('note', '')
    }

# Save merged map
result = {
    'version': '3.0',
    'date': '2026-04-12',
    'description': 'Merged ETF map: user_doc(verified) + news-derived codes',
    'source_note': 'user_doc = authoritative from 1386-ETF list; news = from news analysis (may need verification)',
    'merged': merged,
    'summary': {
        'user_verified': len(user_codes),
        'news_alt_code': len([k for k,v in news_codes.items() if v['status']=='alt_code']),
        'news_in_news': len([k for k,v in news_codes.items() if v['status']=='in_news']),
        'to_verify': len([k for k,v in news_codes.items() if v['status']=='to_verify']),
        'wrong': len([k for k,v in news_codes.items() if v['status']=='wrong']),
    }
}

with open('etf_map.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print('=== Merged ETF Map ===')
print(f"User verified: {result['summary']['user_verified']}")
print(f"News alt codes: {result['summary']['news_alt_code']}")
print(f"News data only: {result['summary']['news_in_news']}")
print(f"To verify: {result['summary']['to_verify']}")
print(f"Wrong codes: {result['summary']['wrong']}")
print(f"Total: {len(merged)}")

print()
print('=== STATUS SUMMARY ===')
for status in ['verified', 'alt_code', 'in_news', 'to_verify', 'wrong']:
    items = {k:v for k,v in merged.items() if v['status']==status}
    if items:
        print(f'\n[{status}] ({len(items)} codes)')
        for code, info in sorted(items.items()):
            print(f'  {code} | {info["name"]}')

print()
print('Saved: etf_map.json')
