const fs = require('fs');

// 2026-04-14 完整数据
const data0414 = {
  "date": "2026-04-14",
  "market_tone": {
    "早报": "【2026-04-14早报】美军封锁霍尔木兹海峡正式生效，全球能源供应链紧张，A股开盘承压但板块分化明显",
    "晚报": "【2026-04-14晚报】A股低开高走强势反弹，锂矿光模块领涨，超2300只个股上涨，市场韧性超预期"
  },
  "all_news": [
    { "title": "美军封锁霍尔木兹海峡正式生效，能源市场高度紧张", "emoji": "🔥", "date": "2026-04-14", "summary": "美军4月14日美东时间10时正式开始封锁伊朗港口海上交通。沙特施压美国放弃行动，北约多国不参与。全球原油供应面临中断风险。" },
    { "title": "上期所调整黄金期货涨跌停板幅度", "emoji": "📊", "date": "2026-04-14", "summary": "上期所宣布调整黄金期货合约涨跌停板幅度，应对地缘风险引发的剧烈波动。黄金价格震荡加剧。" },
    { "title": "A股低开高走，创业板指大涨近4%", "emoji": "📈", "date": "2026-04-14", "summary": "A股三大指数低开后强势反弹，创业板指大涨4.81%，超2300只个股上涨，市场韧性超预期。" },
    { "title": "海南自贸港低空经济招商大会举办", "emoji": "🚁", "date": "2026-04-14", "summary": "海南自贸港举办低空经济招商大会，吸引多家企业参与，推动低空经济产业发展。" },
    { "title": "美媒称沙特施压美国放弃封锁霍尔木兹海峡", "emoji": "🌍", "date": "2026-04-14", "summary": "美媒报道沙特正在施压美国政府放弃封锁霍尔木兹海峡的行动，担心影响全球原油供应。" },
    { "title": "LME铝价升至四年新高", "emoji": "📊", "date": "2026-04-14", "summary": "伦敦金属交易所铝价升至四年新高，供应担忧推动有色金属价格上涨。" },
    { "title": "锂矿光模块板块领涨，宁德时代创历史新高", "emoji": "🔋", "date": "2026-04-14", "summary": "锂矿、光模块板块领涨A股，宁德时代盘中创历史新高，新能源产业链资金关注度高。" }
  ],
  "s_level": [
    {
      "emoji": "🔴",
      "title": "美军封锁霍尔木兹海峡正式生效（地缘风险实质升级）",
      "source": "新华社/路透社",
      "key_point": "美军4月14日美东时间10时正式开始封锁伊朗港口海上交通。沙特施压美国放弃行动，北约多国不参与。GEO-001范式：地缘升级+供应中断=油气高胜率窗口。",
      "duration": "1-4周",
      "etfs": [
        { "name": "561360 石油ETF", "sentiment": "利好" },
        { "name": "15985 能源ETF", "sentiment": "利好" }
      ],
      "stocks": ["中国石油", "中国石化", "中海油服"],
      "signal": "短期：地缘风险已实质性升级，油气板块有支撑；中期：关注沙特调停结果",
      "bayes_analysis": {
        "prior_judgment": "地缘突发事件引发供应担忧，油价短期冲高概率高",
        "prior_prob": 75,
        "likelihood_judgment": "美军封锁伊朗港口=实质性供应中断，布油已突破103美元，市场已定价部分风险",
        "likelihood_prob": 80,
        "posterior": 77,
        "expected_return": "石油ETF短期+5%~+12%",
        "confidence_interval": "[-8%, +15%]",
        "key_variables": "沙特调停结果、伊朗反制措施、北约国家立场"
      }
    }
  ],
  "a_level": [
    {
      "emoji": "🟡",
      "title": "A股低开高走创业板指大涨4.81%",
      "source": "证券时报",
      "key_point": "A股展现强劲韧性，超2300只个股上涨，锂矿光模块领涨。宁德时代、中际旭创创历史新高。",
      "duration": "1-3天",
      "etfs": [{ "name": "515930 创业板ETF", "sentiment": "利好" }],
      "stocks": ["宁德时代", "中际旭创", "中国巨石"],
      "signal": "短期：市场情绪修复，科技股领涨",
      "bayes_analysis": {
        "prior_judgment": "地缘风险下市场通常承压，但A股韧性超预期",
        "prior_prob": 50,
        "likelihood_judgment": "超2300只个股上涨+龙头创新高=资金做多意愿强",
        "likelihood_prob": 70,
        "posterior": 58,
        "expected_return": "创业板ETF短期+2%~+5%",
        "confidence_interval": "[-5%, +8%]",
        "key_variables": "量能持续性、宁德时代走势"
      }
    },
    {
      "emoji": "🟡",
      "title": "上期所调整黄金期货涨跌停板",
      "source": "上期所",
      "key_point": "监管应对地缘波动，黄金期货波动加大。",
      "duration": "1-3天",
      "etfs": [{ "name": "518880 黄金ETF", "sentiment": "中性" }],
      "stocks": ["山东黄金", "中金黄金"],
      "signal": "短期：金价震荡加剧，观望为主",
      "bayes_analysis": {
        "prior_judgment": "地缘风险推高黄金避险需求",
        "prior_prob": 60,
        "likelihood_judgment": "监管调整涨跌停板=波动加大，避险情绪边际减弱",
        "likelihood_prob": 45,
        "posterior": 52,
        "expected_return": "黄金ETF短期-3%~+3%",
        "confidence_interval": "[-6%, +6%]",
        "key_variables": "地缘缓和进度、美元走势"
      }
    }
  ],
  "douyin": [],
  "wukong_judgment": {
    "market_sentiment": "谨慎偏多",
    "core_analysis": [
      "地缘风险实质性升级，但A股展现韧性，低开高走说明市场承接力强",
      "锂矿光模块领涨，科技股主线明确",
      "宁德时代创历史新高，资金抱团核心资产",
      "美沙角力伊朗局势，能源板块短期有支撑"
    ],
    "operations": [
      { "type": "可做", "content": "锂矿/光模块/AI算力核心标的" },
      { "type": "关注", "content": "油气板块，地缘溢价已部分定价" },
      { "type": "警惕", "content": "追高黄金，地缘风险边际减弱" }
    ]
  },
  "bajie_conclusion": {
    "optimal_action": "轻仓参与科技主线",
    "optimal_etfs": "创业板ETF(20%)+芯片ETF(15%)",
    "win_rate": "~58%",
    "max_drawdown": "-8%",
    "overall": {
      "best_action": "轻仓参与科技主线",
      "best_etfs": "创业板ETF+芯片ETF",
      "win_rate": "58%",
      "stop_loss": "-8%"
    },
    "融合说明": ["市场韧性超预期，但地缘不确定性仍在，建议轻仓博弈"]
  },
  "sangsha_module": {
    "overall_sentiment": "积极",
    "advice": "可适度参与",
    "avg_buy_prob": 52,
    "avg_panic_prob": 15,
    "analysis_results": [
      {
        "news": "美军封锁霍尔木兹海峡正式生效，能源市场高度紧张",
        "title": "美军封锁霍尔木兹海峡正式生效",
        "full_title": "美军封锁霍尔木兹海峡正式生效，能源市场高度紧张",
        "summary": "美军4月14日美东时间10时正式开始封锁伊朗港口海上交通。沙特施压美国放弃行动，北约多国不参与。",
        "追高买入概率": 85,
        "抄底买入概率": 5,
        "恐慌卖出概率": 8,
        "观望概率": 15,
        "情绪标签": ["FOMO", "易懂"],
        "韭菜行为总结": "散户担心油价暴涨，想追油气",
        "市场含义": "顶部风险",
        "买入概率": 62,
        "is_long_term": false,
        "date": "2026-04-14",
        "decay": 1.0,
        "weighted_buy_prob": 62
      },
      {
        "news": "上期所调整黄金期货涨跌停板幅度",
        "title": "上期所调整黄金期货涨跌停板幅度",
        "full_title": "上期所调整黄金期货涨跌停板幅度",
        "summary": "上期所宣布调整黄金期货合约涨跌停板幅度，应对地缘风险引发的剧烈波动。",
        "追高买入概率": 25,
        "抄底买入概率": 10,
        "恐慌卖出概率": 20,
        "观望概率": 55,
        "情绪标签": ["观望", "复杂"],
        "韭菜行为总结": "散户看不懂，观望为主",
        "市场含义": "分歧加大",
        "买入概率": 22,
        "is_long_term": false,
        "date": "2026-04-14",
        "decay": 1.0,
        "weighted_buy_prob": 22
      },
      {
        "news": "A股低开高走，创业板指大涨近4%",
        "title": "A股低开高走，创业板指大涨近4%",
        "full_title": "A股低开高走，创业板指大涨近4%",
        "summary": "A股三大指数低开后强势反弹，创业板指大涨4.81%，超2300只个股上涨。",
        "追高买入概率": 78,
        "抄底买入概率": 5,
        "恐慌卖出概率": 5,
        "观望概率": 20,
        "情绪标签": ["FOMO", "易懂"],
        "韭菜行为总结": "散户疯了，都在追！创业板大涨太诱人",
        "市场含义": "顶部风险",
        "买入概率": 58,
        "is_long_term": false,
        "date": "2026-04-14",
        "decay": 1.0,
        "weighted_buy_prob": 58
      },
      {
        "news": "海南自贸港低空经济招商大会举办",
        "title": "海南自贸港低空经济招商大会举办",
        "full_title": "海南自贸港低空经济招商大会举办",
        "summary": "海南自贸港举办低空经济招商大会，吸引多家企业参与。",
        "追高买入概率": 45,
        "抄底买入概率": 15,
        "恐慌卖出概率": 5,
        "观望概率": 45,
        "情绪标签": ["关注"],
        "韭菜行为总结": "散户开始关注低空经济概念",
        "市场含义": "分歧加大",
        "买入概率": 38,
        "is_long_term": false,
        "date": "2026-04-14",
        "decay": 1.0,
        "weighted_buy_prob": 38
      },
      {
        "news": "美媒称沙特施压美国放弃封锁霍尔木兹海峡",
        "title": "美媒称沙特施压美国放弃封锁霍尔木兹海峡",
        "full_title": "美媒称沙特施压美国放弃封锁霍尔木兹海峡",
        "summary": "美媒报道沙特正在施压美国政府放弃封锁霍尔木兹海峡的行动。",
        "追高买入概率": 10,
        "抄底买入概率": 20,
        "恐慌卖出概率": 5,
        "观望概率": 70,
        "情绪标签": ["观望", "复杂"],
        "韭菜行为总结": "散户看不清局势，观望",
        "市场含义": "中性",
        "买入概率": 18,
        "is_long_term": false,
        "date": "2026-04-14",
        "decay": 1.0,
        "weighted_buy_prob": 18
      },
      {
        "news": "LME铝价升至四年新高",
        "title": "LME铝价升至四年新高",
        "full_title": "LME铝价升至四年新高",
        "summary": "伦敦金属交易所铝价升至四年新高，供应担忧推动有色金属价格上涨。",
        "追高买入概率": 65,
        "抄底买入概率": 5,
        "恐慌卖出概率": 5,
        "观望概率": 30,
        "情绪标签": ["FOMO", "易懂"],
        "韭菜行为总结": "散户想追有色金属",
        "市场含义": "分歧加大",
        "买入概率": 48,
        "is_long_term": false,
        "date": "2026-04-14",
        "decay": 1.0,
        "weighted_buy_prob": 48
      },
      {
        "news": "锂矿光模块板块领涨，宁德时代创历史新高",
        "title": "锂矿光模块板块领涨，宁德时代创历史新高",
        "full_title": "锂矿光模块板块领涨，宁德时代创历史新高",
        "summary": "锂矿、光模块板块领涨A股，宁德时代盘中创历史新高。",
        "追高买入概率": 82,
        "抄底买入概率": 5,
        "恐慌卖出概率": 3,
        "观望概率": 15,
        "情绪标签": ["FOMO", "易懂"],
        "韭菜行为总结": "散户疯了！宁德时代创新高必须追！",
        "市场含义": "顶部风险",
        "买入概率": 60,
        "is_long_term": false,
        "date": "2026-04-14",
        "decay": 1.0,
        "weighted_buy_prob": 60
      }
    ]
  },
  "white_dragon": {
    "主力状态": "吸筹",
    "阶段": "早期",
    "行为解释": "放量上涨+散户追高→主力在吸筹",
    "是否利用散户": false,
    "综合建议": "✅ 可适度参与"
  },
  "tang_sanzang": {
    "仓位": "35%",
    "最终行动": "轻仓布局科技主线",
    "仲裁矛盾": [
      { "类型": "地缘不确定性", "描述": "霍尔木兹封锁+沙特调停并存", "唐憎系数": "×0.7" }
    ],
    "仓位公式": {
      "基础仓位": "58%（八戒胜率）",
      "唐憎系数": "0.7（地缘不确定）",
      "风控系数": "1.0",
      "结果": "35%"
    },
    "风控触发": [],
    "唐僧结论": "轻仓博弈科技主线，止损-8%"
  },
  "decision_matrix": [
    { "新闻": "美军封锁霍尔木兹海峡", "做多概率": "77%", "预期收益": "+5%~+12%", "风险比": "1:2", "建议": "✅ 可做" },
    { "新闻": "A股低开高走创业板涨", "做多概率": "58%", "预期收益": "+2%~+5%", "风险比": "1:1.5", "建议": "⚠️ 轻仓" },
    { "新闻": "黄金涨跌停板调整", "做多概率": "52%", "预期收益": "-3%~+3%", "风险比": "1:1", "建议": "⚠️ 观望" }
  ]
};

