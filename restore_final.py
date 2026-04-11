# -*- coding: utf-8 -*-
"""最终恢复脚本"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import subprocess, json, re, glob, os

# ====== 1. 从 git 恢复 ======
print('Step 1: git 45e69d9')
r = subprocess.run(['git', 'show', '45e69d9:news-data.js'], capture_output=True, cwd=os.path.dirname(__file__))
raw = r.stdout.decode('utf-8', errors='replace')

dates_found = re.findall(r'"(2026-\d{2}-\d{2})":\s*\{', raw)
print(f'  找到 {len(dates_found)} 个日期')

def extract_date_block(raw, date):
    pattern = rf'"{re.escape(date)}":\s*\{{'
    m = re.search(pattern, raw)
    if not m:
        return None
    brace = raw.find('{', m.start())
    if brace == -1:
        return None
    depth = 0
    for i in range(brace, len(raw)):
        c = raw[i]
        if c == '{': depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return raw[brace:i+1]
    return None

def parse_json(block):
    clean = block
    clean = clean.replace(''', '"').replace(''', '"')
    clean = clean.replace('\u201c', '"').replace('\u201d', '"')
    clean = clean.replace('\u2018', "'").replace('\u2019', "'")
    clean = re.sub(r'//.*', '', clean)
    clean = re.sub(r',(\s*[}\]])', r'\1', clean)
    def is_valid(c):
        code = ord(c)
        if code < 0x80: return True
        if 0x4E00 <= code <= 0x9FFF: return True
        if 0x3000 <= code <= 0x303F: return True
        if 0xFF00 <= code <= 0xFFEF: return True
        return c in ' \n\t{}[]:,"\'-_()）：【】《》'
    safe = ''.join(c if is_valid(c) else ' ' for c in clean)
    safe = re.sub(r'\s+', ' ', safe)
    try:
        return json.loads(safe)
    except:
        return None

recovered = {}
for date in dates_found:
    if date == '2026-04-05':
        continue  # 单独处理
    block = extract_date_block(raw, date)
    if block:
        data = parse_json(block)
        if data:
            recovered[date] = data

# ====== 2. 手动构建 4.05 ======
print('Step 2: 构建 4.05')
recovered['2026-04-05'] = {
    "date": "2026-04-05",
    "market_tone": "清明假期A股休市，中东危机升级：伊朗拒绝特朗普48小时通牒，中国资产成全球避风港",
    "s_level": [
        {"emoji": "🔴", "title": "伊朗拒绝特朗普48小时通牒！华尔街紧绷：4月6日后会发生什么？",
         "summary": "伊朗拒绝特朗普48小时通牒，地区紧张局势升级，全球市场避险情绪升温。",
         "duration": "1-2周", "etfs": [{"name": "518880 黄金ETF", "sentiment": "利好"}],
         "stocks": ["黄金股"], "signal": "地缘风险升级"},
        {"emoji": "🔴", "title": "中东危机引发全球市场动荡，中国资产成为新避风港",
         "summary": "中东危机升级，中国资产成为全球资金避风港。",
         "duration": "1-4周", "etfs": [{"name": "512760 芯片ETF", "sentiment": "利好"}],
         "stocks": ["中国资产"], "signal": "资金流入中国资产"},
        {"emoji": "🔴", "title": "英伟达H100租赁价格5个月涨40%，OpenAI完成1220亿美元融资",
         "summary": "AI算力需求旺盛，OpenAI完成史上最大规模融资。",
         "duration": "1-3个月", "etfs": [{"name": "512760 芯片ETF", "sentiment": "利好"}],
         "stocks": ["AI算力股"], "signal": "AI算力需求爆发"},
        {"emoji": "🔴", "title": "公募基金盈利2.61万亿元刷新历史最高纪录",
         "summary": "公募基金规模创新高，居民财富向权益市场转移。",
         "duration": "长期", "etfs": [{"name": "510300 沪深300ETF", "sentiment": "利好"}],
         "stocks": ["大市值蓝筹"], "signal": "长期资金入市"}
    ],
    "a_level": [
        {"emoji": "🟡", "title": "美股周线五连阴终结，但服务业PMI跌破荣枯线，滞胀风险升级",
         "summary": "美股反弹但经济数据疲软。",
         "duration": "1-2周", "etfs": [{"name": "513500 标普500ETF", "sentiment": "中性"}],
         "stocks": [], "signal": "美国经济放缓"}
    ],
    "douyin": []
}

# ====== 3. 合并 news_data/ ======
print('Step 3: 合并 news_data/')
news_dir = os.path.join(os.path.dirname(__file__), '..', 'news_data')
all_news = {}
for f in sorted(glob.glob(os.path.join(news_dir, 'news_*.json')), reverse=True):
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    date = d.get('date', '')
    if date:
        all_news[date] = d

merged = {}
for date, data in recovered.items():
    merged[date] = data

for date, data in all_news.items():
    if date in merged:
        if not merged[date].get('wukong_judgment') and data.get('wukong_judgment'):
            merged[date]['wukong_judgment'] = data['wukong_judgment']
            print(f'  补充悟空: {date}')
        if not merged[date].get('bajie_conclusion') and data.get('bajie_conclusion'):
            merged[date]['bajie_conclusion'] = data['bajie_conclusion']
            print(f'  补充八戒: {date}')
    else:
        merged[date] = data
        print(f'  新增: {date} (news_data)')

print(f'  合计: {len(merged)} 个日期')

# ====== 4. 运行模型 ======
print('Step 4: 运行模型')
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
try:
    from market_agents.data_fetcher import get_market_data
    from market_agents.sangsha_model import run_sangsha
    from market_agents.white_dragon_model import run_white_dragon
    codes = ['512760', '512930', '518880', '588890', '159382']
    market_data = get_market_data(codes, 7)
    print(f'  市场数据: {len(market_data)} 个')
except Exception as e:
    print(f'  模型错误: {e}')
    market_data = {}

for date in sorted(merged.keys(), reverse=True):
    sg_result = run_sangsha({date: merged[date]}, date, market_data)
    sg = sg_result.get('沙僧模块', sg_result.get('sengseng', {}))
    wd_result = run_white_dragon(market_data, sg.get('analysis_results', []))
    wd = wd_result.get('白龙马决策', {})
    merged[date]['sangsha_module'] = sg
    merged[date]['white_dragon'] = wd

# ====== 5. 生成文件 ======
print('Step 5: 生成文件')
sorted_dates = sorted(merged.keys(), reverse=True)
output_js = '// 财经新闻数据 - 恢复完整版\n\nconst newsData = ' + json.dumps(merged, ensure_ascii=False, indent=2) + ';\n\nconst availableDates = ' + json.dumps(sorted_dates, ensure_ascii=False) + ';\n\nfunction getNews(date) { return newsData[date] || null; }\nfunction getPreviousDate(date) { const idx = availableDates.indexOf(date); return idx < availableDates.length - 1 ? availableDates[idx + 1] : null; }\nfunction getNextDate(date) { const idx = availableDates.indexOf(date); return idx > 0 ? availableDates[idx - 1] : null; }'

with open('news-data.js', 'w', encoding='utf-8') as f:
    f.write(output_js)

# 验证
print()
for date in sorted_dates:
    d = merged[date]
    wk = bool(d.get('wukong_judgment'))
    bj = bool(d.get('bajie_conclusion'))
    print(f'  {date}: 悟空={wk} 八戒={bj}')

r2 = subprocess.run(['node', '--check', 'news-data.js'], capture_output=True, text=True)
print(f'\nJS语法: {"OK" if r2.returncode == 0 else "ERROR"}')
print(f'完成! 共 {len(sorted_dates)} 个日期')
