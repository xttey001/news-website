// 宏观因子数据 - 全球主要宏观指标
// 更新时间: 2026-05-18
// 说明: 存储美元指数、美债利率、汇率等宏观因子数据

const macroData = {
	"last_update": "2026-05-18 15:30:00",
	"data_source": "TradingView / 公开市场数据",
	
	"indicators": {
		"dxy": {
			"name": "美元指数",
			"symbol": "DXY",
			"category": "美元流动性",
			"value": 99.85,
			"change": -0.15,
			"change_percent": -0.15,
			"trend": "down",
			"level": "neutral",
			"description": "衡量美元对一篮子主要货币的强弱程度",
			"thresholds": {
				"strong": 103,
				"neutral_high": 100,
				"neutral_low": 97,
				"weak": 95
			},
			"market_implication": {
				"high": "美元强势，压制新兴市场和大宗商品",
				"neutral": "美元震荡，关注突破方向",
				"low": "美元弱势，利好新兴市场和大宗商品"
			},
			"wukong_factor": {
				"current_assessment": "美元指数在100附近震荡，处于中性区间",
				"risk_signal": "中性",
				"strategy": "关注99-101区间的突破方向"
			}
		},
		
		"us10y": {
			"name": "美债10年期收益率",
			"symbol": "US10Y",
			"category": "全球无风险利率",
			"value": 4.42,
			"change": 0.03,
			"change_percent": 0.68,
			"trend": "up",
			"level": "high",
			"description": "全球资产定价的锚，影响全球资金成本",
			"thresholds": {
				"very_high": 4.5,
				"high": 4.0,
				"neutral": 3.5,
				"low": 3.0
			},
			"market_implication": {
				"very_high": "压制成长股估值，利好价值股",
				"high": "对科技股形成压力",
				"neutral": "估值环境相对友好",
				"low": "利好成长股和风险资产"
			},
			"wukong_factor": {
				"current_assessment": "10Y收益率在4.4%高位，对科技股估值形成压制",
				"risk_signal": "⚠️ 偏高",
				"strategy": "控制科技股仓位，关注美联储政策转向信号"
			}
		},
		
		"us02y": {
			"name": "美债2年期收益率",
			"symbol": "US02Y",
			"category": "短期利率预期",
			"value": 4.02,
			"change": 0.02,
			"change_percent": 0.50,
			"trend": "up",
			"level": "neutral",
			"description": "反映市场对未来2年利率走势的预期",
			"spread_10y_2y": 0.40,
			"wukong_factor": {
				"current_assessment": "2Y-10Y利差40bp，曲线陡峭化",
				"risk_signal": "中性偏多",
				"strategy": "利差扩大利好银行板块"
			}
		},
		
		"usdjpy": {
			"name": "美元兑日元",
			"symbol": "USDJPY",
			"category": "套息交易",
			"value": 143.25,
			"change": -0.45,
			"change_percent": -0.31,
			"trend": "down",
			"level": "neutral",
			"description": "反映美日利差和套息交易活跃度",
			"thresholds": {
				"very_high": 150,
				"high": 145,
				"neutral": 140,
				"low": 135
			},
			"market_implication": {
				"very_high": "套息交易活跃，日元贬值压力大",
				"high": "日元偏弱，关注日本干预",
				"neutral": "汇率相对稳定",
				"low": "日元走强，套息交易 unwind"
			},
			"wukong_factor": {
				"current_assessment": "USDJPY在143附近，较前期高点回落",
				"risk_signal": "中性",
				"strategy": "关注145阻力位和140支撑位"
			}
		},
		
		"usdcnh": {
			"name": "美元兑离岸人民币",
			"symbol": "USDCNH",
			"category": "人民币汇率",
			"value": 7.1950,
			"change": 0.0080,
			"change_percent": 0.11,
			"trend": "up",
			"level": "neutral",
			"description": "离岸人民币汇率，反映外资对人民币资产态度",
			"thresholds": {
				"very_high": 7.30,
				"high": 7.20,
				"neutral": 7.10,
				"low": 7.00
			},
			"market_implication": {
				"very_high": "人民币贬值压力大，资本外流风险",
				"high": "人民币偏弱，关注央行干预",
				"neutral": "汇率相对稳定",
				"low": "人民币强势，利好外资流入"
			},
			"wukong_factor": {
				"current_assessment": "USDCNH在7.20附近，人民币小幅贬值",
				"risk_signal": "中性",
				"strategy": "关注7.30关键阻力位"
			}
		},
		
		"gold": {
			"name": "现货黄金",
			"symbol": "XAUUSD",
			"category": "避险资产",
			"value": 3280.50,
			"change": 15.30,
			"change_percent": 0.47,
			"trend": "up",
			"level": "high",
			"description": "传统避险资产，与美元负相关",
			"thresholds": {
				"very_high": 3300,
				"high": 3000,
				"neutral": 2800,
				"low": 2600
			},
			"market_implication": {
				"very_high": "避险情绪浓厚，或预示风险资产调整",
				"high": "避险需求上升",
				"neutral": "正常波动区间",
				"low": "风险偏好回升"
			},
			"wukong_factor": {
				"current_assessment": "黄金突破3280，创历史新高",
				"risk_signal": "⚠️ 避险情绪升温",
				"strategy": "黄金新高提示避险情绪，需警惕风险资产回调"
			}
		},
		
		"crude_oil": {
			"name": "WTI原油",
			"symbol": "USOIL",
			"category": "大宗商品",
			"value": 62.35,
			"change": -0.85,
			"change_percent": -1.35,
			"trend": "down",
			"level": "low",
			"description": "全球经济增长和通胀预期的风向标",
			"thresholds": {
				"very_high": 90,
				"high": 80,
				"neutral": 70,
				"low": 60
			},
			"market_implication": {
				"very_high": "通胀压力上升，利好能源股",
				"high": "经济需求强劲",
				"neutral": "供需相对平衡",
				"low": "经济增长担忧，通缩风险"
			},
			"wukong_factor": {
				"current_assessment": "原油跌破65，处于低位区间",
				"risk_signal": "⚠️ 偏低",
				"strategy": "油价低迷反映需求担忧，关注OPEC+政策"
			}
		},
		
		"vix": {
			"name": "VIX恐慌指数",
			"symbol": "VIX",
			"category": "市场情绪",
			"value": 18.50,
			"change": 0.80,
			"change_percent": 4.52,
			"trend": "up",
			"level": "neutral",
			"description": "衡量美股市场波动率和恐慌程度",
			"thresholds": {
				"extreme_fear": 30,
				"fear": 25,
				"neutral": 20,
				"greed": 15
			},
			"market_implication": {
				"extreme_fear": "极度恐慌，逆向买入机会",
				"fear": "市场恐慌，关注超跌反弹",
				"neutral": "情绪正常",
				"greed": "市场贪婪，警惕回调"
			},
			"wukong_factor": {
				"current_assessment": "VIX在18.5，处于中性区间",
				"risk_signal": "中性",
				"strategy": "市场情绪平稳，关注VIX突破20的信号"
			}
		},
		
		"btc": {
			"name": "比特币",
			"symbol": "BTCUSD",
			"category": "风险偏好",
			"value": 104250.00,
			"change": 1250.00,
			"change_percent": 1.21,
			"trend": "up",
			"level": "high",
			"description": "风险资产风向标，反映市场流动性预期",
			"thresholds": {
				"very_high": 110000,
				"high": 100000,
				"neutral": 90000,
				"low": 80000
			},
			"market_implication": {
				"very_high": "风险偏好极高，流动性充裕",
				"high": "风险偏好回升",
				"neutral": "正常波动",
				"low": "风险偏好下降，避险需求上升"
			},
			"wukong_factor": {
				"current_assessment": "BTC在104k附近，风险偏好较高",
				"risk_signal": "中性偏多",
				"strategy": "BTC强势反映风险偏好回升，利好科技股"
			}
		}
	},
	
	"spreads": {
		"us10y_us02y": {
			"name": "美债10Y-2Y利差",
			"value": 0.40,
			"change": 0.01,
			"interpretation": "曲线陡峭化，经济扩张预期",
			"recession_signal": false
		},
		"us10y_jp10y": {
			"name": "美日10Y利差",
			"value": 3.85,
			"change": -0.02,
			"interpretation": "套息交易基础",
			"impact": "利差收窄不利于套息交易"
		},
		"gold_oil_ratio": {
			"name": "金油比",
			"value": 52.6,
			"change": 1.2,
			"interpretation": "避险情绪升温信号",
			"threshold": 25
		}
	},
	
	"composite_index": {
		"liquidity_score": 65,
		"risk_appetite_score": 70,
		"safe_haven_score": 75,
		"overall_assessment": "流动性中性偏紧，风险偏好较高，避险情绪升温",
		"wukong_conclusion": "宏观环境复杂：美债收益率高企压制科技股，黄金新高提示避险需求，BTC强势反映风险偏好分化。建议控制仓位，关注美联储政策转向信号。"
	}
}

