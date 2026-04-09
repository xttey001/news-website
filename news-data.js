// 财经新闻数据 - 恢复完整版

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
        {
          "type": "可做",
          "content": "AI芯片/算力板块：中际旭创、通宇通讯、科创芯片ETF"
        },
        {
          "type": "可做",
          "content": "人工智能ETF：短期反弹趋势确立"
        },
        {
          "type": "警惕",
          "content": "成交量配合，若不放大则冲高回落风险"
        }
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
        "emoji": " ",
        "title": "AI芯片/人工智能板块爆发式上涨",
        "summary": "科创芯片ETF涨超5%，创业板人工智能ETF涨超7%，中际旭创涨超6%，深信服涨6%，光环新网上涨5.92%。美伊谈判现逆转信号，科技板块强势回归，资金回流科技成长股。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "588890 科创芯片ETF",
            "sentiment": "利好"
          },
          {
            "name": "512930 AI人工智能ETF",
            "sentiment": "利好"
          },
          {
            "name": "512760 芯片ETF",
            "sentiment": "利好"
          }
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
        "emoji": " ",
        "title": "美伊谈判现逆转信号",
        "summary": "美伊谈判出现逆转信号，地缘风险降温，市场风险偏好回升。避险资金流出黄金、油气板块，流入科技成长股。",
        "duration": "1-3天",
        "etfs": [
          {
            "name": "512930 AI人工智能ETF",
            "sentiment": "利好"
          },
          {
            "name": "588890 科创芯片ETF",
            "sentiment": "利好"
          },
          {
            "name": "518880 黄金ETF",
            "sentiment": "利空"
          },
          {
            "name": "501018 南方原油",
            "sentiment": "利空"
          }
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
        "emoji": " ",
        "title": "创业板人工智能ETF涨超7%",
        "summary": "创业板人工智能ETF南方(159382)上涨7.03%，冲击3连涨，跟踪指数创业板人工智能指数强势上涨7.18%。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "159382 创业板人工智能ETF",
            "sentiment": "利好"
          },
          {
            "name": "512930 AI人工智能ETF",
            "sentiment": "利好"
          }
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
    "douyin": [],
    "sangsha_module": {
      "overall_sentiment": "平稳",
      "advice": "震荡整理，观望为主",
      "avg_buy_prob": 23,
      "avg_panic_prob": 20,
      "analysis_results": [
        {
          "news": "创业板人工智能ETF涨超7%",
          "title": "创业板人工智能ETF涨超7%",
          "full_title": "创业板人工智能ETF涨超7%",
          "summary": "创业板人工智能ETF南方(159382)上涨7.03%，冲击3连涨，跟踪指数创业板人工智能指数强势上...",
          "追高买入概率": 68,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 69,
          "情绪标签": [
            "FOMO"
          ],
          "韭菜行为总结": "散户疯了，都在追！",
          "市场含义": "顶部风险",
          "买入概率": 43,
          "is_long_term": false,
          "date": "2026-04-08",
          "decay": 1.0,
          "weighted_buy_prob": 43
        },
        {
          "news": "AI芯片/人工智能板块爆发式上涨",
          "title": "AI芯片/人工智能板块爆发式上涨",
          "full_title": "AI芯片/人工智能板块爆发式上涨",
          "summary": "科创芯片ETF涨超5%，创业板人工智能ETF涨超7%，中际旭创涨超6%，深信服涨6%，光环新网上涨5...",
          "追高买入概率": 20,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 89,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 14,
          "is_long_term": false,
          "date": "2026-04-08",
          "decay": 1.0,
          "weighted_buy_prob": 14
        },
        {
          "news": "美伊谈判现逆转信号",
          "title": "美伊谈判现逆转信号",
          "full_title": "美伊谈判现逆转信号",
          "summary": "美伊谈判出现逆转信号，地缘风险降温，市场风险偏好回升。避险资金流出黄金、油气板块，流入科技成长股。",
          "追高买入概率": 5,
          "抄底买入概率": 28,
          "恐慌卖出概率": 51,
          "观望概率": 73,
          "情绪标签": [
            "恐慌"
          ],
          "韭菜行为总结": "散户恐慌，想割肉",
          "市场含义": "可能见底",
          "买入概率": 14,
          "is_long_term": false,
          "date": "2026-04-08",
          "decay": 1.0,
          "weighted_buy_prob": 14
        }
      ],
      "total_news_count": 3,
      "time_window": "7天累积（长期新闻除外）"
    },
    "white_dragon": {
      "主力状态": "出货",
      "阶段": "末期",
      "行为解释": "多个ETF出现主力派发信号，注意风险",
      "是否利用散户": true,
      "散户情绪": {
        "平均买入概率": 23,
        "平均恐慌概率": 20
      },
      "各ETF分析": [
        {
          "code": "512760",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.0
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 21.72,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 23,
          "sangsha_panic_prob": 20
        },
        {
          "code": "512930",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.43
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 11.41,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 23,
          "sangsha_panic_prob": 20
        },
        {
          "code": "518880",
          "price_trend": {
            "trend": "side",
            "strength": 40,
            "change_pct": 1.33
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": -10.83,
            "level": "normal"
          },
          "主力状态": "吸筹",
          "阶段": "早期",
          "行为解释": "价格横盘/小跌，资金流入，主力可能在低位吸筹",
          "是否利用散户": false,
          "sangsha_buy_prob": 23,
          "sangsha_panic_prob": 20
        },
        {
          "code": "588890",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.16
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 0.4,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 23,
          "sangsha_panic_prob": 20
        },
        {
          "code": "159382",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.74
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 29.76,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 23,
          "sangsha_panic_prob": 20
        }
      ],
      "综合建议": "⚠️ 风险提示：主力可能正在派发，散户追高风险大，建议减仓观望"
    }
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
        {
          "type": "可做",
          "content": "加密货币概念股：比特币破7万美元历史新高，矿机/交易所概念股重点配置"
        },
        {
          "type": "可做",
          "content": "AI芯片/算力：美股芯片股大涨映射，A股中际旭创/通宇通讯有望延续"
        },
        {
          "type": "警惕",
          "content": "油气板块：美伊停火原油回落，短期回避油气ETF"
        },
        {
          "type": "警惕",
          "content": "黄金贵金属：避险情绪降温，黄金高位震荡，控制仓位"
        },
        {
          "type": "关注",
          "content": "北向资金流向+成交量能否放大"
        }
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
        "emoji": " ",
        "title": "比特币站稳7万美元创历史新高",
        "summary": "比特币站稳70000美元创历史新高，加密货币概念股开盘领涨，区块链板块涨幅居前。矿机、交易所概念股重点配置。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "512760 芯片ETF",
            "sentiment": "利好"
          },
          {
            "name": "515980 云计算ETF",
            "sentiment": "利好"
          }
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
        "emoji": " ",
        "title": "美伊停火协议正式落地",
        "summary": "美伊停火协议正式落地，地缘风险急剧降温。黄金从4800美元高位回落至4650美元，原油从140美元回落至106美元。避险资金流出，风险偏好回升。",
        "duration": "1-3天",
        "etfs": [
          {
            "name": "512760 芯片ETF",
            "sentiment": "利好"
          },
          {
            "name": "518880 黄金ETF",
            "sentiment": "利空"
          },
          {
            "name": "501018 南方原油",
            "sentiment": "利空"
          }
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
        "emoji": " ",
        "title": "日韩股市强劲反弹",
        "summary": "日经225涨0.72%，韩国KOSPI涨2.02%，三星电子涨近4%。美股科技股隔夜普涨：特斯拉涨1.67%，Meta涨超1%，芯片股闪迪涨超4%。",
        "duration": "1-3天",
        "etfs": [
          {
            "name": "512760 芯片ETF",
            "sentiment": "利好"
          },
          {
            "name": "513500 标普500ETF",
            "sentiment": "利好"
          }
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
    "douyin": [],
    "sangsha_module": {
      "overall_sentiment": "平稳",
      "advice": "震荡整理，观望为主",
      "avg_buy_prob": 31,
      "avg_panic_prob": 20,
      "analysis_results": [
        {
          "news": "比特币站稳7万美元创历史新高",
          "title": "比特币站稳7万美元创历史新高",
          "full_title": "比特币站稳7万美元创历史新高",
          "summary": "比特币站稳70000美元创历史新高，加密货币概念股开盘领涨，区块链板块涨幅居前。矿机、交易所概念股重...",
          "追高买入概率": 82,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 63,
          "情绪标签": [
            "FOMO"
          ],
          "韭菜行为总结": "散户疯了，都在追！",
          "市场含义": "顶部风险",
          "买入概率": 51,
          "is_long_term": false,
          "date": "2026-04-07",
          "decay": 1.0,
          "weighted_buy_prob": 51
        },
        {
          "news": "日韩股市强劲反弹",
          "title": "日韩股市强劲反弹",
          "full_title": "日韩股市强劲反弹",
          "summary": "日经225涨0.72%，韩国KOSPI涨2.02%，三星电子涨近4%。美股科技股隔夜普涨：特斯拉涨1...",
          "追高买入概率": 8,
          "抄底买入概率": 58,
          "恐慌卖出概率": 5,
          "观望概率": 77,
          "情绪标签": [
            "抄底冲动"
          ],
          "韭菜行为总结": "散户想抄底，认为是机会",
          "市场含义": "可能有反弹",
          "买入概率": 28,
          "is_long_term": false,
          "date": "2026-04-07",
          "decay": 1.0,
          "weighted_buy_prob": 28
        },
        {
          "news": "美伊停火协议正式落地",
          "title": "美伊停火协议正式落地",
          "full_title": "美伊停火协议正式落地",
          "summary": "美伊停火协议正式落地，地缘风险急剧降温。黄金从4800美元高位回落至4650美元，原油从140美元回...",
          "追高买入概率": 5,
          "抄底买入概率": 28,
          "恐慌卖出概率": 51,
          "观望概率": 73,
          "情绪标签": [
            "恐慌"
          ],
          "韭菜行为总结": "散户恐慌，想割肉",
          "市场含义": "可能见底",
          "买入概率": 14,
          "is_long_term": false,
          "date": "2026-04-07",
          "decay": 1.0,
          "weighted_buy_prob": 14
        }
      ],
      "total_news_count": 3,
      "time_window": "7天累积（长期新闻除外）"
    },
    "white_dragon": {
      "主力状态": "出货",
      "阶段": "末期",
      "行为解释": "多个ETF出现主力派发信号，注意风险",
      "是否利用散户": true,
      "散户情绪": {
        "平均买入概率": 31,
        "平均恐慌概率": 20
      },
      "各ETF分析": [
        {
          "code": "512760",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.0
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 21.72,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 31,
          "sangsha_panic_prob": 20
        },
        {
          "code": "512930",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.43
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 11.41,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 31,
          "sangsha_panic_prob": 20
        },
        {
          "code": "518880",
          "price_trend": {
            "trend": "side",
            "strength": 40,
            "change_pct": 1.33
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": -10.83,
            "level": "normal"
          },
          "主力状态": "吸筹",
          "阶段": "早期",
          "行为解释": "价格横盘/小跌，资金流入，主力可能在低位吸筹",
          "是否利用散户": false,
          "sangsha_buy_prob": 31,
          "sangsha_panic_prob": 20
        },
        {
          "code": "588890",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.16
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 0.4,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 31,
          "sangsha_panic_prob": 20
        },
        {
          "code": "159382",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.74
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 29.76,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 31,
          "sangsha_panic_prob": 20
        }
      ],
      "综合建议": "⚠️ 风险提示：主力可能正在派发，散户追高风险大，建议减仓观望"
    }
  },
  "2026-04-06": {
    "date": "2026-04-06",
    "market_tone": "重大转折日！美伊停火协议细节公布，避险资产跳水风险资产飙升，比特币突破7万美元创历史新高",
    "wukong_judgment": {
      "emotion": "风险偏好大幅回升，做多窗口开启",
      "analysis": [
        "美伊停火协议细节公布，地缘风险急剧降温：现货黄金跌破4700美元后反弹，WTI原油从114美元跳水至109美元",
        "比特币突破70000美元创历史新高，加密货币概念股盘前普涨，Coinbase涨近4%",
        "日韩股市集体大涨：日经225涨0.72%，韩国KOSPI涨2.02%，三星电子涨近4%，SK海力士涨超2%",
        "美股科技股盘前普涨：特斯拉涨1.67%，Meta涨超1%，微软/谷歌/亚马逊/英伟达涨近1%",
        "Strategy再增持4871枚比特币，均价6.77万美元，累计持有766970枚BTC占总供应量3.65%"
      ],
      "strategy": [
        " 加密货币概念股：比特币破7万美元+Strategy增持，Coinbase/矿机股重点配置",
        " 科技成长股：美股科技股盘前普涨，节后A股科技板块有望跟涨",
        " 油气板块：美伊停火导致原油跳水，短期回避油气ETF",
        " 黄金贵金属：避险情绪降温，黄金高位震荡，控制仓位",
        " 节后关注：4月7日复牌，关注北向资金流向+加密货币概念股表现"
      ]
    },
    "bajie_bayesian": {
      "overall": {
        "win_rate": 72,
        "best_action": "节后重点配置加密货币概念股+科技成长股，回避油气/黄金避险资产",
        "best_etfs": "512760芯片ETF 30% + 515980云计算ETF 25% + 加密货币概念股 15% + 现金 30%",
        "stop_loss": -6,
        "holding_period": "1-2周",
        "conclusion": "美伊停火协议+比特币破7万美元+科技股普涨，风险偏好大幅回升。加密货币胜率75%，科技股胜率72%，油气胜率降至35%回避。节后重点配置成长股。"
      },
      "decision_matrix": [
        {
          "news": "比特币破7万美元",
          "win_rate": 75,
          "expected_return": "+12%~+20%",
          "risk_ratio": "1:0.4",
          "action": " 重点做多",
          "priority": 1
        },
        {
          "news": "美股科技股盘前普涨",
          "win_rate": 72,
          "expected_return": "+8%~+15%",
          "risk_ratio": "1:0.5",
          "action": " 重点做多",
          "priority": 2
        },
        {
          "news": "日韩股市大涨",
          "win_rate": 68,
          "expected_return": "+6%~+12%",
          "risk_ratio": "1:0.6",
          "action": " 可做",
          "priority": 3
        },
        {
          "news": "美伊停火原油跳水",
          "win_rate": 35,
          "expected_return": "-8%~+2%",
          "risk_ratio": "1:2.5",
          "action": " 回避",
          "priority": 4
        },
        {
          "news": "黄金避险情绪降温",
          "win_rate": 42,
          "expected_return": "-5%~+4%",
          "risk_ratio": "1:1.5",
          "action": " 观望",
          "priority": 5
        }
      ],
      "news_analysis": [
        {
          "news_title": "比特币破7万美元",
          "prior": 68,
          "likelihood": 82,
          "posterior": 75,
          "expected_return": "+12%~+20%",
          "confidence": "[+5%, +30%]",
          "key_variable": "比特币能否站稳70000美元（若突破75000，胜率可提升至80%）"
        },
        {
          "news_title": "美股科技股盘前普涨",
          "prior": 65,
          "likelihood": 78,
          "posterior": 72,
          "expected_return": "+8%~+15%",
          "confidence": "[+3%, +22%]",
          "key_variable": "美股今晚收盘表现（若纳指涨超1%，胜率可提升至75%）"
        },
        {
          "news_title": "日韩股市大涨",
          "prior": 60,
          "likelihood": 75,
          "posterior": 68,
          "expected_return": "+6%~+12%",
          "confidence": "[+2%, +18%]",
          "key_variable": "A股节后首日北向资金流向（若净流入>50亿，胜率可提升至72%）"
        },
        {
          "news_title": "美伊停火原油跳水",
          "prior": 45,
          "likelihood": 30,
          "posterior": 35,
          "expected_return": "-8%~+2%",
          "confidence": "[-12%, +4%]",
          "key_variable": "停火协议能否顺利执行（若执行顺利，油价可能进一步回落）"
        },
        {
          "news_title": "黄金避险情绪降温",
          "prior": 50,
          "likelihood": 40,
          "posterior": 42,
          "expected_return": "-5%~+4%",
          "confidence": "[-8%, +8%]",
          "key_variable": "停火协议进展+美联储政策（若协议生变，黄金可能反弹）"
        }
      ]
    },
    "s_level": [
      {
        "emoji": " ",
        "title": "美伊停火协议细节公布：黄金直线拉升原油大跳水，风险资产全面反弹",
        "source": "新浪财经 / 东方财富 / 腾讯新闻",
        "summary": "4月6日美伊停火协议细节公布。现货黄金全天大幅震荡，开盘后持续下挫一度失守4610美元，此后直线拉升涨破4700美元关口，报4702.46美元涨超0.5%。WTI原油期货从早间大涨超3%转为跳水，跌1.81%报109.52美元/桶。ICE布油期货跌0.54%报108.44美元/桶。日韩股市集体收涨，日经225涨0.72%，韩国KOSPI大涨2.02%。美股期货大幅拉升，道指期货涨0.36%，纳斯达克100指数期货涨1%。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "160140 油气ETF",
            "sentiment": "利空",
            "note": "原油跳水承压"
          },
          {
            "name": "518880 黄金ETF",
            "sentiment": "中性",
            "note": "高位震荡"
          },
          {
            "name": "512760 芯片ETF",
            "sentiment": "利好",
            "note": "科技股反弹"
          }
        ],
        "stocks": [
          {
            "name": "中国石油",
            "sentiment": "利空",
            "note": "油价下跌压力"
          },
          {
            "name": "中国海油",
            "sentiment": "利空",
            "note": "原油跳水"
          },
          {
            "name": "山东黄金",
            "sentiment": "中性",
            "note": "黄金震荡"
          }
        ],
        "signal": "美伊停火协议导致避险资产大幅波动，风险偏好急剧回升，节后重点关注科技成长股"
      },
      {
        "emoji": " ",
        "title": "比特币突破70000美元创历史新高！加密货币全线大涨，8万人爆仓",
        "source": "东方财富 / 搜狐 / 腾讯新闻",
        "summary": "4月6日加密货币市场全线反攻。比特币大涨超3%突破70000美元，最高触及70191.2美元，过去24小时涨4.79%。以太坊涨至2168.91美元涨6.19%，SOL/XRP/狗狗币/BNB涨超1%。根据CoinGlass数据统计，最近24小时全球80175人被爆仓。美股加密货币概念股盘前普涨：Coinbase涨3.8%，Strategy涨4.2%，Circle涨4.5%。Strategy宣布再增持4871枚比特币，均价6.77万美元，累计持有766970枚BTC占总供应量3.65%。",
        "duration": "2-4周",
        "etfs": [
          {
            "name": "512760 芯片ETF",
            "sentiment": "利好",
            "note": "加密货币挖矿需求"
          },
          {
            "name": "515980 云计算ETF",
            "sentiment": "利好",
            "note": "区块链基础设施"
          }
        ],
        "stocks": [
          {
            "name": "比特大陆(未上市)",
            "sentiment": "利好",
            "note": "矿机龙头"
          },
          {
            "name": "嘉楠科技",
            "sentiment": "利好",
            "note": "矿机概念"
          },
          {
            "name": "亿邦国际",
            "sentiment": "利好",
            "note": "矿机概念"
          }
        ],
        "signal": "比特币破7万美元+Strategy增持，加密货币概念股节后重点关注，关注矿机/交易所概念股"
      },
      {
        "emoji": " ",
        "title": "美股科技股盘前普涨：特斯拉涨1.67%，芯片股领涨闪迪涨超4%",
        "source": "东方财富 / 财联社",
        "summary": "4月6日美股大型科技股盘前集体上涨。特斯拉涨1.67%，Meta涨超1%，微软/谷歌A/亚马逊/英伟达涨近1%，苹果涨0.22%。芯片股盘前普涨，闪迪涨超4%。石油股盘前下跌，埃克森美孚/德文能源/西方石油跌约1%。开源证券认为最坏定价阶段可能正在过去，建议投资者左侧开始尝试进攻布局，科技成长仍是最值得重视的方向。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "513500 标普ETF",
            "sentiment": "利好",
            "note": "美股反弹"
          },
          {
            "name": "513100 纳指ETF",
            "sentiment": "利好",
            "note": "科技股领涨"
          },
          {
            "name": "512760 芯片ETF",
            "sentiment": "利好",
            "note": "芯片股强势"
          }
        ],
        "stocks": [
          {
            "name": "英伟达",
            "sentiment": "利好",
            "note": "AI芯片龙头"
          },
          {
            "name": "特斯拉",
            "sentiment": "利好",
            "note": "新能源车龙头"
          },
          {
            "name": "Meta",
            "sentiment": "利好",
            "note": "元宇宙龙头"
          }
        ],
        "signal": "美股科技股盘前普涨，节后A股科技板块有望跟涨，重点关注AI芯片/新能源车/元宇宙概念"
      }
    ],
    "a_level": [
      {
        "emoji": " ",
        "title": "日韩股市集体大涨：韩国KOSPI涨2%，三星电子涨近4%",
        "source": "东方财富 / 腾讯新闻",
        "summary": "4月6日日韩股市开盘后集体走高。截至北京时间8:10，日经225指数涨0.72%，韩国KOSPI指数大涨2.02%。三星电子涨近4%，SK海力士涨超2%。亚洲市场风险偏好明显回升，受美伊停火协议消息提振。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "513520 日经ETF",
            "sentiment": "利好",
            "note": "日本股市反弹"
          },
          {
            "name": "513050 港股通ETF",
            "sentiment": "利好",
            "note": "港股联动"
          }
        ],
        "stocks": [
          {
            "name": "三星电子(港股)",
            "sentiment": "利好",
            "note": "存储芯片龙头"
          },
          {
            "name": "SK海力士(港股)",
            "sentiment": "利好",
            "note": "存储芯片"
          }
        ],
        "signal": "日韩股市大涨预示节后A股有望跟涨，重点关注半导体/存储芯片板块"
      },
      {
        "emoji": " ",
        "title": "霍尔木兹海峡传来新消息：国际油价跳水比特币大涨",
        "source": "新浪财经 / 腾讯新闻",
        "summary": "受美伊停火协议消息面影响，国际油价跳水黄金上扬。截至北京时间4月6日17:50，WTI原油期货跌1.69%报109.66美元/桶，ICE布油期货跌1.72%报107.16美元/桶。现货黄金一度向上触及4700美元，日内上涨0.58%。比特币涨至70191美元涨4.79%。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "160140 油气ETF",
            "sentiment": "利空",
            "note": "油价下跌"
          },
          {
            "name": "518880 黄金ETF",
            "sentiment": "中性",
            "note": "震荡为主"
          }
        ],
        "stocks": [
          {
            "name": "中国石油",
            "sentiment": "利空",
            "note": "油价承压"
          },
          {
            "name": "山东黄金",
            "sentiment": "中性",
            "note": "黄金震荡"
          }
        ],
        "signal": "霍尔木兹海峡局势缓和导致油价下跌，避险资产分化，节后规避油气板块"
      }
    ],
    "douyin": [
      {
        "emoji": " ",
        "title": "比特币破7万美元刷屏：8万人爆仓，创历史新高",
        "source": "抖音热榜 / 微博热搜",
        "summary": "比特币突破70000美元创历史新高，社交媒体刷屏。最近24小时全球8万人爆仓。Strategy再增持4871枚比特币。加密货币概念股关注度飙升。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "512760 芯片ETF",
            "sentiment": "利好",
            "note": "矿机需求"
          }
        ],
        "stocks": [
          {
            "name": "嘉楠科技",
            "sentiment": "利好",
            "note": "矿机概念"
          },
          {
            "name": "亿邦国际",
            "sentiment": "利好",
            "note": "矿机概念"
          }
        ],
        "signal": "比特币破7万美元引发热议，节后加密货币概念股有望炒作"
      },
      {
        "emoji": " ",
        "title": "清明节A股休市：4月7日复牌，关注节后行情",
        "source": "交易所公告",
        "summary": "清明节小长假，A股4月4日至6日休市，4月7日（周二）复牌交易。节后首个交易日关注北向资金流向+加密货币概念股表现。",
        "duration": "1天",
        "etfs": [],
        "stocks": [],
        "signal": "假期效应，节后首日关注北向资金动向+美伊停火协议后续进展"
      }
    ],
    "sangsha_module": {
      "overall_sentiment": "平稳",
      "advice": "震荡整理，观望为主",
      "avg_buy_prob": 33,
      "avg_panic_prob": 19,
      "analysis_results": [
        {
          "news": "比特币突破70000美元创历史新高！加密货币全线大涨，8万人...",
          "title": "比特币突破70000美元创历史新高！加密货币全线大涨，8万人爆仓",
          "full_title": "比特币突破70000美元创历史新高！加密货币全线大涨，8万人爆仓",
          "summary": "4月6日加密货币市场全线反攻。比特币大涨超3%突破70000美元，最高触及70191.2美元，过去2...",
          "追高买入概率": 90,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 60,
          "情绪标签": [
            "FOMO"
          ],
          "韭菜行为总结": "散户疯了，都在追！",
          "市场含义": "顶部风险",
          "买入概率": 56,
          "is_long_term": true,
          "date": "2026-04-06",
          "decay": 1.0,
          "weighted_buy_prob": 56
        },
        {
          "news": "比特币破7万美元刷屏：8万人爆仓，创历史新高",
          "title": "比特币破7万美元刷屏：8万人爆仓，创历史新高",
          "full_title": "比特币破7万美元刷屏：8万人爆仓，创历史新高",
          "summary": "比特币突破70000美元创历史新高，社交媒体刷屏。最近24小时全球8万人爆仓。Strategy再增持...",
          "追高买入概率": 85,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 62,
          "情绪标签": [
            "FOMO"
          ],
          "韭菜行为总结": "散户疯了，都在追！",
          "市场含义": "顶部风险",
          "买入概率": 53,
          "is_long_term": true,
          "date": "2026-04-06",
          "decay": 1.0,
          "weighted_buy_prob": 53
        },
        {
          "news": "日韩股市集体大涨：韩国KOSPI涨2%，三星电子涨近4%",
          "title": "日韩股市集体大涨：韩国KOSPI涨2%，三星电子涨近4%",
          "full_title": "日韩股市集体大涨：韩国KOSPI涨2%，三星电子涨近4%",
          "summary": "4月6日日韩股市开盘后集体走高。截至北京时间8:10，日经225指数涨0.72%，韩国KOSPI指数...",
          "追高买入概率": 48,
          "抄底买入概率": 20,
          "恐慌卖出概率": 18,
          "观望概率": 68,
          "情绪标签": [
            "FOMO"
          ],
          "韭菜行为总结": "散户开始眼红，想冲进去",
          "市场含义": "分歧加大",
          "买入概率": 37,
          "is_long_term": true,
          "date": "2026-04-06",
          "decay": 1.0,
          "weighted_buy_prob": 37
        },
        {
          "news": "美股科技股盘前普涨：特斯拉涨1.67%，芯片股领涨闪迪涨超4...",
          "title": "美股科技股盘前普涨：特斯拉涨1.67%，芯片股领涨闪迪涨超4%",
          "full_title": "美股科技股盘前普涨：特斯拉涨1.67%，芯片股领涨闪迪涨超4%",
          "summary": "4月6日美股大型科技股盘前集体上涨。特斯拉涨1.67%，Meta涨超1%，微软/谷歌A/亚马逊/英伟...",
          "追高买入概率": 22,
          "抄底买入概率": 54,
          "恐慌卖出概率": 5,
          "观望概率": 73,
          "情绪标签": [
            "抄底冲动",
            "易懂"
          ],
          "韭菜行为总结": "散户想抄底，认为是机会",
          "市场含义": "可能有反弹",
          "买入概率": 35,
          "is_long_term": true,
          "date": "2026-04-06",
          "decay": 1.0,
          "weighted_buy_prob": 35
        },
        {
          "news": "美伊停火协议细节公布：黄金直线拉升原油大跳水，风险资产全面反...",
          "title": "美伊停火协议细节公布：黄金直线拉升原油大跳水，风险资产全面反弹",
          "full_title": "美伊停火协议细节公布：黄金直线拉升原油大跳水，风险资产全面反弹",
          "summary": "4月6日美伊停火协议细节公布。现货黄金全天大幅震荡，开盘后持续下挫一度失守4610美元，此后直线拉升...",
          "追高买入概率": 36,
          "抄底买入概率": 13,
          "恐慌卖出概率": 44,
          "观望概率": 67,
          "情绪标签": [
            "恐慌",
            "易懂"
          ],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 27,
          "is_long_term": true,
          "date": "2026-04-06",
          "decay": 1.0,
          "weighted_buy_prob": 27
        },
        {
          "news": "霍尔木兹海峡传来新消息：国际油价跳水比特币大涨",
          "title": "霍尔木兹海峡传来新消息：国际油价跳水比特币大涨",
          "full_title": "霍尔木兹海峡传来新消息：国际油价跳水比特币大涨",
          "summary": "受美伊停火协议消息面影响，国际油价跳水黄金上扬。截至北京时间4月6日17:50，WTI原油期货跌1....",
          "追高买入概率": 36,
          "抄底买入概率": 5,
          "恐慌卖出概率": 54,
          "观望概率": 67,
          "情绪标签": [
            "恐慌",
            "易懂"
          ],
          "韭菜行为总结": "散户恐慌，想割肉",
          "市场含义": "可能见底",
          "买入概率": 24,
          "is_long_term": true,
          "date": "2026-04-06",
          "decay": 1.0,
          "weighted_buy_prob": 24
        },
        {
          "news": "清明节A股休市：4月7日复牌，关注节后行情",
          "title": "清明节A股休市：4月7日复牌，关注节后行情",
          "full_title": "清明节A股休市：4月7日复牌，关注节后行情",
          "summary": "清明节小长假，A股4月4日至6日休市，4月7日（周二）复牌交易。节后首个交易日关注北向资金流向+加密...",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 5,
          "is_long_term": true,
          "date": "2026-04-06",
          "decay": 1.0,
          "weighted_buy_prob": 5
        }
      ],
      "total_news_count": 7,
      "time_window": "7天累积（长期新闻除外）"
    },
    "white_dragon": {
      "主力状态": "出货",
      "阶段": "末期",
      "行为解释": "多个ETF出现主力派发信号，注意风险",
      "是否利用散户": true,
      "散户情绪": {
        "平均买入概率": 41,
        "平均恐慌概率": 15
      },
      "各ETF分析": [
        {
          "code": "512760",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.0
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 21.72,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 41,
          "sangsha_panic_prob": 15
        },
        {
          "code": "512930",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.43
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 11.41,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 41,
          "sangsha_panic_prob": 15
        },
        {
          "code": "518880",
          "price_trend": {
            "trend": "side",
            "strength": 40,
            "change_pct": 1.33
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": -10.83,
            "level": "normal"
          },
          "主力状态": "观望",
          "阶段": "整理",
          "行为解释": "价格横盘震荡，等待方向选择",
          "是否利用散户": false,
          "sangsha_buy_prob": 41,
          "sangsha_panic_prob": 15
        },
        {
          "code": "588890",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.16
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 0.4,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 41,
          "sangsha_panic_prob": 15
        },
        {
          "code": "159382",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.74
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 29.76,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 41,
          "sangsha_panic_prob": 15
        }
      ],
      "综合建议": "⚠️ 风险提示：主力可能正在派发，散户追高风险大，建议减仓观望"
    }
  },
  "2026-04-04": {
    "date": "2026-04-04",
    "market_tone": "清明假期A股休市，海外市场剧烈分化：黄金暴跌原油飞天，美股科技股逆势走强",
    "wukong_judgment": {
      "emotion": "震荡分化，结构性机会为主",
      "analysis": [
        "黄金高位跳水，原油暴涨突破106美元，大宗商品进入高波动期，地缘风险定价逻辑生变",
        "美股科技股逆势走强，AI芯片、存储板块领涨，纳斯达克涨0.18%",
        "A股节前缩量回调，沪指失守3900点，但CPO/光模块主力资金大举流入，结构性机会明确",
        "特朗普威胁对伊朗更强火力打击，霍尔木兹海峡局势紧张，原油供应缺口达700万桶/日",
        "机构称油价不可能回到冲突前的65美元，能源股配置价值凸显"
      ],
      "strategy": [
        " 油气/能源：布伦特原油突破106美元，节后重点关注石油石化板块",
        " AI芯片/存储：美股映射，节后A股科技股有望跟涨，关注中际旭创/通宇通讯",
        " 黄金贵金属：高位跳水，避险情绪降温，短期回避",
        " 新能源（锂电/光伏）：节前跌幅较大，节后观察企稳信号",
        " 节后首日：关注北向资金流向+主力调仓方向，CPO/油气优先"
      ]
    },
    "bajie_bayesian": {
      "overall": {
        "win_rate": 68,
        "best_action": "节后布局油气+CPO/光模块组合，回避黄金",
        "best_etfs": "160140油气ETF 30% + 515980云计算ETF 25% + 512760芯片ETF 20% + 现金 25%",
        "stop_loss": -7,
        "holding_period": "1-2周",
        "conclusion": "原油供需紧张+AI芯片需求爆发，结构性机会明确。油气胜率72%，CPO胜率70%，黄金胜率仅35%回避。节后重点配置油气+CPO组合。"
      },
      "decision_matrix": [
        {
          "news": "原油突破106美元",
          "win_rate": 72,
          "expected_return": "+10%~+20%",
          "risk_ratio": "1:0.5",
          "action": " 重点做多",
          "priority": 1
        },
        {
          "news": "美股AI芯片领涨",
          "win_rate": 70,
          "expected_return": "+8%~+15%",
          "risk_ratio": "1:0.6",
          "action": " 重点做多",
          "priority": 2
        },
        {
          "news": "CPO主力大举流入",
          "win_rate": 70,
          "expected_return": "+10%~+18%",
          "risk_ratio": "1:0.6",
          "action": " 重点做多",
          "priority": 3
        },
        {
          "news": "黄金高位跳水",
          "win_rate": 35,
          "expected_return": "-5%~+3%",
          "risk_ratio": "1:2",
          "action": " 回避",
          "priority": 4
        },
        {
          "news": "A股节前缩量回调",
          "win_rate": 45,
          "expected_return": "-3%~+5%",
          "risk_ratio": "1:1.2",
          "action": " 观望",
          "priority": 5
        }
      ],
      "news_analysis": [
        {
          "news_title": "原油突破106美元",
          "prior": 70,
          "likelihood": 78,
          "posterior": 72,
          "expected_return": "+10%~+20%",
          "confidence": "[+5%, +28%]",
          "key_variable": "霍尔木兹海峡局势（短期难以缓解，油价仍有上行空间）"
        },
        {
          "news_title": "美股AI芯片领涨",
          "prior": 65,
          "likelihood": 75,
          "posterior": 70,
          "expected_return": "+8%~+15%",
          "confidence": "[+3%, +22%]",
          "key_variable": "美股科技股持续性（若纳斯达克期货继续走强，胜率可提升至75%）"
        },
        {
          "news_title": "CPO主力大举流入",
          "prior": 65,
          "likelihood": 75,
          "posterior": 70,
          "expected_return": "+10%~+18%",
          "confidence": "[+4%, +25%]",
          "key_variable": "通宇通讯/中际旭创节后能否延续强势"
        },
        {
          "news_title": "黄金高位跳水",
          "prior": 55,
          "likelihood": 40,
          "posterior": 35,
          "expected_return": "-5%~+3%",
          "confidence": "[-8%, +6%]",
          "key_variable": "地缘冲突是否升级（若冲突缓和，黄金可能继续回调）"
        },
        {
          "news_title": "A股节前缩量回调",
          "prior": 50,
          "likelihood": 48,
          "posterior": 45,
          "expected_return": "-3%~+5%",
          "confidence": "[-6%, +8%]",
          "key_variable": "节后北向资金流向（若首日净流入>50亿，胜率可回升至55%）"
        }
      ]
    },
    "s_level": [
      {
        "emoji": " ",
        "title": "黄金暴跌原油飞天：特朗普讲话搅动全球大宗商品市场",
        "source": "新浪财经 / 腾讯新闻",
        "summary": "4月2日大宗商品市场剧烈分化。现货黄金从4800美元高位跳水至4616美元，日内大跌2.97%；布伦特原油强势突破106美元/桶，日内涨超5%，创2008年以来新高。特朗普威胁对伊朗进行更强火力打击，霍尔木兹海峡关闭逾一个月造成历史上最大规模供应中断。机构称原油供应缺口达700万桶/日，油价不可能回到冲突前的65美元。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "160140 油气ETF",
            "sentiment": "利好",
            "note": "直接受益油价上涨"
          },
          {
            "name": "518880 黄金ETF",
            "sentiment": "利空",
            "note": "高位回调风险"
          }
        ],
        "stocks": [
          {
            "name": "中国石油",
            "sentiment": "利好",
            "note": "油气龙头"
          },
          {
            "name": "中国海油",
            "sentiment": "利好",
            "note": "海上油气"
          },
          {
            "name": "山东黄金",
            "sentiment": "利空",
            "note": "黄金股承压"
          }
        ],
        "signal": "黄金高位资金撤离，原油地缘溢价飙升，节后重点关注石油石化板块"
      },
      {
        "emoji": " ",
        "title": "美股科技股逆势走强：AI芯片、存储板块领涨",
        "source": "东方财富 / 腾讯新闻",
        "summary": "4月2日美股三大股指分化，道指跌0.13%，标普500涨0.11%，纳指涨0.18%。AI芯片、存储板块逆势走强，澜起科技涨超1%，北京君正涨0.76%。AI算力需求持续爆发，Arm发布首款自研AI芯片。多家芯片企业披露2025年年报，澜起科技营收同比增长49.9%，归母净利润同比增长58.4%。",
        "duration": "2-4周",
        "etfs": [
          {
            "name": "512760 芯片ETF",
            "sentiment": "利好",
            "note": "AI芯片需求爆发"
          },
          {
            "name": "515980 云计算ETF",
            "sentiment": "利好",
            "note": "算力需求增长"
          }
        ],
        "stocks": [
          {
            "name": "中际旭创",
            "sentiment": "利好",
            "note": "CPO龙头"
          },
          {
            "name": "澜起科技",
            "sentiment": "利好",
            "note": "存储芯片"
          },
          {
            "name": "通宇通讯",
            "sentiment": "利好",
            "note": "CPO概念"
          }
        ],
        "signal": "AI芯片需求爆发，节后A股科技股有望跟涨，重点关注CPO/光模块"
      }
    ],
    "a_level": [
      {
        "emoji": " ",
        "title": "A股三大指数收跌：沪指跌0.74%险守3900点，油气养殖医药逆势走强",
        "source": "新浪财经 / 东方财富",
        "summary": "4月2日A股全天震荡走弱，三大指数集体收跌。沪指跌0.74%报3919点，深成指跌1.60%，创业板指跌2.31%。石油石化、医药商业、能源金属等板块涨幅居前，贵金属、通信服务、元件等板块跌幅居前。主力资金上，石油石化、银行、化学制药等行业概念流入居前。",
        "duration": "1-2天",
        "etfs": [
          {
            "name": "510300 沪深300ETF",
            "sentiment": "中性",
            "note": "大盘震荡"
          },
          {
            "name": "159915 创业板ETF",
            "sentiment": "利空",
            "note": "科技成长承压"
          }
        ],
        "stocks": [
          {
            "name": "中国石化",
            "sentiment": "利好",
            "note": "油气板块"
          },
          {
            "name": "恒瑞医药",
            "sentiment": "利好",
            "note": "医药商业"
          }
        ],
        "signal": "节前避险情绪浓厚，个股普跌，但油气/医药逆势走强"
      },
      {
        "emoji": " ",
        "title": "央行净回笼1452亿元：资金面边际收紧",
        "source": "央行公告",
        "summary": "4月2日央行开展逆回购操作，单日净回笼1452亿元。资金面边际收紧，银行间市场利率小幅上行。",
        "duration": "1-3天",
        "etfs": [
          {
            "name": "511880 银华日利",
            "sentiment": "中性",
            "note": "货币基金"
          }
        ],
        "stocks": [
          {
            "name": "招商银行",
            "sentiment": "中性",
            "note": "银行股"
          }
        ],
        "signal": "资金面边际收紧，关注节后流动性变化"
      }
    ],
    "douyin": [],
    "sangsha_module": {
      "overall_sentiment": "平稳",
      "advice": "震荡整理，观望为主",
      "avg_buy_prob": 23,
      "avg_panic_prob": 17,
      "analysis_results": [
        {
          "news": "美股科技股逆势走强：AI芯片、存储板块领涨",
          "title": "美股科技股逆势走强：AI芯片、存储板块领涨",
          "full_title": "美股科技股逆势走强：AI芯片、存储板块领涨",
          "summary": "4月2日美股三大股指分化，道指跌0.13%，标普500涨0.11%，纳指涨0.18%。AI芯片、存储...",
          "追高买入概率": 50,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 77,
          "情绪标签": [
            "FOMO",
            "易懂"
          ],
          "韭菜行为总结": "散户开始眼红，想冲进去",
          "市场含义": "分歧加大",
          "买入概率": 32,
          "is_long_term": true,
          "date": "2026-04-04",
          "decay": 1.0,
          "weighted_buy_prob": 32
        },
        {
          "news": "A股三大指数收跌：沪指跌0.74%险守3900点，油气养殖医...",
          "title": "A股三大指数收跌：沪指跌0.74%险守3900点，油气养殖医药逆势走强",
          "full_title": "A股三大指数收跌：沪指跌0.74%险守3900点，油气养殖医药逆势走强",
          "summary": "4月2日A股全天震荡走弱，三大指数集体收跌。沪指跌0.74%报3919点，深成指跌1.60%，创业板...",
          "追高买入概率": 50,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 77,
          "情绪标签": [
            "FOMO",
            "易懂"
          ],
          "韭菜行为总结": "散户开始眼红，想冲进去",
          "市场含义": "分歧加大",
          "买入概率": 32,
          "is_long_term": true,
          "date": "2026-04-04",
          "decay": 1.0,
          "weighted_buy_prob": 32
        },
        {
          "news": "黄金暴跌原油飞天：特朗普讲话搅动全球大宗商品市场",
          "title": "黄金暴跌原油飞天：特朗普讲话搅动全球大宗商品市场",
          "full_title": "黄金暴跌原油飞天：特朗普讲话搅动全球大宗商品市场",
          "summary": "4月2日大宗商品市场剧烈分化。现货黄金从4800美元高位跳水至4616美元，日内大跌2.97%；布伦...",
          "追高买入概率": 38,
          "抄底买入概率": 5,
          "恐慌卖出概率": 55,
          "观望概率": 66,
          "情绪标签": [
            "恐慌",
            "易懂"
          ],
          "韭菜行为总结": "散户恐慌，想割肉",
          "市场含义": "可能见底",
          "买入概率": 25,
          "is_long_term": true,
          "date": "2026-04-04",
          "decay": 1.0,
          "weighted_buy_prob": 25
        },
        {
          "news": "央行净回笼1452亿元：资金面边际收紧",
          "title": "央行净回笼1452亿元：资金面边际收紧",
          "full_title": "央行净回笼1452亿元：资金面边际收紧",
          "summary": "4月2日央行开展逆回购操作，单日净回笼1452亿元。资金面边际收紧，银行间市场利率小幅上行。",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 5,
          "is_long_term": true,
          "date": "2026-04-04",
          "decay": 1.0,
          "weighted_buy_prob": 5
        }
      ],
      "total_news_count": 4,
      "time_window": "7天累积（长期新闻除外）"
    },
    "white_dragon": {
      "主力状态": "出货",
      "阶段": "末期",
      "行为解释": "多个ETF出现主力派发信号，注意风险",
      "是否利用散户": true,
      "散户情绪": {
        "平均买入概率": 23,
        "平均恐慌概率": 17
      },
      "各ETF分析": [
        {
          "code": "512760",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.0
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 21.72,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 23,
          "sangsha_panic_prob": 17
        },
        {
          "code": "512930",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.43
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 11.41,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 23,
          "sangsha_panic_prob": 17
        },
        {
          "code": "518880",
          "price_trend": {
            "trend": "side",
            "strength": 40,
            "change_pct": 1.33
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": -10.83,
            "level": "normal"
          },
          "主力状态": "吸筹",
          "阶段": "早期",
          "行为解释": "价格横盘/小跌，资金流入，主力可能在低位吸筹",
          "是否利用散户": false,
          "sangsha_buy_prob": 23,
          "sangsha_panic_prob": 17
        },
        {
          "code": "588890",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.16
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 0.4,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 23,
          "sangsha_panic_prob": 17
        },
        {
          "code": "159382",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.74
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 29.76,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 23,
          "sangsha_panic_prob": 17
        }
      ],
      "综合建议": "⚠️ 风险提示：主力可能正在派发，散户追高风险大，建议减仓观望"
    }
  },
  "2026-04-02": {
    "date": "2026-04-02",
    "market_tone": "谨慎偏空 A股全线收跌，创业板指跌近2%，科技/新能源领跌，油气/存储逆势走强，市场防御情绪浓厚",
    "wukong_judgment": {
      "emotion": "谨慎偏空",
      "analysis": [
        "A股四大指数集体收跌，创业板指跌1.78%，沪指跌0.53%，全市场逾4200只个股下跌",
        "锂电池、光伏、黄金等昨日强势板块今日补跌，资金轮动至油气/存储板块",
        "特朗普称2-3周内结束对伊战争，避险情绪降温，黄金原油双双回落",
        "美股收高但纳斯达克期货跌1%，警惕今夜美股压力传导"
      ],
      "strategy": [
        " 油气/存储：逆势走强，短线资金可关注",
        " 芯片ETF：美股芯片暴涨映射，A股跟涨有限但不追高",
        " 新能源（锂电/光伏）：今日跌幅大，短线回避",
        " 黄金板块：冲高回落，短期顶部信号，控制风险",
        " 医药：分化明显，观望为主"
      ]
    },
    "s_level": [
      {
        "emoji": " ",
        "title": "A股全线收跌 创业板指跌1.78%，逾4200股下跌",
        "source": "新浪财经 / 东方财富",
        "summary": "4月2日A股四大指数集体收跌，创业板指跌1.78%，沪指跌0.53%，深成指跌1.12%，科创50跌0.89%。全市场逾4200只个股下跌，成交额萎缩至1.1万亿。锂电池、光伏、黄金、铝业等板块跌幅靠前，油气、存储器板块逆势走强。",
        "duration": "1-2天",
        "etfs": [
          {
            "name": "159915 创业板ETF",
            "sentiment": "利空",
            "note": "科技成长承压"
          },
          {
            "name": "515700 新能源ETF",
            "sentiment": "利空",
            "note": "锂电/光伏跌幅大"
          },
          {
            "name": "518880 黄金ETF",
            "sentiment": "利空",
            "note": "避险情绪回落"
          },
          {
            "name": "160140 油气ETF",
            "sentiment": "利好",
            "note": "逆势走强"
          }
        ],
        "stocks": [
          {
            "name": "600028 中国石化",
            "sentiment": "利好",
            "note": "油气板块相对抗跌"
          },
          {
            "name": "601857 中国石油",
            "sentiment": "利好",
            "note": "油气板块相对抗跌"
          },
          {
            "name": "300750 宁德时代",
            "sentiment": "利空",
            "note": "新能源板块领跌"
          },
          {
            "name": "601012 隆基绿能",
            "sentiment": "利空",
            "note": "光伏板块跌幅靠前"
          }
        ]
      },
      {
        "emoji": " ",
        "title": "黄金冲高回落 现货黄金跌破4700美元",
        "source": "搜狐 / 新华社 / 金投网",
        "summary": "4月2日现货黄金一度涨破4800美元/盎司，创历史新高后回落，收盘跌超2%报4656美元。特朗普称将在2-3周内结束对伊战争，市场避险情绪降温，黄金多头获利了结。国内黄金股集体回调。",
        "duration": "1-3天",
        "etfs": [
          {
            "name": "518880 黄金ETF",
            "sentiment": "警惕",
            "note": "短期顶部信号，高位回落"
          }
        ],
        "stocks": [
          {
            "name": "600547 山东黄金",
            "sentiment": "警惕",
            "note": "金价回落，短线回避"
          },
          {
            "name": "601899 紫金矿业",
            "sentiment": "警惕",
            "note": "金价回落，短线回避"
          },
          {
            "name": "600489 中金黄金",
            "sentiment": "警惕",
            "note": "跟随回调"
          }
        ],
        "warning": "黄金冲高后大幅回落，短期顶部信号明显。勿追高，等回调后再关注"
      },
      {
        "emoji": " ",
        "title": "美股收高但期货下跌 纳指涨1.16%芯片暴涨",
        "source": "财联社 / 华尔街见闻",
        "summary": "美股周三收高，纳指涨1.16%，芯片股暴涨：西部数据+10%，美光科技/英特尔+8%，AMD+3%。但盘后期货走弱，纳指期货跌超1%，警惕今夜美股压力传导。A股存储芯片板块今日逆势走强。",
        "duration": "1-2天",
        "etfs": [
          {
            "name": "513500 标普ETF",
            "sentiment": "中性",
            "note": "美股收高但期货弱"
          },
          {
            "name": "512760 芯片ETF",
            "sentiment": "利好",
            "note": "美股芯片暴涨映射"
          }
        ],
        "stocks": [
          {
            "name": "688981 中芯国际",
            "sentiment": "关注",
            "note": "跟涨美股芯片但力度有限"
          },
          {
            "name": "688008 澜起科技",
            "sentiment": "利好",
            "note": "存储芯片逆势走强"
          },
          {
            "name": "002049 国星光电",
            "sentiment": "关注",
            "note": "存储概念"
          }
        ]
      },
      {
        "emoji": " ",
        "title": "原油暴跌 布伦特原油跌破100美元",
        "source": "腾讯网 / 财联社",
        "summary": "4月2日布伦特原油期货暴跌，跌破100美元关口，报99.95美元/桶，日内跌超1.5%。WTI原油跌至95美元附近。特朗普称将2-3周内结束对伊战争，市场对原油供应中断担忧缓解，油价承压。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "160140 油气ETF",
            "sentiment": "利空",
            "note": "油价跌破关键支撑"
          },
          {
            "name": "512880 国债ETF",
            "sentiment": "利好",
            "note": "通胀预期回落"
          }
        ],
        "stocks": [
          {
            "name": "600188 兖矿能源",
            "sentiment": "利空",
            "note": "煤炭跟油气联动"
          },
          {
            "name": "601666 平煤股份",
            "sentiment": "利空",
            "note": "煤价承压"
          },
          {
            "name": "601857 中国石油",
            "sentiment": "利空",
            "note": "油价下跌压力"
          }
        ]
      }
    ],
    "a_level": [
      {
        "emoji": " ",
        "title": "医药板块分化 化学制药相对抗跌",
        "source": "新浪财经 / 东方财富",
        "summary": "昨日医药涨停潮今日果然分化，化学制药板块相对抗跌，但整体医药板块走弱。CXO、中药板块回调明显，资金获利了结。创新药ETF跌1.2%。",
        "duration": "1-2天",
        "etfs": [
          {
            "name": "159992 创新药ETF",
            "sentiment": "中性",
            "note": "分化行情"
          },
          {
            "name": "512010 医药ETF",
            "sentiment": "中性",
            "note": "整体回调"
          }
        ],
        "stocks": [
          {
            "name": "300759 凯莱英",
            "sentiment": "中性",
            "note": "昨日涨停今日承压"
          },
          {
            "name": "603259 药明康德",
            "sentiment": "中性",
            "note": "CXO板块分化"
          },
          {
            "name": "300760 迈瑞医疗",
            "sentiment": "中性",
            "note": "医疗器械相对稳定"
          }
        ],
        "warning": "昨日追高医药的投资者需警惕，获利盘兑现压力较大"
      },
      {
        "emoji": " ",
        "title": "SpaceX递交上市申请 A股航天板块蠢蠢欲动",
        "source": "新华社",
        "summary": "SpaceX已秘密提交IPO申请，估值超1.75万亿美元，成三巨头超级IPO首家。A股航天军工板块有望跟随炒作。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "515980 云计算ETF",
            "sentiment": "利好",
            "note": "商业航天概念"
          }
        ],
        "stocks": [
          {
            "name": "600760 中航沈飞",
            "sentiment": "关注",
            "note": "航天军工龙头"
          },
          {
            "name": "002025 航天电器",
            "sentiment": "关注",
            "note": "航天连接器"
          }
        ]
      },
      {
        "emoji": " ",
        "title": "存储芯片/油气板块逆势走强",
        "source": "财联社",
        "summary": "存储器板块和油气开采板块今日逆势走强，贝肯能源高开近6%，市场资金寻找相对安全方向。",
        "duration": "1-3天",
        "etfs": [
          {
            "name": "512760 芯片ETF",
            "sentiment": "利好",
            "note": "存储芯片相对强势"
          },
          {
            "name": "160140 油气ETF",
            "sentiment": "利好",
            "note": "防御性资金流入"
          }
        ],
        "stocks": [
          {
            "name": "688981 中芯国际",
            "sentiment": "关注",
            "note": "存储/成熟制程相对抗跌"
          },
          {
            "name": "600028 中国石化",
            "sentiment": "关注",
            "note": "油气防御性"
          }
        ]
      }
    ],
    "douyin": [
      {
        "emoji": " ",
        "title": "SpaceX IPO消息持续发酵 社交媒体热度不减",
        "source": "抖音热榜 / 微博热搜",
        "summary": "SpaceX递交上市申请消息在社交媒体刷屏，马斯克1.75万亿美元超级独角兽成为热议话题。A股航天军工板块关注度提升。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "515980 云计算ETF",
            "sentiment": "关注",
            "note": "商业航天概念"
          }
        ],
        "stocks": [
          {
            "name": "600760 中航沈飞",
            "sentiment": "关注",
            "note": "航天军工龙头"
          },
          {
            "name": "002025 航天电器",
            "sentiment": "关注",
            "note": "航天连接器"
          }
        ],
        "signal": "题材炒作为主，A股实质受益标的有限，注意风险"
      },
      {
        "emoji": " ",
        "title": "AI大模型第一股智谱涨31.94%",
        "source": "新浪新闻 / 抖音财经",
        "summary": "4月1日AI大模型第一股智谱涨31.94%，人形机器人第一股优必选涨17.10%。AI算力需求持续爆发，带动相关概念股走强。但今日A股AI板块跟随大盘回调。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "512930 AI人工智能ETF",
            "sentiment": "利好",
            "note": "AI算力需求"
          }
        ],
        "stocks": [
          {
            "name": "688981 中芯国际",
            "sentiment": "关注",
            "note": "AI算力需求"
          },
          {
            "name": "688008 澜起科技",
            "sentiment": "关注",
            "note": "AI算力需求"
          },
          {
            "name": "688111 金山办公",
            "sentiment": "关注",
            "note": "AI办公应用"
          }
        ],
        "signal": "AI概念短期回调，中长期仍具配置价值"
      }
    ],
    "sangsha_module": {
      "overall_sentiment": "平稳",
      "advice": "震荡整理，观望为主",
      "avg_buy_prob": 23,
      "avg_panic_prob": 13,
      "analysis_results": [
        {
          "news": "医药板块分化 化学制药相对抗跌",
          "title": "医药板块分化 化学制药相对抗跌",
          "full_title": "医药板块分化 化学制药相对抗跌",
          "summary": "昨日医药涨停潮今日果然分化，化学制药板块相对抗跌，但整体医药板块走弱。CXO、中药板块回调明显，资金...",
          "追高买入概率": 95,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 59,
          "情绪标签": [
            "FOMO",
            "易懂"
          ],
          "韭菜行为总结": "散户疯了，都在追！",
          "市场含义": "顶部风险",
          "买入概率": 59,
          "is_long_term": false,
          "date": "2026-04-02",
          "decay": 1.0,
          "weighted_buy_prob": 59
        },
        {
          "news": "美股收高但期货下跌 纳指涨1.16%芯片暴涨",
          "title": "美股收高但期货下跌 纳指涨1.16%芯片暴涨",
          "full_title": "美股收高但期货下跌 纳指涨1.16%芯片暴涨",
          "summary": "美股周三收高，纳指涨1.16%，芯片股暴涨：西部数据+10%，美光科技/英特尔+8%，AMD+3%。...",
          "追高买入概率": 89,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 61,
          "情绪标签": [
            "FOMO",
            "易懂"
          ],
          "韭菜行为总结": "散户疯了，都在追！",
          "市场含义": "顶部风险",
          "买入概率": 55,
          "is_long_term": false,
          "date": "2026-04-02",
          "decay": 1.0,
          "weighted_buy_prob": 55
        },
        {
          "news": "黄金冲高回落 现货黄金跌破4700美元",
          "title": "黄金冲高回落 现货黄金跌破4700美元",
          "full_title": "黄金冲高回落 现货黄金跌破4700美元",
          "summary": "4月2日现货黄金一度涨破4800美元/盎司，创历史新高后回落，收盘跌超2%报4656美元。特朗普称将...",
          "追高买入概率": 82,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 64,
          "情绪标签": [
            "FOMO",
            "易懂"
          ],
          "韭菜行为总结": "散户疯了，都在追！",
          "市场含义": "顶部风险",
          "买入概率": 51,
          "is_long_term": false,
          "date": "2026-04-02",
          "decay": 1.0,
          "weighted_buy_prob": 51
        },
        {
          "news": "A股全线收跌 创业板指跌1.78%，逾4200股下跌",
          "title": "A股全线收跌 创业板指跌1.78%，逾4200股下跌",
          "full_title": "A股全线收跌 创业板指跌1.78%，逾4200股下跌",
          "summary": "4月2日A股四大指数集体收跌，创业板指跌1.78%，沪指跌0.53%，深成指跌1.12%，科创50跌...",
          "追高买入概率": 20,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 89,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 14,
          "is_long_term": false,
          "date": "2026-04-02",
          "decay": 1.0,
          "weighted_buy_prob": 14
        },
        {
          "news": "AI大模型第一股智谱涨31.94%",
          "title": "AI大模型第一股智谱涨31.94%",
          "full_title": "AI大模型第一股智谱涨31.94%",
          "summary": "4月1日AI大模型第一股智谱涨31.94%，人形机器人第一股优必选涨17.10%。AI算力需求持续爆...",
          "追高买入概率": 20,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 89,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 14,
          "is_long_term": false,
          "date": "2026-04-02",
          "decay": 1.0,
          "weighted_buy_prob": 14
        },
        {
          "news": "原油暴跌 布伦特原油跌破100美元",
          "title": "原油暴跌 布伦特原油跌破100美元",
          "full_title": "原油暴跌 布伦特原油跌破100美元",
          "summary": "4月2日布伦特原油期货暴跌，跌破100美元关口，报99.95美元/桶，日内跌超1.5%。WTI原油跌...",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 78,
          "观望概率": 73,
          "情绪标签": [
            "恐慌"
          ],
          "韭菜行为总结": "散户恐慌，想割肉",
          "市场含义": "可能见底",
          "买入概率": 5,
          "is_long_term": false,
          "date": "2026-04-02",
          "decay": 1.0,
          "weighted_buy_prob": 5
        },
        {
          "news": "SpaceX递交上市申请 A股航天板块蠢蠢欲动",
          "title": "SpaceX递交上市申请 A股航天板块蠢蠢欲动",
          "full_title": "SpaceX递交上市申请 A股航天板块蠢蠢欲动",
          "summary": "SpaceX已秘密提交IPO申请，估值超1.75万亿美元，成三巨头超级IPO首家。A股航天军工板块有...",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 5,
          "is_long_term": false,
          "date": "2026-04-02",
          "decay": 1.0,
          "weighted_buy_prob": 5
        },
        {
          "news": "存储芯片/油气板块逆势走强",
          "title": "存储芯片/油气板块逆势走强",
          "full_title": "存储芯片/油气板块逆势走强",
          "summary": "存储器板块和油气开采板块今日逆势走强，贝肯能源高开近6%，市场资金寻找相对安全方向。",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 5,
          "is_long_term": false,
          "date": "2026-04-02",
          "decay": 1.0,
          "weighted_buy_prob": 5
        },
        {
          "news": "SpaceX IPO消息持续发酵 社交媒体热度不减",
          "title": "SpaceX IPO消息持续发酵 社交媒体热度不减",
          "full_title": "SpaceX IPO消息持续发酵 社交媒体热度不减",
          "summary": "SpaceX递交上市申请消息在社交媒体刷屏，马斯克1.75万亿美元超级独角兽成为热议话题。A股航天军...",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 5,
          "is_long_term": false,
          "date": "2026-04-02",
          "decay": 1.0,
          "weighted_buy_prob": 5
        }
      ],
      "total_news_count": 9,
      "time_window": "7天累积（长期新闻除外）"
    },
    "white_dragon": {
      "主力状态": "出货",
      "阶段": "末期",
      "行为解释": "多个ETF出现主力派发信号，注意风险",
      "是否利用散户": true,
      "散户情绪": {
        "平均买入概率": 38,
        "平均恐慌概率": 5
      },
      "各ETF分析": [
        {
          "code": "512760",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.0
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 21.72,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 38,
          "sangsha_panic_prob": 5
        },
        {
          "code": "512930",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.43
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 11.41,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 38,
          "sangsha_panic_prob": 5
        },
        {
          "code": "518880",
          "price_trend": {
            "trend": "side",
            "strength": 40,
            "change_pct": 1.33
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": -10.83,
            "level": "normal"
          },
          "主力状态": "吸筹",
          "阶段": "早期",
          "行为解释": "价格横盘/小跌，资金流入，主力可能在低位吸筹",
          "是否利用散户": false,
          "sangsha_buy_prob": 38,
          "sangsha_panic_prob": 5
        },
        {
          "code": "588890",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.16
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 0.4,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 38,
          "sangsha_panic_prob": 5
        },
        {
          "code": "159382",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.74
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 29.76,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 38,
          "sangsha_panic_prob": 5
        }
      ],
      "综合建议": "⚠️ 风险提示：主力可能正在派发，散户追高风险大，建议减仓观望"
    }
  },
  "2026-04-01": {
    "date": "2026-04-01",
    "market_tone": "情绪反转日！美伊释放停火信号，全球风险资产普涨，A股跟涨1%+",
    "wukong_judgment": {
      "emotion": "偏多",
      "analysis": [
        "美伊局势缓和预期引爆全球反弹，A股跟涨",
        "科技股、医药股领涨，避险资产承压",
        "情绪修复明显，但仍需关注后续谈判进展"
      ],
      "strategy": [
        " 跟随情绪修复，优先布局超跌科技/医药",
        " 避险资产短期回调，等待地缘风险反复再介入",
        " 关注SpaceX IPO概念股"
      ]
    },
    "s_level": [
      {
        "emoji": " ",
        "title": "全球股市暴涨：日经+4%、韩国+8%",
        "source": "财联社",
        "summary": "美伊局势缓和预期升温，全球风险资产狂欢。日经225涨4%，韩国KOSPI涨8%，欧洲多国涨3%以上。",
        "duration": "2-4周",
        "etfs": [
          {
            "name": "512500 中证500ETF",
            "sentiment": "利好"
          },
          {
            "name": "159915 创业板ETF",
            "sentiment": "利好"
          },
          {
            "name": "512760 芯片ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          {
            "name": "688981 中芯国际",
            "sentiment": "利好"
          },
          {
            "name": "300750 宁德时代",
            "sentiment": "利好"
          },
          {
            "name": "600519 贵州茅台",
            "sentiment": "利好"
          }
        ]
      }
    ],
    "a_level": [
      {
        "emoji": " ",
        "title": "医药板块掀涨停潮",
        "source": "东方财富",
        "summary": "医药生物板块领涨两市，港股创新药ETF暴涨超7%，A股多股涨停。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "159992 创新药ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          {
            "name": "广生堂",
            "sentiment": "利好"
          },
          {
            "name": "睿智医药",
            "sentiment": "利好"
          },
          {
            "name": "凯莱英",
            "sentiment": "利好"
          }
        ]
      },
      {
        "emoji": " ",
        "title": "SpaceX载人飞船发射成功",
        "source": "新浪财经",
        "summary": "美国SpaceX载人飞船搭载4名宇航员发射升空。SpaceX已秘密提交IPO申请。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "515980 云计算ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          {
            "name": "600760 中航沈飞",
            "sentiment": "利好"
          },
          {
            "name": "002025 航天电器",
            "sentiment": "利好"
          }
        ]
      }
    ],
    "douyin": [
      {
        "emoji": " ",
        "title": "SpaceX IPO消息刷屏",
        "source": "社交媒体",
        "summary": "SpaceX IPO消息在社交媒体引发热议，估值1.75万亿美元。",
        "duration": "1-2周",
        "etfs": [],
        "stocks": []
      }
    ],
    "sangsha_module": {
      "overall_sentiment": "平稳",
      "advice": "震荡整理，观望为主",
      "avg_buy_prob": 25,
      "avg_panic_prob": 11,
      "analysis_results": [
        {
          "news": "医药板块掀涨停潮",
          "title": "医药板块掀涨停潮",
          "full_title": "医药板块掀涨停潮",
          "summary": "医药生物板块领涨两市，港股创新药ETF暴涨超7%，A股多股涨停。",
          "追高买入概率": 95,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 59,
          "情绪标签": [
            "FOMO",
            "易懂"
          ],
          "韭菜行为总结": "散户疯了，都在追！",
          "市场含义": "顶部风险",
          "买入概率": 59,
          "is_long_term": false,
          "date": "2026-04-01",
          "decay": 1.0,
          "weighted_buy_prob": 59
        },
        {
          "news": "全球股市暴涨：日经+4%、韩国+8%",
          "title": "全球股市暴涨：日经+4%、韩国+8%",
          "full_title": "全球股市暴涨：日经+4%、韩国+8%",
          "summary": "美伊局势缓和预期升温，全球风险资产狂欢。日经225涨4%，韩国KOSPI涨8%，欧洲多国涨3%以上。",
          "追高买入概率": 48,
          "抄底买入概率": 5,
          "恐慌卖出概率": 31,
          "观望概率": 69,
          "情绪标签": [
            "FOMO"
          ],
          "韭菜行为总结": "散户开始眼红，想冲进去",
          "市场含义": "分歧加大",
          "买入概率": 31,
          "is_long_term": false,
          "date": "2026-04-01",
          "decay": 1.0,
          "weighted_buy_prob": 31
        },
        {
          "news": "SpaceX载人飞船发射成功",
          "title": "SpaceX载人飞船发射成功",
          "full_title": "SpaceX载人飞船发射成功",
          "summary": "美国SpaceX载人飞船搭载4名宇航员发射升空。SpaceX已秘密提交IPO申请。",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 5,
          "is_long_term": false,
          "date": "2026-04-01",
          "decay": 1.0,
          "weighted_buy_prob": 5
        },
        {
          "news": "SpaceX IPO消息刷屏",
          "title": "SpaceX IPO消息刷屏",
          "full_title": "SpaceX IPO消息刷屏",
          "summary": "SpaceX IPO消息在社交媒体引发热议，估值1.75万亿美元。",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 5,
          "is_long_term": false,
          "date": "2026-04-01",
          "decay": 1.0,
          "weighted_buy_prob": 5
        }
      ],
      "total_news_count": 4,
      "time_window": "7天累积（长期新闻除外）"
    },
    "white_dragon": {
      "主力状态": "出货",
      "阶段": "末期",
      "行为解释": "多个ETF出现主力派发信号，注意风险",
      "是否利用散户": true,
      "散户情绪": {
        "平均买入概率": 25,
        "平均恐慌概率": 11
      },
      "各ETF分析": [
        {
          "code": "512760",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.0
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 21.72,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 25,
          "sangsha_panic_prob": 11
        },
        {
          "code": "512930",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.43
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 11.41,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 25,
          "sangsha_panic_prob": 11
        },
        {
          "code": "518880",
          "price_trend": {
            "trend": "side",
            "strength": 40,
            "change_pct": 1.33
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": -10.83,
            "level": "normal"
          },
          "主力状态": "吸筹",
          "阶段": "早期",
          "行为解释": "价格横盘/小跌，资金流入，主力可能在低位吸筹",
          "是否利用散户": false,
          "sangsha_buy_prob": 25,
          "sangsha_panic_prob": 11
        },
        {
          "code": "588890",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.16
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 0.4,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 25,
          "sangsha_panic_prob": 11
        },
        {
          "code": "159382",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.74
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 29.76,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 25,
          "sangsha_panic_prob": 11
        }
      ],
      "综合建议": "⚠️ 风险提示：主力可能正在派发，散户追高风险大，建议减仓观望"
    }
  },
  "2026-03-31": {
    "date": "2026-03-31",
    "market_tone": "季末收官战，多空博弈激烈，科技股分化明显",
    "wukong_judgment": {
      "emotion": "中性偏谨慎",
      "analysis": [
        "季末资金面紧张，机构调仓换股",
        "科技股业绩分化，龙头走强、小票承压",
        "等待4月财报季明朗方向"
      ],
      "strategy": [
        " 控制仓位，观望为主",
        " 关注一季报超预期个股",
        " 黄金/避险资产可适当配置"
      ]
    },
    "s_level": [
      {
        "emoji": " ",
        "title": "季末资金面紧张 利率上行压力",
        "source": "央行公开市场操作",
        "summary": "季末流动性紧张，央行连续多日净投放，但资金利率仍上行。银行间7天回购利率突破3%。",
        "duration": "1周",
        "etfs": [
          {
            "name": "512880 国债ETF",
            "sentiment": "利空",
            "note": "利率上行压力"
          },
          {
            "name": "511010 国债ETF",
            "sentiment": "利空"
          }
        ],
        "stocks": [
          {
            "name": "600036 招商银行",
            "sentiment": "关注",
            "note": "息差管理能力"
          },
          {
            "name": "601398 工商银行",
            "sentiment": "关注"
          }
        ]
      }
    ],
    "a_level": [
      {
        "emoji": " ",
        "title": "消博会即将开幕 海南自贸港概念",
        "source": "商务部公告",
        "summary": "第三届消博会4月10日开幕，海南自贸港政策利好预期升温。",
        "duration": "1-2周",
        "etfs": [],
        "stocks": [
          {
            "name": "002594 比亚迪",
            "sentiment": "关注",
            "note": "新能源车参展"
          },
          {
            "name": "600745 闻泰科技",
            "sentiment": "关注"
          }
        ]
      }
    ],
    "douyin": [],
    "sangsha_module": {
      "overall_sentiment": "平稳",
      "advice": "震荡整理，观望为主",
      "avg_buy_prob": 19,
      "avg_panic_prob": 5,
      "analysis_results": [
        {
          "news": "季末资金面紧张 利率上行压力",
          "title": "季末资金面紧张 利率上行压力",
          "full_title": "季末资金面紧张 利率上行压力",
          "summary": "季末流动性紧张，央行连续多日净投放，但资金利率仍上行。银行间7天回购利率突破3%。",
          "追高买入概率": 54,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 75,
          "情绪标签": [
            "FOMO"
          ],
          "韭菜行为总结": "散户开始眼红，想冲进去",
          "市场含义": "分歧加大",
          "买入概率": 34,
          "is_long_term": true,
          "date": "2026-03-31",
          "decay": 1.0,
          "weighted_buy_prob": 34
        },
        {
          "news": "消博会即将开幕 海南自贸港概念",
          "title": "消博会即将开幕 海南自贸港概念",
          "full_title": "消博会即将开幕 海南自贸港概念",
          "summary": "第三届消博会4月10日开幕，海南自贸港政策利好预期升温。",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 5,
          "is_long_term": true,
          "date": "2026-03-31",
          "decay": 1.0,
          "weighted_buy_prob": 5
        }
      ],
      "total_news_count": 2,
      "time_window": "7天累积（长期新闻除外）"
    },
    "white_dragon": {
      "主力状态": "出货",
      "阶段": "末期",
      "行为解释": "多个ETF出现主力派发信号，注意风险",
      "是否利用散户": true,
      "散户情绪": {
        "平均买入概率": 19,
        "平均恐慌概率": 5
      },
      "各ETF分析": [
        {
          "code": "512760",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.0
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 21.72,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 19,
          "sangsha_panic_prob": 5
        },
        {
          "code": "512930",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.43
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 11.41,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 19,
          "sangsha_panic_prob": 5
        },
        {
          "code": "518880",
          "price_trend": {
            "trend": "side",
            "strength": 40,
            "change_pct": 1.33
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": -10.83,
            "level": "normal"
          },
          "主力状态": "吸筹",
          "阶段": "早期",
          "行为解释": "价格横盘/小跌，资金流入，主力可能在低位吸筹",
          "是否利用散户": false,
          "sangsha_buy_prob": 19,
          "sangsha_panic_prob": 5
        },
        {
          "code": "588890",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.16
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 0.4,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 19,
          "sangsha_panic_prob": 5
        },
        {
          "code": "159382",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.74
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 29.76,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 19,
          "sangsha_panic_prob": 5
        }
      ],
      "综合建议": "⚠️ 风险提示：主力可能正在派发，散户追高风险大，建议减仓观望"
    }
  },
  "2026-03-30": {
    "date": "2026-03-30",
    "market_tone": "科技股分化日，业绩为王，龙头走强",
    "wukong_judgment": {
      "emotion": "中性偏多",
      "analysis": [
        "TCL科技业绩超预期，面板周期拐点确认",
        "小米汽车交付数据亮眼，新能源车链活跃",
        "黄金避险情绪延续"
      ],
      "strategy": [
        " 关注业绩超预期的科技龙头",
        " 黄金/白银ETF可持有",
        " 高估值小票规避"
      ]
    },
    "s_level": [
      {
        "emoji": " ",
        "title": "TCL科技业绩超预期 面板周期拐点",
        "source": "公司公告",
        "summary": "TCL科技发布2026年一季报，净利润同比增长150%，面板价格持续上涨。行业周期拐点确认。",
        "duration": "2-4周",
        "etfs": [
          {
            "name": "512760 芯片ETF",
            "sentiment": "利好",
            "note": "电子产业链联动"
          },
          {
            "name": "159995 芯片ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          {
            "name": "000100 TCL科技",
            "sentiment": "利好",
            "note": "业绩超预期"
          },
          {
            "name": "002049 国星光电",
            "sentiment": "利好",
            "note": "LED面板"
          },
          {
            "name": "002241 歌尔股份",
            "sentiment": "利好",
            "note": "消费电子"
          }
        ]
      },
      {
        "emoji": " ",
        "title": "小米汽车交付破万 新能源车链活跃",
        "source": "小米汽车官方",
        "summary": "小米汽车3月交付量突破1万台，超市场预期。新能源汽车市场竞争加剧。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "515030 新能源车ETF",
            "sentiment": "利好"
          },
          {
            "name": "516390 智能汽车ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          {
            "name": "300750 宁德时代",
            "sentiment": "利好",
            "note": "动力电池龙头"
          },
          {
            "name": "002594 比亚迪",
            "sentiment": "利好",
            "note": "新能源车龙头"
          }
        ]
      }
    ],
    "a_level": [
      {
        "emoji": " ",
        "title": "汇川技术港股上市 工业自动化龙头",
        "source": "港交所公告",
        "summary": "汇川技术港股成功上市，募资用于工业自动化产能扩张。",
        "duration": "1周",
        "etfs": [],
        "stocks": [
          {
            "name": "300124 汇川技术",
            "sentiment": "利好",
            "note": "工业自动化龙头"
          }
        ]
      },
      {
        "emoji": " ",
        "title": "瑞云冷链IPO过会 冷链物流概念",
        "source": "证监会公告",
        "summary": "瑞云冷链IPO过会，冷链物流板块关注度提升。",
        "duration": "1周",
        "etfs": [],
        "stocks": [
          {
            "name": "002153 石基信息",
            "sentiment": "关注",
            "note": "冷链信息化"
          }
        ]
      }
    ],
    "douyin": [],
    "sangsha_module": {
      "overall_sentiment": "平稳",
      "advice": "震荡整理，观望为主",
      "avg_buy_prob": 21,
      "avg_panic_prob": 5,
      "analysis_results": [
        {
          "news": "TCL科技业绩超预期 面板周期拐点",
          "title": "TCL科技业绩超预期 面板周期拐点",
          "full_title": "TCL科技业绩超预期 面板周期拐点",
          "summary": "TCL科技发布2026年一季报，净利润同比增长150%，面板价格持续上涨。行业周期拐点确认。",
          "追高买入概率": 67,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 70,
          "情绪标签": [
            "FOMO"
          ],
          "韭菜行为总结": "散户疯了，都在追！",
          "市场含义": "顶部风险",
          "买入概率": 42,
          "is_long_term": false,
          "date": "2026-03-30",
          "decay": 1.0,
          "weighted_buy_prob": 42
        },
        {
          "news": "小米汽车交付破万 新能源车链活跃",
          "title": "小米汽车交付破万 新能源车链活跃",
          "full_title": "小米汽车交付破万 新能源车链活跃",
          "summary": "小米汽车3月交付量突破1万台，超市场预期。新能源汽车市场竞争加剧。",
          "追高买入概率": 54,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 75,
          "情绪标签": [
            "FOMO"
          ],
          "韭菜行为总结": "散户开始眼红，想冲进去",
          "市场含义": "分歧加大",
          "买入概率": 34,
          "is_long_term": false,
          "date": "2026-03-30",
          "decay": 1.0,
          "weighted_buy_prob": 34
        },
        {
          "news": "汇川技术港股上市 工业自动化龙头",
          "title": "汇川技术港股上市 工业自动化龙头",
          "full_title": "汇川技术港股上市 工业自动化龙头",
          "summary": "汇川技术港股成功上市，募资用于工业自动化产能扩张。",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 5,
          "is_long_term": false,
          "date": "2026-03-30",
          "decay": 1.0,
          "weighted_buy_prob": 5
        },
        {
          "news": "瑞云冷链IPO过会 冷链物流概念",
          "title": "瑞云冷链IPO过会 冷链物流概念",
          "full_title": "瑞云冷链IPO过会 冷链物流概念",
          "summary": "瑞云冷链IPO过会，冷链物流板块关注度提升。",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 5,
          "is_long_term": false,
          "date": "2026-03-30",
          "decay": 1.0,
          "weighted_buy_prob": 5
        }
      ],
      "total_news_count": 4,
      "time_window": "7天累积（长期新闻除外）"
    },
    "white_dragon": {
      "主力状态": "出货",
      "阶段": "末期",
      "行为解释": "多个ETF出现主力派发信号，注意风险",
      "是否利用散户": true,
      "散户情绪": {
        "平均买入概率": 21,
        "平均恐慌概率": 5
      },
      "各ETF分析": [
        {
          "code": "512760",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.0
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 21.72,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 21,
          "sangsha_panic_prob": 5
        },
        {
          "code": "512930",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.43
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 11.41,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 21,
          "sangsha_panic_prob": 5
        },
        {
          "code": "518880",
          "price_trend": {
            "trend": "side",
            "strength": 40,
            "change_pct": 1.33
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": -10.83,
            "level": "normal"
          },
          "主力状态": "吸筹",
          "阶段": "早期",
          "行为解释": "价格横盘/小跌，资金流入，主力可能在低位吸筹",
          "是否利用散户": false,
          "sangsha_buy_prob": 21,
          "sangsha_panic_prob": 5
        },
        {
          "code": "588890",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.16
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 0.4,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 21,
          "sangsha_panic_prob": 5
        },
        {
          "code": "159382",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.74
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 29.76,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 21,
          "sangsha_panic_prob": 5
        }
      ],
      "综合建议": "⚠️ 风险提示：主力可能正在派发，散户追高风险大，建议减仓观望"
    }
  },
  "2026-03-29": {
    "date": "2026-03-29",
    "market_tone": "地缘风险升温日！霍尔木兹局势紧张，能源化工暴涨",
    "wukong_judgment": {
      "emotion": "谨慎偏防御",
      "analysis": [
        "霍尔木兹海峡局势升级，原油供应中断风险上升",
        "中信证券、比亚迪年报落地，业绩验证期",
        "避险资产（黄金、国债）配置价值凸显"
      ],
      "strategy": [
        " 黄金ETF、国债ETF加仓",
        " 能源化工股短线博弈",
        " 科技股、消费股暂时回避"
      ]
    },
    "s_level": [
      {
        "emoji": " ",
        "title": "霍尔木兹海峡危机升级 能源化工暴涨",
        "source": "路透 / 新华社",
        "summary": "伊朗威胁封锁霍尔木兹海峡，胡塞武装宣布参战。原油期货暴涨8%，能源化工板块全线大涨。",
        "duration": "2-4周",
        "etfs": [
          {
            "name": "160140 油气ETF",
            "sentiment": "利好",
            "note": "原油涨价直接受益"
          },
          {
            "name": "159869 化工ETF",
            "sentiment": "利好",
            "note": "化工品跟涨"
          },
          {
            "name": "518880 黄金ETF",
            "sentiment": "利好",
            "note": "避险资产"
          },
          {
            "name": "512880 国债ETF",
            "sentiment": "利好",
            "note": "避险情绪升温"
          }
        ],
        "stocks": [
          {
            "name": "601857 中国石油",
            "sentiment": "利好",
            "note": "原油涨价受益"
          },
          {
            "name": "600028 中国石化",
            "sentiment": "利好"
          },
          {
            "name": "600188 兖矿能源",
            "sentiment": "利好",
            "note": "煤炭联动"
          },
          {
            "name": "601899 紫金矿业",
            "sentiment": "利好",
            "note": "黄金+铜"
          }
        ]
      },
      {
        "emoji": " ",
        "title": "中信证券年报落地 300亿净利润",
        "source": "公司公告",
        "summary": "中信证券2025年净利润300亿元，符合预期。券商板块估值修复逻辑延续。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "512880 证券ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          {
            "name": "600030 中信证券",
            "sentiment": "利好",
            "note": "业绩落地"
          },
          {
            "name": "601211 国泰君安",
            "sentiment": "利好"
          }
        ]
      },
      {
        "emoji": " ",
        "title": "比亚迪年报发布 营收8040亿",
        "source": "公司公告",
        "summary": "比亚迪2025年营收8040亿元，同比增长35%。新能源车龙头地位稳固。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "515030 新能源车ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          {
            "name": "002594 比亚迪",
            "sentiment": "利好",
            "note": "业绩验证"
          },
          {
            "name": "300750 宁德时代",
            "sentiment": "利好"
          }
        ]
      }
    ],
    "a_level": [
      {
        "emoji": " ",
        "title": "工商银行分红预案 1100亿现金分红",
        "source": "公司公告",
        "summary": "工商银行2025年分红1100亿元，股息率超6%。银行板块高股息价值凸显。",
        "duration": "1周",
        "etfs": [
          {
            "name": "512800 银行ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          {
            "name": "601398 工商银行",
            "sentiment": "利好",
            "note": "高股息"
          },
          {
            "name": "601288 农业银行",
            "sentiment": "利好"
          }
        ]
      },
      {
        "emoji": " ",
        "title": "铜价突围 伦铜突破11000美元",
        "source": "LME / 上期所",
        "summary": "伦铜突破11000美元/吨，创历史新高。新能源+AI算力需求驱动铜价上涨。",
        "duration": "2-4周",
        "etfs": [
          {
            "name": "562330 有色ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          {
            "name": "601899 紫金矿业",
            "sentiment": "利好",
            "note": "铜+金双驱动"
          },
          {
            "name": "600547 山东黄金",
            "sentiment": "利好"
          }
        ]
      },
      {
        "emoji": " ",
        "title": "月之暗面冲刺IPO AI应用赛道",
        "source": "科创板日报",
        "summary": "月之暗面启动港股IPO筹备，估值超200亿美元。AI大模型应用赛道持续火热。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "515980 云计算ETF",
            "sentiment": "利好"
          },
          {
            "name": "588000 科创50ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          {
            "name": "688111 金山办公",
            "sentiment": "利好",
            "note": "AI办公应用"
          }
        ]
      }
    ],
    "douyin": [],
    "sangsha_module": {
      "overall_sentiment": "平稳",
      "advice": "震荡整理，观望为主",
      "avg_buy_prob": 25,
      "avg_panic_prob": 5,
      "analysis_results": [
        {
          "news": "霍尔木兹海峡危机升级 能源化工暴涨",
          "title": "霍尔木兹海峡危机升级 能源化工暴涨",
          "full_title": "霍尔木兹海峡危机升级 能源化工暴涨",
          "summary": "伊朗威胁封锁霍尔木兹海峡，胡塞武装宣布参战。原油期货暴涨8%，能源化工板块全线大涨。",
          "追高买入概率": 87,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 62,
          "情绪标签": [
            "FOMO"
          ],
          "韭菜行为总结": "散户疯了，都在追！",
          "市场含义": "顶部风险",
          "买入概率": 54,
          "is_long_term": true,
          "date": "2026-03-29",
          "decay": 1.0,
          "weighted_buy_prob": 54
        },
        {
          "news": "铜价突围 伦铜突破11000美元",
          "title": "铜价突围 伦铜突破11000美元",
          "full_title": "铜价突围 伦铜突破11000美元",
          "summary": "伦铜突破11000美元/吨，创历史新高。新能源+AI算力需求驱动铜价上涨。",
          "追高买入概率": 85,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 62,
          "情绪标签": [
            "FOMO"
          ],
          "韭菜行为总结": "散户疯了，都在追！",
          "市场含义": "顶部风险",
          "买入概率": 53,
          "is_long_term": true,
          "date": "2026-03-29",
          "decay": 1.0,
          "weighted_buy_prob": 53
        },
        {
          "news": "中信证券年报落地 300亿净利润",
          "title": "中信证券年报落地 300亿净利润",
          "full_title": "中信证券年报落地 300亿净利润",
          "summary": "中信证券2025年净利润300亿元，符合预期。券商板块估值修复逻辑延续。",
          "追高买入概率": 5,
          "抄底买入概率": 73,
          "恐慌卖出概率": 5,
          "观望概率": 74,
          "情绪标签": [
            "抄底冲动"
          ],
          "韭菜行为总结": "散户想抄底，认为是机会",
          "市场含义": "可能有反弹",
          "买入概率": 32,
          "is_long_term": true,
          "date": "2026-03-29",
          "decay": 1.0,
          "weighted_buy_prob": 32
        },
        {
          "news": "比亚迪年报发布 营收8040亿",
          "title": "比亚迪年报发布 营收8040亿",
          "full_title": "比亚迪年报发布 营收8040亿",
          "summary": "比亚迪2025年营收8040亿元，同比增长35%。新能源车龙头地位稳固。",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 5,
          "is_long_term": true,
          "date": "2026-03-29",
          "decay": 1.0,
          "weighted_buy_prob": 5
        },
        {
          "news": "工商银行分红预案 1100亿现金分红",
          "title": "工商银行分红预案 1100亿现金分红",
          "full_title": "工商银行分红预案 1100亿现金分红",
          "summary": "工商银行2025年分红1100亿元，股息率超6%。银行板块高股息价值凸显。",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 5,
          "is_long_term": true,
          "date": "2026-03-29",
          "decay": 1.0,
          "weighted_buy_prob": 5
        },
        {
          "news": "月之暗面冲刺IPO AI应用赛道",
          "title": "月之暗面冲刺IPO AI应用赛道",
          "full_title": "月之暗面冲刺IPO AI应用赛道",
          "summary": "月之暗面启动港股IPO筹备，估值超200亿美元。AI大模型应用赛道持续火热。",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 5,
          "is_long_term": true,
          "date": "2026-03-29",
          "decay": 1.0,
          "weighted_buy_prob": 5
        }
      ],
      "total_news_count": 6,
      "time_window": "7天累积（长期新闻除外）"
    },
    "white_dragon": {
      "主力状态": "出货",
      "阶段": "末期",
      "行为解释": "多个ETF出现主力派发信号，注意风险",
      "是否利用散户": true,
      "散户情绪": {
        "平均买入概率": 29,
        "平均恐慌概率": 5
      },
      "各ETF分析": [
        {
          "code": "512760",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.0
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 21.72,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 29,
          "sangsha_panic_prob": 5
        },
        {
          "code": "512930",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.43
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 11.41,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 29,
          "sangsha_panic_prob": 5
        },
        {
          "code": "518880",
          "price_trend": {
            "trend": "side",
            "strength": 40,
            "change_pct": 1.33
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": -10.83,
            "level": "normal"
          },
          "主力状态": "吸筹",
          "阶段": "早期",
          "行为解释": "价格横盘/小跌，资金流入，主力可能在低位吸筹",
          "是否利用散户": false,
          "sangsha_buy_prob": 29,
          "sangsha_panic_prob": 5
        },
        {
          "code": "588890",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.16
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 0.4,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 29,
          "sangsha_panic_prob": 5
        },
        {
          "code": "159382",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.74
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 29.76,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 29,
          "sangsha_panic_prob": 5
        }
      ],
      "综合建议": "⚠️ 风险提示：主力可能正在派发，散户追高风险大，建议减仓观望"
    }
  },
  "2026-03-28": {
    "date": "2026-03-28",
    "market_tone": "鹰派冲击日！美联储暗示不降息，科技股领跌",
    "wukong_judgment": {
      "emotion": "偏空",
      "analysis": [
        "美联储鹰派言论打压全球风险资产",
        "人民币贬值压力上升，北向资金流出",
        "科技股、成长股承压，避险情绪升温"
      ],
      "strategy": [
        " 降低仓位，控制风险",
        " 黄金、国债等避险资产配置",
        " 等待美联储政策明朗后再布局"
      ]
    },
    "s_level": [
      {
        "emoji": " ",
        "title": "美联储鹰派言论 降息预期降温",
        "source": "美联储议息会议",
        "summary": "美联储主席暗示2026年可能不降息，通胀压力持续。全球股市承压，美元指数走强。",
        "duration": "2-4周",
        "etfs": [
          {
            "name": "513500 标普ETF",
            "sentiment": "利空",
            "note": "美股承压"
          },
          {
            "name": "588000 科创50ETF",
            "sentiment": "利空",
            "note": "成长股估值压力"
          },
          {
            "name": "512880 国债ETF",
            "sentiment": "利好",
            "note": "避险资产"
          }
        ],
        "stocks": [
          {
            "name": "688981 中芯国际",
            "sentiment": "利空",
            "note": "科技股估值压力"
          },
          {
            "name": "300750 宁德时代",
            "sentiment": "利空"
          }
        ]
      }
    ],
    "a_level": [
      {
        "emoji": " ",
        "title": "人民币贬值压力 北向资金流出",
        "source": "外汇市场",
        "summary": "美元走强，人民币兑美元跌破7.3关口。北向资金连续3日净流出。",
        "duration": "1-2周",
        "etfs": [],
        "stocks": [
          {
            "name": "601318 中国平安",
            "sentiment": "利空",
            "note": "外资重仓股承压"
          }
        ]
      },
      {
        "emoji": " ",
        "title": "央行逆回购投放 流动性对冲",
        "source": "央行公开市场",
        "summary": "央行开展1500亿逆回购操作，对冲季末流动性紧张。",
        "duration": "1周",
        "etfs": [
          {
            "name": "512880 国债ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": []
      },
      {
        "emoji": " ",
        "title": "新能源车销量不及预期 板块调整",
        "source": "中汽协数据",
        "summary": "3月新能源车销量增速放缓，市场预期落空。板块短期承压。",
        "duration": "1周",
        "etfs": [
          {
            "name": "515030 新能源车ETF",
            "sentiment": "利空"
          }
        ],
        "stocks": [
          {
            "name": "002594 比亚迪",
            "sentiment": "利空"
          },
          {
            "name": "300750 宁德时代",
            "sentiment": "利空"
          }
        ]
      }
    ],
    "douyin": [],
    "sangsha_module": {
      "overall_sentiment": "平稳",
      "advice": "震荡整理，观望为主",
      "avg_buy_prob": 7,
      "avg_panic_prob": 5,
      "analysis_results": [
        {
          "news": "人民币贬值压力 北向资金流出",
          "title": "人民币贬值压力 北向资金流出",
          "full_title": "人民币贬值压力 北向资金流出",
          "summary": "美元走强，人民币兑美元跌破7.3关口。北向资金连续3日净流出。",
          "追高买入概率": 20,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 89,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 14,
          "is_long_term": true,
          "date": "2026-03-28",
          "decay": 1.0,
          "weighted_buy_prob": 14
        },
        {
          "news": "美联储鹰派言论 降息预期降温",
          "title": "美联储鹰派言论 降息预期降温",
          "full_title": "美联储鹰派言论 降息预期降温",
          "summary": "美联储主席暗示2026年可能不降息，通胀压力持续。全球股市承压，美元指数走强。",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 5,
          "is_long_term": true,
          "date": "2026-03-28",
          "decay": 1.0,
          "weighted_buy_prob": 5
        },
        {
          "news": "央行逆回购投放 流动性对冲",
          "title": "央行逆回购投放 流动性对冲",
          "full_title": "央行逆回购投放 流动性对冲",
          "summary": "央行开展1500亿逆回购操作，对冲季末流动性紧张。",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [
            "迷茫"
          ],
          "韭菜行为总结": "散户看不懂，在观望",
          "市场含义": "震荡整理",
          "买入概率": 5,
          "is_long_term": true,
          "date": "2026-03-28",
          "decay": 1.0,
          "weighted_buy_prob": 5
        },
        {
          "news": "新能源车销量不及预期 板块调整",
          "title": "新能源车销量不及预期 板块调整",
          "full_title": "新能源车销量不及预期 板块调整",
          "summary": "3月新能源车销量增速放缓，市场预期落空。板块短期承压。",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 5,
          "is_long_term": true,
          "date": "2026-03-28",
          "decay": 1.0,
          "weighted_buy_prob": 5
        }
      ],
      "total_news_count": 4,
      "time_window": "7天累积（长期新闻除外）"
    },
    "white_dragon": {
      "主力状态": "出货",
      "阶段": "末期",
      "行为解释": "多个ETF出现主力派发信号，注意风险",
      "是否利用散户": true,
      "散户情绪": {
        "平均买入概率": 7,
        "平均恐慌概率": 5
      },
      "各ETF分析": [
        {
          "code": "512760",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.0
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 21.72,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 7,
          "sangsha_panic_prob": 5
        },
        {
          "code": "512930",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.43
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 11.41,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 7,
          "sangsha_panic_prob": 5
        },
        {
          "code": "518880",
          "price_trend": {
            "trend": "side",
            "strength": 40,
            "change_pct": 1.33
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": -10.83,
            "level": "normal"
          },
          "主力状态": "吸筹",
          "阶段": "早期",
          "行为解释": "价格横盘/小跌，资金流入，主力可能在低位吸筹",
          "是否利用散户": false,
          "sangsha_buy_prob": 7,
          "sangsha_panic_prob": 5
        },
        {
          "code": "588890",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.16
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 0.4,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 7,
          "sangsha_panic_prob": 5
        },
        {
          "code": "159382",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.74
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 29.76,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 7,
          "sangsha_panic_prob": 5
        }
      ],
      "综合建议": "⚠️ 风险提示：主力可能正在派发，散户追高风险大，建议减仓观望"
    }
  },
  "2026-03-27": {
    "date": "2026-03-27",
    "market_tone": "业绩验证日，龙头分化，黄金避险升温",
    "wukong_judgment": {
      "emotion": "中性",
      "analysis": [
        "TCL科技业绩超预期，面板周期拐点",
        "美团财报落地，互联网股估值修复",
        "黄金价格持续走高，避险情绪延续"
      ],
      "strategy": [
        " 关注业绩超预期龙头",
        " 黄金ETF持有",
        " 高估值小票规避"
      ]
    },
    "s_level": [
      {
        "emoji": " ",
        "title": "TCL科技业绩大增 面板周期拐点",
        "source": "公司公告",
        "summary": "TCL科技一季报净利润同比增150%，面板价格持续上涨，行业周期反转确认。",
        "duration": "2-4周",
        "etfs": [
          {
            "name": "512760 芯片ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          {
            "name": "000100 TCL科技",
            "sentiment": "利好"
          },
          {
            "name": "002049 国星光电",
            "sentiment": "利好"
          }
        ]
      }
    ],
    "a_level": [
      {
        "emoji": " ",
        "title": "美团财报发布 营收超预期",
        "source": "公司公告",
        "summary": "美团2025年Q4营收同比增长25%，外卖业务盈利能力改善。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "159805 互联网ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          {
            "name": "3690 美团",
            "sentiment": "利好"
          }
        ]
      },
      {
        "emoji": " ",
        "title": "茅台涨价预期 消费股估值修复",
        "source": "市场传闻",
        "summary": "市场预期茅台将上调出厂价，白酒板块估值修复。",
        "duration": "1周",
        "etfs": [
          {
            "name": "512810 消费ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          {
            "name": "600519 贵州茅台",
            "sentiment": "利好"
          }
        ]
      },
      {
        "emoji": " ",
        "title": "黄金ETF持续吸金 避险情绪延续",
        "source": "上交所数据",
        "summary": "黄金ETF规模突破400亿，避险资金持续流入。",
        "duration": "持续",
        "etfs": [
          {
            "name": "518880 黄金ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          {
            "name": "600547 山东黄金",
            "sentiment": "利好"
          }
        ]
      }
    ],
    "douyin": [],
    "sangsha_module": {
      "overall_sentiment": "平稳",
      "advice": "震荡整理，观望为主",
      "avg_buy_prob": 39,
      "avg_panic_prob": 5,
      "analysis_results": [
        {
          "news": "美团财报发布 营收超预期",
          "title": "美团财报发布 营收超预期",
          "full_title": "美团财报发布 营收超预期",
          "summary": "美团2025年Q4营收同比增长25%，外卖业务盈利能力改善。",
          "追高买入概率": 77,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 66,
          "情绪标签": [
            "FOMO"
          ],
          "韭菜行为总结": "散户疯了，都在追！",
          "市场含义": "顶部风险",
          "买入概率": 48,
          "is_long_term": false,
          "date": "2026-03-27",
          "decay": 1.0,
          "weighted_buy_prob": 48
        },
        {
          "news": "TCL科技业绩大增 面板周期拐点",
          "title": "TCL科技业绩大增 面板周期拐点",
          "full_title": "TCL科技业绩大增 面板周期拐点",
          "summary": "TCL科技一季报净利润同比增150%，面板价格持续上涨，行业周期反转确认。",
          "追高买入概率": 41,
          "抄底买入概率": 38,
          "恐慌卖出概率": 5,
          "观望概率": 70,
          "情绪标签": [
            "FOMO",
            "抄底冲动"
          ],
          "韭菜行为总结": "散户开始眼红，想冲进去",
          "市场含义": "分歧加大",
          "买入概率": 40,
          "is_long_term": false,
          "date": "2026-03-27",
          "decay": 1.0,
          "weighted_buy_prob": 40
        },
        {
          "news": "茅台涨价预期 消费股估值修复",
          "title": "茅台涨价预期 消费股估值修复",
          "full_title": "茅台涨价预期 消费股估值修复",
          "summary": "市场预期茅台将上调出厂价，白酒板块估值修复。",
          "追高买入概率": 5,
          "抄底买入概率": 84,
          "恐慌卖出概率": 5,
          "观望概率": 71,
          "情绪标签": [
            "抄底冲动"
          ],
          "韭菜行为总结": "散户想抄底，认为是机会",
          "市场含义": "可能有反弹",
          "买入概率": 36,
          "is_long_term": false,
          "date": "2026-03-27",
          "decay": 1.0,
          "weighted_buy_prob": 36
        },
        {
          "news": "黄金ETF持续吸金 避险情绪延续",
          "title": "黄金ETF持续吸金 避险情绪延续",
          "full_title": "黄金ETF持续吸金 避险情绪延续",
          "summary": "黄金ETF规模突破400亿，避险资金持续流入。",
          "追高买入概率": 54,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 75,
          "情绪标签": [
            "FOMO"
          ],
          "韭菜行为总结": "散户开始眼红，想冲进去",
          "市场含义": "分歧加大",
          "买入概率": 34,
          "is_long_term": false,
          "date": "2026-03-27",
          "decay": 1.0,
          "weighted_buy_prob": 34
        }
      ],
      "total_news_count": 4,
      "time_window": "7天累积（长期新闻除外）"
    },
    "white_dragon": {
      "主力状态": "出货",
      "阶段": "末期",
      "行为解释": "多个ETF出现主力派发信号，注意风险",
      "是否利用散户": true,
      "散户情绪": {
        "平均买入概率": 39,
        "平均恐慌概率": 5
      },
      "各ETF分析": [
        {
          "code": "512760",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.0
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 21.72,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 39,
          "sangsha_panic_prob": 5
        },
        {
          "code": "512930",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.43
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 11.41,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 39,
          "sangsha_panic_prob": 5
        },
        {
          "code": "518880",
          "price_trend": {
            "trend": "side",
            "strength": 40,
            "change_pct": 1.33
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": -10.83,
            "level": "normal"
          },
          "主力状态": "吸筹",
          "阶段": "早期",
          "行为解释": "价格横盘/小跌，资金流入，主力可能在低位吸筹",
          "是否利用散户": false,
          "sangsha_buy_prob": 39,
          "sangsha_panic_prob": 5
        },
        {
          "code": "588890",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.16
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 0.4,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 39,
          "sangsha_panic_prob": 5
        },
        {
          "code": "159382",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.74
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 29.76,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 39,
          "sangsha_panic_prob": 5
        }
      ],
      "综合建议": "⚠️ 风险提示：主力可能正在派发，散户追高风险大，建议减仓观望"
    }
  },
  "2026-03-26": {
    "date": "2026-03-26",
    "market_tone": "政策博弈日！地产松绑预期升温，消费复苏预期增强",
    "wukong_judgment": {
      "emotion": "偏多",
      "analysis": [
        "地产政策松绑预期升温，地产链反弹",
        "消费复苏信号增强，社零数据改善",
        "AI芯片国产替代加速，半导体设备股走强"
      ],
      "strategy": [
        " 地产链短线博弈",
        " 消费股中线布局",
        " 半导体设备长线持有"
      ]
    },
    "s_level": [
      {
        "emoji": " ",
        "title": "地产政策松绑预期 地产链反弹",
        "source": "住建部传闻",
        "summary": "市场传闻多地将出台地产松绑政策，包括限购放松、首付比例下调等。地产股集体反弹。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "512200 房地产ETF",
            "sentiment": "利好"
          },
          {
            "name": "159619 建材ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          {
            "name": "000002 万科A",
            "sentiment": "利好"
          },
          {
            "name": "600048 保利发展",
            "sentiment": "利好"
          },
          {
            "name": "600383 金地集团",
            "sentiment": "利好"
          }
        ]
      },
      {
        "emoji": " ",
        "title": "AI芯片国产替代加速 半导体设备股走强",
        "source": "科创板日报",
        "summary": "美对华芯片限制升级，国产替代加速。北方华创、中微公司订单大幅增长。",
        "duration": "2-4周",
        "etfs": [
          {
            "name": "512760 芯片ETF",
            "sentiment": "利好"
          },
          {
            "name": "588000 科创50ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          {
            "name": "002371 北方华创",
            "sentiment": "利好",
            "note": "半导体设备龙头"
          },
          {
            "name": "688012 中微公司",
            "sentiment": "利好"
          },
          {
            "name": "688981 中芯国际",
            "sentiment": "利好"
          }
        ]
      }
    ],
    "a_level": [
      {
        "emoji": " ",
        "title": "消费复苏信号增强 社零数据改善",
        "source": "统计局数据",
        "summary": "2月社零同比增长5.5%，好于预期。消费复苏势头延续。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "512810 消费ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          {
            "name": "600519 贵州茅台",
            "sentiment": "利好"
          },
          {
            "name": "000858 五粮液",
            "sentiment": "利好"
          }
        ]
      }
    ],
    "douyin": [],
    "sangsha_module": {
      "overall_sentiment": "平稳",
      "advice": "震荡整理，观望为主",
      "avg_buy_prob": 13,
      "avg_panic_prob": 22,
      "analysis_results": [
        {
          "news": "地产政策松绑预期 地产链反弹",
          "title": "地产政策松绑预期 地产链反弹",
          "full_title": "地产政策松绑预期 地产链反弹",
          "summary": "市场传闻多地将出台地产松绑政策，包括限购放松、首付比例下调等。地产股集体反弹。",
          "追高买入概率": 5,
          "抄底买入概率": 66,
          "恐慌卖出概率": 5,
          "观望概率": 76,
          "情绪标签": [
            "抄底冲动"
          ],
          "韭菜行为总结": "散户想抄底，认为是机会",
          "市场含义": "可能有反弹",
          "买入概率": 29,
          "is_long_term": false,
          "date": "2026-03-26",
          "decay": 1.0,
          "weighted_buy_prob": 29
        },
        {
          "news": "AI芯片国产替代加速 半导体设备股走强",
          "title": "AI芯片国产替代加速 半导体设备股走强",
          "full_title": "AI芯片国产替代加速 半导体设备股走强",
          "summary": "美对华芯片限制升级，国产替代加速。北方华创、中微公司订单大幅增长。",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 57,
          "观望概率": 79,
          "情绪标签": [
            "恐慌"
          ],
          "韭菜行为总结": "散户恐慌，想割肉",
          "市场含义": "可能见底",
          "买入概率": 5,
          "is_long_term": false,
          "date": "2026-03-26",
          "decay": 1.0,
          "weighted_buy_prob": 5
        },
        {
          "news": "消费复苏信号增强 社零数据改善",
          "title": "消费复苏信号增强 社零数据改善",
          "full_title": "消费复苏信号增强 社零数据改善",
          "summary": "2月社零同比增长5.5%，好于预期。消费复苏势头延续。",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 5,
          "is_long_term": false,
          "date": "2026-03-26",
          "decay": 1.0,
          "weighted_buy_prob": 5
        }
      ],
      "total_news_count": 3,
      "time_window": "7天累积（长期新闻除外）"
    },
    "white_dragon": {
      "主力状态": "出货",
      "阶段": "末期",
      "行为解释": "多个ETF出现主力派发信号，注意风险",
      "是否利用散户": true,
      "散户情绪": {
        "平均买入概率": 13,
        "平均恐慌概率": 22
      },
      "各ETF分析": [
        {
          "code": "512760",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.0
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 21.72,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 13,
          "sangsha_panic_prob": 22
        },
        {
          "code": "512930",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.43
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 11.41,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 13,
          "sangsha_panic_prob": 22
        },
        {
          "code": "518880",
          "price_trend": {
            "trend": "side",
            "strength": 40,
            "change_pct": 1.33
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": -10.83,
            "level": "normal"
          },
          "主力状态": "吸筹",
          "阶段": "早期",
          "行为解释": "价格横盘/小跌，资金流入，主力可能在低位吸筹",
          "是否利用散户": false,
          "sangsha_buy_prob": 13,
          "sangsha_panic_prob": 22
        },
        {
          "code": "588890",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.16
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 0.4,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 13,
          "sangsha_panic_prob": 22
        },
        {
          "code": "159382",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.74
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 29.76,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 13,
          "sangsha_panic_prob": 22
        }
      ],
      "综合建议": "⚠️ 风险提示：主力可能正在派发，散户追高风险大，建议减仓观望"
    }
  },
  "2026-03-25": {
    "date": "2026-03-25",
    "market_tone": "分化启动日！半导体设备超预期，新能源车下乡补贴落地",
    "wukong_judgment": {
      "emotion": "中性偏多",
      "analysis": [
        "半导体设备订单超预期，国产替代逻辑强化",
        "新能源车下乡补贴政策落地，三四线城市渗透率提升",
        "消费电子回暖信号明确，手机出货量连续增长"
      ],
      "strategy": [
        " 半导体设备股持有",
        " 新能源车ETF可加仓",
        " 消费电子股中线布局"
      ]
    },
    "s_level": [
      {
        "emoji": " ",
        "title": "半导体设备订单超预期 国产替代加速",
        "source": "SEMI数据",
        "summary": "一季度中国大陆半导体设备采购额同比增长45%，北方华创订单排产至2027年。国产替代进程加速。",
        "duration": "2-4周",
        "etfs": [
          {
            "name": "512760 芯片ETF",
            "sentiment": "利好"
          },
          {
            "name": "588000 科创50ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          {
            "name": "002371 北方华创",
            "sentiment": "利好",
            "note": "订单排产至2027年"
          },
          {
            "name": "688012 中微公司",
            "sentiment": "利好"
          },
          {
            "name": "603501 沪硅产业",
            "sentiment": "利好"
          }
        ]
      },
      {
        "emoji": " ",
        "title": "新能源车下乡补贴落地 三四线城市渗透率提升",
        "source": "工信部公告",
        "summary": "新能源车下乡补贴政策正式落地，补贴金额最高5000元。三四线城市新能源车渗透率有望快速提升。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "515030 新能源车ETF",
            "sentiment": "利好"
          },
          {
            "name": "516390 智能汽车ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          {
            "name": "002594 比亚迪",
            "sentiment": "利好",
            "note": "直接受益"
          },
          {
            "name": "601238 广汽集团",
            "sentiment": "利好"
          },
          {
            "name": "000625 长安汽车",
            "sentiment": "利好"
          }
        ]
      }
    ],
    "a_level": [
      {
        "emoji": " ",
        "title": "消费电子回暖信号 手机出货量增长",
        "source": "信通院数据",
        "summary": "2月国内手机出货量同比增长12%，连续4个月正增长。消费电子周期见底信号明确。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "159732 消费电子ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          {
            "name": "002241 歌尔股份",
            "sentiment": "利好",
            "note": "苹果链"
          },
          {
            "name": "002475 立讯精密",
            "sentiment": "利好"
          }
        ]
      }
    ],
    "douyin": [],
    "sangsha_module": {
      "overall_sentiment": "平稳",
      "advice": "震荡整理，观望为主",
      "avg_buy_prob": 14,
      "avg_panic_prob": 5,
      "analysis_results": [
        {
          "news": "半导体设备订单超预期 国产替代加速",
          "title": "半导体设备订单超预期 国产替代加速",
          "full_title": "半导体设备订单超预期 国产替代加速",
          "summary": "一季度中国大陆半导体设备采购额同比增长45%，北方华创订单排产至2027年。国产替代进程加速。",
          "追高买入概率": 54,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 75,
          "情绪标签": [
            "FOMO"
          ],
          "韭菜行为总结": "散户开始眼红，想冲进去",
          "市场含义": "分歧加大",
          "买入概率": 34,
          "is_long_term": false,
          "date": "2026-03-25",
          "decay": 1.0,
          "weighted_buy_prob": 34
        },
        {
          "news": "新能源车下乡补贴落地 三四线城市渗透率提升",
          "title": "新能源车下乡补贴落地 三四线城市渗透率提升",
          "full_title": "新能源车下乡补贴落地 三四线城市渗透率提升",
          "summary": "新能源车下乡补贴政策正式落地，补贴金额最高5000元。三四线城市新能源车渗透率有望快速提升。",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 5,
          "is_long_term": false,
          "date": "2026-03-25",
          "decay": 1.0,
          "weighted_buy_prob": 5
        },
        {
          "news": "消费电子回暖信号 手机出货量增长",
          "title": "消费电子回暖信号 手机出货量增长",
          "full_title": "消费电子回暖信号 手机出货量增长",
          "summary": "2月国内手机出货量同比增长12%，连续4个月正增长。消费电子周期见底信号明确。",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 5,
          "is_long_term": false,
          "date": "2026-03-25",
          "decay": 1.0,
          "weighted_buy_prob": 5
        }
      ],
      "total_news_count": 3,
      "time_window": "7天累积（长期新闻除外）"
    },
    "white_dragon": {
      "主力状态": "出货",
      "阶段": "末期",
      "行为解释": "多个ETF出现主力派发信号，注意风险",
      "是否利用散户": true,
      "散户情绪": {
        "平均买入概率": 14,
        "平均恐慌概率": 5
      },
      "各ETF分析": [
        {
          "code": "512760",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.0
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 21.72,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 14,
          "sangsha_panic_prob": 5
        },
        {
          "code": "512930",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.43
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 11.41,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 14,
          "sangsha_panic_prob": 5
        },
        {
          "code": "518880",
          "price_trend": {
            "trend": "side",
            "strength": 40,
            "change_pct": 1.33
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": -10.83,
            "level": "normal"
          },
          "主力状态": "吸筹",
          "阶段": "早期",
          "行为解释": "价格横盘/小跌，资金流入，主力可能在低位吸筹",
          "是否利用散户": false,
          "sangsha_buy_prob": 14,
          "sangsha_panic_prob": 5
        },
        {
          "code": "588890",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.16
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 0.4,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 14,
          "sangsha_panic_prob": 5
        },
        {
          "code": "159382",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.74
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 29.76,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 14,
          "sangsha_panic_prob": 5
        }
      ],
      "综合建议": "⚠️ 风险提示：主力可能正在派发，散户追高风险大，建议减仓观望"
    }
  },
  "2026-04-05": {
    "date": "2026-04-05",
    "market_tone": "清明假期A股休市，中东危机升级：伊朗拒绝特朗普48小时通牒，中国资产成全球避风港",
    "s_level": [
      {
        "emoji": "🔴",
        "title": "伊朗拒绝特朗普48小时通牒！华尔街紧绷：4月6日后会发生什么？",
        "summary": "伊朗拒绝特朗普48小时通牒，地区紧张局势升级，全球市场避险情绪升温。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "518880 黄金ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          "黄金股"
        ],
        "signal": "地缘风险升级"
      },
      {
        "emoji": "🔴",
        "title": "中东危机引发全球市场动荡，中国资产成为新避风港",
        "summary": "中东危机升级，中国资产成为全球资金避风港。",
        "duration": "1-4周",
        "etfs": [
          {
            "name": "512760 芯片ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          "中国资产"
        ],
        "signal": "资金流入中国资产"
      },
      {
        "emoji": "🔴",
        "title": "英伟达H100租赁价格5个月涨40%，OpenAI完成1220亿美元融资",
        "summary": "AI算力需求旺盛，OpenAI完成史上最大规模融资。",
        "duration": "1-3个月",
        "etfs": [
          {
            "name": "512760 芯片ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          "AI算力股"
        ],
        "signal": "AI算力需求爆发"
      },
      {
        "emoji": "🔴",
        "title": "公募基金盈利2.61万亿元刷新历史最高纪录",
        "summary": "公募基金规模创新高，居民财富向权益市场转移。",
        "duration": "长期",
        "etfs": [
          {
            "name": "510300 沪深300ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          "大市值蓝筹"
        ],
        "signal": "长期资金入市"
      }
    ],
    "a_level": [
      {
        "emoji": "🟡",
        "title": "美股周线五连阴终结，但服务业PMI跌破荣枯线，滞胀风险升级",
        "summary": "美股反弹但经济数据疲软。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "513500 标普500ETF",
            "sentiment": "中性"
          }
        ],
        "stocks": [],
        "signal": "美国经济放缓"
      }
    ],
    "douyin": [],
    "sangsha_module": {
      "overall_sentiment": "平稳",
      "advice": "震荡整理，观望为主",
      "avg_buy_prob": 17,
      "avg_panic_prob": 11,
      "analysis_results": [
        {
          "news": "公募基金盈利2.61万亿元刷新历史最高纪录",
          "title": "公募基金盈利2.61万亿元刷新历史最高纪录",
          "full_title": "公募基金盈利2.61万亿元刷新历史最高纪录",
          "summary": "公募基金规模创新高，居民财富向权益市场转移。",
          "追高买入概率": 72,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 67,
          "情绪标签": [
            "FOMO"
          ],
          "韭菜行为总结": "散户疯了，都在追！",
          "市场含义": "顶部风险",
          "买入概率": 45,
          "is_long_term": false,
          "date": "2026-04-05",
          "decay": 1.0,
          "weighted_buy_prob": 45
        },
        {
          "news": "美股周线五连阴终结，但服务业PMI跌破荣枯线，滞胀风险升级",
          "title": "美股周线五连阴终结，但服务业PMI跌破荣枯线，滞胀风险升级",
          "full_title": "美股周线五连阴终结，但服务业PMI跌破荣枯线，滞胀风险升级",
          "summary": "美股反弹但经济数据疲软。",
          "追高买入概率": 5,
          "抄底买入概率": 37,
          "恐慌卖出概率": 35,
          "观望概率": 75,
          "情绪标签": [
            "抄底冲动",
            "恐慌"
          ],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 18,
          "is_long_term": false,
          "date": "2026-04-05",
          "decay": 1.0,
          "weighted_buy_prob": 18
        },
        {
          "news": "英伟达H100租赁价格5个月涨40%，OpenAI完成122...",
          "title": "英伟达H100租赁价格5个月涨40%，OpenAI完成1220亿美元融资",
          "full_title": "英伟达H100租赁价格5个月涨40%，OpenAI完成1220亿美元融资",
          "summary": "AI算力需求旺盛，OpenAI完成史上最大规模融资。",
          "追高买入概率": 20,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 89,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 14,
          "is_long_term": false,
          "date": "2026-04-05",
          "decay": 1.0,
          "weighted_buy_prob": 14
        },
        {
          "news": "伊朗拒绝特朗普48小时通牒！华尔街紧绷：4月6日后会发生什么...",
          "title": "伊朗拒绝特朗普48小时通牒！华尔街紧绷：4月6日后会发生什么？",
          "full_title": "伊朗拒绝特朗普48小时通牒！华尔街紧绷：4月6日后会发生什么？",
          "summary": "伊朗拒绝特朗普48小时通牒，地区紧张局势升级，全球市场避险情绪升温。",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 5,
          "is_long_term": false,
          "date": "2026-04-05",
          "decay": 1.0,
          "weighted_buy_prob": 5
        },
        {
          "news": "中东危机引发全球市场动荡，中国资产成为新避风港",
          "title": "中东危机引发全球市场动荡，中国资产成为新避风港",
          "full_title": "中东危机引发全球市场动荡，中国资产成为新避风港",
          "summary": "中东危机升级，中国资产成为全球资金避风港。",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 5,
          "is_long_term": false,
          "date": "2026-04-05",
          "decay": 1.0,
          "weighted_buy_prob": 5
        }
      ],
      "total_news_count": 5,
      "time_window": "7天累积（长期新闻除外）"
    },
    "white_dragon": {
      "主力状态": "出货",
      "阶段": "末期",
      "行为解释": "多个ETF出现主力派发信号，注意风险",
      "是否利用散户": true,
      "散户情绪": {
        "平均买入概率": 17,
        "平均恐慌概率": 11
      },
      "各ETF分析": [
        {
          "code": "512760",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.0
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 21.72,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 17,
          "sangsha_panic_prob": 11
        },
        {
          "code": "512930",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.43
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 11.41,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 17,
          "sangsha_panic_prob": 11
        },
        {
          "code": "518880",
          "price_trend": {
            "trend": "side",
            "strength": 40,
            "change_pct": 1.33
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": -10.83,
            "level": "normal"
          },
          "主力状态": "吸筹",
          "阶段": "早期",
          "行为解释": "价格横盘/小跌，资金流入，主力可能在低位吸筹",
          "是否利用散户": false,
          "sangsha_buy_prob": 17,
          "sangsha_panic_prob": 11
        },
        {
          "code": "588890",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.16
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 0.4,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 17,
          "sangsha_panic_prob": 11
        },
        {
          "code": "159382",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.74
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 29.76,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 17,
          "sangsha_panic_prob": 11
        }
      ],
      "综合建议": "⚠️ 风险提示：主力可能正在派发，散户追高风险大，建议减仓观望"
    }
  },
  "2026-04-09": {
    "date": "2026-04-09",
    "market_tone": "科技股强势领涨！芯片、人工智能板块爆发，复旦微电大涨超10%，寒武纪涨超8%，市场做多情绪高涨",
    "wukong_judgment": {
      "market_sentiment": "震荡偏多，科技成长股领涨",
      "core_analysis": [
        "AI芯片/人工智能板块爆发：复旦微电大涨超10%，寒武纪-U涨超8%，金山办公涨超7%，人工智能AIETF(515070)盘中涨超3%",
        "科技股重估进入阶段性休整后反弹：海外关税风险落地，市场进入财报窗口期，业绩确定性成为超额收益抓手",
        "芯片板块集体走强：芯原股份、景嘉微等个股跟涨，科创AI指数异动拉升",
        "进入4月财报季，业绩确定性将成为市场风格主要抓手，关注业绩超预期个股"
      ],
      "operations": [
        {
          "type": "可做",
          "content": "AI芯片/人工智能板块：复旦微电、寒武纪-U、金山办公、人工智能AIETF(515070)"
        },
        {
          "type": "可做",
          "content": "科创芯片ETF：588890科创芯片ETF、588780科创芯片设计ETF"
        },
        {
          "type": "警惕",
          "content": "短期涨幅较大个股，注意获利回吐风险"
        },
        {
          "type": "关注",
          "content": "4月财报季业绩超预期个股"
        }
      ]
    },
    "bajie_conclusion": {
      "optimal_action": "重点配置AI芯片+人工智能ETF，科技成长股业绩驱动行情",
      "optimal_etfs": "515070人工智能AIETF(40%) + 588890科创芯片ETF(30%) + 512930AI人工智能ETF(20%) + 现金(10%)",
      "win_rate": "~72%（贝叶斯后验）",
      "max_drawdown": "-5%（止损线）",
      "holding_period": "1-2周"
    },
    "s_level": [
      {
        "emoji": "🔴",
        "title": "AI芯片/人工智能板块爆发：复旦微电大涨超10%，寒武纪涨超8%",
        "summary": "4月9日科技板块快速拉升，芯片、人工智能、军工板块走强。人工智能AIETF(515070)盘中上涨超3%，持仓股复旦微电大涨超10%，寒武纪-U大涨超8%，金山办公大涨超7%，芯原股份、景嘉微等个股跟涨。中银证券表示，科技股重估进入阶段性休整，海外关税风险落地，短期A股或进入震荡调整阶段。进入4月，A股即将进入财报窗口期，业绩确定性将会成为4月市场风格超额收益主要抓手。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "515070 人工智能AIETF",
            "sentiment": "利好"
          },
          {
            "name": "588890 科创芯片ETF",
            "sentiment": "利好"
          },
          {
            "name": "512930 AI人工智能ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          "复旦微电",
          "寒武纪-U",
          "金山办公",
          "芯原股份",
          "景嘉微"
        ],
        "signal": "主力资金回流科技板块，AI芯片需求持续爆发，短期做多情绪高涨",
        "bayes_analysis": {
          "prior_judgment": "科技股修复反弹",
          "prior_prob": 62,
          "likelihood_judgment": "AI芯片爆发+个股大涨超10%",
          "likelihood_prob": 80,
          "posterior": 72,
          "expected_return": "+6%~+12%",
          "confidence_interval": "[+3%, +18%]",
          "key_variables": "4月财报季业绩兑现情况（若业绩超预期，胜率提升至75%）"
        }
      }
    ],
    "a_level": [
      {
        "emoji": "🟡",
        "title": "科技股重估进入阶段性休整后反弹",
        "summary": "中银证券表示，科技股重估进入阶段性休整，海外关税风险落地，短期A股或进入震荡调整阶段。进入4月，A股即将进入财报窗口期，业绩确定性将会成为4月市场风格超额收益主要抓手。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "588000 科创50ETF",
            "sentiment": "利好"
          },
          {
            "name": "512760 芯片ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          "中芯国际",
          "澜起科技",
          "北方华创"
        ],
        "signal": "科技股业绩驱动行情开启，关注财报超预期个股",
        "bayes_analysis": {
          "prior_judgment": "科技股估值修复",
          "prior_prob": 58,
          "likelihood_judgment": "关税风险落地+业绩窗口期",
          "likelihood_prob": 72,
          "posterior": 66,
          "expected_return": "+5%~+10%",
          "confidence_interval": "[+2%, +15%]",
          "key_variables": "Q1财报业绩表现（若整体超预期，胜率可提升至70%）"
        }
      },
      {
        "emoji": "🟡",
        "title": "科创AI指数异动拉升，芯片设计ETF交投活跃",
        "summary": "科创AI指数午盘异动拉升涨超2%，科创AIETF(588790)直线拉升涨超2%，成交额超2000万元，换手率12.18%，交投活跃。成分股中，乐鑫科技涨超9%，恒玄科技、虹软科技涨超8%。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "588790 科创AIETF",
            "sentiment": "利好"
          },
          {
            "name": "588780 科创芯片设计ETF",
            "sentiment": "利好"
          }
        ],
        "stocks": [
          "乐鑫科技",
          "恒玄科技",
          "虹软科技"
        ],
        "signal": "科创板AI概念股活跃，资金关注度高",
        "bayes_analysis": {
          "prior_judgment": "科创板AI概念活跃",
          "prior_prob": 55,
          "likelihood_judgment": "ETF涨超2%+换手率超12%",
          "likelihood_prob": 70,
          "posterior": 64,
          "expected_return": "+4%~+8%",
          "confidence_interval": "[+2%, +12%]",
          "key_variables": "科创板整体流动性（若成交持续放大，胜率可提升至68%）"
        }
      }
    ],
    "douyin": [],
    "sangsha_module": {
      "overall_sentiment": "平稳",
      "advice": "震荡整理，观望为主",
      "avg_buy_prob": 25,
      "avg_panic_prob": 19,
      "analysis_results": [
        {
          "news": "AI芯片/人工智能板块爆发：复旦微电大涨超10%，寒武纪涨超...",
          "title": "AI芯片/人工智能板块爆发：复旦微电大涨超10%，寒武纪涨超8%",
          "full_title": "AI芯片/人工智能板块爆发：复旦微电大涨超10%，寒武纪涨超8%",
          "summary": "4月9日科技板块快速拉升，芯片、人工智能、军工板块走强。人工智能AIETF(515070)盘中上涨超...",
          "追高买入概率": 70,
          "抄底买入概率": 5,
          "恐慌卖出概率": 18,
          "观望概率": 64,
          "情绪标签": [
            "FOMO"
          ],
          "韭菜行为总结": "散户疯了，都在追！",
          "市场含义": "顶部风险",
          "买入概率": 44,
          "is_long_term": false,
          "date": "2026-04-09",
          "decay": 1.0,
          "weighted_buy_prob": 44
        },
        {
          "news": "科技股重估进入阶段性休整后反弹",
          "title": "科技股重估进入阶段性休整后反弹",
          "full_title": "科技股重估进入阶段性休整后反弹",
          "summary": "中银证券表示，科技股重估进入阶段性休整，海外关税风险落地，短期A股或进入震荡调整阶段。进入4月，A股...",
          "追高买入概率": 5,
          "抄底买入概率": 37,
          "恐慌卖出概率": 35,
          "观望概率": 76,
          "情绪标签": [
            "抄底冲动",
            "恐慌"
          ],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 18,
          "is_long_term": false,
          "date": "2026-04-09",
          "decay": 1.0,
          "weighted_buy_prob": 18
        },
        {
          "news": "科创AI指数异动拉升，芯片设计ETF交投活跃",
          "title": "科创AI指数异动拉升，芯片设计ETF交投活跃",
          "full_title": "科创AI指数异动拉升，芯片设计ETF交投活跃",
          "summary": "科创AI指数午盘异动拉升涨超2%，科创AIETF(588790)直线拉升涨超2%，成交额超2000万...",
          "追高买入概率": 20,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 89,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 14,
          "is_long_term": false,
          "date": "2026-04-09",
          "decay": 1.0,
          "weighted_buy_prob": 14
        }
      ],
      "total_news_count": 3,
      "time_window": "7天累积（长期新闻除外）"
    },
    "white_dragon": {
      "主力状态": "出货",
      "阶段": "末期",
      "行为解释": "多个ETF出现主力派发信号，注意风险",
      "是否利用散户": true,
      "散户情绪": {
        "平均买入概率": 25,
        "平均恐慌概率": 19
      },
      "各ETF分析": [
        {
          "code": "512760",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.0
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 21.72,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 25,
          "sangsha_panic_prob": 19
        },
        {
          "code": "512930",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.43
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 11.41,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 25,
          "sangsha_panic_prob": 19
        },
        {
          "code": "518880",
          "price_trend": {
            "trend": "side",
            "strength": 40,
            "change_pct": 1.33
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": -10.83,
            "level": "normal"
          },
          "主力状态": "吸筹",
          "阶段": "早期",
          "行为解释": "价格横盘/小跌，资金流入，主力可能在低位吸筹",
          "是否利用散户": false,
          "sangsha_buy_prob": 25,
          "sangsha_panic_prob": 19
        },
        {
          "code": "588890",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.16
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 0.4,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 25,
          "sangsha_panic_prob": 19
        },
        {
          "code": "159382",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.74
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 29.76,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 25,
          "sangsha_panic_prob": 19
        }
      ],
      "综合建议": "⚠️ 风险提示：主力可能正在派发，散户追高风险大，建议减仓观望"
    }
  },
  "2026-04-03": {
    "date": "2026-04-03",
    "market_tone": "清明节A股休市，海外市场震荡偏强，AI与医药板块迎重磅催化",
    "s_level": [
      {
        "emoji": "🔴",
        "title": "字节豆包日均Token消耗破120万亿，两年翻1000倍",
        "source": "界面新闻 / 火山引擎",
        "summary": "4月2日火山引擎总裁谭待披露，豆包大模型日均Token使用量超120万亿，过去三个月翻倍，比2024年5月发布时增长1000倍。累计Token使用量超万亿的企业从100家增至140家。核心驱动来自AI视频创作爆发与AI智能体加速普及。火山引擎已把2026年MaaS业务收入目标提至超百亿，年营收目标1000亿。字节同时推出ArkClaw智能体与Seedance 2.0视频模型。",
        "duration": "1-4周",
        "etfs": [
          {
            "name": "515980 云计算与大数据ETF",
            "sentiment": "利好",
            "note": "AI算力需求爆发"
          },
          {
            "name": "159869 科创50ETF",
            "sentiment": "利好",
            "note": "科技成长受益"
          }
        ],
        "stocks": [
          {
            "name": "字节跳动",
            "sentiment": "利好",
            "note": "未上市，映射关注AI应用"
          },
          {
            "name": "中际旭创",
            "sentiment": "利好",
            "note": "光模块龙头"
          },
          {
            "name": "天孚通信",
            "sentiment": "利好",
            "note": "光通信精密器件"
          }
        ],
        "signal": "AI算力需求持续爆发，光模块/光通信板块节后重点关注"
      },
      {
        "emoji": "🔴",
        "title": "礼来口服GLP-1减肥药Foundayo获FDA批准，口服时代正式开启",
        "source": "界面新闻 / FDA",
        "summary": "4月1日晚礼来宣布口服小分子GLP-1受体激动剂orforglipron（商品名Foundayo）在美获批，用于肥胖治疗，4月6日开始发货。这是目前唯一无饮食饮水限制的口服减重GLP-药物，与诺和诺德口服Wegovy正面竞争，两家定价均为最低每月149美元。礼来同时宣布未来十年投资30亿美元扩展中国供应链。中国市场上orforglipron上市申请已获国家药监局受理。",
        "duration": "2-4周",
        "etfs": [
          {
            "name": "512010 医药ETF",
            "sentiment": "利好",
            "note": "GLP-1产业链"
          },
          {
            "name": "159805 医疗ETF",
            "sentiment": "利好",
            "note": "创新药"
          }
        ],
        "stocks": [
          {
            "name": "恒瑞医药",
            "sentiment": "利好",
            "note": "GLP-1资产出海授权Kailera"
          },
          {
            "name": "华东医药",
            "sentiment": "利好",
            "note": "GLP-1布局"
          },
          {
            "name": "信达生物",
            "sentiment": "利好",
            "note": "减重赛道"
          }
        ],
        "signal": "GLP-1口服时代开启，国内药企竞争分化，恒瑞出海模式值得关注"
      }
    ],
    "a_level": [
      {
        "emoji": "🟡",
        "title": "六大行年报出炉：营收增速转正，净息差降幅收窄",
        "source": "界面新闻",
        "summary": "截至4月2日22家A股上市银行发布2025年报，总资产约300万亿。六大行营收增速终于转正（同比+1.2%），告别连续两年负增长。手续费和佣金净收入增长是转正关键，招行代理基金收入同比增40%，农行代理业务增近90%。净息差呈下降态势但降幅收窄，主因同业存款成本大降。债券牛市不再，银行通过兑现浮盈债券增厚利润，2025年投资收益合计4878亿元同比增18%。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "512800 银行ETF",
            "sentiment": "中性",
            "note": "防御属性"
          }
        ],
        "stocks": [
          {
            "name": "招商银行",
            "sentiment": "利好",
            "note": "零售+财富管理"
          },
          {
            "name": "中国银行",
            "sentiment": "利好",
            "note": "国际业务高增"
          }
        ],
        "signal": "银行基本面触底信号，但零售贷款乏力，对公贷款价格战白热化"
      },
      {
        "emoji": "🟡",
        "title": "中企出海加速：恒瑞GLP-1授权Kailera赴美IPO，轮胎/黄金龙头海外布局",
        "source": "界面新闻",
        "summary": "恒瑞医药GLP-1全球资产通过Kailera Therapeutics赴纳斯达克IPO，Kailera无自有实验室，核心资产来自恒瑞独家授权，为恒瑞NewCo出海模式关键验证。中策橡胶拟投资10.4亿在越南建设轮胎基地年产500万条；灵宝黄金完成收购巴布亚新几内亚Simberi金矿；江波龙完成收购巴西子公司Zilia剩余19%股权；海昌新材越南工厂奠基。",
        "duration": "1-2周",
        "etfs": [
          {
            "name": "515050 港股通ETF",
            "sentiment": "利好",
            "note": "港股中国资产"
          }
        ],
        "stocks": [
          {
            "name": "恒瑞医药",
            "sentiment": "利好",
            "note": "创新药出海"
          },
          {
            "name": "中策橡胶",
            "sentiment": "利好",
            "note": "轮胎出海"
          },
          {
            "name": "江波龙",
            "sentiment": "利好",
            "note": "存储出海"
          }
        ],
        "signal": "中企出海从产品出口升级为资产+资本+人才体系出海，出海产业链持续受益"
      },
      {
        "emoji": "🟡",
        "title": "SpaceX IPO超级独角兽：估值1.75万亿美元，6月挂牌",
        "source": "媒体报道",
        "summary": "SpaceX已秘密提交IPO申请，寻求6月上市，估值超1.75万亿美元，募资或超750亿美元，成三巨头超级IPO首家。商业航天题材持续升温。",
        "duration": "1-2个月",
        "etfs": [
          {
            "name": "515980 云计算与大数据ETF",
            "sentiment": "利好",
            "note": "商业航天题材"
          }
        ],
        "stocks": [
          {
            "name": "中航沈飞",
            "sentiment": "利好",
            "note": "军工航天"
          },
          {
            "name": "航天电器",
            "sentiment": "利好",
            "note": "航天配套"
          }
        ],
        "signal": "SpaceX上市催化国内商业航天板块，但实质受益标的有限，题材炒作需谨慎"
      }
    ],
    "douyin": [
      {
        "emoji": "📱",
        "title": "清明节A股休市安排：4月4日至6日休市，7日复牌",
        "source": "交易所公告",
        "summary": "清明节小长假，A股4月4日至6日休市，4月7日（周二）复牌交易。港股4月4日休市半天。",
        "duration": "1天",
        "etfs": [],
        "stocks": [],
        "signal": "假期效应，市场无明显方向，节后首日关注北向资金动向"
      }
    ],
    "sangsha_module": {
      "overall_sentiment": "平稳",
      "advice": "震荡整理，观望为主",
      "avg_buy_prob": 18,
      "avg_panic_prob": 13,
      "analysis_results": [
        {
          "news": "字节豆包日均Token消耗破120万亿，两年翻1000倍",
          "title": "字节豆包日均Token消耗破120万亿，两年翻1000倍",
          "full_title": "字节豆包日均Token消耗破120万亿，两年翻1000倍",
          "summary": "4月2日火山引擎总裁谭待披露，豆包大模型日均Token使用量超120万亿，过去三个月翻倍，比2024...",
          "追高买入概率": 80,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 64,
          "情绪标签": [
            "FOMO",
            "易懂"
          ],
          "韭菜行为总结": "散户疯了，都在追！",
          "市场含义": "顶部风险",
          "买入概率": 50,
          "is_long_term": false,
          "date": "2026-04-03",
          "decay": 1.0,
          "weighted_buy_prob": 50
        },
        {
          "news": "中企出海加速：恒瑞GLP-1授权Kailera赴美IPO，轮...",
          "title": "中企出海加速：恒瑞GLP-1授权Kailera赴美IPO，轮胎/黄金龙头海外布局",
          "full_title": "中企出海加速：恒瑞GLP-1授权Kailera赴美IPO，轮胎/黄金龙头海外布局",
          "summary": "恒瑞医药GLP-1全球资产通过Kailera Therapeutics赴纳斯达克IPO，Kailer...",
          "追高买入概率": 5,
          "抄底买入概率": 54,
          "恐慌卖出概率": 5,
          "观望概率": 80,
          "情绪标签": [
            "抄底冲动"
          ],
          "韭菜行为总结": "散户想抄底，认为是机会",
          "市场含义": "可能有反弹",
          "买入概率": 24,
          "is_long_term": false,
          "date": "2026-04-03",
          "decay": 1.0,
          "weighted_buy_prob": 24
        },
        {
          "news": "六大行年报出炉：营收增速转正，净息差降幅收窄",
          "title": "六大行年报出炉：营收增速转正，净息差降幅收窄",
          "full_title": "六大行年报出炉：营收增速转正，净息差降幅收窄",
          "summary": "截至4月2日22家A股上市银行发布2025年报，总资产约300万亿。六大行营收增速终于转正（同比+1...",
          "追高买入概率": 34,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 83,
          "情绪标签": [
            "易懂"
          ],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 22,
          "is_long_term": false,
          "date": "2026-04-03",
          "decay": 1.0,
          "weighted_buy_prob": 22
        },
        {
          "news": "礼来口服GLP-1减肥药Foundayo获FDA批准，口服时...",
          "title": "礼来口服GLP-1减肥药Foundayo获FDA批准，口服时代正式开启",
          "full_title": "礼来口服GLP-1减肥药Foundayo获FDA批准，口服时代正式开启",
          "summary": "4月1日晚礼来宣布口服小分子GLP-1受体激动剂orforglipron（商品名Foundayo）在...",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 57,
          "观望概率": 79,
          "情绪标签": [
            "恐慌"
          ],
          "韭菜行为总结": "散户恐慌，想割肉",
          "市场含义": "可能见底",
          "买入概率": 5,
          "is_long_term": false,
          "date": "2026-04-03",
          "decay": 1.0,
          "weighted_buy_prob": 5
        },
        {
          "news": "SpaceX IPO超级独角兽：估值1.75万亿美元，6月挂...",
          "title": "SpaceX IPO超级独角兽：估值1.75万亿美元，6月挂牌",
          "full_title": "SpaceX IPO超级独角兽：估值1.75万亿美元，6月挂牌",
          "summary": "SpaceX已秘密提交IPO申请，寻求6月上市，估值超1.75万亿美元，募资或超750亿美元，成三巨...",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 5,
          "is_long_term": false,
          "date": "2026-04-03",
          "decay": 1.0,
          "weighted_buy_prob": 5
        },
        {
          "news": "清明节A股休市安排：4月4日至6日休市，7日复牌",
          "title": "清明节A股休市安排：4月4日至6日休市，7日复牌",
          "full_title": "清明节A股休市安排：4月4日至6日休市，7日复牌",
          "summary": "清明节小长假，A股4月4日至6日休市，4月7日（周二）复牌交易。港股4月4日休市半天。",
          "追高买入概率": 5,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 95,
          "情绪标签": [],
          "韭菜行为总结": "散户情绪平稳",
          "市场含义": "中性",
          "买入概率": 5,
          "is_long_term": false,
          "date": "2026-04-03",
          "decay": 1.0,
          "weighted_buy_prob": 5
        }
      ],
      "total_news_count": 6,
      "time_window": "7天累积（长期新闻除外）"
    },
    "white_dragon": {
      "主力状态": "出货",
      "阶段": "末期",
      "行为解释": "多个ETF出现主力派发信号，注意风险",
      "是否利用散户": true,
      "散户情绪": {
        "平均买入概率": 21,
        "平均恐慌概率": 15
      },
      "各ETF分析": [
        {
          "code": "512760",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.0
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 21.72,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 21,
          "sangsha_panic_prob": 15
        },
        {
          "code": "512930",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 5.43
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 11.41,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 21,
          "sangsha_panic_prob": 15
        },
        {
          "code": "518880",
          "price_trend": {
            "trend": "side",
            "strength": 40,
            "change_pct": 1.33
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": -10.83,
            "level": "normal"
          },
          "主力状态": "吸筹",
          "阶段": "早期",
          "行为解释": "价格横盘/小跌，资金流入，主力可能在低位吸筹",
          "是否利用散户": false,
          "sangsha_buy_prob": 21,
          "sangsha_panic_prob": 15
        },
        {
          "code": "588890",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.16
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 0.4,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 21,
          "sangsha_panic_prob": 15
        },
        {
          "code": "159382",
          "price_trend": {
            "trend": "up",
            "strength": 90,
            "change_pct": 6.74
          },
          "volume_trend": {
            "trend": "side",
            "change_pct": 29.76,
            "level": "normal"
          },
          "主力状态": "出货",
          "阶段": "末期",
          "行为解释": "价格上涨但量能不足，主力高位派发可能性大",
          "是否利用散户": true,
          "sangsha_buy_prob": 21,
          "sangsha_panic_prob": 15
        }
      ],
      "综合建议": "⚠️ 风险提示：主力可能正在派发，散户追高风险大，建议减仓观望"
    }
  }
};

const availableDates = ["2026-04-09", "2026-04-08", "2026-04-07", "2026-04-06", "2026-04-05", "2026-04-04", "2026-04-03", "2026-04-02", "2026-04-01", "2026-03-31", "2026-03-30", "2026-03-29", "2026-03-28", "2026-03-27", "2026-03-26", "2026-03-25"];

function getNews(date) { return newsData[date] || null; }
function getPreviousDate(date) { const idx = availableDates.indexOf(date); return idx < availableDates.length - 1 ? availableDates[idx + 1] : null; }
function getNextDate(date) { const idx = availableDates.indexOf(date); return idx > 0 ? availableDates[idx - 1] : null; }