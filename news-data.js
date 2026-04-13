// 新闻数据 - 自动生成
const newsData = {
  "2026-04-08": {
    "date": "2026-04-08",
    "market_tone": "科技股强势回归！美伊谈判现逆转信号，AI芯片、人工智能板块领涨，创业板人工智能ETF涨超7%",
    "wukong_judgment": {
      "market_sentiment": "震荡偏多，科技成长股修复反弹",
      "core_analysis": [
        "AI芯片爆发：科创芯片ETF涨超5%，创业板人工智能ETF涨超7%，中际旭创涨超6%",
        "科技股集体上攻：美伊谈判现逆转信号，市场风险偏好回升",
        "AI人工智能ETF平安涨超4.2%，冲击3连涨，深信服涨6%，光环新网上涨5.92%",
        "资金回流科技板块：前期调整后迎来修复行情"
      ],
      "operations": [
        {"type": "可做", "content": "AI芯片/算力板块：中际旭创、通宇通讯、科创芯片ETF"},
        {"type": "可做", "content": "人工智能ETF：短期反弹趋势确立"},
        {"type": "警惕", "content": "成交量配合，若不放大则冲高回落风险"}
      ]
    },
    "bajie_conclusion": {
      "optimal_action": "重点配置AI芯片+人工智能ETF，科技成长股修复行情",
      "optimal_etfs": "588890科创芯片ETF(40%) + 512930 AI人工智能ETF(30%) + 现金(30%)",
      "win_rate": "~70%（贝叶斯后验）",
      "max_drawdown": "-5%（止损线）",
      "holding_period": "1-2周"
    },
    "s_level": [
      {
        "emoji": "🔴",
        "title": "AI芯片/人工智能板块爆发式上涨",
        "summary": "科创芯片ETF涨超5%，创业板人工智能ETF涨超7%，中际旭创涨超6%，深信服涨6%，光环新网上涨5.92%。美伊谈判现逆转信号，科技板块强势回归，资金回流科技成长股。",
        "duration": "1-2周",
        "etfs": [
          {"name": "588890 科创芯片ETF", "sentiment": "利好"},
          {"name": "512930 AI人工智能ETF", "sentiment": "利好"},
          {"name": "512760 芯片ETF", "sentiment": "利好"}
        ],
        "stocks": [
          "中际旭创",
          "深信服",
          "光环新网",
          "润泽科技",
          "星宸科技"
        ],
        "signal": "主力资金回流科技板块，短期做多情绪高涨",
        "bayes_analysis": {
          "prior_judgment": "科技股修复反弹",
          "prior_prob": 60,
          "likelihood_judgment": "AI芯片爆发+ETF涨超7%",
          "likelihood_prob": 78,
          "posterior": 72,
          "expected_return": "+5%~+10%",
          "confidence_interval": "[+3%, +15%]",
          "key_variables": "成交量能否持续放大（若破万亿，胜率提升至75%）"
        }
      },
      {
        "emoji": "🔴",
        "title": "美伊谈判现逆转信号",
        "summary": "美伊谈判出现逆转信号，地缘风险降温，市场风险偏好回升。避险资金流出黄金、油气板块，流入科技成长股。",
        "duration": "1-3天",
        "etfs": [
          {"name": "512930 AI人工智能ETF", "sentiment": "利好"},
          {"name": "588890 科创芯片ETF", "sentiment": "利好"},
          {"name": "518880 黄金ETF", "sentiment": "利空"},
          {"name": "501018 南方原油", "sentiment": "利空"}
        ],
        "stocks": [
          "中际旭创",
          "深信服",
          "光环新网"
        ],
        "signal": "避险资金流出，成长股资金流入",
        "bayes_analysis": {
          "prior_judgment": "地缘风险定价",
          "prior_prob": 55,
          "likelihood_judgment": "谈判逆转信号明确",
          "likelihood_prob": 75,
          "posterior": 68,
          "expected_return": "+4%~+8%",
          "confidence_interval": "[+2%, +12%]",
          "key_variables": "谈判能否实质性落地（若达成停火，胜率提升至75%）"
        }
      }
    ],
    "a_level": [
      {
        "emoji": "🟡",
        "title": "创业板人工智能ETF涨超7%",
        "summary": "创业板人工智能ETF南方(159382)上涨7.03%，冲击3连涨，跟踪指数创业板人工智能指数强势上涨7.18%。",
        "duration": "1-2周",
        "etfs": [
          {"name": "159382 创业板人工智能ETF", "sentiment": "利好"},
          {"name": "512930 AI人工智能ETF", "sentiment": "利好"}
        ],
        "stocks": [
          "中际旭创",
          "深信服",
          "光环新网"
        ],
        "signal": "AI板块强势反弹，短期趋势确立",
        "bayes_analysis": {
          "prior_judgment": "AI板块调整充分，估值合理",
          "prior_prob": 58,
          "likelihood_judgment": "ETF涨超7%，资金回流明确",
          "likelihood_prob": 72,
          "posterior": 67,
          "expected_return": "+4%~+8%",
          "confidence_interval": "[+2%, +12%]",
          "key_variables": "成交量、北向资金流向"
        }
      }
    ],
    "douyin": []
  },
  "2026-04-07": {
    "date": "2026-04-07",
    "market_tone": "节后首日修复！美伊停火协议落地，风险偏好回升，A股温和高开，加密货币概念股领涨",
    "wukong_judgment": {
      "market_sentiment": "偏多，修复性反弹为主",
      "core_analysis": [
        "美伊停火协议正式落地，地缘风险急剧降温：黄金从4800美元高位回落至4650美元，原油从140美元回落至106美元",
        "比特币站稳70000美元创历史新高，加密货币概念股开盘领涨，区块链板块涨幅居前",
        "日韩股市强劲反弹映射：日经225涨0.72%，韩国KOSPI涨2.02%，三星电子涨近4%",
        "美股科技股隔夜普涨：特斯拉涨1.67%，Meta涨超1%，芯片股闪迪涨超4%",
        "北向资金节后首日流向是关键观察指标，若净流入>50亿则确认修复行情"
      ],
      "operations": [
        {"type": "可做", "content": "加密货币概念股：比特币破7万美元历史新高，矿机/交易所概念股重点配置"},
        {"type": "可做", "content": "AI芯片/算力：美股芯片股大涨映射，A股中际旭创/通宇通讯有望延续"},
        {"type": "警惕", "content": "油气板块：美伊停火原油回落，短期回避油气ETF"},
        {"type": "警惕", "content": "黄金贵金属：避险情绪降温，黄金高位震荡，控制仓位"},
        {"type": "关注", "content": "北向资金流向+成交量能否放大"}
      ]
    },
    "bajie_conclusion": {
      "optimal_action": "节后首日重点配置加密货币概念股+AI芯片，回避油气/黄金避险资产",
      "optimal_etfs": "512760芯片ETF(30%) + 515980云计算ETF(25%) + 加密货币概念股(15%) + 现金(30%)",
      "win_rate": "~70%（贝叶斯后验）",
      "max_drawdown": "-6%（止损线）",
      "holding_period": "1-2周"
    },
    "s_level": [
      {
        "emoji": "🔴",
        "title": "比特币站稳7万美元创历史新高",
        "summary": "比特币站稳70000美元创历史新高，加密货币概念股开盘领涨，区块链板块涨幅居前。矿机、交易所概念股重点配置。",
        "duration": "1-2周",
        "etfs": [
          {"name": "512760 芯片ETF", "sentiment": "利好"},
          {"name": "515980 云计算ETF", "sentiment": "利好"}
        ],
        "stocks": [
          "中际旭创",
          "通宇通讯",
          "矿机概念股"
        ],
        "signal": "加密货币胜率75%，AI芯片胜率72%",
        "bayes_analysis": {
          "prior_judgment": "比特币突破历史新高",
          "prior_prob": 68,
          "likelihood_judgment": "站稳70000美元，市场情绪高涨",
          "likelihood_prob": 82,
          "posterior": 75,
          "expected_return": "+12%~+18%",
          "confidence_interval": "[+5%, +25%]",
          "key_variables": "比特币能否站稳72000美元（若突破75000，胜率可提升至80%）"
        }
      },
      {
        "emoji": "🔴",
        "title": "美伊停火协议正式落地",
        "summary": "美伊停火协议正式落地，地缘风险急剧降温。黄金从4800美元高位回落至4650美元，原油从140美元回落至106美元。避险资金流出，风险偏好回升。",
        "duration": "1-3天",
        "etfs": [
          {"name": "512760 芯片ETF", "sentiment": "利好"},
          {"name": "518880 黄金ETF", "sentiment": "利空"},
          {"name": "501018 南方原油", "sentiment": "利空"}
        ],
        "stocks": [
          "科技龙头股"
        ],
        "signal": "避险资金流出，成长股资金流入",
        "bayes_analysis": {
          "prior_judgment": "地缘风险降温",
          "prior_prob": 60,
          "likelihood_judgment": "停火协议落地，风险偏好回升",
          "likelihood_prob": 78,
          "posterior": 70,
          "expected_return": "+5%~+10%",
          "confidence_interval": "[+2%, +15%]",
          "key_variables": "协议执行情况、后续局势发展"
        }
      }
    ],
    "a_level": [
      {
        "emoji": "🟡",
        "title": "日韩股市强劲反弹",
        "summary": "日经225涨0.72%，韩国KOSPI涨2.02%，三星电子涨近4%。美股科技股隔夜普涨：特斯拉涨1.67%，Meta涨超1%，芯片股闪迪涨超4%。",
        "duration": "1-3天",
        "etfs": [
          {"name": "512760 芯片ETF", "sentiment": "利好"},
          {"name": "513500 标普500ETF", "sentiment": "利好"}
        ],
        "stocks": [
          "三星产业链",
          "科技龙头股"
        ],
        "signal": "日韩大涨映射，A股节后有望跟涨",
        "bayes_analysis": {
          "prior_judgment": "外围市场反弹",
          "prior_prob": 60,
          "likelihood_judgment": "日韩大涨，美股科技股普涨",
          "likelihood_prob": 75,
          "posterior": 68,
          "expected_return": "+5%~+10%",
          "confidence_interval": "[+2%, +15%]",
          "key_variables": "A股节后成交量能否放大（若>1.5万亿，胜率可提升至72%）"
        }
      }
    ],
    "douyin": []
  },
  "2026-04-03": {
    "date": "2026-04-03",
    "market_tone": "清明假期A股休市，海外市场剧烈分化，黄金暴跌原油暴涨，科技股逆势走强，关注节后A股方向",
    "wukong_judgment": {
      "market_sentiment": "震荡分化，结构性机会为主",
      "core_analysis": [
        "黄金高位跳水，原油暴涨突破106美元，大宗商品进入高波动期",
        "美股科技股逆势走强，AI芯片、存储板块领涨，A股节后有望跟涨",
        "医药板块持续活跃，津药药业5连板，防御性板块受资金青睐",
        "清明节期间外围波动加剧，节后A股或面临方向选择"
      ],
      "operations": [
        {"type": "可做", "content": "AI芯片、存储半导体（美股映射）"},
        {"type": "可做", "content": "医药商业、化学制药（防御配置）"},
        {"type": "警惕", "content": "黄金贵金属（高位回调风险）"},
        {"type": "关注", "content": "油气板块（地缘冲突催化）"}
      ]
    },
    "bajie_conclusion": {
      "optimal_action": "轻仓过节，节后布局AI芯片+医药防御组合",
      "optimal_etfs": "512760芯片ETF(30%) + 512010医药ETF(30%) + 518880黄金ETF(20%) + 现金(20%)",
      "win_rate": "~65%（贝叶斯后验）",
      "max_drawdown": "-8%（止损线）"
    },
    "s_level": [
      {
        "emoji": "🔴",
        "title": "黄金暴跌原油飞天：大宗商品剧烈分化",
        "summary": "4月2日大宗商品市场剧烈波动，现货黄金从4800美元高位跳水至4616美元，日内大跌2.97%；布伦特原油暴涨突破106美元/桶，日内涨超5%。特朗普威胁对伊朗更强火力打击，地缘风险推升油价，但黄金避险逻辑生变。",
        "duration": "1-2周",
        "etfs": [
          {"name": "518880 黄金ETF", "sentiment": "利空"},
          {"name": "501018 南方原油", "sentiment": "利好"},
          {"name": "513500 标普500ETF", "sentiment": "中性"}
        ],
        "stocks": [
          "中国石油",
          "中国海油",
          "山东黄金"
        ],
        "signal": "黄金高位资金撤离，原油地缘溢价飙升，大宗商品进入高波动交易模式",
        "bayes_analysis": {
          "prior_judgment": "地缘冲突支撑避险资产",
          "prior_prob": 60,
          "likelihood_judgment": "特朗普威胁打击伊朗，原油供应风险上升",
          "likelihood_prob": 75,
          "posterior": 72,
          "expected_return": "+3%~+8%",
          "confidence_interval": "[+1%, +12%]",
          "key_variables": "美伊谈判进展、OPEC+产量政策、美联储态度"
        }
      },
      {
        "emoji": "🔴",
        "title": "美股科技股逆势走强：AI芯片存储领涨",
        "summary": "4月2日美股三大股指收高，纳指涨0.18%。AI芯片、存储板块领涨，Arm发布首款自研AI芯片，澜起科技年报业绩大增58.4%，多家芯片企业业绩亮眼。AI算力需求持续爆发，创业板人工智能ETF涨约2%。",
        "duration": "2-4周",
        "etfs": [
          {"name": "512760 芯片ETF", "sentiment": "利好"},
          {"name": "159819 人工智能ETF", "sentiment": "利好"},
          {"name": "588200 科创芯片ETF", "sentiment": "利好"}
        ],
        "stocks": [
          "中芯国际",
          "澜起科技",
          "寒武纪",
          "海光信息"
        ],
        "signal": "AI算力需求爆发，存储芯片涨价，节后A股科技股有望跟涨",
        "bayes_analysis": {
          "prior_judgment": "AI产业趋势向上，业绩验证期",
          "prior_prob": 70,
          "likelihood_judgment": "Arm自研芯片+业绩大增，产业景气度确认",
          "likelihood_prob": 80,
          "posterior": 78,
          "expected_return": "+5%~+15%",
          "confidence_interval": "[+2%, +20%]",
          "key_variables": "AI应用落地进度、海外映射强度、一季报业绩"
        }
      }
    ],
    "a_level": [
      {
        "emoji": "🟡",
        "title": "医药板块持续活跃：津药药业5连板",
        "summary": "4月2日医药商业、化学制药板块涨幅居前，津药药业5连板，医药概念持续走强。主力资金流入化学制药行业，医药ETF表现亮眼，防御性配置价值凸显。",
        "duration": "1-2周",
        "etfs": [
          {"name": "512010 医药ETF", "sentiment": "利好"},
          {"name": "159929 医药龙头ETF", "sentiment": "利好"}
        ],
        "stocks": [
          "津药药业",
          "国药股份",
          "上海医药"
        ],
        "signal": "医药防御属性受青睐，资金避险需求上升",
        "bayes_analysis": {
          "prior_judgment": "医药板块估值合理，防御价值显现",
          "prior_prob": 55,
          "likelihood_judgment": "津药药业5连板，板块活跃度提升",
          "likelihood_prob": 65,
          "posterior": 62,
          "expected_return": "+2%~+6%",
          "confidence_interval": "[0%, +10%]",
          "key_variables": "板块轮动节奏、大盘风险偏好、政策催化"
        }
      },
      {
        "emoji": "🟡",
        "title": "A股缩量调整：超4300股下跌，成交不足1.9万亿",
        "summary": "4月2日A股三大指数集体收跌，沪指跌0.74%，创业板指跌2.31%，全市场超4300股下跌。成交额约1.84万亿，较前日缩量。石油石化、医药商业逆市走强，AI应用、半导体跌幅靠前。",
        "duration": "1-3天",
        "etfs": [
          {"name": "510300 沪深300ETF", "sentiment": "利空"},
          {"name": "512880 国债ETF", "sentiment": "利好"}
        ],
        "stocks": [
          "中国石油",
          "中国石化"
        ],
        "signal": "节前避险情绪升温，资金观望情绪浓厚，等待节后方向",
        "bayes_analysis": {
          "prior_judgment": "节前缩量调整属正常，节后有望修复",
          "prior_prob": 50,
          "likelihood_judgment": "超4300股下跌，情绪偏悲观",
          "likelihood_prob": 40,
          "posterior": 45,
          "expected_return": "-2%~+3%",
          "confidence_interval": "[-5%, +5%]",
          "key_variables": "假期外围走势、节后资金回流、政策面变化"
        }
      }
    ],
    "douyin": [
      {
        "emoji": "📱",
        "title": "抖音电商GMV增长放缓，内容电商竞争加剧",
        "summary": "抖音电商2026年Q1 GMV增速放缓至15%，低于去年同期的35%。淘宝直播、视频号电商加速追赶，内容电商进入存量竞争阶段。抖音加大本地生活投入，寻求第二增长曲线。",
        "duration": "1-3个月",
        "etfs": [
          {"name": "513050 中概互联网ETF", "sentiment": "中性"}
        ],
        "stocks": [
          "美团",
          "拼多多"
        ],
        "signal": "内容电商红利见顶，平台转向精细化运营",
        "bayes_analysis": {
          "prior_judgment": "短视频电商仍处增长期",
          "prior_prob": 55,
          "likelihood_judgment": "GMV增速大幅放缓，竞争加剧",
          "likelihood_prob": 45,
          "posterior": 48,
          "expected_return": "-3%~+5%",
          "confidence_interval": "[-8%, +8%]",
          "key_variables": "用户时长变化、广告主预算、监管政策"
        }
      }
    ]
  },
  "2026-04-02": {
    "date": "2026-04-02",
    "market_tone": "清明假期A股休市，海外市场延续反弹，美伊局势有所缓和，关注节后A股方向选择",
    "s_level": [
      {
        "emoji": "🔴",
        "title": "美伊停火谈判持续博弈，霍尔木兹海峡控制权成核心分歧",
        "summary": "美伊双方就停火协议展开密集磋商，美方要求伊朗重开霍尔木兹海峡作为停火条件，伊朗坚持将封锁海峡作为反制手段。谈判进展缓慢但双方均保持接触。",
        "duration": "1-2周",
        "etfs": [
          {"name": "518880 黄金ETF", "sentiment": "利好"},
          {"name": "512880 国债ETF", "sentiment": "利空"}
        ],
        "stocks": ["中航沈飞", "中国石油"],
        "signal": "黄金高位震荡，油运板块承压，避险情绪反复"
      },
      {
        "emoji": "🔴",
        "title": "美股存储板块暴涨：美光+11%、铠侠再发停产通知",
        "summary": "存储芯片大厂铠侠再度发布停产通知，叠加AI驱动HBM需求爆发，美光、西部数据、闪迪均暴涨10%以上。英伟达涨1.56%，科技股整体走强。",
        "duration": "2-4周",
        "etfs": [
          {"name": "512760 芯片ETF", "sentiment": "利好"},
          {"name": "515980 云计算与大数据ETF", "sentiment": "利好"}
        ],
        "stocks": ["中芯国际", "澜起科技"],
        "signal": "存储和AI半导体板块情绪高涨，节后A股科技股有望跟涨"
      }
    ],
    "a_level": [
      {
        "emoji": "🟡",
        "title": "SpaceX IPO超级独角兽：估值1.75万亿美元，6月挂牌",
        "summary": "SpaceX已秘密提交IPO申请，寻求6月上市，估值超1.75万亿美元，募资或超750亿美元，成三巨头超级IPO首家。",
        "duration": "1-2个月",
        "etfs": [{"name": "515980 云计算与大数据ETF", "sentiment": "利好"}],
        "stocks": ["中航沈飞", "航天电器"],
        "signal": "商业航天题材升温，但A股实质受益标的有限"
      },
      {
        "emoji": "🟡",
        "title": "一季度财报季开启：半导体龙头业绩暴涨4659%",
        "summary": "一季度财报季启幕，多家公司提前发布业绩，半导体龙头利润暴增4659%，10只个股利润翻倍，但也有2家公司业绩暴雷。",
        "duration": "1-2周",
        "etfs": [{"name": "512760 芯片ETF", "sentiment": "利好"}],
        "stocks": ["扬杰科技", "中芯国际"],
        "signal": "资金提前布局业绩超预期个股，绩优科技股受青睐"
      },
      {
        "emoji": "🟡",
        "title": "特斯拉欧洲销售分化：意大利大增32%，葡萄牙下滑2%",
        "summary": "特斯拉欧洲多国销售数据出炉，意大利3月注册量同比大增32%，但葡萄牙下滑2%。整体1-3月欧洲市场增长27%。",
        "duration": "2-4周",
        "etfs": [{"name": "515700 新能源ETF", "sentiment": "利好"}],
        "stocks": ["比亚迪"],
        "signal": "新能源车欧洲竞争加剧，比亚迪出海逻辑持续"
      },
      {
        "emoji": "🟡",
        "title": "美联储会议纪要：通胀回落缓慢，降息预期推迟至9月",
        "summary": "3月FOMC会议纪要显示，美联储官员普遍认为通胀回落速度慢于预期，多数支持将首次降息推迟至9月，全年降息次数从3次缩减至2次。",
        "duration": "1-3个月",
        "etfs": [
          {"name": "512880 国债ETF", "sentiment": "利空"},
          {"name": "518880 黄金ETF", "sentiment": "利好"}
        ],
        "stocks": ["招商银行", "中国平安"],
        "signal": "美债收益率上行，美元指数走强，新兴市场资金承压"
      }
    ],
    "douyin": [
      {
        "emoji": "📱",
        "title": "抖音电商发布2026战略：加码本地生活与跨境电商",
        "summary": "抖音电商发布2026年战略规划，重点加码本地生活服务与跨境电商业务，目标GMV增长30%。同时推出"品牌成长计划"，扶持1000个新品牌。",
        "duration": "1-3个月",
        "etfs": [{"name": "513050 中概互联网ETF", "sentiment": "利好"}],
        "stocks": ["美团", "阿里巴巴"],
        "signal": "抖音电商进入精细化运营阶段，本地生活竞争白热化"
      }
    ]
  }
};

// 可用日期列表（从新到旧）
const availableDates = ["2026-04-08", "2026-04-07", "2026-04-03", "2026-04-02"];

// 获取指定日期的新闻
function getNews(date) {
    return newsData[date] || null;
}

// 获取前一天
function getPreviousDate(date) {
    const idx = availableDates.indexOf(date);
    return idx < availableDates.length - 1 ? availableDates[idx + 1] : null;
}

// 获取后一天
function getNextDate(date) {
    const idx = availableDates.indexOf(date);
    return idx > 0 ? availableDates[idx - 1] : null;
}
