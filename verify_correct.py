# -*- coding: utf-8 -*-
"""Properly verify sangsha_module position"""
import sys, io, os, json, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

os.chdir('C:\\Users\\asus\\.qclaw\\workspace\\news-server')

# Load all data
all_news = {}
for f in sorted(glob.glob('news_data/news_*.json'), reverse=True):
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    date = d.get('date', '')
    if date:
        all_news[date] = d

# Add sangsha and white_dragon
sys.path.insert(0, '.')
from market_agents.data_fetcher import get_market_data
from market_agents.sangsha_model import run_sangsha
from market_agents.white_dragon_model import run_white_dragon

codes = ['512760', '512930', '518880', '588890', '159382']
try:
    market_data = get_market_data(codes, 7)
except:
    market_data = {}

for date in sorted(all_news.keys(), reverse=True):
    try:
        sg_result = run_sangsha({date: all_news[date]}, date, market_data)
        sg = sg_result.get('沙僧模块', sg_result.get('sengseng', {}))
    except:
        sg = {'overall_sentiment': '平稳', 'advice': '', 'avg_buy_prob': 0,
              'avg_panic_prob': 0, 'analysis_results': []}
    
    try:
        wd_result = run_white_dragon(market_data, sg.get('analysis_results', []))
        wd = wd_result.get('白龙马决策', {})
    except:
        wd = {'主力状态': '观望', '阶段': '观察', '行为解释': '',
              '是否利用散户': False, '综合建议': '暂无数据'}
    
    all_news[date]['sangsha_module'] = sg
    all_news[date]['white_dragon'] = wd

# Generate JSON
json_str = json.dumps(all_news, ensure_ascii=False, indent=2)

# Find the structure - look for the pattern "2026-04-10": { ... "2026-04-09":
# The top-level date keys are followed by a colon and then the object
import re

# Find top-level date keys (they appear as "2026-04-10": { at the beginning of lines or after commas)
pattern = r'"(2026-\d{2}-\d{2})":\s*\{'
matches = list(re.finditer(pattern, json_str))

print('Top-level date keys found:')
for m in matches:
    print(f'  {m.group(1)} at position {m.start()}')

# Find sangsha_module occurrences
sg_matches = list(re.finditer(r'"sangsha_module"', json_str))
print(f'\nFound {len(sg_matches)} sangsha_module occurrences')

# For each date, find which sangsha_module belongs to it
for i, date_match in enumerate(matches):
    date = date_match.group(1)
    start = date_match.start()
    end = matches[i+1].start() if i+1 < len(matches) else len(json_str)
    
    # Check if sangsha_module is in this range
    sg_in_range = [m for m in sg_matches if start < m.start() < end]
    print(f'{date}: has {len(sg_in_range)} sangsha_module in its section')