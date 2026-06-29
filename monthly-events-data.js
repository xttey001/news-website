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
				"date": "2026-06-01",
				"title": "指数样本调整生效",
				"type": "市场事件",
				"impact_level": "A级",
				"description": "沪深300、科创50等指数样本调整生效，数千亿被动资金调仓",
				"affected_sectors": ["调入个股", "调出个股", "ETF"],
				"market_implication": "被动调仓放大波动，调入个股获资金流入",
				"wukong_factor": {
					"risk_definition": "中性",
					"reason": "调仓影响短期，不改变中期趋势",
					"strategy": "关注调入个股机会，回避调出个股抛压"
				},
				"bajie_factor": {
					"probability": 60,
					"confidence": "中",
					"expected_return": "调入+1%~+3%，调出-2%~-5%"
				}
			},
			{
				"date": "2026-06-02",
				"title": "台北电脑展开幕",
				"type": "产业事件",
				"impact_level": "A级",
				"description": "全球最大科技盛会之一，英伟达、AMD、台积电等巨头参会，发布AI芯片新品",
				"affected_sectors": ["AI芯片", "半导体", "PC产业链"],
				"market_implication": "AI硬件创新周期，关注新品超预期程度",
				"wukong_factor": {
					"risk_definition": "中性",
					"reason": "创新预期已高，需警惕不及预期",
					"strategy": "关注新品发布，精选受益标的"
				},
				"bajie_factor": {
					"probability": 55,
					"confidence": "中",
					"expected_return": "+1%~+3%"
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
	},
	"2026-07": {
		"month": "2026年7月",
		"theme": "半年报验证+央行超级周+政治局会议",
		"overview": "7月进入半年报集中披露期，业绩验证成为核心主线；同时迎来央行超级周、美联储议息会议和政治局会议，多重因素交织下市场波动加大",
		"events": [
			{
				"date": "2026-06-29~07-01",
				"title": "葡萄牙辛特拉央行论坛",
				"type": "宏观政策",
				"impact_level": "S级",
				"description": "美联储主席、欧央行行长拉加德、英央行行长贝利等全球主要央行决策者集中发表讲话，定调下半年货币政策路径",
				"affected_sectors": ["全球股市", "黄金", "美元", "北向资金重仓股"],
				"market_implication": "全球流动性预期关键定价窗口，影响北向资金流向和成长股估值",
				"wukong_factor": {
					"risk_definition": "待观察",
					"reason": "鹰派表态将压制高估值成长股，鸽派表态将提振风险偏好",
					"strategy": "论坛期间控制仓位，关注美元指数和美债收益率变化"
				},
				"bajie_factor": {
					"probability": 55,
					"confidence": "中",
					"expected_return": "±2%"
				}
			},
			{
				"date": "2026-07-02",
				"title": "美国6月非农就业数据",
				"type": "宏观数据",
				"impact_level": "S级",
				"description": "美国6月非农就业人口、失业率数据发布，直接影响美联储7月议息决策",
				"affected_sectors": ["纳指", "黄金", "新兴市场", "美元"],
				"market_implication": "数据强劲将强化加息预期，数据疲软将提振降息预期",
				"wukong_factor": {
					"risk_definition": "待观察",
					"reason": "就业数据是美联储政策决策的核心指标之一",
					"strategy": "数据公布前不开新仓，数据落地后根据市场反应调整"
				},
				"bajie_factor": {
					"probability": 50,
					"confidence": "中",
					"expected_return": "±3%"
				}
			},
			{
				"date": "2026-07-04",
				"title": "美国独立日假期",
				"type": "市场事件",
				"impact_level": "B级",
				"description": "美国市场休市，A股受外围扰动减小，关注国内政策面消息",
				"affected_sectors": ["全市场"],
				"market_implication": "外围休市期间A股有望走出独立行情",
				"wukong_factor": {
					"risk_definition": "中性",
					"reason": "假期影响短期交易，不改变中期趋势",
					"strategy": "利用外围休市窗口关注国内政策信号"
				},
				"bajie_factor": {
					"probability": 50,
					"confidence": "低",
					"expected_return": "±1%"
				}
			},
			{
				"date": "2026-07-15",
				"title": "半年报预告强制披露截止日",
				"type": "业绩事件",
				"impact_level": "S级",
				"description": "沪深主板企业净利润大幅变动、亏损、扭亏必须在此日前发布预告，是半年报业绩雷集中释放窗口",
				"affected_sectors": ["全市场", "ST板块", "绩差股", "高位题材股"],
				"market_implication": "业绩暴雷集中释放，题材股承压，绩优股获资金追捧",
				"wukong_factor": {
					"risk_definition": "高风险窗口",
					"reason": "垃圾财报扎堆最后截止日，无基本面支撑的小票杀估值",
					"strategy": "回避无业绩支撑的高位题材股，保留订单充足、提前预增的核心龙头"
				},
				"bajie_factor": {
					"probability": 75,
					"confidence": "高",
					"expected_return": "绩优+1%~+3%，绩差-5%~-15%"
				}
			},
			{
				"date": "2026-07下旬",
				"title": "中央政治局会议",
				"type": "政策事件",
				"impact_level": "S级",
				"description": "年中政治局会议，定调下半年经济政策方向，关注财政政策、货币政策、地产政策表述变化",
				"affected_sectors": ["基建", "地产", "金融", "科技", "消费"],
				"market_implication": "政策方向决定下半年市场主线，超预期政策将提振市场信心",
				"wukong_factor": {
					"risk_definition": "待观察",
					"reason": "政策表述变化是关键，超预期利好将带来结构性机会",
					"strategy": "会议前保持中性仓位，关注政策受益方向"
				},
				"bajie_factor": {
					"probability": 60,
					"confidence": "中",
					"expected_return": "+2%~+5%"
				}
			},
			{
				"date": "2026-07-28~07-29",
				"title": "美联储7月议息会议",
				"type": "宏观政策",
				"impact_level": "S级",
				"description": "美联储7月利率决议，北京时间7月30日凌晨公布，主席沃什新闻发布会定调后续政策路径",
				"affected_sectors": ["纳指", "黄金", "北向资金重仓股", "成长股"],
				"market_implication": "下半年首次重要议息会议，决定全球流动性拐点",
				"wukong_factor": {
					"risk_definition": "高波动窗口",
					"reason": "叠加半年报披露中期窗口，多空博弈剧烈",
					"strategy": "决议公布前控制仓位在5成以内，回避北向重仓高估值赛道"
				},
				"bajie_factor": {
					"probability": 50,
					"confidence": "中",
					"expected_return": "±3%"
				}
			},
			{
				"date": "2026-07全月",
				"title": "半年报正式披露期",
				"type": "业绩事件",
				"impact_level": "A级",
				"description": "上市公司陆续披露半年报正式报告，市场从'炒预期'切换为'验业绩'",
				"affected_sectors": ["全市场"],
				"market_implication": "业绩驱动行情，业绩超预期标的获资金持续流入",
				"wukong_factor": {
					"risk_definition": "结构性机会",
					"reason": "业绩确定性成为核心，真成长脱颖而出",
					"strategy": "聚焦业绩超预期板块和个股，回避业绩雷区"
				},
				"bajie_factor": {
					"probability": 70,
					"confidence": "中高",
					"expected_return": "绩优+3%~+10%，绩差-3%~-10%"
				}
			}
		],
		"monthly_summary": {
			"key_themes": ["半年报验证", "央行超级周", "政治局会议", "美联储议息"],
			"risk_factors": ["业绩暴雷", "美联储鹰派", "政策不及预期", "机构止盈"],
			"opportunity_sectors": ["半年报超预期", "高股息防御", "政策受益板块"],
			"overall_outlook": "业绩验证期，严控仓位，精选确定性机会"
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
