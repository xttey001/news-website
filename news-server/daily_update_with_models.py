# -*- coding: utf-8 -*-
"""每日自动更新脚本 v3 - 四层交叉分析版

执行顺序（关键）：
1. 沙僧：处理 all_news → 散户情绪概率
2. 白龙马：沙僧 + K线 + 悟空信号 → 主力状态（含矛盾检测）
3. 八戒融合：悟空 + 原始八戒 + 沙僧 + 白龙马 → 最终结论（三层信号融合）

三层交叉分析：
- 白龙马 ← 悟空信号 + 八戒胜率（可信度调整）
- 八戒最终 ← 沙僧情绪 + 白龙马主力状态（胜率+行动调整）
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import os
import json
from datetime import datetime
import subprocess

print('=== Daily Update v3 - 四层交叉分析版 ===')

# 1. 搜索最新新闻（调用原有搜索脚本）
print('Step 1: Searching latest news...')
try:
    subprocess.run(['python', 'search_today.py'], check=True)
    print('  News search done')
except Exception as e:
    print(f'  Warning: News search failed: {e}')

# 2. 导入模型（含八戒融合模型）
sys.path.insert(0, '.')
from market_agents.data_fetcher import get_market_data
from market_agents.sangsha_model import run_sangsha
from market_agents.white_dragon_model import run_white_dragon
from market_agents.bajie_model import run_bajie_cross

# 3. 加载今天的新闻
today = datetime.now().strftime('%Y-%m-%d')
news_file = f'news_data/news_{today}.json'
NEWS_SERVER_DIR = os.getcwd()  # 保存当前目录，后续切回用

if os.path.exists(news_file):
    with open(news_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    today_news = {today: data}
    
    # 提取悟空和原始八戒结论（由Agent生成）
    wukong = data.get('wukong_judgment', {})
    orig_bajie = data.get('bajie_conclusion', {})
    print(f'  悟空: {bool(wukong)} | 原始八戒: {bool(orig_bajie)}')

    # 4. 获取市场数据
    print('Step 2: Fetching market data...')
    codes = ['512760', '512930', '518880', '588890', '159382']
    try:
        market_data = get_market_data(codes, 7)
        print(f'  Market data: {len(market_data)} codes')
    except Exception as e:
        print(f'  Market data error: {e}, using empty')
        market_data = {}
    
    # === 第一层：沙僧（散户行为预测）===
    print('Step 3: Running Sangsha model...')
    try:
        sangsha_result = run_sangsha(today_news, today, market_data)
        sangsha = sangsha_result.get('沙僧模块', sangsha_result.get('sengseng', {}))
    except Exception as e:
        print(f'  Sangsha error: {e}')
        sangsha = {'overall_sentiment': '平稳', 'advice': '', 'avg_buy_prob': 50,
                   'avg_panic_prob': 30, 'analysis_results': [], 'total_news_count': 0}
    sg_s = sangsha.get('overall_sentiment', '?')
    print(f'  沙僧情绪: {sg_s} (买入{sangsha.get("avg_buy_prob",0)}% / 恐慌{sangsha.get("avg_panic_prob",0)}%)')

    # === 第二层：白龙马（主力行为，含悟空/八戒交叉分析）===
    print('Step 4: Running WhiteDragon model (with wukong+bajie cross)...')
    try:
        wd_result = run_white_dragon(
            market_data,
            sangsha.get('analysis_results', []),
            wukong,      # 【悟空信号】注入白龙马
            orig_bajie   # 【八戒胜率】注入白龙马
        )
        white_dragon = wd_result.get('白龙马决策', {})
    except Exception as e:
        print(f'  WhiteDragon error: {e}')
        white_dragon = {'主力状态': '观望', '阶段': '观察', '综合建议': '暂无数据',
                        '悟空信号': '', '八戒胜率': '', '可信度': 1.0}
    wd_s = white_dragon.get('主力状态', '?')
    wd_cred = white_dragon.get('可信度', '?')
    print(f'  白龙马: {wd_s} (可信度{wd_cred})')

    # === 第三层：八戒融合（最终决策，融合四层信号）===
    print('Step 5: Running Bajie fusion model (cross-analysis)...')
    try:
        fused_bajie = run_bajie_cross(wukong, orig_bajie, sangsha, white_dragon)
        final_bajie = {
            'optimal_action': fused_bajie.get('optimal_action', ''),
            'optimal_etfs': fused_bajie.get('optimal_etfs', ''),
            'win_rate': fused_bajie.get('win_rate', ''),
            'max_drawdown': fused_bajie.get('max_drawdown', ''),
            'holding_period': orig_bajie.get('holding_period', ''),
            # 融合详情
            '沙僧信号': fused_bajie.get('沙僧信号', {}),
            '白龙马信号': fused_bajie.get('白龙马信号', {}),
            '悟空信号': fused_bajie.get('悟空信号', {}),
            '信号一致性': fused_bajie.get('信号一致性', ''),
            '融合说明': fused_bajie.get('融合说明', []),
            'original_bajie': fused_bajie.get('original_bajie', {})
        }
    except Exception as e:
        print(f'  Bajie fusion error: {e}, using original bajie')
        final_bajie = orig_bajie
    bj_wr = final_bajie.get('win_rate', '?')
    bj_consistency = final_bajie.get('信号一致性', '')[:20]
    print(f'  八戒最终: 胜率={bj_wr} | 一致性={bj_consistency}')

    # 6. 更新新闻文件（写入三层分析结果）
    with open(news_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    data['sangsha_module'] = sangsha
    data['white_dragon'] = white_dragon
    data['bajie_conclusion'] = final_bajie  # 覆盖为融合后的八戒
    with open(news_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f'  Updated {news_file}')
    
    # 7. 重新生成 news-data.js（也含交叉分析）
    print('Step 6: Regenerating news-data.js...')
    subprocess.run(['python', 'generate_full_newsdata.py'])
    
    # 8. 生成 news-data.js
    print('Step 7: Regenerating full news-data.js...')
    subprocess.run([sys.executable, 'generate_full_newsdata.py'])

    # 9. 推送到 news-website 仓库
    print('Step 8: Pushing to news-website...')
    os.chdir('github-pages-deploy')
    os.system('git add -A')
    os.system('git commit -m "Auto update: ' + today + ' with 4-layer cross analysis"')
    os.system('git push origin main')
    os.chdir('..')

    # 10. 同步推送到 wnews 仓库
    print('Step 9: Syncing to wnews repository...')
    import shutil
    wnews_dir = r'c:\Users\asus\wnews'
    src_js = os.path.join(os.getcwd(), 'github-pages-deploy', 'news-data.js')
    if not os.path.exists(src_js):
        src_js = os.path.join(os.getcwd(), 'news-data.js')
    
    if os.path.exists(src_js) and os.path.exists(wnews_dir):
        # 复制 news-data.js
        shutil.copy2(src_js, os.path.join(wnews_dir, 'news-data.js'))
        # 复制 index.html（如有更新版本）
        src_html = os.path.join(os.getcwd(), 'github-pages-deploy', 'index.html')
        if not os.path.exists(src_html):
            src_html = os.path.join(os.getcwd(), 'index.html')
        if os.path.exists(src_html):
            shutil.copy2(src_html, os.path.join(wnews_dir, 'index.html'))
        # 推送
        os.chdir(wnews_dir)
        os.system('git add -A')
        os.system('git commit -m "Auto update: ' + today + ' with 4-layer cross analysis"')
        os.system('git push origin main')
        os.chdir(NEWS_SERVER_DIR)
        print('  wnews pushed ✅')
    else:
        print(f'  wnews sync skipped (src={os.path.exists(src_js)}, dst={os.path.exists(wnews_dir)})')
    
    print('\n=== Done! 四层交叉分析已完成 ===')
    print(f'沙僧: {sg_s} | 白龙马: {wd_s} | 八戒胜率: {bj_wr}')
    print(f'网站1: https://xttey001.github.io/news-website/')
    print(f'网站2: https://xttey001.github.io/wnews/')
else:
    print(f'No news file for today: {news_file}')
    print('Please run search_today.py first')
