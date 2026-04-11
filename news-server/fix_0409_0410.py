# -*- coding: utf-8 -*-
"""修正 4.09 和 4.10 新闻 - 三层交叉分析注入"""
import json, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

sys.path.insert(0, '.')
from market_agents.sangsha_model import run_sangsha
from market_agents.white_dragon_model import run_white_dragon
from market_agents.bajie_model import run_bajie_cross

# ========== 1. 读取原始数据 ==========
dates_to_fix = ['2026-04-09', '2026-04-10']

results = {}
for date in dates_to_fix:
    fname = 'news_data/news_' + date + '.json'
    try:
        with open(fname, encoding='utf-8') as f:
            d = json.load(f)
        results[date] = d
        print('\n=== ' + date + ' ===')
        print('S级: ' + str(len(d.get('s_level',[]))) + '条')
        print('A级: ' + str(len(d.get('a_level',[]))) + '条')
        print('all_news: ' + str(len(d.get('all_news',[]))) + '条')
    except FileNotFoundError:
        print(fname + ' not found')
        results[date] = {}

# ========== 2. 读取 market_data ==========
from market_agents.data_fetcher import get_market_data
codes = ['512760', '512930', '518880', '588890', '159382']
try:
    market_data = get_market_data(codes, 7)
    print('\n市场数据: ' + str(len(market_data)) + '个标的')
except Exception as e:
    print('Market data error: ' + str(e))
    market_data = {}

# ========== 3. 对每个日期运行三层分析 ==========
for date in dates_to_fix:
    d = results[date]
    if not d:
        continue

    wukong = d.get('wukong_judgment', {})
    orig_bajie = d.get('bajie_conclusion', {})

    # --- 沙僧（7天累积，含all_news）---
    try:
        # 需要构建7天数据：从4.03到4.10
        seven_day_data = {}
        for i in range(3, 11):
            fname = 'news_data/news_2026-04-' + str(i).zfill(2) + '.json'
            try:
                with open(fname, encoding='utf-8') as f:
                    day_d = json.load(f)
                seven_day_data['2026-04-' + str(i).zfill(2)] = day_d
            except FileNotFoundError:
                pass

        if seven_day_data:
            sg_result = run_sangsha(seven_day_data, date, market_data)
            sangsha = sg_result.get('沙僧模块', sg_result.get('sengseng', {}))
        else:
            # 兜底：只用当天数据
            sg_result = run_sangsha({date: d}, date, market_data)
            sangsha = sg_result.get('沙僧模块', sg_result.get('sengseng', {}))
    except Exception as e:
        print('  沙僧错误 [' + date + ']: ' + str(e))
        sangsha = {'overall_sentiment': '平稳', 'avg_buy_prob': 50, 'avg_panic_prob': 30,
                   'analysis_results': [], 'total_news_count': 0, 'advice': ''}

    # --- 白龙马（融合悟空+八戒）---
    try:
        wd_result = run_white_dragon(
            market_data,
            sangsha.get('analysis_results', []),
            wukong,
            orig_bajie
        )
        white_dragon = wd_result.get('白龙马决策', {})
    except Exception as e:
        print('  白龙马错误 [' + date + ']: ' + str(e))
        white_dragon = {'主力状态': '观望', '阶段': '观察', '综合建议': '暂无数据',
                        '可信度': 1.0, '悟空信号': '', '八戒胜率': '', '矛盾ETF数': 0,
                        '散户情绪': {'平均买入概率': 50, '平均恐慌概率': 30}}

    # --- 八戒融合（最终决策）---
    try:
        fused_bajie = run_bajie_cross(wukong, orig_bajie, sangsha, white_dragon)
        final_bajie = {
            'optimal_action': fused_bajie.get('optimal_action', ''),
            'optimal_etfs': fused_bajie.get('optimal_etfs', ''),
            'win_rate': fused_bajie.get('win_rate', ''),
            'max_drawdown': fused_bajie.get('max_drawdown', ''),
            'holding_period': orig_bajie.get('holding_period', ''),
            '沙僧信号': fused_bajie.get('沙僧信号', {}),
            '白龙马信号': fused_bajie.get('白龙马信号', {}),
            '悟空信号': fused_bajie.get('悟空信号', {}),
            '信号一致性': fused_bajie.get('信号一致性', ''),
            '融合说明': fused_bajie.get('融合说明', []),
            'original_bajie': fused_bajie.get('original_bajie', {})
        }
    except Exception as e:
        print('  八戒融合错误 [' + date + ']: ' + str(e))
        final_bajie = orig_bajie

    # --- 保存结果 ---
    results[date]['sangsha_module'] = sangsha
    results[date]['white_dragon'] = white_dragon
    results[date]['bajie_conclusion'] = final_bajie

    # --- 打印摘要 ---
    print('\n[' + date + '] 修正结果:')
    sg_s = sangsha.get('overall_sentiment', '?')
    sg_buy = sangsha.get('avg_buy_prob', '?')
    sg_panic = sangsha.get('avg_panic_prob', '?')
    wd_s = white_dragon.get('主力状态', '?')
    wd_cred = white_dragon.get('可信度', '?')
    wd_conflict = white_dragon.get('矛盾ETF数', 0)
    sg_signal = sangsha.get('advice', '')
    wd_signal = white_dragon.get('综合建议', '')[:50]

    print('  沙僧: 情绪=' + sg_s + ' | 买入=' + str(sg_buy) + '% | 恐慌=' + str(sg_panic) + '%')
    print('  白龙马: ' + wd_s + '(可信' + str(wd_cred) + ') | 矛盾ETF:' + str(wd_conflict))
    print('  八戒胜率: ' + final_bajie.get('win_rate', '?'))
    print('  八戒行动: ' + final_bajie.get('optimal_action', '?'))
    print('  一致性: ' + final_bajie.get('信号一致性', '')[:30])
    print('  融合说明:')
    for note in final_bajie.get('融合说明', []):
        print('    - ' + note[:80])

# ========== 4. 写回 news_data/ 文件 ==========
for date in dates_to_fix:
    fname = 'news_data/news_' + date + '.json'
    with open(fname, 'w', encoding='utf-8') as f:
        json.dump(results[date], f, ensure_ascii=False, indent=2)
    print('\n已写回: ' + fname)

print('\n=== 完成 ===')
