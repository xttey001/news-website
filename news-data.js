// 新闻数据 - 悟空财经判断格式
var newsData = {
  "2026-04-02": {
    "date": "2026-04-02",
    "market_tone": "谨慎偏多 — 美伊谈判利好全球风险资产，但A股财报季压力对冲，整体震荡为主",
    "wukong_judgment": {
      "emotion": "谨慎偏多",
      "analysis": [
        "美伊谈判利好全球风险资产，但A股自身财报季压力对冲",
        "医药昨日涨停潮情绪可能延续到今日上午，下午警惕分化",
        "资金可能在「科技（财报）」和「医药（主题）」之间轮动"
      ],
      "strategy": [
        "✅ 持仓医药ETF的：考虑部分锁利",
        "✅ 想入场的：等医药冲高回落后低吸，不要追涨停",
        "⚠️ 水泥/基建：短线别碰",
        "📌 科创50/芯片：若今晚有龙头业绩超预期，明日可关注"
      ]
    },
    "s_level": [
      {
        "emoji": "🔴",
        "title": "美伊谈判重启 → 全球风险偏好切换",
        "source": "Bloomberg / 路透",
        "summary": "美伊在阿曼恢复间接谈判，讨论解除制裁换取核限制。油价承压预期升温，全球避险情绪降温。特朗普称伊朗请求停火，但伊朗外交部否认。",
        "duration": "2-4周",
        "etfs": [
          {"name": "512880 国债ETF", "sentiment": "利好", "note": "避险降温→长债压力减轻"},
          {"name": "513500 标普ETF", "sentiment": "利好", "note": "美股情绪修复"},
          {"name": "588000 科创50ETF", "sentiment": "利好", "note": "科技风险偏好提升"},
          {"name": "160140 油气ETF", "sentiment": "利空", "note": "油价压力"}
        ],
        "stocks": [
          {"name": "601318 中国平安", "sentiment": "利好", "note": "权益风险偏好提升"},
          {"name": "600030 中信证券", "sentiment": "利好", "note": "券商β行情"},
          {"name": "600188 兖矿能源", "sentiment": "利空", "note": "煤炭跟油气联动"},
          {"name": "601666 平煤股份", "sentiment": "利空", "note": "煤价承压"}
        ]
      },
      {
        "emoji": "🔴",
        "title": "一季度财报季开幕 → 盈利压力测试",
        "source": "上交所/深交所公告",
        "summary": "4月起进入一季报密集披露期。机构预期整体盈利增速回落，部分科技股可能超预期。半导体龙头业绩暴涨4659%，10只个股利润翻倍。",
        "duration": "3-4周",
        "etfs": [
          {"name": "588000 科创50ETF", "sentiment": "关注"},
          {"name": "512760 芯片ETF", "sentiment": "关注", "note": "业绩超预期可能性大"},
          {"name": "515050 5GETF", "sentiment": "回避", "note": "业绩分化风险"}
        ],
        "stocks": [
          {"name": "688981 中芯国际", "sentiment": "关注", "note": "若业绩超预期可带动芯片板块"},
          {"name": "002415 海康威视", "sentiment": "关注", "note": "AI业务增速"},
          {"name": "000001 平安银行", "sentiment": "警惕", "note": "银行坏账率可能抬头"},
          {"name": "600519 贵州茅台", "sentiment": "警惕", "note": "消费需求仍待验证"}
        ]
      }
    ],
    "a_level": [
      {
        "emoji": "🟡",
        "title": "医药板块涨停潮延续 → 创新药领涨",
        "source": "财联社 / 163财经收盘总结",
        "summary": "港股创新药ETF暴涨超7%，A股广生堂、凯莱英、睿智医药等多股涨停。梦回去年创新药牛市情绪。",
        "duration": "2-3天（警惕今日冲高回落）",
        "etfs": [
          {"name": "159992 创新药ETF", "sentiment": "利好"},
          {"name": "512010 医药ETF", "sentiment": "利好"}
        ],
        "stocks": [
          {"name": "300759 凯莱英", "sentiment": "利好", "note": "CDMO龙头"},
          {"name": "300199 睿智医药", "sentiment": "利好", "note": "CRO+创新药"},
          {"name": "603259 药明康德", "sentiment": "利好", "note": "CXO总龙头"},
          {"name": "300122 智飞生物", "sentiment": "利好", "note": "疫苗+创新药"}
        ],
        "warning": "昨日涨停个股若今日高开低走，需警惕获利盘兑现，勿追高"
      },
      {
        "emoji": "🟡",
        "title": "水泥/基建板块暴跌 → 需求预期恶化",
        "source": "同花顺 / 163财经",
        "summary": "水泥巨头业绩巨亏，海螺水泥巨亏72亿，基建需求疲软信号持续。",
        "duration": "1-2天（短线博弈机会）",
        "etfs": [
          {"name": "159619 建材ETF", "sentiment": "回避"}
        ],
        "stocks": [
          {"name": "600585 海螺水泥", "sentiment": "回避", "note": "业绩压力持续"},
          {"name": "000672 上峰水泥", "sentiment": "回避"},
          {"name": "516190 传媒ETF", "sentiment": "利好", "note": "资金可能从基建链轮动"}
        ]
      }
    ],
    "douyin": [
      {
        "emoji": "📱",
        "title": "直播电商数据继续爆 → 新消费结构性机会",
        "source": "抖音官方数据",
        "summary": "3月直播电商GMV同比+35%，中小主播增速超越头部格局延续。",
        "duration": "1-2周",
        "etfs": [
          {"name": "516190 传媒ETF", "sentiment": "利好"},
          {"name": "159805 互联网ETF", "sentiment": "利好"}
        ],
        "stocks": [
          {"name": "300058 蓝色光标", "sentiment": "利好", "note": "MCN+AI营销"},
          {"name": "002027 分众传媒", "sentiment": "利好", "note": "广告复苏"},
          {"name": "300413 芒果超媒", "sentiment": "利好", "note": "内容电商"},
          {"name": "603198 壹网壹创", "sentiment": "利好", "note": "代运营"}
        ]
      }
    ]
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
        "✅ 跟随情绪修复，优先布局超跌科技/医药",
        "⚠️ 避险资产短期回调，等待地缘风险反复再介入",
        "📌 关注SpaceX IPO概念股"
      ]
    },
    "s_level": [
      {
        "emoji": "🔴",
        "title": "全球股市暴涨：日经+4%、韩国+8%",
        "source": "财联社",
        "summary": "美伊局势缓和预期升温，全球风险资产狂欢。日经225涨4%，韩国KOSPI涨8%，欧洲多国涨3%以上。",
        "duration": "2-4周",
        "etfs": [
          {"name": "512500 中证500ETF", "sentiment": "利好"},
          {"name": "159915 创业板ETF", "sentiment": "利好"},
          {"name": "512760 芯片ETF", "sentiment": "利好"}
        ],
        "stocks": [
          {"name": "688981 中芯国际", "sentiment": "利好"},
          {"name": "300750 宁德时代", "sentiment": "利好"},
          {"name": "600519 贵州茅台", "sentiment": "利好"}
        ]
      }
    ],
    "a_level": [
      {
        "emoji": "🟡",
        "title": "医药板块掀涨停潮",
        "source": "东方财富",
        "summary": "医药生物板块领涨两市，港股创新药ETF暴涨超7%，A股多股涨停。",
        "duration": "1-2周",
        "etfs": [
          {"name": "159992 创新药ETF", "sentiment": "利好"}
        ],
        "stocks": [
          {"name": "广生堂", "sentiment": "利好"},
          {"name": "睿智医药", "sentiment": "利好"},
          {"name": "凯莱英", "sentiment": "利好"}
        ]
      },
      {
        "emoji": "🟡",
        "title": "SpaceX载人飞船发射成功",
        "source": "新浪财经",
        "summary": "美国SpaceX载人飞船搭载4名宇航员发射升空。SpaceX已秘密提交IPO申请。",
        "duration": "1-2周",
        "etfs": [
          {"name": "515980 云计算ETF", "sentiment": "利好"}
        ],
        "stocks": [
          {"name": "600760 中航沈飞", "sentiment": "利好"},
          {"name": "002025 航天电器", "sentiment": "利好"}
        ]
      }
    ],
    "douyin": [
      {
        "emoji": "📱",
        "title": "SpaceX IPO消息刷屏",
        "source": "社交媒体",
        "summary": "SpaceX IPO消息在社交媒体引发热议，估值1.75万亿美元。",
        "duration": "1-2周",
        "etfs": [],
        "stocks": []
      }
    ]
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
        "⚠️ 控制仓位，观望为主",
        "📌 关注一季报超预期个股",
        "✅ 黄金/避险资产可适当配置"
      ]
    },
    "s_level": [
      {
        "emoji": "🔴",
        "title": "季末资金面紧张 → 利率上行压力",
        "source": "央行公开市场操作",
        "summary": "季末流动性紧张，央行连续多日净投放，但资金利率仍上行。银行间7天回购利率突破3%。",
        "duration": "1周",
        "etfs": [
          {"name": "512880 国债ETF", "sentiment": "利空", "note": "利率上行压力"},
          {"name": "511010 国债ETF", "sentiment": "利空"}
        ],
        "stocks": [
          {"name": "600036 招商银行", "sentiment": "关注", "note": "息差管理能力"},
          {"name": "601398 工商银行", "sentiment": "关注"}
        ]
      }
    ],
    "a_level": [
      {
        "emoji": "🟡",
        "title": "消博会即将开幕 → 海南自贸港概念",
        "source": "商务部公告",
        "summary": "第三届消博会4月10日开幕，海南自贸港政策利好预期升温。",
        "duration": "1-2周",
        "etfs": [],
        "stocks": [
          {"name": "002594 比亚迪", "sentiment": "关注", "note": "新能源车参展"},
          {"name": "600745 闻泰科技", "sentiment": "关注"}
        ]
      }
    ],
    "douyin": []
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
        "✅ 关注业绩超预期的科技龙头",
        "✅ 黄金/白银ETF可持有",
        "⚠️ 高估值小票规避"
      ]
    },
    "s_level": [
      {
        "emoji": "🔴",
        "title": "TCL科技业绩超预期 → 面板周期拐点",
        "source": "公司公告",
        "summary": "TCL科技发布2026年一季报，净利润同比增长150%，面板价格持续上涨。行业周期拐点确认。",
        "duration": "2-4周",
        "etfs": [
          {"name": "512760 芯片ETF", "sentiment": "利好", "note": "电子产业链联动"},
          {"name": "159995 芯片ETF", "sentiment": "利好"}
        ],
        "stocks": [
          {"name": "000100 TCL科技", "sentiment": "利好", "note": "业绩超预期"},
          {"name": "002049 国星光电", "sentiment": "利好", "note": "LED面板"},
          {"name": "002241 歌尔股份", "sentiment": "利好", "note": "消费电子"}
        ]
      },
      {
        "emoji": "🔴",
        "title": "小米汽车交付破万 → 新能源车链活跃",
        "source": "小米汽车官方",
        "summary": "小米汽车3月交付量突破1万台，超市场预期。新能源汽车市场竞争加剧。",
        "duration": "1-2周",
        "etfs": [
          {"name": "515030 新能源车ETF", "sentiment": "利好"},
          {"name": "516390 智能汽车ETF", "sentiment": "利好"}
        ],
        "stocks": [
          {"name": "300750 宁德时代", "sentiment": "利好", "note": "动力电池龙头"},
          {"name": "002594 比亚迪", "sentiment": "利好", "note": "新能源车龙头"}
        ]
      }
    ],
    "a_level": [
      {
        "emoji": "🟡",
        "title": "汇川技术港股上市 → 工业自动化龙头",
        "source": "港交所公告",
        "summary": "汇川技术港股成功上市，募资用于工业自动化产能扩张。",
        "duration": "1周",
        "etfs": [],
        "stocks": [
          {"name": "300124 汇川技术", "sentiment": "利好", "note": "工业自动化龙头"}
        ]
      },
      {
        "emoji": "🟡",
        "title": "瑞云冷链IPO过会 → 冷链物流概念",
        "source": "证监会公告",
        "summary": "瑞云冷链IPO过会，冷链物流板块关注度提升。",
        "duration": "1周",
        "etfs": [],
        "stocks": [
          {"name": "002153 石基信息", "sentiment": "关注", "note": "冷链信息化"}
        ]
      }
    ],
    "douyin": []
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
        "✅ 黄金ETF、国债ETF加仓",
        "✅ 能源化工股短线博弈",
        "⚠️ 科技股、消费股暂时回避"
      ]
    },
    "s_level": [
      {
        "emoji": "🔴",
        "title": "霍尔木兹海峡危机升级 → 能源化工暴涨",
        "source": "路透 / 新华社",
        "summary": "伊朗威胁封锁霍尔木兹海峡，胡塞武装宣布参战。原油期货暴涨8%，能源化工板块全线大涨。",
        "duration": "2-4周",
        "etfs": [
          {"name": "160140 油气ETF", "sentiment": "利好", "note": "原油涨价直接受益"},
          {"name": "159869 化工ETF", "sentiment": "利好", "note": "化工品跟涨"},
          {"name": "518880 黄金ETF", "sentiment": "利好", "note": "避险资产"},
          {"name": "512880 国债ETF", "sentiment": "利好", "note": "避险情绪升温"}
        ],
        "stocks": [
          {"name": "601857 中国石油", "sentiment": "利好", "note": "原油涨价受益"},
          {"name": "600028 中国石化", "sentiment": "利好"},
          {"name": "600188 兖矿能源", "sentiment": "利好", "note": "煤炭联动"},
          {"name": "601899 紫金矿业", "sentiment": "利好", "note": "黄金+铜"}
        ]
      },
      {
        "emoji": "🔴",
        "title": "中信证券年报落地 → 300亿净利润",
        "source": "公司公告",
        "summary": "中信证券2025年净利润300亿元，符合预期。券商板块估值修复逻辑延续。",
        "duration": "1-2周",
        "etfs": [
          {"name": "512880 证券ETF", "sentiment": "利好"}
        ],
        "stocks": [
          {"name": "600030 中信证券", "sentiment": "利好", "note": "业绩落地"},
          {"name": "601211 国泰君安", "sentiment": "利好"}
        ]
      },
      {
        "emoji": "🔴",
        "title": "比亚迪年报发布 → 营收8040亿",
        "source": "公司公告",
        "summary": "比亚迪2025年营收8040亿元，同比增长35%。新能源车龙头地位稳固。",
        "duration": "1-2周",
        "etfs": [
          {"name": "515030 新能源车ETF", "sentiment": "利好"}
        ],
        "stocks": [
          {"name": "002594 比亚迪", "sentiment": "利好", "note": "业绩验证"},
          {"name": "300750 宁德时代", "sentiment": "利好"}
        ]
      }
    ],
    "a_level": [
      {
        "emoji": "🟡",
        "title": "工商银行分红预案 → 1100亿现金分红",
        "source": "公司公告",
        "summary": "工商银行2025年分红1100亿元，股息率超6%。银行板块高股息价值凸显。",
        "duration": "1周",
        "etfs": [
          {"name": "512800 银行ETF", "sentiment": "利好"}
        ],
        "stocks": [
          {"name": "601398 工商银行", "sentiment": "利好", "note": "高股息"},
          {"name": "601288 农业银行", "sentiment": "利好"}
        ]
      },
      {
        "emoji": "🟡",
        "title": "铜价突围 → 伦铜突破11000美元",
        "source": "LME / 上期所",
        "summary": "伦铜突破11000美元/吨，创历史新高。新能源+AI算力需求驱动铜价上涨。",
        "duration": "2-4周",
        "etfs": [
          {"name": "562330 有色ETF", "sentiment": "利好"}
        ],
        "stocks": [
          {"name": "601899 紫金矿业", "sentiment": "利好", "note": "铜+金双驱动"},
          {"name": "600547 山东黄金", "sentiment": "利好"}
        ]
      },
      {
        "emoji": "🟡",
        "title": "月之暗面冲刺IPO → AI应用赛道",
        "source": "科创板日报",
        "summary": "月之暗面启动港股IPO筹备，估值超200亿美元。AI大模型应用赛道持续火热。",
        "duration": "1-2周",
        "etfs": [
          {"name": "515980 云计算ETF", "sentiment": "利好"},
          {"name": "588000 科创50ETF", "sentiment": "利好"}
        ],
        "stocks": [
          {"name": "688111 金山办公", "sentiment": "利好", "note": "AI办公应用"}
        ]
      }
    ],
    "douyin": []
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
        "⚠️ 降低仓位，控制风险",
        "✅ 黄金、国债等避险资产配置",
        "📌 等待美联储政策明朗后再布局"
      ]
    },
    "s_level": [
      {
        "emoji": "🔴",
        "title": "美联储鹰派言论 → 降息预期降温",
        "source": "美联储议息会议",
        "summary": "美联储主席暗示2026年可能不降息，通胀压力持续。全球股市承压，美元指数走强。",
        "duration": "2-4周",
        "etfs": [
          {"name": "513500 标普ETF", "sentiment": "利空", "note": "美股承压"},
          {"name": "588000 科创50ETF", "sentiment": "利空", "note": "成长股估值压力"},
          {"name": "512880 国债ETF", "sentiment": "利好", "note": "避险资产"}
        ],
        "stocks": [
          {"name": "688981 中芯国际", "sentiment": "利空", "note": "科技股估值压力"},
          {"name": "300750 宁德时代", "sentiment": "利空"}
        ]
      }
    ],
    "a_level": [
      {
        "emoji": "🟡",
        "title": "人民币贬值压力 → 北向资金流出",
        "source": "外汇市场",
        "summary": "美元走强，人民币兑美元跌破7.3关口。北向资金连续3日净流出。",
        "duration": "1-2周",
        "etfs": [],
        "stocks": [
          {"name": "601318 中国平安", "sentiment": "利空", "note": "外资重仓股承压"}
        ]
      },
      {
        "emoji": "🟡",
        "title": "央行逆回购投放 → 流动性对冲",
        "source": "央行公开市场",
        "summary": "央行开展1500亿逆回购操作，对冲季末流动性紧张。",
        "duration": "1周",
        "etfs": [
          {"name": "512880 国债ETF", "sentiment": "利好"}
        ],
        "stocks": []
      },
      {
        "emoji": "🟡",
        "title": "新能源车销量不及预期 → 板块调整",
        "source": "中汽协数据",
        "summary": "3月新能源车销量增速放缓，市场预期落空。板块短期承压。",
        "duration": "1周",
        "etfs": [
          {"name": "515030 新能源车ETF", "sentiment": "利空"}
        ],
        "stocks": [
          {"name": "002594 比亚迪", "sentiment": "利空"},
          {"name": "300750 宁德时代", "sentiment": "利空"}
        ]
      }
    ],
    "douyin": []
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
        "✅ 关注业绩超预期龙头",
        "✅ 黄金ETF持有",
        "⚠️ 高估值小票规避"
      ]
    },
    "s_level": [
      {
        "emoji": "🔴",
        "title": "TCL科技业绩大增 → 面板周期拐点",
        "source": "公司公告",
        "summary": "TCL科技一季报净利润同比增150%，面板价格持续上涨，行业周期反转确认。",
        "duration": "2-4周",
        "etfs": [
          {"name": "512760 芯片ETF", "sentiment": "利好"}
        ],
        "stocks": [
          {"name": "000100 TCL科技", "sentiment": "利好"},
          {"name": "002049 国星光电", "sentiment": "利好"}
        ]
      }
    ],
    "a_level": [
      {
        "emoji": "🟡",
        "title": "美团财报发布 → 营收超预期",
        "source": "公司公告",
        "summary": "美团2025年Q4营收同比增长25%，外卖业务盈利能力改善。",
        "duration": "1-2周",
        "etfs": [
          {"name": "159805 互联网ETF", "sentiment": "利好"}
        ],
        "stocks": [
          {"name": "3690 美团", "sentiment": "利好"}
        ]
      },
      {
        "emoji": "🟡",
        "title": "茅台涨价预期 → 消费股估值修复",
        "source": "市场传闻",
        "summary": "市场预期茅台将上调出厂价，白酒板块估值修复。",
        "duration": "1周",
        "etfs": [
          {"name": "512810 消费ETF", "sentiment": "利好"}
        ],
        "stocks": [
          {"name": "600519 贵州茅台", "sentiment": "利好"}
        ]
      },
      {
        "emoji": "🟡",
        "title": "黄金ETF持续吸金 → 避险情绪延续",
        "source": "上交所数据",
        "summary": "黄金ETF规模突破400亿，避险资金持续流入。",
        "duration": "持续",
        "etfs": [
          {"name": "518880 黄金ETF", "sentiment": "利好"}
        ],
        "stocks": [
          {"name": "600547 山东黄金", "sentiment": "利好"}
        ]
      }
    ],
    "douyin": []
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
        "✅ 地产链短线博弈",
        "✅ 消费股中线布局",
        "📌 半导体设备长线持有"
      ]
    },
    "s_level": [
      {
        "emoji": "🔴",
        "title": "地产政策松绑预期 → 地产链反弹",
        "source": "住建部传闻",
        "summary": "市场传闻多地将出台地产松绑政策，包括限购放松、首付比例下调等。地产股集体反弹。",
        "duration": "1-2周",
        "etfs": [
          {"name": "512200 房地产ETF", "sentiment": "利好"},
          {"name": "159619 建材ETF", "sentiment": "利好"}
        ],
        "stocks": [
          {"name": "000002 万科A", "sentiment": "利好"},
          {"name": "600048 保利发展", "sentiment": "利好"},
          {"name": "600383 金地集团", "sentiment": "利好"}
        ]
      },
      {
        "emoji": "🔴",
        "title": "AI芯片国产替代加速 → 半导体设备股走强",
        "source": "科创板日报",
        "summary": "美对华芯片限制升级，国产替代加速。北方华创、中微公司订单大幅增长。",
        "duration": "2-4周",
        "etfs": [
          {"name": "512760 芯片ETF", "sentiment": "利好"},
          {"name": "588000 科创50ETF", "sentiment": "利好"}
        ],
        "stocks": [
          {"name": "002371 北方华创", "sentiment": "利好", "note": "半导体设备龙头"},
          {"name": "688012 中微公司", "sentiment": "利好"},
          {"name": "688981 中芯国际", "sentiment": "利好"}
        ]
      }
    ],
    "a_level": [
      {
        "emoji": "🟡",
        "title": "消费复苏信号增强 → 社零数据改善",
        "source": "统计局数据",
        "summary": "2月社零同比增长5.5%，好于预期。消费复苏势头延续。",
        "duration": "1-2周",
        "etfs": [
          {"name": "512810 消费ETF", "sentiment": "利好"}
        ],
        "stocks": [
          {"name": "600519 贵州茅台", "sentiment": "利好"},
          {"name": "000858 五粮液", "sentiment": "利好"}
        ]
      }
    ],
    "douyin": []
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
        "✅ 半导体设备股持有",
        "✅ 新能源车ETF可加仓",
        "📌 消费电子股中线布局"
      ]
    },
    "s_level": [
      {
        "emoji": "🔴",
        "title": "半导体设备订单超预期 → 国产替代加速",
        "source": "SEMI数据",
        "summary": "一季度中国大陆半导体设备采购额同比增长45%，北方华创订单排产至2027年。国产替代进程加速。",
        "duration": "2-4周",
        "etfs": [
          {"name": "512760 芯片ETF", "sentiment": "利好"},
          {"name": "588000 科创50ETF", "sentiment": "利好"}
        ],
        "stocks": [
          {"name": "002371 北方华创", "sentiment": "利好", "note": "订单排产至2027年"},
          {"name": "688012 中微公司", "sentiment": "利好"},
          {"name": "603501 沪硅产业", "sentiment": "利好"}
        ]
      },
      {
        "emoji": "🔴",
        "title": "新能源车下乡补贴落地 → 三四线城市渗透率提升",
        "source": "工信部公告",
        "summary": "新能源车下乡补贴政策正式落地，补贴金额最高5000元。三四线城市新能源车渗透率有望快速提升。",
        "duration": "1-2周",
        "etfs": [
          {"name": "515030 新能源车ETF", "sentiment": "利好"},
          {"name": "516390 智能汽车ETF", "sentiment": "利好"}
        ],
        "stocks": [
          {"name": "002594 比亚迪", "sentiment": "利好", "note": "直接受益"},
          {"name": "601238 广汽集团", "sentiment": "利好"},
          {"name": "000625 长安汽车", "sentiment": "利好"}
        ]
      }
    ],
    "a_level": [
      {
        "emoji": "🟡",
        "title": "消费电子回暖信号 → 手机出货量增长",
        "source": "信通院数据",
        "summary": "2月国内手机出货量同比增长12%，连续4个月正增长。消费电子周期见底信号明确。",
        "duration": "1-2周",
        "etfs": [
          {"name": "159732 消费电子ETF", "sentiment": "利好"}
        ],
        "stocks": [
          {"name": "002241 歌尔股份", "sentiment": "利好", "note": "苹果链"},
          {"name": "002475 立讯精密", "sentiment": "利好"}
        ]
      }
    ],
    "douyin": []
  }
};

// 获取所有可用日期（从最新到最旧）
var availableDates = [
  "2026-04-02",
  "2026-04-01",
  "2026-03-31",
  "2026-03-30",
  "2026-03-29",
  "2026-03-28",
  "2026-03-27",
  "2026-03-26",
  "2026-03-25"
];
