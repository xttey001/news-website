// 新闻数据 - 自动生成
const newsData = {
  "2026-04-02": {
    "date": "2026-04-02",
    "market_tone": "谨慎偏多 — 美伊谈判利好全球风险资产，但A股财报季压力对冲，整体震荡为主",
    "s_level": [
      {
        "emoji": "🔴",
        "title": "美伊谈判重启 → 全球风险偏好切换",
        "summary": "美伊在阿曼恢复间接谈判，讨论解除制裁换取核限制。油价承压预期升温，全球避险情绪降温。",
        "duration": "2-4周",
        "etfs": [
          {"name": "512880 国债ETF", "sentiment": "利好"},
          {"name": "513500 标普ETF", "sentiment": "利好"},
          {"name": "588000 科创50ETF", "sentiment": "利好"},
          {"name": "160140 油气ETF", "sentiment": "利空"}
        ],
        "stocks": ["601318 中国平安", "600030 中信证券", "600188 兖矿能源", "601666 平煤股份"],
        "signal": "避险降温→长债压力减轻，权益风险偏好提升，油气/煤炭联动承压"
      },
      {
        "emoji": "🔴",
        "title": "一季度财报季开幕 → 盈利压力测试",
        "summary": "4月起进入一季报密集披露期。机构预期整体盈利增速回落，部分科技股可能超预期。",
        "duration": "3-4周",
        "etfs": [
          {"name": "588000 科创50ETF", "sentiment": "关注"},
          {"name": "512760 芯片ETF", "sentiment": "关注"},
          {"name": "515050 5GETF", "sentiment": "警惕"}
        ],
        "stocks": ["688981 中芯国际", "002415 海康威视", "000001 平安银行", "600519 贵州茅台"],
        "signal": "整体盈利增速回落，绩优科技股可关注，消费/银行需警惕"
      },
      {
        "emoji": "🔴",
        "title": "伊朗将对霍尔木兹海峡收通行费，特朗普希望4月6日前达成协议",
        "summary": "伊朗宣布将对霍尔木兹海峡收取通行费，作为对美制裁的反制措施。特朗普表示希望4月6日前达成停火协议，地缘博弈进入关键窗口。",
        "duration": "1-2周",
        "etfs": [
          {"name": "518880 黄金ETF", "sentiment": "利好"},
          {"name": "160140 油气ETF", "sentiment": "关注"}
        ],
        "stocks": ["中航沈飞", "中国石油", "招商轮船"],
        "signal": "海峡通行费政策增加油运不确定性，黄金避险属性强化"
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
        "stocks": ["688981 中芯国际", "603501 澜起科技"],
        "signal": "存储和AI半导体板块情绪高涨，节后A股科技股有望跟涨"
      }
    ],
    "a_level": [
      {
        "emoji": "🟡",
        "title": "医药板块涨停潮延续 → 创新药领涨",
        "summary": "港股创新药ETF暴涨超7%，A股广生堂、凯莱英、睿智医药等多股涨停。创新药出海逻辑持续验证。",
        "duration": "2-3天（警惕今日冲高回落）",
        "etfs": [
          {"name": "159992 创新药产业ETF", "sentiment": "利好"},
          {"name": "512010 医药ETF", "sentiment": "利好"}
        ],
        "stocks": ["300759 凯莱英", "300199 睿智医药", "603259 药明康德", "300122 智飞生物"],
        "signal": "昨日涨停情绪可能延续到今日上午，下午警惕分化，冲高回落需锁利"
      },
      {
        "emoji": "🟡",
        "title": "水泥/基建板块暴跌 → 需求预期恶化",
        "summary": "水泥巨头业绩巨亏，基建需求疲软信号持续。",
        "duration": "1-2天（短线博弈机会）",
        "etfs": [{"name": "159619 建材ETF", "sentiment": "回避"}],
        "stocks": ["600585 海螺水泥", "000672 上峰水泥"],
        "signal": "资金腾挪方向：可能轮动至传媒ETF等"
      },
      {
        "emoji": "🟡",
        "title": "SpaceX IPO超级独角兽：估值1.75万亿美元，6月挂牌",
        "summary": "SpaceX已秘密提交IPO申请，寻求6月上市，估值超1.75万亿美元，募资或超750亿美元。",
        "duration": "1-2个月",
        "etfs": [{"name": "515980 云计算与大数据ETF", "sentiment": "利好"}],
        "stocks": ["中航沈飞", "航天电器"],
        "signal": "商业航天题材升温，但A股实质受益标的有限"
      },
      {
        "emoji": "🟡",
        "title": "一季度财报季开启：半导体龙头业绩暴涨4659%",
        "summary": "一季度财报季启幕，多家公司提前发布业绩，半导体龙头利润暴增4659%，10只个股利润翻倍。",
        "duration": "1-2周",
        "etfs": [{"name": "512760 芯片ETF", "sentiment": "利好"}],
        "stocks": ["扬杰科技", "中芯国际"],
        "signal": "资金提前布局业绩超预期个股，绩优科技股受青睐"
      },
      {
        "emoji": "🟡",
        "title": "特斯拉欧洲销售分化：意大利大增32%，葡萄牙下滑2%",
        "summary": "特斯拉欧洲多国销售数据出炉，意大利3月注册量同比大增32%，但葡萄牙下滑2%。",
        "duration": "2-4周",
        "etfs": [{"name": "515700 新能源ETF", "sentiment": "利好"}],
        "stocks": ["比亚迪"],
        "signal": "新能源车欧洲竞争加剧，比亚迪出海逻辑持续"
      },
      {
        "emoji": "🟡",
        "title": "礼来减肥药FOUNDAYO获美国批准",
        "summary": "礼来公司减肥药FOUNDAYO获美国FDA批准，GLP-1减肥药市场持续扩大。",
        "duration": "1-2个月",
        "etfs": [],
        "stocks": ["华东医药", "恒瑞医药"],
        "signal": "GLP-1减肥药概念节后可能再次发酵"
      }
    ],
    "douyin": [
      {
        "emoji": "📱",
        "title": "直播电商数据继续爆 → 新消费结构性机会",
        "summary": "3月直播电商GMV同比+35%，中小主播增速超越头部格局延续。",
        "duration": "1-2周",
        "etfs": [
          {"name": "516190 传媒ETF", "sentiment": "利好"},
          {"name": "159805 互联网ETF", "sentiment": "利好"}
        ],
        "stocks": ["300058 蓝色光标", "002027 分众传媒", "300413 芒果超媒", "603198 壹网壹创"],
        "signal": "新消费结构性机会，MCN+AI营销、广告复苏、内容电商概念持续受益"
      },
      {
        "emoji": "📱",
        "title": "清明节A股休市安排：4月4日至6日休市，7日复牌",
        "summary": "清明节小长假，A股4月4日至6日休市，4月7日复牌交易。",
        "duration": "1天",
        "etfs": [],
        "stocks": [],
        "signal": "假期效应，市场无明显方向，节后首日关注北向资金动向"
      }
    ]
  },
  "2026-04-01": {
    "date": "2026-04-01",
    "market_tone": "美伊释放停火信号，全球风险资产普涨，A股跟涨1%+，市场情绪由空转多",
    "s_level": [
      {
        "emoji": "🔴",
        "title": "美伊讨论以重开霍尔木兹海峡为条件的停火协议",
        "summary": "美伊双方正就潜在停火协议展开讨论，美方要求伊朗重开霍尔木兹海峡换取停火。",
        "duration": "1-2天",
        "etfs": [{"name": "512880 国债ETF", "sentiment": "利空"}],
        "stocks": ["中国石油", "中国石化", "招商轮船"],
        "signal": "避险资金撤出油运板块，油价大幅回落，能源股承压"
      },
      {
        "emoji": "🔴",
        "title": "全球股市暴涨：日经+4%、韩国+8%、美股存储板块爆发",
        "summary": "美伊局势缓和预期升温，全球风险资产狂欢。存储芯片大厂铠侠再度发布停产通知。",
        "duration": "2-4周",
        "etfs": [
          {"name": "512500 中证500ETF", "sentiment": "利好"},
          {"name": "159915 创业板ETF", "sentiment": "利好"},
          {"name": "512760 芯片ETF", "sentiment": "利好"}
        ],
        "stocks": ["美光科技", "西部数据", "长江存储"],
        "signal": "资金大幅流入科技股和新兴市场，风险偏好明显回升"
      }
    ],
    "a_level": [
      {
        "emoji": "🟡",
        "title": "医药板块掀涨停潮：港股创新药ETF暴涨超7%",
        "summary": "医药生物板块领涨两市，港股创新药ETF暴涨超7%，A股多股涨停。",
        "duration": "1-2周",
        "etfs": [{"name": "159992 创新药产业ETF", "sentiment": "利好"}],
        "stocks": ["广生堂", "睿智医药", "凯莱英", "昂利康", "海欣股份"],
        "signal": "资金大幅流入医药板块，超跌反弹叠加创新药出海逻辑"
      },
      {
        "emoji": "🟡",
        "title": "SpaceX载人飞船发射成功，6月IPO在即",
        "summary": "美国SpaceX载人飞船搭载4名宇航员发射升空。SpaceX已秘密提交IPO申请。",
        "duration": "1-2周",
        "etfs": [{"name": "515980 云计算与大数据ETF", "sentiment": "利好"}],
        "stocks": [],
        "signal": "航天概念股关注度提升"
      },
      {
        "emoji": "🟡",
        "title": "小鹏汽车单季度盈利，全力押注AI",
        "summary": "小鹏汽车实现单季度盈利，将盈利归因于AI智驾技术商业化突破。",
        "duration": "2-3个月",
        "etfs": [{"name": "515700 新能源ETF", "sentiment": "利好"}],
        "stocks": ["小鹏汽车"],
        "signal": "新能源车板块情绪改善"
      },
      {
        "emoji": "🟡",
        "title": "比亚迪冲刺海外年销150万辆",
        "summary": "比亚迪2026年海外销量目标锁定150万辆，重点布局东南亚、欧洲、中东市场。",
        "duration": "3-6个月",
        "etfs": [{"name": "515700 新能源ETF", "sentiment": "利好"}],
        "stocks": ["比亚迪"],
        "signal": "新能源龙头出海逻辑持续"
      },
      {
        "emoji": "🟡",
        "title": "台积电计划2028年在日本生产3nm芯片",
        "summary": "台积电宣布将在日本工厂于2028年开始生产3nm先进制程芯片。",
        "duration": "1-2年",
        "etfs": [{"name": "512760 芯片ETF", "sentiment": "利好"}],
        "stocks": ["中芯国际"],
        "signal": "半导体国产替代逻辑强化"
      },
      {
        "emoji": "🟡",
        "title": "水泥巨头业绩雪崩，海螺水泥巨亏72亿",
        "summary": "水泥行业景气度持续低迷，海螺水泥等巨头年报出现巨额亏损。",
        "duration": "6-12个月",
        "etfs": [],
        "stocks": ["海螺水泥", "华新水泥"],
        "signal": "周期股业绩压力持续释放"
      }
    ],
    "douyin": [
      {
        "emoji": "📱",
        "title": "SpaceX IPO消息刷屏：马斯克1.75万亿美元超级独角兽",
        "summary": "SpaceX IPO消息在社交媒体引发热议。",
        "duration": "1-2周",
        "etfs": [],
        "stocks": [],
        "signal": "社交媒体情绪高涨，但实际A股映射有限"
      }
    ]
  },
  "2026-03-31": {
    "date": "2026-03-31",
    "market_tone": "市场震荡分化，机器人概念持续活跃，新能源赛道修复反弹",
    "s_level": [
      {
        "emoji": "🔴",
        "title": "人形机器人产业加速跑，OpenAI重启机器人部门",
        "summary": "OpenAI重新组建机器人部门；特斯拉公布2026年人形机器人量产目标5万台",
        "duration": "3-12月",
        "etfs": [
          {"name": "159770 机器人ETF", "sentiment": "利好"},
          {"name": "159819 人工智能ETF", "sentiment": "利好"}
        ],
        "stocks": ["003021 兆威机电", "002031 巨轮智能"],
        "signal": "AI+机器人融合加速，产业落地预期强烈"
      },
      {
        "emoji": "🔴",
        "title": "宁德时代发布骁遥电池，钠锂混合技术突破",
        "summary": "宁德时代发布骁遥电池；国内首条全固态锂电池量产线正式投产",
        "duration": "6-12月",
        "etfs": [
          {"name": "159755 电池ETF", "sentiment": "利好"},
          {"name": "159863 光伏ETF", "sentiment": "利好"}
        ],
        "stocks": ["300750 宁德时代", "601012 隆基绿能"],
        "signal": "电池技术迭代加速，新能源赛道估值修复"
      }
    ],
    "a_level": [
      {
        "emoji": "🟡",
        "title": "大金融板块集体走强，保险券商领涨",
        "summary": "银行、保险、券商等大金融板块震荡走强",
        "duration": "1-4周",
        "etfs": [
          {"name": "512880 银行ETF", "sentiment": "利好"},
          {"name": "512900 证券ETF", "sentiment": "利好"}
        ],
        "stocks": ["601318 中国平安", "601628 中国人寿"],
        "signal": "估值低位叠加政策预期，金融板块或迎来修复行情"
      }
    ],
    "douyin": [
      {
        "emoji": "📱",
        "title": "机器人概念股逆势爆发，十余股涨停",
        "summary": "机器人板块持续火热",
        "duration": "1-2周",
        "etfs": [{"name": "159770 机器人ETF", "sentiment": "利好"}],
        "stocks": ["003021 兆威机电", "002031 巨轮智能"],
        "signal": "机器人概念火爆，短线资金追捧"
      }
    ]
  },
  "2026-03-30": {
    "date": "2026-03-30",
    "market_tone": "市场观望情绪浓厚，权重股表现平淡，科技股局部活跃",
    "s_level": [],
    "a_level": [
      {
        "emoji": "📱",
        "title": "TCL科技等在深圳成立创新科技技术公司",
        "summary": "TCL科技牵头成立创新科技技术公司，布局前沿技术领域",
        "duration": "1-6月",
        "etfs": [{"name": "159819 人工智能", "sentiment": "利好"}],
        "stocks": ["000100 TCL科技"],
        "signal": "科技股研发加码，关注前沿技术布局"
      }
    ],
    "douyin": []
  },
  "2026-03-29": {
    "date": "2026-03-29",
    "market_tone": "中东地缘风险主导市场，霍尔木兹海峡局势升温",
    "s_level": [
      {
        "emoji": "🔥",
        "title": "霍尔木兹海峡局势升温，原油/能源板块全线暴涨",
        "summary": "地缘冲突升级，原油期货大涨",
        "duration": "1-3天",
        "etfs": [
          {"name": "159627 能源化工", "sentiment": "利好"},
          {"name": "518880 黄金ETF", "sentiment": "利好"}
        ],
        "stocks": ["600028 中国石化", "601857 中国石油"],
        "signal": "避险资金流入能源/黄金"
      }
    ],
    "a_level": [
      {
        "emoji": "🚗",
        "title": "比亚迪2025年营收达8040亿",
        "summary": "比亚迪2025年营收8040亿元，境外业务增长40%",
        "duration": "1-2个月",
        "etfs": [{"name": "159825 新能源车", "sentiment": "利好"}],
        "stocks": ["002594 比亚迪"],
        "signal": "新能源车龙头业绩超预期"
      }
    ],
    "douyin": [
      {
        "emoji": "📱",
        "title": "月之暗面冲刺IPO",
        "summary": "月之暗面（Kimi）冲刺IPO，AI大模型竞争进入商业化定价阶段",
        "duration": "1-2个月",
        "etfs": [{"name": "159819 人工智能", "sentiment": "利好"}],
        "stocks": [],
        "signal": "AI大模型商业化加速"
      }
    ]
  },
  "2026-03-28": {
    "date": "2026-03-28",
    "market_tone": "A股低开低走，科技股领跌，消费板块抗跌",
    "s_level": [
      {
        "emoji": "📉",
        "title": "美联储鹰派言论引发全球股市下跌",
        "summary": "美联储官员释放鹰派信号，全球股市普遍下跌",
        "duration": "2-3天",
        "etfs": [
          {"name": "159995 科技ETF", "sentiment": "利空"},
          {"name": "512480 芯片ETF", "sentiment": "利空"}
        ],
        "stocks": ["300750 宁德时代", "688012 中芯国际"],
        "signal": "外部风险冲击，避险情绪升温"
      }
    ],
    "a_level": [],
    "douyin": []
  },
  "2026-03-27": {
    "date": "2026-03-27",
    "market_tone": "A股反弹，金融股领涨，房地产板块止跌企稳",
    "s_level": [
      {
        "emoji": "📈",
        "title": "金融股集体上涨，银行/保险板块领涨超2%",
        "summary": "金融股全线上涨，银行、保险等板块领涨",
        "duration": "2-3天",
        "etfs": [
          {"name": "512800 银行ETF", "sentiment": "利好"},
          {"name": "512070 保险ETF", "sentiment": "利好"}
        ],
        "stocks": ["601398 工商银行", "601988 中国银行"],
        "signal": "金融股估值修复，机构看好"
      }
    ],
    "a_level": [],
    "douyin": []
  },
  "2026-03-26": {
    "date": "2026-03-26",
    "market_tone": "A股低开低走，市场风险偏好下降",
    "s_level": [],
    "a_level": [],
    "douyin": []
  },
  "2026-03-25": {
    "date": "2026-03-25",
    "market_tone": "A股高开高走，科技股领涨，市场情绪乐观",
    "s_level": [
      {
        "emoji": "🚀",
        "title": "AI概念股爆发，科技龙头股价创新高",
        "summary": "AI概念股集体上涨，科技龙头股价创新高",
        "duration": "1-2周",
        "etfs": [
          {"name": "159819 人工智能", "sentiment": "利好"},
          {"name": "512480 芯片ETF", "sentiment": "利好"}
        ],
        "stocks": ["688008 澜起科技", "688012 中芯国际"],
        "signal": "AI热点持续，科技股领涨"
      }
    ],
    "a_level": [],
    "douyin": []
  }
};

// 获取所有可用日期
const availableDates = ["2026-04-02", "2026-04-01", "2026-03-31", "2026-03-30", "2026-03-29", "2026-03-28", "2026-03-27", "2026-03-26", "2026-03-25"];

// 获取指定日期的新闻
function getNews(date) {
    return newsData[date] || null;
}

// 获取前一天
function getPreviousDate(date) {
    const idx = availableDates.indexOf(date);
    return idx > 0 ? availableDates[idx - 1] : null;
}

// 获取后一天
function getNextDate(date) {
    const idx = availableDates.indexOf(date);
    return idx < availableDates.length - 1 ? availableDates[idx + 1] : null;
}