// 2026-04-15 完整数据
const data0415 = {
  "date": "2026-04-15",
  "market_tone": {
    "早报": "【2026-04-15早报】霍尔木兹海峡部分恢复通航，特朗普称'美伊战争已结束'，避险情绪降温",
    "晚报": "【2026-04-15晚报】A股高开低走创业板指跌超1%，医药商业航天逆势走强，市场分歧加大"
  },
  "all_news": [
    { "title": "霍尔木兹海峡部分恢复通航，特朗普称美伊战争已结束", "emoji": "🕊️", "date": "2026-04-15", "summary": "24小时内超20艘商船通过海峡，特朗普发推称'美伊战争已结束'，地缘风险快速降温。" },
    { "title": "A股高开低走，创业板指创新高后跌超1%", "emoji": "📉", "date": "2026-04-15", "summary": "A股高开后走弱，创业板指盘中创新高后回落跌超1%，医药商业航天逆势走强。" },
    { "title": "包钢厂区爆炸78人送医，容百科技被立案调查", "emoji": "⚠️", "date": "2026-04-15", "summary": "包钢厂区发生爆炸事故78人送医，容百科技因重大合同公告涉嫌误导性陈述被证监会立案调查。" },
    { "title": "国资委召开低空经济产业发展专题推进会", "emoji": "🚁", "date": "2026-04-15", "summary": "国资委召开央企低空经济产业发展专题推进会，要求加快低空航空装备创新迭代。" },
    { "title": "康众医疗拟4亿现金收购AI医疗公司脉得智能", "emoji": "🤖", "date": "2026-04-15", "summary": "康众医疗公告拟以4亿元现金收购AI医疗公司脉得智能100%股权。" },
    { "title": "美元人民币汇率6.8，黄金4867美元上涨", "emoji": "💰", "date": "2026-04-15", "summary": "美元兑人民币汇率报6.8，黄金价格4867美元上涨，市场情绪分化。" },
    { "title": "医药商业航天概念逆势走强", "emoji": "💊", "date": "2026-04-15", "summary": "医药、商业航天概念股逆势走强，资金防御性配置明显。" }
  ],
  "s_level": [
    {
      "emoji": "🔴",
      "title": "霍尔木兹海峡恢复通航+特朗普称战争结束（地缘风险快速降温）",
      "source": "微博/新华社",
      "key_point": "24小时内超20艘商船通过海峡，特朗普称'美伊战争已结束'。GEO-001范式：地缘缓和=避险资产快速回撤。",
      "duration": "1-2天",
      "etfs": [
        { "name": "518880 黄金ETF", "sentiment": "利空" },
        { "name": "561360 石油ETF", "sentiment": "利空" }
      ],
      "stocks": ["山东黄金", "中金黄金", "中国石油"],
      "signal": "短期：避险逻辑快速瓦解，油气黄金承压",
      "bayes_analysis": {
        "prior_judgment": "地缘缓和导致避险资产回撤",
        "prior_prob": 70,
        "likelihood_judgment": "特朗普明确表态'战争结束'+20艘商船通过=缓和信号明确",
        "likelihood_prob": 85,
        "posterior": 78,
        "expected_return": "黄金/石油ETF短期-5%~-10%",
        "confidence_interval": "[-12%, +3%]",
        "key_variables": "谈判重启进度、伊朗核计划立场"
      }
    }
  ],
  "a_level": [
    {
      "emoji": "🟡",
      "title": "A股高开低走创业板指跌超1%",
      "source": "每日经济新闻",
      "key_point": "市场分歧加大，医药商业航天逆势走强，锂电池存储芯片调整。",
      "duration": "1-3天",
      "etfs": [
        { "name": "512010 医药ETF", "sentiment": "利好" },
        { "name": "159920 半导体ETF", "sentiment": "利空" }
      ],
      "stocks": ["恒瑞医药", "药明康德", "宁德时代"],
      "signal": "短期：震荡分化，关注医药低吸机会",
      "bayes_analysis": {
        "prior_judgment": "创业板新高后通常有获利了结压力",
        "prior_prob": 55,
        "likelihood_judgment": "高开低走+成交缩量=资金分歧加大",
        "likelihood_prob": 60,
        "posterior": 57,
        "expected_return": "医药ETF短期+2%~+5%",
        "confidence_interval": "[-4%, +8%]",
        "key_variables": "量能变化、医药板块持续性"
      }
    },
    {
      "emoji": "🟡",
      "title": "国资委推进低空经济产业发展",
      "source": "国资委",
      "key_point": "央企低空经济专题会，加快航空装备创新迭代。",
      "duration": "1-4周",
      "etfs": [{ "name": "588560 航空航天ETF", "sentiment": "利好" }],
      "stocks": ["中航沈飞", "中航西飞", "纵横股份"],
      "signal": "中期：低空经济政策持续加码",
      "bayes_analysis": {
        "prior_judgment": "政策利好推动板块上涨",
        "prior_prob": 65,
        "likelihood_judgment": "国资委专题会=政策级别高，产业资本关注度提升",
        "likelihood_prob": 70,
        "posterior": 67,
        "expected_return": "航空航天ETF中期+5%~+15%",
        "confidence_interval": "[-6%, +18%]",
        "key_variables": "政策落地节奏、订单释放"
      }
    },
    {
      "emoji": "🟡",
      "title": "容百科技被立案调查+包钢爆炸事故",
      "source": "证监会/界面新闻",
      "key_point": "容百科技重大合同公告涉嫌误导性陈述被立案，包钢爆炸事故78人送医。",
      "duration": "1-3天",
      "etfs": [],
      "stocks": ["容百科技", "包钢股份"],
      "signal": "回避相关个股",
      "bayes_analysis": {
        "prior_judgment": "利空事件导致股价下跌",
        "prior_prob": 80,
        "likelihood_judgment": "证监会立案=监管风险明确，包钢爆炸=安全生产风险",
        "likelihood_prob": 90,
        "posterior": 85,
        "expected_return": "相关个股短期-10%~-20%",
        "confidence_interval": "[-25%, -5%]",
        "key_variables": "调查结果、事故调查进展"
      }
    }
  ],
  "douyin": [],
  "wukong_judgment": {
    "market_sentiment": "中性分歧",
    "core_analysis": [
      "地缘风险快速降温，避险逻辑瓦解，黄金油气承压",
      "A股高开低走显示市场分歧，创业板新高后获利了结",
      "医药商业航天逆势走强，资金寻找新主线",
      "低空经济政策加码，中期逻辑清晰"
    ],
    "operations": [
      { "type": "可做", "content": "医药板块低吸" },
      { "type": "警惕", "content": "追高油气黄金" },
      { "type": "关注", "content": "低空经济产业链龙头" }
    ]
  },
  "bajie_conclusion": {
    "optimal_action": "观望为主轻仓医药",
    "optimal_etfs": "医药ETF(15%)+航空航天ETF(10%)",
    "win_rate": "~45%",
    "max_drawdown": "-6%",
    "overall": {
      "best_action": "观望为主轻仓医药",
      "best_etfs": "医药ETF+航空航天ETF",
      "win_rate": "45%",
      "stop_loss": "-6%"
    },
    "融合说明": ["地缘缓和引发避险资产回撤，市场分歧加大，建议降低仓位"]
  },
  "sangsha_module": {
    "overall_sentiment": "分歧",
    "advice": "震荡分化，观望为主",
    "avg_buy_prob": 38,
    "avg_panic_prob": 25,
    "analysis_results": [
      {
        "news": "霍尔木兹海峡部分恢复通航，特朗普称美伊战争已结束",
        "title": "霍尔木兹海峡部分恢复通航",
        "full_title": "霍尔木兹海峡部分恢复通航，特朗普称美伊战争已结束",
        "summary": "24小时内超20艘商船通过海峡，特朗普发推称'美伊战争已结束'。",
        "追高买入概率": 5,
        "抄底买入概率": 10,
        "恐慌卖出概率": 45,
        "观望概率": 45,
        "情绪标签": ["恐慌", "易懂"],
        "韭菜行为总结": "散户恐慌卖出油气黄金，避险资产遭抛售",
        "市场含义": "底部可能",
        "买入概率": 22,
        "is_long_term": false,
        "date": "2026-04-15",
        "decay": 1.0,
        "weighted_buy_prob": 22
      },
      {
        "news": "A股高开低走，创业板指创新高后跌超1%",
        "title": "A股高开低走，创业板指跌超1%",
        "full_title": "A股高开低走，创业板指创新高后跌超1%",
        "summary": "A股高开后走弱，创业板指盘中创新高后回落跌超1%。",
        "追高买入概率": 35,
        "抄底买入概率": 20,
        "恐慌卖出概率": 25,
        "观望概率": 35,
        "情绪标签": ["恐慌", "复杂"],
        "韭菜行为总结": "散户看不懂，高开低走太坑，想跑又舍不得",
        "市场含义": "分歧加大",
        "买入概率": 32,
        "is_long_term": false,
        "date": "2026-04-15",
        "decay": 1.0,
        "weighted_buy_prob": 32
      },
      {
        "news": "包钢厂区爆炸78人送医，容百科技被立案调查",
        "title": "包钢爆炸+容百科技被立案",
        "full_title": "包钢厂区爆炸78人送医，容百科技被立案调查",
        "summary": "包钢厂区发生爆炸事故，容百科技因公告涉嫌误导性陈述被立案。",
        "追高买入概率": 5,
        "抄底买入概率": 5,
        "恐慌卖出概率": 65,
        "观望概率": 30,
        "情绪标签": ["恐慌", "易懂"],
        "韭菜行为总结": "散户恐慌，赶紧跑！立案调查太可怕",
        "市场含义": "恐慌底部",
        "买入概率": 12,
        "is_long_term": false,
        "date": "2026-04-15",
        "decay": 1.0,
        "weighted_buy_prob": 12
      },
      {
        "news": "国资委召开低空经济产业发展专题推进会",
        "title": "国资委推进低空经济产业发展",
        "full_title": "国资委召开低空经济产业发展专题推进会",
        "summary": "国资委召开央企低空经济产业发展专题推进会。",
        "追高买入概率": 55,
        "抄底买入概率": 10,
        "恐慌卖出概率": 5,
        "观望概率": 35,
        "情绪标签": ["FOMO", "易懂"],
        "韭菜行为总结": "散户觉得低空经济是机会，想跟政策走",
        "市场含义": "分歧加大",
        "买入概率": 42,
        "is_long_term": false,
        "date": "2026-04-15",
        "decay": 1.0,
        "weighted_buy_prob": 42
      },
      {
        "news": "康众医疗拟4亿现金收购AI医疗公司脉得智能",
        "title": "康众医疗收购AI医疗公司",
        "full_title": "康众医疗拟4亿现金收购AI医疗公司脉得智能",
        "summary": "康众医疗公告拟以4亿元现金收购AI医疗公司脉得智能。",
        "追高买入概率": 40,
        "抄底买入概率": 15,
        "恐慌卖出概率": 5,
        "观望概率": 45,
        "情绪标签": ["关注"],
        "韭菜行为总结": "散户关注AI医疗概念",
        "市场含义": "中性",
        "买入概率": 35,
        "is_long_term": false,
        "date": "2026-04-15",
        "decay": 1.0,
        "weighted_buy_prob": 35
      },
      {
        "news": "美元人民币汇率6.8，黄金4867美元上涨",
        "title": "美元人民币汇率6.8，黄金上涨",
        "full_title": "美元人民币汇率6.8，黄金4867美元上涨",
        "summary": "美元兑人民币汇率报6.8，黄金价格4867美元上涨。",
        "追高买入概率": 25,
        "抄底买入概率": 15,
        "恐慌卖出概率": 10,
        "观望概率": 55,
        "情绪标签": ["观望", "复杂"],
        "韭菜行为总结": "散户看不懂汇率和黄金走势",
        "市场含义": "中性",
        "买入概率": 25,
        "is_long_term": false,
        "date": "2026-04-15",
        "decay": 1.0,
        "weighted_buy_prob": 25
      },
      {
        "news": "医药商业航天概念逆势走强",
        "title": "医药商业航天逆势走强",
        "full_title": "医药商业航天概念逆势走强",
        "summary": "医药、商业航天概念股逆势走强，资金防御性配置明显。",
        "追高买入概率": 60,
        "抄底买入概率": 10,
        "恐慌卖出概率": 5,
        "观望概率": 30,
        "情绪标签": ["FOMO", "易懂"],
        "韭菜行为总结": "散户觉得医药安全，想避险买医药",
        "市场含义": "分歧加大",
        "买入概率": 45,
        "is_long_term": false,
        "date": "2026-04-15",
        "decay": 1.0,
        "weighted_buy_prob": 45
      }
    ]
  },
  "white_dragon": {
    "主力状态": "洗盘",
    "阶段": "早期",
    "行为解释": "缩量下跌+横盘震荡→主力在洗盘",
    "是否利用散户": false,
    "综合建议": "⚠️ 观望等待企稳"
  },
  "tang_sanzang": {
    "仓位": "25%",
    "最终行动": "观望为主，轻仓医药",
    "仲裁矛盾": [
      { "类型": "方向分歧", "描述": "地缘缓和vs市场分歧", "唐憎系数": "×0.6" }
    ],
    "仓位公式": {
      "基础仓位": "45%（八戒胜率）",
      "唐憎系数": "0.6（方向分歧）",
      "风控系数": "1.0",
      "结果": "25%"
    },
    "风控触发": [],
    "唐僧结论": "降低仓位观望，轻仓医药试水"
  },
  "decision_matrix": [
    { "新闻": "霍尔木兹海峡恢复通航", "做多概率": "22%", "预期收益": "-5%~-10%", "风险比": "1:0.5", "建议": "❌ 回避" },
    { "新闻": "A股高开低走创业板跌", "做多概率": "43%", "预期收益": "-2%~+3%", "风险比": "1:1", "建议": "⚠️ 观望" },
    { "新闻": "国资委推进低空经济", "做多概率": "67%", "预期收益": "+5%~+15%", "风险比": "1:2.5", "建议": "✅ 可做" },
    { "新闻": "容百科技被立案调查", "做多概率": "15%", "预期收益": "-10%~-20%", "风险比": "1:0.2", "建议": "❌ 回避" }
  ]
};