// 获取指定指标数据
function getMacroIndicator(indicatorKey) {
	return macroData.indicators[indicatorKey] || null
}

// 获取所有指标
function getAllMacroIndicators() {
	return macroData.indicators
}

// 获取利差数据
function getSpreads() {
	return macroData.spreads
}

// 获取综合评估
function getCompositeIndex() {
	return macroData.composite_index
}

// 获取指标趋势
function getIndicatorTrend(indicatorKey) {
	const indicator = macroData.indicators[indicatorKey]
	if (!indicator) return null
	
	const trends = {
		"up": "📈 上升",
		"down": "📉 下降",
		"flat": "➡️ 平稳"
	}
	
	return {
		"trend": indicator.trend,
		"trend_text": trends[indicator.trend],
		"change": indicator.change,
		"change_percent": indicator.change_percent
	}
}

// 获取指标级别
function getIndicatorLevel(indicatorKey) {
	const indicator = macroData.indicators[indicatorKey]
	if (!indicator) return null
	
	const levels = {
		"very_high": "极高",
		"high": "偏高",
		"neutral": "中性",
		"low": "偏低",
		"very_low": "极低"
	}
	
	return levels[indicator.level] || "未知"
}

// 导出数据
if (typeof module !== "undefined" && module.exports) {
	module.exports = { macroData, getMacroIndicator, getAllMacroIndicators, getSpreads, getCompositeIndex }
}
