// 新闻数据 - 悟空财经判断格式
const newsData = {
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
  }
};

// 获取所有可用日期（从最新到最旧）
const availableDates = [
  "2026-04-02",
  "2026-04-01"
];
