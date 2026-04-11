# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

"""测试沙僧和白龙马模型 - 使用内嵌测试数据"""

import sys
sys.path.insert(0, '.')
import json

# ========== 1. 创建测试新闻数据 ==========
test_news_data = {
    "2026-04-08": {
        "date": "2026-04-08",
        "market_tone": "科技股强势回升！创业板AI判断震荡反弹信号，AI芯片、光模块、人工智能ETF涨超7%",
        "s_level": [
            {
                "emoji": "🔴",
                "title": "AI芯片/半导体板块暴涨，创业板人工智能ETF涨超7%",
                "summary": "科创芯片ETF涨超5%，创业板AI ETF涨超7%，中际旭创涨停，光模块继续涨",
                "etfs": [
                    {"name": "588890 科创芯片ETF", "sentiment": "利好"},
                    {"name": "512930 AI人工智能ETF", "sentiment": "利好"}
                ],
                "stocks": ["中际旭创", "新易盛", "天孚通信"]
            },
            {
                "emoji": "🔴",
                "title": "创业板AI判断震荡反弹信号",
                "summary": "创业板AI判断出现反弹信号，地缘风险降低，市场风险偏好回升",
                "etfs": [
                    {"name": "512930 AI人工智能ETF", "sentiment": "利好"},
                    {"name": "518880 黄金ETF", "sentiment": "利空"}
                ],
                "stocks": ["中际旭创", "新易盛"]
            }
        ],
        "a_level": [
            {
                "emoji": "🟡",
                "title": "创业板人工智能ETF南方(159382)涨超7%",
                "summary": "创业板人工智能ETF涨停附近，跟踪创业板AI指数强势上涨",
                "etfs": [{"name": "159382 创业板AI ETF", "sentiment": "利好"}],
                "stocks": ["中际旭创", "新易盛"]
            }
        ],
        "douyin": []
    },
    "2026-04-07": {
        "date": "2026-04-07",
        "market_tone": "节后第一天反弹！美联储停火协议落地，地缘风险偏好回升，A股温和高开",
        "s_level": [
            {
                "emoji": "🔴",
                "title": "COMEX黄金突破70000美元创历史新高",
                "summary": "COMEX黄金突破70000美元大关，加密货币概念股开盘涨停，交易所概念股重配置",
                "etfs": [
                    {"name": "512760 芯片ETF", "sentiment": "利好"},
                    {"name": "515980 云计算ETF", "sentiment": "利好"}
                ],
                "stocks": ["中际旭创", "天风证券", "炒币概念股"]
            },
            {
                "emoji": "🔴",
                "title": "美联储停火协议正式落地",
                "summary": "美联储停火协议正式落地，地缘风险偏好回升。黄金从4800美元高位回落至4650美元，原油从140美元回落至106美元",
                "etfs": [
                    {"name": "512760 芯片ETF", "sentiment": "利好"},
                    {"name": "518880 黄金ETF", "sentiment": "利空"},
                    {"name": "501018 南方原油", "sentiment": "利空"}
                ],
                "stocks": ["科技龙头股"]
            }
        ],
        "a_level": [],
        "douyin": []
    },
    "2026-04-03": {
        "date": "2026-04-03",
        "market_tone": "清明假期A 股休市，海外市场剧烈分化，黄金暴跌原油大跌，科技股趋势走强",
        "s_level": [
            {
                "emoji": "🔴",
                "title": "黄金暴跌原油大跌：大商所原油暴跌逾7%",
                "summary": "4月3日大商所原油市场暴跌，大户商品恐慌性抛售，纽油期货跌破106美元/桶，日内跌超5%",
                "etfs": [
                    {"name": "518880 黄金ETF", "sentiment": "利空"},
                    {"name": "501018 南方原油", "sentiment": "利好"},
                    {"name": "513500 标普500ETF", "sentiment": "中性"}
                ],
                "stocks": ["中国石油", "中国石化", "东银黄金"]
            },
            {
                "emoji": "🔴",
                "title": "美股科技股趋势走强：AI芯片存储领涨",
                "summary": "4月3日美股三大指数收涨，AI芯片、存储板块领涨，英特尔涨1.67%，Meta涨超1%，英伟达概念股艾罗兹涨超4%",
                "etfs": [
                    {"name": "512760 芯片ETF", "sentiment": "利好"},
                    {"name": "159819 人工智能ETF", "sentiment": "利好"},
                    {"name": "588200 科创芯片ETF", "sentiment": "利好"}
                ],
                "stocks": ["中际旭创", "海光信息", "光模块股票"]
            }
        ],
        "a_level": [],
        "douyin": []
    }
}

print('✓ 测试新闻数据准备完成')

# ========== 2. 获取市场数据 ==========
from market_agents.data_fetcher import get_market_data

codes = ['512760', '512930', '518880', '588890', '159382']
market_data = get_market_data(codes, 7)
print(f'✓ 市场数据获取成功: {len(market_data)} 个标的')

for code, info in market_data.items():
    if info['klines']:
        latest = info['klines'][-1]
        print(f'  {code}: {latest["date"]} 收盘={latest["close"]} 涨跌={latest["change_pct"]}%')

# ========== 3. 运行沙僧模型 ==========
from market_agents.sangsha_model import run_sangsha

sangsha_result = run_sangsha(test_news_data, '2026-04-09', market_data)

# 兼容不同key
if '沙僧模块' in sangsha_result:
    sg = sangsha_result['沙僧模块']
elif 'sengseng' in sangsha_result:
    sg = sangsha_result['sengseng']
else:
    sg = sangsha_result

print('\n========== 沙僧模型输出 ==========')
print(f'市场情绪: {sg.get("overall_sentiment", "N/A")}')
print(f'建议: {sg.get("advice", "N/A")}')
print(f'平均买入概率: {sg.get("avg_buy_prob", "N/A")}%')
print(f'平均恐慌概率: {sg.get("avg_panic_prob", "N/A")}%')
print('\nTOP 3 最易催动散户买入的新闻:')
for i, r in enumerate(sg.get('analysis_results', [])[:3]):
    title = r.get('full_title', r.get('title', ''))[:30]
    print(f'  {i+1}. {title}...')
    print(f'     买入:{r.get("买入概率")}% 情绪:{r.get("情绪标签", [])}')

# ========== 4. 运行白龙马模型 ==========
from market_agents.white_dragon_model import run_white_dragon

dragon_result = run_white_dragon(market_data, sg.get('analysis_results', []))
wd = dragon_result.get('白龙马决策', {})

print('\n========== 白龙马模型输出 ==========')
print(f'主力状态: {wd.get("主力状态", "N/A")}')
print(f'阶段: {wd.get("阶段", "N/A")}')
print(f'是否利用散户: {wd.get("是否利用散户", "N/A")}')
print(f'行为解释: {wd.get("行为解释", "N/A")}')
print(f'综合建议: {wd.get("综合建议", "N/A")}')

# ========== 5. 写入输出文件 ==========
output_path = 'market_agents_output.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump({
        'sangsha': sangsha_result,
        'white_dragon': dragon_result
    }, f, ensure_ascii=False, indent=2)

print(f'\n✓ 结果已保存到 {output_path}')
print('\n========== 完成 ==========')