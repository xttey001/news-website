# -*- coding: utf-8 -*-
"""用git show直接提取数据（避免PowerShell编码问题）"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import subprocess
import json
import re
import glob

# 用subprocess获取git show输出（UTF-8）
result = subprocess.run(
    ['git', 'show', '45e69d9:news-data.js'],
    capture_output=True,
    cwd='..'
)

# git默认输出可能不是UTF-8，尝试解码
raw_bytes = result.stdout
for encoding in ['utf-8', 'gbk', 'latin-1', 'cp936']:
    try:
        raw = raw_bytes.decode(encoding)
        print(f'Decoded with: {encoding}')
        break
    except:
        continue

# 找所有日期
dates_found = re.findall(r'"(2026-\d{2}-\d{2})":\s*\{', raw)
print(f'找到 {len(dates_found)} 个日期: {dates_found}')

# 提取每个日期块
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

def parse_json_block(block):
    clean = block
    clean = clean.replace(''', '"').replace(''', '"')
    clean = clean.replace('\u201c', '"').replace('\u201d', '"')
    clean = clean.replace('\u2018', "'").replace('\u2019', "'")
    clean = re.sub(r'//.*', '', clean)
    clean = re.sub(r',(\s*[}\]])', r'\1', clean)
    
    # 逐字符检查，保留有效字符
    def is_valid(c):
        code = ord(c)
        if code < 0x80: return True
        if 0x4E00 <= code <= 0x9FFF: return True
        if 0x3000 <= code <= 0x303F: return True
        if 0xFF00 <= code <= 0xFFEF: return True
        if c in ' \n\t{}[]:,"\'-_()）：【】《》':
            return True
        return False
    
    safe = ''.join(c if is_valid(c) else ' ' for c in clean)
    safe = re.sub(r'\s+', ' ', safe)
    
    try:
        return json.loads(safe)
    except:
        return None

recovered_dates = {}
for date in dates_found:
    block = extract_date_block(raw, date)
    if not block:
        print(f'  {date}: 提取失败')
        continue
    data = parse_json_block(block)
    if data:
        recovered_dates[date] = data
        wk = bool(data.get('wukong_judgment'))
        bj = bool(data.get('bajie_conclusion'))
        s = len(data.get('s_level', []))
        print(f'  {date}: OK 悟空={wk} 八戒={bj} S={s}')
    else:
        print(f'  {date}: 解析失败')

# 合并 news_data/ 目录
all_news = {}
for f in sorted(glob.glob('news_data/news_*.json'), reverse=True):
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    date = d.get('date', '')
    if date:
        all_news[date] = d

merged = {}
for date, data in all_news.items():
    merged[date] = data

for date, data in recovered_dates.items():
    if date not in merged:
        merged[date] = data
        print(f'补充: {date}')

print(f'\n合并: {len(merged)} 个日期')

# 运行模型
print('\n=== 模型 ===')
sys.path.insert(0, '..')
from market_agents.data_fetcher import get_market_data
from market_agents.sangsha_model import run_sangsha
from market_agents.white_dragon_model import run_white_dragon

codes = ['512760', '512930', '518880', '588890', '159382']
market_data = get_market_data(codes, 7)
print(f'市场数据: {len(market_data)} 个')

for date in sorted(merged.keys(), reverse=True):
    sg_result = run_sangsha({date: merged[date]}, date, market_data)
    sg = sg_result.get('沙僧模块', sg_result.get('sengseng', {}))
    wd_result = run_white_dragon(market_data, sg.get('analysis_results', []))
    wd = wd_result.get('白龙马决策', {})
    merged[date]['sangsha_module'] = sg
    merged[date]['white_dragon'] = wd

# 生成
sorted_dates = sorted(merged.keys(), reverse=True)
output_js = '// 财经新闻数据 - 恢复完整版\n\nconst newsData = ' + json.dumps(merged, ensure_ascii=False, indent=2) + ';\n\nconst availableDates = ' + json.dumps(sorted_dates, ensure_ascii=False) + ';\n\nfunction getNews(date) { return newsData[date] || null; }\nfunction getPreviousDate(date) { const idx = availableDates.indexOf(date); return idx < availableDates.length - 1 ? availableDates[idx + 1] : null; }\nfunction getNextDate(date) { const idx = availableDates.indexOf(date); return idx > 0 ? availableDates[idx - 1] : null; }'

with open('news-data.js', 'w', encoding='utf-8') as f:
    f.write(output_js)

print(f'\n保存: {len(sorted_dates)} 个日期')
for date in sorted_dates:
    d = merged[date]
    print(f'  {date}: 悟空={bool(d.get("wukong_judgment"))} 八戒={bool(d.get("bajie_conclusion"))}')

# JS验证
r = subprocess.run(['node', '--check', 'news-data.js'], capture_output=True, text=True)
print(f'JS语法: {"OK" if r.returncode == 0 else "ERROR"}')
