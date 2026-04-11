# -*- coding: utf-8 -*-
"""最终数据合并脚本 v2 - 四层交叉分析版

执行顺序（重要）：
1. 沙僧：处理all_news → 散户情绪概率
2. 白龙马：沙僧+K线+悟空 → 主力状态（含矛盾检测）
3. 八戒融合：悟空+八戒+沙僧+白龙马 → 最终结论（含三层信号融合）

三层交叉分析：
- 白龙马 ← 悟空信号 + 沙僧信号（可信度调整）
- 八戒最终 ← 悟空分析 + 沙僧情绪 + 白龙马主力状态（四层信号融合）
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import os, json, glob, subprocess

print('=== Step 1: 收集所有数据源 ===')

all_news = {}

# 1a. news_data/ 目录
for f in sorted(glob.glob('news_data/news_*.json'), reverse=True):
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    date = d.get('date', '')
    if date:
        all_news[date] = d
        src = '悟空' if 'wukong_judgment' in d else '仅S级'
        print(f'  {date}: {src}')

# 1b. orig_2026*.json（4.07, 4.08优先）
for f in glob.glob('orig_2026*.json'):
    with open(f, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    date = d.get('date', '')
    if date:
        all_news[date] = d
        had_wk = 'wukong_judgment' in d
        src = '完整(悟空+八戒)' if had_wk else '仅S级'
        print(f'  {date}: {src} (覆盖)')

print(f'\n合并后总计: {len(all_news)} 个日期')

# ========== 2. 模型三层交叉分析 ==========
print('\n=== Step 2: 四层模型（三层交叉分析）===')
sys.path.insert(0, '.')
from market_agents.data_fetcher import get_market_data
from market_agents.sangsha_model import run_sangsha
from market_agents.white_dragon_model import run_white_dragon
from market_agents.bajie_model import run_bajie_cross

codes = ['512760', '512930', '518880', '588890', '159382']
try:
    market_data = get_market_data(codes, 7)
    print(f'市场数据: {len(market_data)} 个标的')
except Exception as e:
    print(f'Market data error: {e}')
    market_data = {}

for date in sorted(all_news.keys(), reverse=True):
    day_data = all_news[date]
    wukong = day_data.get('wukong_judgment', {})
    orig_bajie = day_data.get('bajie_conclusion', {})

    # === 沙僧（第一层：散户行为）===
    try:
        sg_result = run_sangsha({date: day_data}, date, market_data)
        sangsha = sg_result.get('沙僧模块', sg_result.get('sengseng', {}))
    except Exception as e:
        print(f'  沙僧错误 [{date}]: {e}')
        sangsha = {'overall_sentiment': '平稳', 'advice': '', 'avg_buy_prob': 50,
                  'avg_panic_prob': 30, 'analysis_results': [], 'total_news_count': 0}

    # === 白龙马（第二层：主力行为，含悟空交叉）===
    try:
        wd_result = run_white_dragon(
            market_data,
            sangsha.get('analysis_results', []),
            wukong,      # 【悟空信号】注入白龙马
            orig_bajie   # 【八戒信号】注入白龙马
        )
        white_dragon = wd_result.get('白龙马决策', {})
    except Exception as e:
        print(f'  白龙马错误 [{date}]: {e}')
        white_dragon = {'主力状态': '观望', '阶段': '观察', '综合建议': '暂无数据',
                        '悟空信号': '', '八戒胜率': '', '可信度': 1.0}

    # === 八戒融合（第三层：最终决策，含沙僧+白龙马）===
    try:
        fused_bajie = run_bajie_cross(wukong, orig_bajie, sangsha, white_dragon)
        final_bajie = {
            'optimal_action': fused_bajie.get('optimal_action', ''),
            'optimal_etfs': fused_bajie.get('optimal_etfs', ''),
            'win_rate': fused_bajie.get('win_rate', ''),
            'max_drawdown': fused_bajie.get('max_drawdown', ''),
            'holding_period': orig_bajie.get('holding_period', ''),
            # 【修复】添加 overall 字段供前端渲染
            'overall': {
                'best_action': fused_bajie.get('optimal_action', ''),
                'best_etfs': fused_bajie.get('optimal_etfs', ''),
                'win_rate': fused_bajie.get('win_rate', ''),
                'stop_loss': fused_bajie.get('max_drawdown', ''),
            },
            # 融合详情
            '沙僧信号': fused_bajie.get('沙僧信号', {}),
            '白龙马信号': fused_bajie.get('白龙马信号', {}),
            '悟空信号': fused_bajie.get('悟空信号', {}),
            '信号一致性': fused_bajie.get('信号一致性', ''),
            '信号一致性得分': fused_bajie.get('信号一致性得分', 2),
            '融合说明': fused_bajie.get('融合说明', []),
            'original_bajie': fused_bajie.get('original_bajie', {})
        }
    except Exception as e:
        print(f'  八戒融合错误 [{date}]: {e}')
        final_bajie = orig_bajie  # 回退到原始八戒

    all_news[date]['sangsha_module'] = sangsha
    all_news[date]['white_dragon'] = white_dragon
    all_news[date]['bajie_conclusion'] = final_bajie

    # 打印摘要
    sg_s = sangsha.get('overall_sentiment', '?')
    wd_s = white_dragon.get('主力状态', '?')
    wd_cred = white_dragon.get('可信度', '?')
    wd_conflict = white_dragon.get('矛盾ETF数', 0)
    bj_wr = final_bajie.get('win_rate', '?')
    bj_consistency = final_bajie.get('信号一致性', '')[:10]
    print(f'  {date}: 沙僧={sg_s} | 白龙马={wd_s}(可信{wd_cred}) | 八戒胜率={bj_wr} | 一致性={bj_consistency}')

# ========== 3. 生成输出 ==========
print('\n=== Step 3: 生成 news-data.js ===')

sorted_dates = sorted(all_news.keys(), reverse=True)

header = '// 财经新闻数据 - 四层交叉分析版\n'
header += '// 生成时间: 2026-04-10\n'
header += '// 架构: 悟空+八戒(优质新闻) → 沙僧+白龙马(全量新闻+市场数据)\n'
header += '// 三层交叉: 白龙马融合悟空信号 | 八戒融合沙僧+白龙马信号\n\n'

output_js = header + 'const newsData = ' + json.dumps(all_news, ensure_ascii=False, indent=2) + ';\n\n'
output_js += 'const availableDates = ' + json.dumps(sorted_dates, ensure_ascii=False) + ';\n\n'
output_js += '''function getNews(date) { return newsData[date] || null; }
function getPreviousDate(date) { const idx = availableDates.indexOf(date); return idx < availableDates.length - 1 ? availableDates[idx + 1] : null; }
function getNextDate(date) { const idx = availableDates.indexOf(date); return idx > 0 ? availableDates[idx - 1] : null; }'''

out_path = 'github-pages-deploy/news-data.js'
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(output_js)

# ========== 4. 验证 ==========
print('\n=== Step 4: 验证 ===')
r = subprocess.run(['node', '--check', out_path], capture_output=True, text=True)
print(f'JS语法: {"OK ✅" if r.returncode == 0 else "ERROR ❌: " + str(r.stderr)[:100]}')
print(f'日期数: {len(sorted_dates)}')
print(f'文件大小: {len(output_js)} bytes')

print('\n=== 完成 ===')
