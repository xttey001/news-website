# -*- coding: utf-8 -*-
"""从recovered_data.js恢复所有日期（含编码修复）"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import json
import re
import glob

# 1. 读取恢复的数据
with open('recovered_data.js', 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

dates_found = re.findall(r'"(2026-\d{2}-\d{2})":\s*\{', raw)
print(f'找到 {len(dates_found)} 个日期: {dates_found}')

def extract_date_block(raw, date):
    pattern = rf'"({re.escape(date)})":\s*\{{'
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
    """智能解析JSON块，修复常见问题"""
    clean = block
    # 替换各种引号
    clean = clean.replace(''', '"').replace(''', '"')
    clean = clean.replace('\u201c', '"').replace('\u201d', '"')
    clean = clean.replace('\u2018', "'").replace('\u2019', "'")
    clean = re.sub(r'//.*', '', clean)  # 移除JS注释
    clean = re.sub(r',(\s*[}\]])', r'\1', clean)  # 移除尾随逗号
    
    # 修复编码损坏的中文字符（跳过整个summary字段）
    # 策略：找到 "summary": "..." 模式，处理损坏内容
    def fix_summary(m):
        prefix = m.group(1)
        content = m.group(2)
        suffix = m.group(3)
        # 尝试清理内容中的乱码字符
        try:
            # 检查是否有明显的编码损坏（连续多个 ? 或 ���）
            if '�' in content or '\ufffd' in content:
                # 替换乱码为占位符
                content = content.replace('\ufffd', '?')
            return prefix + content + suffix
        except:
            return prefix + '[内容编码损坏]' + suffix
    
    clean = re.sub(r'("summary":\s*")([^"]*)(")', fix_summary, clean)
    
    # 逐字符检查，保留有效字符
    def is_valid_char(c):
        code = ord(c)
        if code < 0x80:  # ASCII
            return True
        if 0x4E00 <= code <= 0x9FFF:  # CJK
            return True
        if 0x3000 <= code <= 0x303F:  # CJK符号
            return True
        if 0xFF00 <= code <= 0xFFEF:  # 全角
            return True
        if c in ' \n\t{}[]:,"\'-_()（）【】《》':
            return True
        return False
    
    safe = ''.join(c if is_valid_char(c) else ' ' for c in clean)
    safe = re.sub(r'\s+', ' ', safe)
    
    try:
        return json.loads(safe)
    except json.JSONDecodeError as e:
        return None

# 2. 解析每个日期
recovered_dates = {}
for date in dates_found:
    block = extract_date_block(raw, date)
    if not block:
        print(f'  {date}: 提取失败')
        continue
    
    data = parse_json_block(block)
    if data:
        recovered_dates[date] = data
        has_wk = 'wukong_judgment' in data
        has_bj = 'bajie_conclusion' in data
        s = len(data.get('s_level', []))
        print(f'  {date}: OK 悟空={has_wk} 八戒={has_bj} S={s}')
    else:
        print(f'  {date}: 解析失败（编码损坏）')

# 3. 读取 news_data/ 目录（优先级更高）
all_news = {}
for f in sorted(glob.glob('news_data/news_*.json'), reverse=True):
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    date = d.get('date', '')
    if date:
        all_news[date] = d
print(f'\nnews_data/ 有 {len(all_news)} 个')

# 4. 合并：news_data/ 优先，恢复数据补充
merged = {}
for date, data in all_news.items():
    merged[date] = data

for date, data in recovered_dates.items():
    if date not in merged:
        merged[date] = data
        print(f'补充: {date} (recovered)')

print(f'\n合并后: {len(merged)} 个日期')

# 5. 运行模型
print('\n=== 运行模型 ===')
sys.path.insert(0, '..')
try:
    from market_agents.data_fetcher import get_market_data
    from market_agents.sangsha_model import run_sangsha
    from market_agents.white_dragon_model import run_white_dragon
    codes = ['512760', '512930', '518880', '588890', '159382']
    market_data = get_market_data(codes, 7)
    print(f'市场数据: {len(market_data)} 个')
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

# 6. 生成文件
print('\n=== 生成 news-data.js ===')
sorted_dates = sorted(merged.keys(), reverse=True)

output_js = '// 财经新闻数据 - 恢复完整版\n'
output_js += '// 恢复自 git commit 45e69d9 + news_data/\n\n'
output_js += 'const newsData = ' + json.dumps(merged, ensure_ascii=False, indent=2) + ';\n\n'
output_js += 'const availableDates = ' + json.dumps(sorted_dates, ensure_ascii=False) + ';\n\n'
output_js += '''// 获取指定日期的新闻
function getNews(date) { return newsData[date] || null; }
function getPreviousDate(date) { const idx = availableDates.indexOf(date); return idx < availableDates.length - 1 ? availableDates[idx + 1] : null; }
function getNextDate(date) { const idx = availableDates.indexOf(date); return idx > 0 ? availableDates[idx - 1] : null; }'''

with open('news-data.js', 'w', encoding='utf-8') as f:
    f.write(output_js)

# 7. 验证
print(f'\n保存成功！共 {len(sorted_dates)} 个日期:')
for date in sorted_dates:
    d = merged[date]
    wk = bool(d.get('wukong_judgment'))
    bj = bool(d.get('bajie_conclusion'))
    sg = bool(d.get('sangsha_module'))
    print(f'  {date}: 悟空={wk} 八戒={bj} 沙僧={sg}')

import subprocess
r = subprocess.run(['node', '--check', 'news-data.js'], capture_output=True, text=True)
print(f'\nJS语法: {"OK" if r.returncode == 0 else "ERROR: " + r.stderr[:100]}')