// 2026-04-16 完整数据
const data0416 = {
  "date": "2026-04-16",
  "market_tone": {
    "早报": "【2026-04-16早报】一季度GDP同比增5%超预期，经济开局良好，A股集体高开",
    "晚报": "【2026-04-16晚报】A股集体大涨创业板指涨超3%，宁德时代AH股双双创历史新高，亚太股市全线飘红"
  },
  "all_news": [
    { "title": "一季度GDP同比增5.0%，中国经济开局良好", "emoji": "📊", "date": "2026-04-16", "summary": "国家统计局4月16日发布数据，一季度GDP33.4万亿元，同比增长5.0%，比去年Q4回升0.5个百分点。CPI同比上涨0.9%，居民收入实际增4%。" },
    { "title": "A股集体大涨，创业板指涨超3%，超4400只个股上涨", "emoji": "🚀", "date": "2026-04-16", "summary": "A股三大指数大幅高开高走，科创综指盘中大涨逾3%，上证指数收复3900点，创业板指大涨超3%站上3200点。超4400只个股上涨。" },
    { "title": "宁德时代AH股双双创历史新高，市值破2万亿", "emoji": "🔋", "date": "2026-04-16", "summary": "宁德时代A股涨超4%，H股大涨超10%，双双创历史新高。A股总市值突破2万亿元大关。" },
    { "title": "它石智航完成4.5亿美元Pre-A轮融资，创中国具身智能纪录", "emoji": "🤖", "date": "2026-04-16", "summary": "它石智航宣布完成超4.5亿美元Pre-A轮融资，创下中国具身智能有史以来最高单轮融资纪录。" },
    { "title": "一季度居民人均可支配收入实际增长4%", "emoji": "💰", "date": "2026-04-16", "summary": "国家统计局披露，一季度全国居民人均可支配收入实际增长4%。3月份社会消费品零售总额同比增长1.7%。" },
    { "title": "3月原油加工由增转降，工业生产稳定", "emoji": "🛢️", "date": "2026-04-16", "summary": "3月份规模以上工业原油加工由增转降，原煤生产规模稳定，原油生产保持稳定。能源供给侧运行平稳。" },
    { "title": "特斯拉宣布对欧盟110亿美元商品征收关税", "emoji": "⚔️", "date": "2026-04-16", "summary": "特朗普在推特宣布美国将对价值110亿美元的欧盟产品征收关税，称欧盟给空客的补贴对美国产生负面影响。" },
    { "title": "国资委要求加快低空航空装备创新迭代", "emoji": "🚁", "date": "2026-04-16", "summary": "国务院国资委强调央企要加快低空航空装备创新迭代，推动低空经济产业高质量发展。" },
    { "title": "日经225创历史新高，亚太股市全线飘红", "emoji": "📈", "date": "2026-04-16", "summary": "日经225指数涨2.38%创历史新高，韩国指数涨2.21%，亚太股市全线飘红。" }
  ],
  "s_level": [
    {
      "emoji": "🔴",
      "title": "一季度GDP同比增5.0%超预期（宏观经济强劲开局）",
      "source": "国家统计局/央广网",
      "key_point": "一季度GDP增长5.0%超预期，比去年Q4回升0.5个百分点。CPI温和上涨0.9%，居民收入实际增4%，消费零售增长。经济数据全面向好，A股基本面支撑强。",
      "duration": "1-4周",
      "etfs": [
        { "name": "515930 创业板ETF", "sentiment": "利好" },
        { "name": "510300 沪深300ETF", "sentiment": "利好" }
      ],
      "stocks": ["宁德时代", "中国中免", "贵州茅台"],
      "signal": "中期：经济基本面支撑A股，可增加权益仓位",
      "bayes_analysis": {
        "prior_judgment": "GDP数据超预期通常推动股市上涨",
        "prior_prob": 70,
        "likelihood_judgment": "GDP增5%+收入增4%+消费回暖=经济复苏确立，数据质量高",
        "likelihood_prob": 85,
        "posterior": 78,
        "expected_return": "沪深300ETF中期+5%~+15%",
        "confidence_interval": "[-5%, +18%]",
        "key_variables": "后续消费数据、政策支持力度"
      }
    },
    {
      "emoji": "🔴",
      "title": "宁德时代AH股创历史新高，市值破2万亿",
      "source": "证券时报",
      "key_point": "宁德时代A股涨超4%、H股涨超10%双双创历史新高，市值破2万亿。龙头公司持续创新高，说明机构资金核心资产牛市。",
      "duration": "1-2周",
      "etfs": [
        { "name": "159755 锂电池ETF", "sentiment": "利好" },
        { "name": "515930 创业板ETF", "sentiment": "利好" }
      ],
      "stocks": ["宁德时代", "比亚迪", "亿纬锂能"],
      "signal": "短期：龙头领涨，锂电池板块可跟随",
      "bayes_analysis": {
        "prior_judgment": "龙头创新高通常带动板块上涨",
        "prior_prob": 75,
        "likelihood_judgment": "AH股双双创新高+市值破2万亿=资金抱团强化，趋势明确",
        "likelihood_prob": 85,
        "posterior": 80,
        "expected_return": "锂电池ETF短期+3%~+8%",
        "confidence_interval": "[-4%, +12%]",
        "key_variables": "宁德时代持续性、板块跟涨力度"
      }
    }
  ],
  "a_level": [
    {
      "emoji": "🟡",
      "title": "A股集体大涨创业板指涨超3%",
      "source": "证券时报",
      "key_point": "超4400只个股上涨，成交放量。日经225创历史新高，亚太股市全线飘红。",
      "duration": "1-3天",
      "etfs": [{ "name": "515930 创业板ETF", "sentiment": "利好" }],
      "stocks": ["宁德时代", "中际旭创", "东方财富"],
      "signal": "短期：情绪高涨，可积极参与",
      "bayes_analysis": {
        "prior_judgment": "亚太股市联动上涨推动A股",
        "prior_prob": 65,
        "likelihood_judgment": "超4400只个股上涨+日经创新高=情绪高涨，做多窗口开启",
        "likelihood_prob": 80,
        "posterior": 72,
        "expected_return": "创业板ETF短期+2%~+6%",
        "confidence_interval": "[-3%, +8%]",
        "key_variables": "量能持续性、亚太股市走势"
      }
    },
    {
      "emoji": "🟡",
      "title": "它石智航完成4.5亿美元融资",
      "source": "证券时报",
      "key_point": "中国具身智能最大单轮融资，AI机器人赛道热度持续。",
      "duration": "1-2周",
      "etfs": [{ "name": "515070 AI智能ETF", "sentiment": "利好" }],
      "stocks": ["机器人概念股", "AI算力龙头"],
      "signal": "中期：具身智能赛道持续关注",
      "bayes_analysis": {
        "prior_judgment": "大额融资推动AI板块热度",
        "prior_prob": 60,
        "likelihood_judgment": "4.5亿美元创纪录融资+明星资本集结=产业看好度高",
        "likelihood_prob": 75,
        "posterior": 68,
        "expected_return": "AI智能ETF中期+5%~+12%",
        "confidence_interval": "[-6%, +15%]",
        "key_variables": "后续融资节奏、政策支持"
      }
    },
    {
      "emoji": "🟡",
      "title": "特朗普对欧盟征收110亿美元关税",
      "source": "上观新闻",
      "key_point": "贸易战再度升温，欧美贸易摩擦加剧。",
      "duration": "1-4周",
      "etfs": [],
      "stocks": ["出口欧洲板块谨慎"],
      "signal": "关注贸易摩擦升级风险",
      "bayes_analysis": {
        "prior_judgment": "贸易摩擦增加市场不确定性",
        "prior_prob": 40,
        "likelihood_judgment": "特朗普关税威胁=短期避险情绪升温，但实际影响待观察",
        "likelihood_prob": 50,
        "posterior": 45,
        "expected_return": "不确定性高",
        "confidence_interval": "[-8%, +4%]",
        "key_variables": "欧盟反制措施、是否波及中国"
      }
    }
  ],
  "douyin": [],
  "wukong_judgment": {
    "market_sentiment": "积极做多",
    "core_analysis": [
      "一季度GDP增5%超预期，经济基本面强劲",
      "宁德时代AH股双双创新高，龙头股牛市确立",
      "A股集体大涨，超4400只个股上涨，情绪高涨",
      "它石智航融资创纪录，AI具身智能赛道热度不减",
      "亚太股市全线飘红，风险偏好上升"
    ],
    "operations": [
      { "type": "可做", "content": "锂电池/AI算力/核心资产" },
      { "type": "可做", "content": "增加仓位，把握做多窗口" },
      { "type": "关注", "content": "低空经济政策持续加码" }
    ]
  },
  "bajie_conclusion": {
    "optimal_action": "积极做多核心资产",
    "optimal_etfs": "创业板ETF(40%)+锂电池ETF(20%)+AI智能ETF(15%)",
    "win_rate": "~72%",
    "max_drawdown": "-10%",
    "overall": {
      "best_action": "积极做多核心资产",
      "best_etfs": "创业板ETF+锂电池ETF+AI智能ETF",
      "win_rate": "72%",
      "stop_loss": "-10%"
    },
    "融合说明": ["经济数据超预期+龙头创新高+情绪高涨=做多窗口开启"]
  },
  "sangsha_module": {
    "overall_sentiment": "狂热",
    "advice": "积极参与，注意风险",
    "avg_buy_prob": 68,
    "avg_panic_prob": 8,
    "analysis_results": [
      {
        "news": "一季度GDP同比增5.0%，中国经济开局良好",
        "title": "一季度GDP同比增5.0%",
        "full_title": "一季度GDP同比增5.0%，中国经济开局良好",
        "summary": "国家统计局4月16日发布数据，一季度GDP33.4万亿元，同比增长5.0%，比去年Q4回升0.5个百分点。",
        "追高买入概率": 82,
        "抄底买入概率": 5,
        "恐慌卖出概率": 3,
        "观望概率": 15,
        "情绪标签": ["FOMO", "易懂"],
        "韭菜行为总结": "散户觉得经济好=A股要涨，赶紧追！",
        "市场含义": "顶部风险",
        "买入概率": 62,
        "is_long_term": false,
        "date": "2026-04-16",
        "decay": 1.0,
        "weighted_buy_prob": 62
      },
      {
        "news": "A股集体大涨，创业板指涨超3%，超4400只个股上涨",
        "title": "A股集体大涨创业板指涨超3%",
        "full_title": "A股集体大涨，创业板指涨超3%，超4400只个股上涨",
        "summary": "A股三大指数大幅高开高走，超4400只个股上涨。",
        "追高买入概率": 88,
        "抄底买入概率": 3,
        "恐慌卖出概率": 2,
        "观望概率": 10,
        "情绪标签": ["FOMO", "易懂"],
        "韭菜行为总结": "散户疯了！4400只股票上涨，不买就亏了！",
        "市场含义": "顶部风险",
        "买入概率": 72,
        "is_long_term": false,
        "date": "2026-04-16",
        "decay": 1.0,
        "weighted_buy_prob": 72
      },
      {
        "news": "宁德时代AH股双双创历史新高，市值破2万亿",
        "title": "宁德时代AH股创新高",
        "full_title": "宁德时代AH股双双创历史新高，市值破2万亿",
        "summary": "宁德时代A股涨超4%，H股大涨超10%，双双创历史新高。",
        "追高买入概率": 85,
        "抄底买入概率": 5,
        "恐慌卖出概率": 2,
        "观望概率": 12,
        "情绪标签": ["FOMO", "易懂"],
        "韭菜行为总结": "散户疯了！宁德时代创新高，必须追！",
        "市场含义": "顶部风险",
        "买入概率": 68,
        "is_long_term": false,
        "date": "2026-04-16",
        "decay": 1.0,
        "weighted_buy_prob": 68
      },
      {
        "news": "它石智航完成4.5亿美元Pre-A轮融资，创中国具身智能纪录",
        "title": "它石智航完成4.5亿美元融资",
        "full_title": "它石智航完成4.5亿美元Pre-A轮融资，创中国具身智能纪录",
        "summary": "它石智航宣布完成超4.5亿美元Pre-A轮融资，创中国具身智能最高单轮融资纪录。",
        "追高买入概率": 65,
        "抄底买入概率": 10,
        "恐慌卖出概率": 3,
        "观望概率": 25,
        "情绪标签": ["FOMO", "复杂"],
        "韭菜行为总结": "散户觉得AI机器人是风口，想跟",
        "市场含义": "分歧加大",
        "买入概率": 52,
        "is_long_term": false,
        "date": "2026-04-16",
        "decay": 1.0,
        "weighted_buy_prob": 52
      },
      {
        "news": "一季度居民人均可支配收入实际增长4%",
        "title": "居民收入实际增长4%",
        "full_title": "一季度居民人均可支配收入实际增长4%",
        "summary": "国家统计局披露，一季度全国居民人均可支配收入实际增长4%。",
        "追高买入概率": 55,
        "抄底买入概率": 10,
        "恐慌卖出概率": 5,
        "观望概率": 35,
        "情绪标签": ["关注"],
        "韭菜行为总结": "散户觉得收入涨了，消费股有戏",
        "市场含义": "中性偏多",
        "买入概率": 42,
        "is_long_term": false,
        "date": "2026-04-16",
        "decay": 1.0,
        "weighted_buy_prob": 42
      },
      {
        "news": "3月原油加工由增转降，工业生产稳定",
        "title": "3月原油加工由增转降",
        "full_title": "3月原油加工由增转降，工业生产稳定",
        "summary": "3月份规模以上工业原油加工由增转降，原煤生产规模稳定。",
        "追高买入概率": 20,
        "抄底买入概率": 15,
        "恐慌卖出概率": 10,
        "观望概率": 60,
        "情绪标签": ["观望", "复杂"],
        "韭菜行为总结": "散户看不懂能源数据",
        "市场含义": "中性",
        "买入概率": 22,
        "is_long_term": false,
        "date": "2026-04-16",
        "decay": 1.0,
        "weighted_buy_prob": 22
      },
      {
        "news": "特斯拉宣布对欧盟110亿美元商品征收关税",
        "title": "特朗普对欧盟征收关税",
        "full_title": "特朗普宣布对欧盟110亿美元商品征收关税",
        "summary": "特朗普在推特宣布美国将对价值110亿美元的欧盟产品征收关税。",
        "追高买入概率": 10,
        "抄底买入概率": 5,
        "恐慌卖出概率": 35,
        "观望概率": 55,
        "情绪标签": ["恐慌", "复杂"],
        "韭菜行为总结": "散户担心贸易战又来了，有点怕",
        "市场含义": "分歧加大",
        "买入概率": 18,
        "is_long_term": false,
        "date": "2026-04-16",
        "decay": 1.0,
        "weighted_buy_prob": 18
      },
      {
        "news": "国资委要求加快低空航空装备创新迭代",
        "title": "国资委推进低空航空装备",
        "full_title": "国资委要求加快低空航空装备创新迭代",
        "summary": "国务院国资委强调央企要加快低空航空装备创新迭代。",
        "追高买入概率": 60,
        "抄底买入概率": 15,
        "恐慌卖出概率": 3,
        "观望概率": 25,
        "情绪标签": ["FOMO", "易懂"],
        "韭菜行为总结": "散户觉得低空经济政策又来了，可以追",
        "市场含义": "分歧加大",
        "买入概率": 48,
        "is_long_term": false,
        "date": "2026-04-16",
        "decay": 1.0,
        "weighted_buy_prob": 48
      },
      {
        "news": "日经225创历史新高，亚太股市全线飘红",
        "title": "日经225创历史新高",
        "full_title": "日经225创历史新高，亚太股市全线飘红",
        "summary": "日经225指数涨2.38%创历史新高，韩国指数涨2.21%。",
        "追高买入概率": 75,
        "抄底买入概率": 5,
        "恐慌卖出概率": 3,
        "观望概率": 20,
        "情绪标签": ["FOMO", "易懂"],
        "韭菜行为总结": "散户觉得亚太都涨，A股肯定也涨",
        "市场含义": "顶部风险",
        "买入概率": 58,
        "is_long_term": false,
        "date": "2026-04-16",
        "decay": 1.0,
        "weighted_buy_prob": 58
      }
    ]
  },
  "white_dragon": {
    "主力状态": "拉升",
    "阶段": "中期",
    "行为解释": "放量上涨+散户追高→主力在拉升",
    "是否利用散户": false,
    "综合建议": "✅ 积极参与"
  },
  "tang_sanzang": {
    "仓位": "75%",
    "最终行动": "积极参与核心资产",
    "仲裁矛盾": [
      { "类型": "情绪过热", "描述": "沙僧狂热+八戒胜率高", "唐憎系数": "×0.95" }
    ],
    "仓位公式": {
      "基础仓位": "72%（八戒胜率）",
      "唐憎系数": "0.95（情绪过热略降）",
      "风控系数": "1.1（经济数据利好）",
      "结果": "75%"
    },
    "风控触发": [],
    "唐僧结论": "积极参与核心资产，注意追高风险，止损-10%"
  },
  "decision_matrix": [
    { "新闻": "一季度GDP增5%超预期", "做多概率": "78%", "预期收益": "+5%~+15%", "风险比": "1:3", "建议": "✅ 可做" },
    { "新闻": "宁德时代创新高市值破2万亿", "做多概率": "80%", "预期收益": "+3%~+8%", "风险比": "1:2", "建议": "✅ 可做" },
    { "新闻": "A股集体大涨创业板涨3%", "做多概率": "72%", "预期收益": "+2%~+6%", "风险比": "1:2", "建议": "✅ 可做" },
    { "新闻": "它石智航完成融资", "做多概率": "68%", "预期收益": "+5%~+12%", "风险比": "1:2", "建议": "✅ 可做" },
    { "新闻": "特朗普对欧盟关税", "做多概率": "45%", "预期收益": "不确定", "风险比": "1:1", "建议": "⚠️ 关注" }
  ]
};

