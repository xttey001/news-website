# -*- coding: utf-8 -*-
"""从git历史恢复完整数据"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
import re
import glob

# 1. 从恢复的数据提取日期块
with open('recovered_data.js', 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

# 找所有日期
dates_in_recovered = re.findall(r'"(2026-\d{2}-\d{2})":\s*\{', raw)
print(f'恢复的数据包含 {len(dates_in_recovered)} 个日期: {dates_in_recovered}')

# 2. 读取 news_data/ 目录（当前有悟空/八戒的数据）
all_news = {}
for f in sorted(glob.glob('news_data/news_*.json'), reverse=True):
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    date = d.get('date', '')
    if date:
        all_news[date] = d

print(f'news_data/ 有 {len(all_news)} 个日期: {list(all_news.keys())}')

# 3. 从恢复的数据中提取每个日期块
def extract_date_block(raw, date):
    """提取指定日期的JSON块"""
    pattern = rf'"({re.escape(date)})":\s*\{{'
    m = re.search(pattern, raw)
    if not m:
        return None
    
    # 找到 { 开始
    brace = raw.find('{', m.start())
    if brace == -1:
        return None
    
    # 平衡括号找结束
    depth = 0
    for i in range(brace, len(raw)):
        c = raw[i]
        if c == '{':
            depth += 1
        elif c == '}':
            depth -= 1
            if depth == 0:
                return raw[brace:i+1]
    return None

# 4. 从恢复数据中提取每个日期
recovered_dates = {}
for date in dates_in_recovered:
    block = extract_date_block(raw, date)
    if block:
        # 清理和解析
        clean = block
        # 替换单引号和中文引号
        clean = clean.replace("'", '"').replace('\u201c', '"').replace('\u201d', '"')
        # 移除 // 注释
        clean = re.sub(r'//.*', '', clean)
        # 移除尾随逗号
        clean = re.sub(r',(\s*[}\]])', r'\1', clean)
        
        try:
            data = json.loads(clean)
            recovered_dates[date] = data
            has_wk = 'wukong_judgment' in data
            has_bj = 'bajie_conclusion' in data
            s_count = len(data.get('s_level', []))
            print(f'  {date}: 悟空={has_wk} 八戒={has_bj} S={s_count}')
        except json.JSONDecodeError as e:
            print(f'  {date}: 解析失败 {e}')
    else:
        print(f'  {date}: 提取失败')

# 5. 合并：优先用 news_data/（有悟空/八戒），补充恢复数据中没有的
merged = {}

# 先加 news_data/ 的（优先级高）
for date, data in all_news.items():
    merged[date] = data

# 再加恢复数据中没有的
for date, data in recovered_dates.items():
    if date not in merged:
        merged[date] = data
        print(f'补充: {date} (from recovered)')

print(f'\n合并后: {len(merged)} 个日期')

# 6. 运行沙僧/白龙马模型
print('\n=== 运行模型 ===')
sys.path.insert(0, '..')
try:
    from market_agents.data_fetcher import get_market_data
    from market_agents.sangsha_model import run_sangsha
    from market_agents.white_dragon_model import run_white_dragon
    
    codes = ['512760', '512930', '518880', '588890', '159382']
    market_data = get_market_data(codes, 7)
    print(f'市场数据: {len(market_data)} 个标的')
except Exception as e:
    print(f'Model error: {e}')
    market_data = {}

for date in sorted(merged.keys(), reverse=True):
    sg_result = run_sangsha({date: merged[date]}, date, market_data)
    sg = sg_result.get('沙僧模块', sg_result.get('sengseng', {}))
    
    wd_result = run_white_dragon(market_data, sg.get('analysis_results', []))
    wd = wd_result.get('白龙马决策', {})
    
    merged[date]['sangsha_module'] = sg
    merged[date]['white_dragon'] = wd

# 7. 生成最终文件
print('\n=== 生成 news-data.js ===')
sorted_dates = sorted(merged.keys(), reverse=True)

output_js = '// 财经新闻数据 - 恢复完整版\n'
output_js += '// 恢复自 git commit 45e69d9，14天完整数据\n\n'
output_js += 'const newsData = ' + json.dumps(merged, ensure_ascii=False, indent=2) + ';\n\n'
output_js += 'const availableDates = ' + json.dumps(sorted_dates, ensure_ascii=False) + ';\n\n'
output_js += '''// 获取指定日期的新闻
function getNews(date) {
    return newsData[date] || null;
}

function getPreviousDate(date) {
    const idx = availableDates.indexOf(date);
    return idx < availableDates.length - 1 ? availableDates[idx + 1] : null;
}

function getNextDate(date) {
    const idx = availableDates.indexOf(date);
    return idx > 0 ? availableDates[idx - 1] : null;
}'''

with open('news-data.js', 'w', encoding='utf-8') as f:
    f.write(output_js)

# 8. 验证
print(f'保存成功')
print(f'日期: {sorted_dates}')
for date in sorted_dates[:5]:
    d = merged[date]
    print(f'  {date}: 悟空={bool(d.get("wukong_judgment"))} 八戒={bool(d.get("bajie_conclusion"))} 沙僧={bool(d.get("sangsha_module"))}')
print('...')

# 9. node验证
import subprocess
result = subprocess.run(['node', '--check', 'news-data.js'], 
                       capture_output=True, text=True)
if result.returncode == 0:
    print('\nJS语法验证: OK')
else:
    print(f'\nJS语法错误: {result.stderr[:200]}')
