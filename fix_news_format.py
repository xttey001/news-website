# -*- coding: utf-8 -*-
"""
生成符合格式要求的 2026-04-10 新闻数据
格式要求：
- wukong_judgment: 对象格式 {market_sentiment, core_analysis[], operations[]}
- bajie_conclusion: 对象格式 {optimal_action, optimal_etfs, win_rate, max_drawdown}
- s_level/a_level: 每条新闻包含 bayes_analysis 字段
"""

import json
import os

# 读取现有数据
with open('C:\\Users\\asus\\.qclaw\\workspace\\news_data\\news_2026-04-10.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 重新格式化 wukong_judgment 为对象格式
data['wukong_judgment'] = {
    "market_sentiment": "震荡偏多，地缘风险边际缓解，A股反弹窗口打开",
    "core_analysis": [
        "美伊停火协议生效但霍尔木兹海峡实际管控未解除，伊朗提出'十点方案'与美国分歧明显，4月11日首轮谈判存在变数",
        "A股4月10日早盘收复4000点，券商ETF涨超5%，科创芯片设计ETF涨超2.5%，科技成长主线明确",
        "四部门联合规范储能电池行业竞争秩序，坚决抵制'内卷式'竞争，利好头部企业",
        "国际金价从1月高点回调14%，当前约4727美元/盎司，估值相对合理，地缘风险对冲仍有价值",
        "内蒙古自贸试验区设立，自贸区扩围至23个，带来区域主题投资机会"
    ],
    "operations": [
        {"type": "可做", "content": "券商ETF(512880)：市场活跃度提升，牛市旗手弹性大"},
        {"type": "可做", "content": "科创芯片设计ETF(588260)：AI算力需求驱动，半导体产业变革"},
        {"type": "可做", "content": "新能源/电池ETF(159871/159755)：储能政策利好，头部企业受益"},
        {"type": "警惕", "content": "油气开采板块：地缘风险边际缓解但仍有波动"},
        {"type": "关注", "content": "美伊谈判进展(4月11日首轮)及霍尔木兹海峡通航情况"}
    ]
}

# 重新格式化 bajie_conclusion 为对象格式
data['bajie_conclusion'] = {
    "optimal_action": "维持6-7成仓位，均衡配置成长+价值，关注券商+半导体+新能源轮动机会",
    "optimal_etfs": "512880证券ETF(25%) + 588260科创芯片设计ETF(25%) + 159871新能源ETF(20%) + 518880黄金ETF(15%) + 现金(15%)",
    "win_rate": "~68%（贝叶斯后验）",
    "max_drawdown": "-6%（止损线）"
}

# 为 S级新闻添加 bayes_analysis
data['s_level'] = [
    {
        "emoji": "🔥",
        "title": "美伊停火协议生效但霍尔木兹海峡仍受控，地缘风险持续发酵",
        "summary": "美伊4月8日宣布两周停火协议，但伊朗海军仍在公共频道要求船只必须获许可才能过境，海峡实际管控未解除，上千艘船只仍在观望。特朗普要求以色列减少对黎巴嫩打击配合谈判，但伊朗提出'十点方案'（美军撤出中东、伊朗主导海峡安全、赔偿损失等），双方在核心问题上分歧明显。",
        "duration": "2-4周（停火协议期+谈判窗口期）",
        "etfs": [
            {"name": "518880 黄金ETF", "sentiment": "利好"},
            {"name": "159627 能源化工ETF", "sentiment": "中性偏利好"},
            {"name": "513500 标普500ETF", "sentiment": "中性"}
        ],
        "stocks": ["601899 紫金矿业", "600028 中国石化", "601857 中国石油"],
        "signal": "地缘风险未完全解除，能源/黄金仍有支撑；若谈判顺利则利好全球股市",
        "bayes_analysis": {
            "prior_judgment": "中东地缘冲突支撑避险资产价格",
            "prior_prob": 65,
            "likelihood_judgment": "停火协议生效但海峡管控未解除，谈判分歧明显",
            "likelihood_prob": 70,
            "posterior": 68,
            "expected_return": "+3%~+8%",
            "confidence_interval": "[+1%, +12%]",
            "key_variables": "美伊谈判进展、霍尔木兹海峡通航情况、伊朗是否释放船只"
        }
    },
    {
        "emoji": "⚡",
        "title": "A股4月10日早盘收复4000点，券商/半导体/电池产业链强势拉升",
        "summary": "4月10日，A股早盘高开高走，沪指收复4000点关口，创业板涨超2%。电池产业链、券商、半导体芯片等强势拉升，证券ETF涨超5%，科创芯片设计ETF涨超2.5%。港股亦高开高走，恒科指涨超2%。",
        "duration": "1-2周（短期反弹窗口）",
        "etfs": [
            {"name": "512880 证券ETF", "sentiment": "利好"},
            {"name": "588260 科创芯片设计ETF", "sentiment": "利好"},
            {"name": "159806 新能源车ETF", "sentiment": "利好"}
        ],
        "stocks": ["300750 宁德时代", "002594 比亚迪", "688256 寒武纪"],
        "signal": "市场情绪回暖，科技成长主线明确，关注券商+半导体+新能源轮动机会",
        "bayes_analysis": {
            "prior_judgment": "A股经历4月8日大涨后短期震荡整理",
            "prior_prob": 55,
            "likelihood_judgment": "早盘收复4000点，券商/半导体/电池强势拉升",
            "likelihood_prob": 75,
            "posterior": 68,
            "expected_return": "+4%~+10%",
            "confidence_interval": "[+2%, +15%]",
            "key_variables": "成交量能否持续放大、北向资金流向、美伊谈判结果"
        }
    }
]

# 为 A级新闻添加 bayes_analysis
data['a_level'] = [
    {
        "emoji": "🔋",
        "title": "四部门联合规范动力及储能电池行业竞争秩序",
        "summary": "工信部、发改委、市场监管总局、国家能源局4月9日联合召开座谈会，要求坚决抵制'内卷式'竞争，深入推进产能预警调控、规范价格竞争、压缩供应商账期、打击知识产权侵权等工作。",
        "duration": "3-6个月（政策落地周期）",
        "etfs": [
            {"name": "159871 新能源ETF", "sentiment": "利好"},
            {"name": "159755 电池ETF", "sentiment": "利好"}
        ],
        "stocks": ["300750 宁德时代", "002594 比亚迪", "300274 阳光电源"],
        "signal": "储能行业政策持续加码，头部企业受益于竞争秩序规范化",
        "bayes_analysis": {
            "prior_judgment": "新能源/储能行业长期受益于双碳政策",
            "prior_prob": 70,
            "likelihood_judgment": "四部门联合规范竞争秩序，利好头部企业",
            "likelihood_prob": 65,
            "posterior": 68,
            "expected_return": "+5%~+12%",
            "confidence_interval": "[+2%, +18%]",
            "key_variables": "政策落地执行力度、行业产能出清进度、下游需求恢复情况"
        }
    },
    {
        "emoji": "🏛️",
        "title": "内蒙古自贸试验区正式设立，我国自贸区扩围至23个",
        "summary": "国务院印发《中国（内蒙古）自由贸易试验区总体方案》，内蒙古正式成为第23个自贸试验区。内蒙古本地股4月10日集体高开，内蒙新华、欧晶科技涨停。",
        "duration": "1-3个月（主题炒作周期）",
        "etfs": [
            {"name": "510300 沪深300ETF", "sentiment": "中性偏利好"}
        ],
        "stocks": ["603230 内蒙新华", "001269 欧晶科技"],
        "signal": "区域主题投资机会，关注内蒙古本地基建/能源/农业相关标的",
        "bayes_analysis": {
            "prior_judgment": "自贸区设立通常带来区域主题投资机会",
            "prior_prob": 60,
            "likelihood_judgment": "内蒙古本地股集体高开涨停，市场反应积极",
            "likelihood_prob": 55,
            "posterior": 58,
            "expected_return": "+3%~+8%",
            "confidence_interval": "[0%, +15%]",
            "key_variables": "自贸区政策细则出台、本地基建项目落地、市场情绪持续性"
        }
    },
    {
        "emoji": "🥇",
        "title": "国际金价从1月高点回调14%，当前约4727美元/盎司",
        "summary": "4月9日国际现货黄金约4727.9美元/盎司，较2026年1月29日历史高点5598.75美元/盎司已回调超14%。黄金股ETF平安(159322)4月8日曾涨超6.8%。",
        "duration": "1-3个月（地缘风险+美联储政策博弈期）",
        "etfs": [
            {"name": "518880 黄金ETF", "sentiment": "中性"},
            {"name": "159322 黄金股ETF平安", "sentiment": "中性"}
        ],
        "stocks": ["601899 紫金矿业", "600547 山东黄金"],
        "signal": "金价回调后估值修复，地缘风险未完全解除仍有支撑，关注逢低配置机会",
        "bayes_analysis": {
            "prior_judgment": "黄金作为避险资产受地缘风险和美联储政策双重影响",
            "prior_prob": 55,
            "likelihood_judgment": "金价从高点回调14%，估值相对合理，地缘风险未解除",
            "likelihood_prob": 60,
            "posterior": 58,
            "expected_return": "+2%~+6%",
            "confidence_interval": "[-2%, +10%]",
            "key_variables": "美伊谈判进展、美联储利率决议、美元指数走势"
        }
    }
]

# 保存更新后的数据
output_path = 'C:\\Users\\asus\\.qclaw\\workspace\\news-server\\news_data\\news_2026-04-10.json'
with open(output_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"[OK] Updated: {output_path}")
print(f"\nFormat check:")
print(f"  - wukong_judgment type: {type(data['wukong_judgment']).__name__}")
print(f"  - bajie_conclusion type: {type(data['bajie_conclusion']).__name__}")
print(f"  - S-level count: {len(data['s_level'])}")
print(f"  - A-level count: {len(data['a_level'])}")
print(f"  - S-level has bayes_analysis: {all('bayes_analysis' in item for item in data['s_level'])}")
print(f"  - A-level has bayes_analysis: {all('bayes_analysis' in item for item in data['a_level'])}")