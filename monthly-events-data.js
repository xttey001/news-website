// 每月重大事件数据 - 作为五维智能体分析的衡量因子
// 更新时间: 2026-05-18
// 说明: 提前总结每月重大事件，用于综合裁量和投资决策参考

const monthlyEventsData = {
	"2026-05": {
		"month": "2026年5月",
		"theme": "中美经贸磋商+业绩驱动",
		"overview": "5月市场聚焦中美经贸磋商进展、存储芯片业绩爆发、以及政策催化下的结构性机会",
		"events": [
			{
				"date": "2026-05-18",
				"title": "中美经贸磋商初步成果公布",
				"type": "地缘政治",
				"impact_level": "S级",
				"description": "双方就关税安排形成积极共识，成立贸易理事会和投资理事会，推动扩大双向贸易",
				"affected_sectors": ["航空", "农产品", "出口链"],
				"market_implication": "贸易摩擦缓和，出口受益板块风险偏好修复",
				"wukong_factor": {
					"risk_definition": "假风险",
					"reason": "行政层面推动缓和，但需警惕利好兑现",
					"strategy": "逢低布局出口受益板块，不追高"
				},
				"bajie_factor": {
					"probability": 65,
					"confidence": "中",
					"expected_return": "+2%~+5%"
				}
			},
			{
				"date": "2026-05-18",
				"title": "长鑫科技业绩爆发",
				"type": "业绩事件",
				"impact_level": "S级",
				"description": "Q1净利润330亿元，同比增长1268%，上半年盈利指引增长超2200%",
				"affected_sectors": ["存储芯片", "半导体", "AI算力"],
				"market_implication": "存储芯片超级周期确认，国产替代加速",
				"wukong_factor": {
					"risk_definition": "真机会",
					"reason": "业绩验证产业趋势，非概念炒作",
					"strategy": "积极布局业绩确定性强的存储芯片板块"
				},
				"bajie_factor": {
					"probability": 85,
					"confidence": "高",
					"expected_return": "+5%~+15%"
				}
			},
			{
				"date": "2026-05-17",
				"title": "央行科创再贷款扩容至1.2万亿",
				"type": "货币政策",
				"impact_level": "S级",
				"description": "科技创新再贷款从5000亿扩容至1.2万亿，定向支持AI算力、半导体等14大硬科技领域",
				"affected_sectors": ["科创50", "芯片", "AI算力"],
				"market_implication": "硬科技政策底确立，流动性定向支持",
				"wukong_factor": {
					"risk_definition": "假机会",
					"reason": "政策利好密集发布，需警惕利好出尽",
					"strategy": "政策催化下逢低布局，不追高"
				},
				"bajie_factor": {
					"probability": 70,
					"confidence": "中高",
					"expected_return": "+3%~+8%"
				}
			},
			{
				"date": "2026-05-17",
				"title": "国常会定调7万亿新基建",
				"type": "财政政策",
				"impact_level": "A级",
				"description": "聚焦'六张网'（水网、电网、算力网、通信网、地下管网、物流网），算力网首次纳入",
				"affected_sectors": ["算力基建", "通信", "基建"],
				"market_implication": "算力基建迎来政策强力支持",
				"wukong_factor": {
					"risk_definition": "中性",
					"reason": "政策利好但落地需要时间",
					"strategy": "关注项目落地进度，精选受益标的"
				},
				"bajie_factor": {
					"probability": 60,
					"confidence": "中",
					"expected_return": "+2%~+6%"
				}
			},
			{
				"date": "2026-05-15",
				"title": "央行降准释放1万亿流动性",
				"type": "货币政策",
				"impact_level": "A级",
				"description": "降准1万亿释放长期流动性，支持实体经济发展",
				"affected_sectors": ["金融", "地产", "宽基指数"],
				"market_implication": "市场流动性保持充裕，宽信用环境延续",
				"wukong_factor": {
					"risk_definition": "中性",
					"reason": "预期内政策，市场已部分price in",
					"strategy": "关注资金流向，精选受益板块"
				},
				"bajie_factor": {
					"probability": 55,
					"confidence": "中",
					"expected_return": "+0.5%~+2%"
				}
			},
			{
				"date": "2026-05-20",
				"title": "英伟达财报发布",
				"type": "业绩事件",
				"impact_level": "S级",
				"description": "全球AI芯片龙头财报，指引AI算力需求趋势",
				"affected_sectors": ["AI芯片", "算力", "科技股"],
				"market_implication": "全球AI产业链风向标",
				"wukong_factor": {
					"risk_definition": "待观察",
					"reason": "业绩预期已高，需警惕不及预期风险",
					"strategy": "财报前控制仓位，财报后根据指引调整"
				},
				"bajie_factor": {
					"probability": 50,
					"confidence": "低",
					"expected_return": "±3%"
				}
			},
			{
				"date": "2026-05-25",
				"title": "美联储5月议息会议",
				"type": "宏观政策",
				"impact_level": "S级",
				"description": "美联储利率决议及 Powell 讲话，影响全球流动性预期",
				"affected_sectors": ["纳指", "黄金", "新兴市场"],
				"market_implication": "全球流动性拐点信号",
				"wukong_factor": {
					"risk_definition": "待观察",
					"reason": "降息预期已部分price in，关注点阵图指引",
					"strategy": "会议前控制仓位，关注美元指数变化"
				},
				"bajie_factor": {
					"probability": 45,
					"confidence": "低",
					"expected_return": "±2%"
				}
			}
		],
		"monthly_summary": {
			"key_themes": ["中美经贸", "存储芯片业绩", "政策催化"],
			"risk_factors": ["美股波动", "美联储政策", "地缘政治"],
			"opportunity_sectors": ["存储芯片", "AI算力", "出口受益"],
			"overall_outlook": "结构性机会为主，关注业绩验证和政策落地"
		}
	},
	"2026-06": {
		"month": "2026年6月",
		"theme": "半年报预告+政策窗口期",
		"overview": "6月进入半年报预告期，业绩确定性成为主线；同时关注政策窗口期的结构性机会",
		"events": [
			{
				"date": "2026-06-01",
				"title": "半年报预告期开启",
				"type": "业绩事件",
				"impact_level": "S级",
				"description": "上市公司开始披露半年报业绩预告，业绩确定性成为市场主线",
				"affected_sectors": ["全市场"],
				"market_implication": "业绩驱动行情，绩优股受追捧",
				"wukong_factor": {
					"risk_definition": "真机会",
					"reason": "业绩验证期，真成长脱颖而出",
					"strategy": "提前布局业绩超预期标的，回避业绩雷区"
				},
				"bajie_factor": {
					"probability": 70,
					"confidence": "中高",
					"expected_return": "+3%~+10%"
				}
			},
			{
				"date": "2026-06-15",
				"title": "苹果WWDC大会",
				"type": "产业事件",
				"impact_level": "A级",
				"description": "苹果全球开发者大会，关注AI功能集成和新品发布",
				"affected_sectors": ["苹果产业链", "消费电子", "AI应用"],
				"market_implication": "消费电子创新周期，AI应用落地",
				"wukong_factor": {
					"risk_definition": "中性",
					"reason": "创新预期已高，需警惕不及预期",
					"strategy": "关注AI功能落地进展，精选产业链受益标的"
				},
				"bajie_factor": {
					"probability": 55,
					"confidence": "中",
					"expected_return": "+2%~+5%"
				}
			},
			{
				"date": "2026-06-18",
				"title": "美联储6月议息会议",
				"type": "宏观政策",
				"impact_level": "S级",
				"description": "美联储利率决议，关注降息路径指引",
				"affected_sectors": ["纳指", "黄金", "全球股市"],
				"market_implication": "全球流动性预期关键节点",
				"wukong_factor": {
					"risk_definition": "待观察",
					"reason": "降息时点存在不确定性",
					"strategy": "会议前控制仓位，关注点阵图变化"
				},
				"bajie_factor": {
					"probability": 50,
					"confidence": "低",
					"expected_return": "±3%"
				}
			},
			{
				"date": "2026-06-30",
				"title": "半年度收官",
				"type": "市场事件",
				"impact_level": "A级",
				"description": "半年度最后一个交易日，基金调仓、业绩排名影响市场",
				"affected_sectors": ["全市场"],
				"market_implication": "资金面波动，风格切换风险",
				"wukong_factor": {
					"risk_definition": "中性",
					"reason": "调仓影响短期，不改变中期趋势",
					"strategy": "回避机构重仓股调仓压力，关注半年报超预期标的"
				},
				"bajie_factor": {
					"probability": 50,
					"confidence": "中",
					"expected_return": "±2%"
				}
			}
		],
		"monthly_summary": {
			"key_themes": ["半年报预告", "苹果WWDC", "美联储政策"],
			"risk_factors": ["业绩不及预期", "美联储鹰派", "地缘政治"],
			"opportunity_sectors": ["业绩超预期", "苹果产业链", "AI应用"],
			"overall_outlook": "业绩为王，关注确定性机会"
		}
	}
}

