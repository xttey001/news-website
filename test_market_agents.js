const marketAgentsOutput = {
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
        "情绪标签": [
          "FOMO"
        ],
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
        "full_title": "AI芯片暴涨，创业板AI ETF涨超7%",
        "summary": "科创芯片ETF涨停，中际旭创涨停",
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
        "date": "2026-04-08",
        "decay": 0.7,
        "weighted_buy_prob": 41
      }
    ],
    "time_window": "7天累积（长期新闻除外）"
  },
  "white_dragon": {
    "主力状态": "分化",
    "阶段": "观察",
    "行为解释": "各ETF分化明显，需要精选标的",
    "是否利用散户": false,
    "散户情绪": {
      "平均买入概率": 55,
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
        "fund_flow": {
          "trend": "side",
          "net_amt": 0,
          "days": 0
        },
        "主力状态": "观望",
        "阶段": "整理",
        "行为解释": "多空平衡，观望为主",
        "是否利用散户": false,
        "sangsha_buy_prob": 55,
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
        "fund_flow": {
          "trend": "side",
          "net_amt": 0,
          "days": 0
        },
        "主力状态": "观望",
        "阶段": "整理",
        "行为解释": "多空平衡，观望为主",
        "是否利用散户": false,
        "sangsha_buy_prob": 55,
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
        "fund_flow": {
          "trend": "side",
          "net_amt": 0,
          "days": 0
        },
        "主力状态": "观望",
        "阶段": "整理",
        "行为解释": "价格横盘震荡，等待方向选择",
        "是否利用散户": false,
        "sangsha_buy_prob": 55,
        "sangsha_panic_prob": 5
      }
    ],
    "综合建议": "📊 观望为主：市场方向不明，建议轻仓观望"
  }
};