// 读取现有文件
const newsDataPath = 'C:\\Users\\asus\\temp-news-website\\news-data.js';
let content = fs.readFileSync(newsDataPath, 'utf-8');

// 提取availableDates
const datesMatch = content.match(/const availableDates = \[([^\]]+)\]/);
let existingDates = [];
if (datesMatch) {
  existingDates = datesMatch[1].match(/"\d{4}-\d{2}-\d{2}"/g).map(d => d.replace(/"/g, ''));
}

// 找到原有数据开始位置
const originalDataStart = content.indexOf('"2026-04-13"');
let originalData = '';
if (originalDataStart > 0) {
  const endBrace = content.lastIndexOf('};');
  originalData = content.substring(originalDataStart, endBrace);
}

// 构建新数据
const newDaysData = {
  "2026-04-14": data0414,
  "2026-04-15": data0415,
  "2026-04-16": data0416
};

const newEntries = Object.entries(newDaysData).map(([date, data]) => {
  return `"${date}": ${JSON.stringify(data, null, 2)}`;
}).join(',\n');

// 更新日期列表
const newDates = Object.keys(newDaysData);
const allDates = [...new Set([...newDates, ...existingDates])].sort().reverse();

// 构建新文件内容
const header = `// 财经新闻数据 - 四层交叉分析版
// 生成时间: ${(new Date()).toISOString().split('T')[0]}
// 架构: 悟空(优质新闻深度分析) + 沙僧(全量新闻韭菜直觉) → 八戒(贝叶斯融合) → 白龙马(主力行为) → 唐僧(跨层仲裁)

const newsData = {
${newEntries},
${originalData}`;

const footer = `
};

const availableDates = ${JSON.stringify(allDates)};

function getNews(date) { return newsData[date] || null; }
function getPreviousDate(date) { const idx = availableDates.indexOf(date); return idx < availableDates.length - 1 ? availableDates[idx + 1] : null; }
function getNextDate(date) { const idx = availableDates.indexOf(date); return idx > 0 ? availableDates[idx - 1] : null; }
`;

const newFileContent = header + footer;

// 写入文件
fs.writeFileSync(newsDataPath, newFileContent, 'utf-8');
console.log('✅ Updated news-data.js with complete sangsha analysis');
console.log('📅 Dates:', allDates.slice(0, 5).join(', '), '...');
console.log('📦 File size:', (newFileContent.length / 1024).toFixed(1), 'KB');

// 验证沙僧数据
const testContent = fs.readFileSync(newsDataPath, 'utf-8');
const hasSangshaAnalysis = testContent.includes('"韭菜行为总结"');
const hasAnalysisResults = testContent.includes('"analysis_results"');
console.log('🔍 Has 沙僧韭菜直觉分析:', hasSangshaAnalysis ? 'YES' : 'NO');
console.log('🔍 Has analysis_results:', hasAnalysisResults ? 'YES' : 'NO');
