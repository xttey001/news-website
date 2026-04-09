// 财经新闻数据 - 2026-04-09 测试版
const newsData = {
  "2026-04-09": {
    "date": "2026-04-09",
    "market_tone": "科技股持续强势，AI芯片继续爆发",
    "wukong_judgment": {
      "market_sentiment": "积极做多",
      "core_analysis": [
        "AI芯片板块持续爆发，龙头股继续涨停",
        "市场情绪高涨，但需注意追高风险"
      ],
      "operations": [
        {"type": "可以做", "content": "AI芯片/光模块：关注回调机会"},
        {"type": "警惕", "content": "涨幅过大，注意回调风险"}
      ]
    },
    "bajie_conclusion": {
      "optimal_action": "重点配置AI芯片+人工智能ETF，科技股持续看涨",
      "optimal_etfs": "588890科创芯片ETF(40%) + 512930 AI人工智能ETF(30%) + 现金(30%)",
      "win_rate": "~70%",
      "max_drawdown": "-5%"
    },
    "s_level": [
      {
        "emoji": "🔴",
        "title": "AI芯片/半导体板块暴涨，创业板人工智能ETF涨超7%",
        "summary": "科创芯片ETF涨超5%，创业板AI ETF涨超7%，中际旭创涨停，光模块继续涨",
        "duration": "1-2周",
        "etfs": [
          {"name": "588890 科创芯片ETF", "sentiment": "利好"},
          {"name": "512930 AI人工智能ETF", "sentiment": "利好"},
          {"name": "512760 芯片ETF", "sentiment": "利好"}
        ],
        "stocks": ["中际旭创", "新易盛", "天孚通信"],
        "signal": "主力资金流入科技板块，短期做多情绪高涨"
      }
    ],
    "a_level": [],
    "douyin": [],
    // 沙僧模块
    "sangsha_module": {
      "overall_sentiment": "积极",
      "advice": "可适度参与，但需谨慎",
      "avg_buy_prob": 55,
      "avg_panic_prob": 5,
      "analysis_results": [
        {
          "news": "COMEX黄金突破70000美元创历史新高",
          "title": "COMEX黄金突破70000美元创历史新高",
          "full_title": "COMEX黄金突破70000美元创历史新高",
          "summary": "黄金创历史新高",
          "追高买入概率": 81,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 64,
          "情绪标签": ["FOMO"],
          "韭菜行为总结": "散户疯了，都在追！",
          "市场含义": "顶部风险",
          "买入概率": 51,
          "is_long_term": true,
          "date": "2026-04-07",
          "decay": 1.0,
          "weighted_buy_prob": 51
        },
        {
          "news": "AI芯片暴涨，创业板AI ETF涨超7%",
          "title": "AI芯片暴涨，创业板AI ETF涨超7%",
          "full_title": "AI芯片/半导体板块暴涨，创业板人工智能ETF涨超7%",
          "summary": "科创芯片ETF涨停",
          "追高买入概率": 95,
          "抄底买入概率": 5,
          "恐慌卖出概率": 5,
          "观望概率": 59,
          "情绪标签": ["FOMO", "易懂"],
          "韭菜行为总结": "散户疯了，都在追！",
          "市场含义": "顶部风险",
          "买入概率": 59,
          "is_long_term": false,
          "date": "2026-04-09",
          "decay": 1.0,
          "weighted_buy_prob": 59
        }
      ],
      "time_window": "7天累积（长期新闻除外）"
    },
    // 白龙马模块
    "white_dragon": {
      "主力状态": "分化",
      "阶段": "观察",
      "行为解释": "各ETF分化明显，需要精选标的",
      "是否利用散户": false,
      "综合建议": "📊 观望为主：市场方向不明，建议轻仓观望",
      "散户情绪": {
        "平均买入概率": 55,
        "平均恐慌概率": 5
      }
    }
  }
};

// 可用日期列表（从新到旧）
const availableDates = ["2026-04-09"];

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