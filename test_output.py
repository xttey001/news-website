# -*- coding: utf-8 -*-
"""Complete test of generate_full_newsdata.py output"""
import sys, io, os, json, glob
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

os.chdir('C:\\Users\\asus\\.qclaw\\workspace\\news-server')

# Load all data exactly like the script does
all_news = {}
for f in sorted(glob.glob('news_data/news_*.json'), reverse=True):
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    date = d.get('date', '')
    if date:
        all_news[date] = d

print(f'Loaded {len(all_news)} dates from news_data/')

# Add sangsha and white_dragon like the script does
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
    except Exception as e:
        print(f'{date} sangsha error: {e}')
        sg = {'overall_sentiment': '平稳', 'advice': '', 'avg_buy_prob': 0,
              'avg_panic_prob': 0, 'analysis_results': []}
    
    try:
        wd_result = run_white_dragon(market_data, sg.get('analysis_results', []))
        wd = wd_result.get('白龙马决策', {})
    except Exception as e:
        print(f'{date} white_dragon error: {e}')
        wd = {'主力状态': '观望', '阶段': '观察', '行为解释': '',
              '是否利用散户': False, '综合建议': '📊 暂无数据'}
    
    all_news[date]['sangsha_module'] = sg
    all_news[date]['white_dragon'] = wd

# Check 2026-04-10
d = all_news.get('2026-04-10', {})
print(f'\n2026-04-10 after processing:')
print(f'  sangsha_module present: {"sangsha_module" in d}')
print(f'  white_dragon present: {"white_dragon" in d}')

# Generate output like the script does
sorted_dates = sorted(all_news.keys(), reverse=True)
output_js = '// 财经新闻数据 - 沙僧白龙马集成版\n'
output_js += '// 生成时间: 2026-04-10 四层分析:悟空+八戒+沙僧+白龙马\n\n'
output_js += 'const newsData = ' + json.dumps(all_news, ensure_ascii=False, indent=2) + ';\n\n'
output_js += 'const availableDates = ' + json.dumps(sorted_dates, ensure_ascii=False) + ';\n\n'

# Check if output contains sangsha_module for 2026-04-10
has_sangsha = '"sangsha_module"' in output_js and '"2026-04-10"' in output_js
print(f'\nOutput JS contains sangsha_module: {has_sangsha}')

# Find position of 2026-04-10 sangsha_module
idx = output_js.find('"2026-04-10"')
if idx > 0:
    section = output_js[idx:idx+5000]
    has_sangsha_in_section = 'sangsha_module' in section
    print(f'sangsha_module in 2026-04-10 section: {has_sangsha_in_section}')
    
    # Save test output
    with open('github-pages-deploy/test-news-data.js', 'w', encoding='utf-8') as f:
        f.write(output_js)
    print('\nSaved to github-pages-deploy/test-news-data.js')