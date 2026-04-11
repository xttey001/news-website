# -*- coding: utf-8 -*-
"""
正确的数据合并脚本
策略：
1. 从 news_data/ 目录读取有完整悟空/八戒的新闻
2. 从原始 news-data.js 读取4.04-4.08的新闻（只有旧格式）
3. 对所有日期运行沙僧/白龙马模型
4. 合并悟空/八戒 + 沙僧/白龙马
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import os
import json
import glob
import re

print('=== Step 1: 读取 news_data/ 目录（完整数据）===')
all_news = {}

# 从 news_data 目录读取（这些有悟空/八戒）
for f in sorted(glob.glob('news_data/news_*.json'), reverse=True):
    try:
        with open(f, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
            date = data.get('date', '')
            if date:
                all_news[date] = data
                print(f'  目录: {date}')
    except Exception as e:
        print(f'  Error: {f}: {e}')

print(f'\n目录数据: {len(all_news)} 个日期')

print('\n=== Step 2: 从原始 news-data.js 补充缺失日期 ===')
# 读取原始 news-data.js（4.04-4.08）
original_path = 'news-data.js'  # 根目录的原始文件

if os.path.exists(original_path):
    try:
        with open(original_path, 'r', encoding='utf-8') as f:
            raw = f.read()
        
        # 提取 JSON 部分
        m = re.search(r'const newsData = (.+?);?const availableDates', raw, re.DOTALL)
        if m:
            json_str = m.group(1).strip().rstrip(';')
            orig_data = json.loads(json_str)
            
            for date, data in orig_data.items():
                if date == 'availableDates':
                    continue
                if date not in all_news:
                    all_news[date] = data
                    print(f'  原始: {date}')
            
            print(f'\n原始数据补充: {len(orig_data)} 个日期')
        else:
            print('  无法解析原始文件')
    except Exception as e:
        print(f'  Error: {e}')

print(f'\n合并后: {len(all_news)} 个日期')

# ========== 3. 运行模型 ==========
print('\n=== Step 3: 运行沙僧/白龙马模型 ===')
sys.path.insert(0, '.')
try:
    from market_agents.data_fetcher import get_market_data
    from market_agents.sangsha_model import run_sangsha
    from market_agents.white_dragon_model import run_white_dragon
    
    codes = ['512760', '512930', '518880', '588890', '159382']
    market_data = get_market_data(codes, 7)
    print(f'市场数据: {len(market_data)} 个标的')
except Exception as e:
    print(f'Model import error: {e}')
    market_data = {}

for date in sorted(all_news.keys(), reverse=True):
    print(f'  处理: {date}')
    
    # 沙僧
    try:
        sg_result = run_sangsha({date: all_news[date]}, date, market_data)
        sg = sg_result.get('沙僧模块', sg_result.get('sengseng', {}))
    except Exception as e:
        print(f'    Sangsha error: {e}')
        sg = {'overall_sentiment': '平稳', 'advice': '', 'avg_buy_prob': 0, 
              'avg_panic_prob': 0, 'analysis_results': []}
    
    # 白龙马
    try:
        wd_result = run_white_dragon(market_data, sg.get('analysis_results', []))
        wd = wd_result.get('白龙马决策', {})
    except Exception as e:
        print(f'    WhiteDragon error: {e}')
        wd = {'主力状态': '观望', '阶段': '观察', '行为解释': '', 
              '是否利用散户': False, '综合建议': '📊 暂无数据'}
    
    # 追加模型输出（不覆盖悟空/八戒）
    all_news[date]['sangsha_module'] = sg
    all_news[date]['white_dragon'] = wd

# ========== 4. 生成输出 ==========
print('\n=== Step 4: 生成 news-data.js ===')

sorted_dates = sorted(all_news.keys(), reverse=True)

output_js = '// 财经新闻数据 - 沙僧白龙马集成版\n'
output_js += '// 生成时间: 2026-04-10 包含悟空/八戒/沙僧/白龙马四层分析\n\n'
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

# 保存到 github-pages-deploy
out_path = 'github-pages-deploy/news-data.js'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(output_js)

print(f'\n保存: {out_path}')
print(f'日期: {sorted_dates}')

# ========== 5. 验证 ==========
print('\n=== Step 5: 验证 ===')
with open(out_path, 'r', encoding='utf-8') as f:
    content = f.read()

for date in sorted_dates[:3]:
    d = all_news[date]
    has_wk = 'wukong_judgment' in d
    has_bj = 'bajie_conclusion' in d
    has_sg = 'sangsha_module' in d
    has_wd = 'white_dragon' in d
    print(f'  {date}: 悟空={has_wk} 八戒={has_bj} 沙僧={has_sg} 白龙马={has_wd}')

print('\n=== 完成 ===')