// 获取指定月份的事件数据
function getMonthlyEvents(yearMonth) {
	return monthlyEventsData[yearMonth] || null
}

// 获取所有可用月份列表
function getAvailableMonths() {
	return Object.keys(monthlyEventsData).sort().reverse()
}

// 获取事件影响因子（用于五维智能体分析）
function getEventImpactFactor(yearMonth, eventType) {
	const monthData = monthlyEventsData[yearMonth]
	if (!monthData) return null
	
	const events = monthData.events.filter(e => e.type === eventType)
	if (events.length === 0) return null
	
	// 计算平均影响概率
	const avgProbability = events.reduce((sum, e) => sum + e.bajie_factor.probability, 0) / events.length
	const avgExpectedReturn = events.map(e => e.bajie_factor.expected_return)
	
	return {
		"event_count": events.length,
		"avg_probability": avgProbability,
		"expected_returns": avgExpectedReturn,
		"events": events.map(e => ({
			"title": e.title,
			"impact_level": e.impact_level,
			"probability": e.bajie_factor.probability,
			"wukong_factor": e.wukong_factor
		}))
	}
}

// 导出数据供其他模块使用
if (typeof module !== "undefined" && module.exports) {
	module.exports = { monthlyEventsData, getMonthlyEvents, getAvailableMonths, getEventImpactFactor }
}
