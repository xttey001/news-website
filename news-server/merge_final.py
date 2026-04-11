# -*- coding: utf-8 -*-
"""最终数据合并脚本
优先级：
1. news_data/ 目录（最新）
2. orig_20260XXX.json（从原始news-data.js提取的补充数据）
3. 对所有日期运行沙僧/白龙马模型
4. 保留悟空/八戒/s_level等原始字段
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import os
import json
import glob

print('=== Step 1: 收集所有数据源 ===')

all_news = {}

# 1a. 从 news_data/ 目录
print('\n[1a] news_data/ 目录:')
for f in sorted(glob.glob('news_data/news_*.json'), reverse=True):
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    date = d.get('date', '')
    if date:
        all_news[date] = d
        src = '悟空' if 'wukong_judgment' in d else '仅S级'
        print(f'  {date}: {src}')

# 1b. 从原始提取文件（4.07, 4.08优先）
print('\n[1b] 原始提取文件（补充/覆盖）:')
orig_files = glob.glob('orig_2026*.json')
for f in orig_files:
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    date = d.get('date', '')
    if date:
        had_wk = 'wukong_judgment' in d
        all_news[date] = d  # 覆盖或补充
        src = '完整(悟空+八戒)' if had_wk else '仅S级'
        print(f'  {date}: {src} (覆盖={date in all_news})')

print(f'\n合并后总计: {len(all_news)} 个日期')

# ========== 2. 运行模型 ==========
print('\n=== Step 2: 运行沙僧/白龙马模型 ===')
sys.path.insert(0, '.')
from market_agents.data_fetcher import get_market_data
from market_agents.sangsha_model import run_sangsha
from market_agents.white_dragon_model import run_white_dragon

codes = ['512760', '512930', '518880', '588890', '159382']
try:
    market_data = get_market_data(codes, 7)
    print(f'市场数据: {len(market_data)} 个标的')
except Exception as e:
    print(f'Market data error: {e}')
    market_data = {}

for date in sorted(all_news.keys(), reverse=True):
    # 沙僧
    try:
        sg_result = run_sangsha({date: all_news[date]}, date, market_data)
        sg = sg_result.get('沙僧模块', sg_result.get('sengseng', {}))
    except:
        sg = {'overall_sentiment': '平稳', 'advice': '', 'avg_buy_prob': 0,
              'avg_panic_prob': 0, 'analysis_results': []}
    
    # 白龙马
    try:
        wd_result = run_white_dragon(market_data, sg.get('analysis_results', []))
        wd = wd_result.get('白龙马决策', {})
    except:
        wd = {'主力状态': '观望', '阶段': '观察', '行为解释': '',
              '是否利用散户': False, '综合建议': '📊 暂无数据'}
    
    all_news[date]['sangsha_module'] = sg
    all_news[date]['white_dragon'] = wd

# ========== 3. 生成输出 ==========
print('\n=== Step 3: 生成 news-data.js ===')

sorted_dates = sorted(all_news.keys(), reverse=True)

output_js = '// 财经新闻数据 - 沙僧白龙马集成版\n'
output_js += '// 生成时间: 2026-04-10 四层分析:悟空+八戒+沙僧+白龙马\n\n'
output_js += 'const newsData = ' + json.dumps(all_news, ensure_ascii=False, indent=2) + ';\n\n'
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

out_path = 'github-pages-deploy/news-data.js'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(output_js)

# ========== 4. 验证 ==========
print('\n=== Step 4: 验证 ===')
with open(out_path, 'r', encoding='utf-8') as f:
    content = f.read()

print(f'保存: {out_path}')
print(f'日期: {sorted_dates}')
print()
for date in sorted_dates:
    d = all_news[date]
    print(f'  {date}: 悟空={bool(d.get("wukong_judgment"))} '
          f'八戒={bool(d.get("bajie_conclusion"))} '
          f'沙僧={bool(d.get("sangsha_module"))} '
          f'白龙马={bool(d.get("white_dragon"))}')

print(f'\n文件大小: {len(content)} bytes')
print('\n=== 完成 ===')
