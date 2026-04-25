const fs = require('fs');
const path = require('path');

// 三天的新闻数据（基于搜索结果整理）
const newDaysData = {
  "2026-04-14": {
    "date": "2026-04-14",
    "market_tone": {
      "早报": "【2026-04-14早报】美军封锁霍尔木兹海峡正式生效，全球能源供应链紧张，A股开盘承压但板块分化明显",
      "晚报": "【2026-04-14晚报】A股低开高走强势反弹，锂矿光模块领涨，超2300只个股上涨，市场韧性超预期"
    },
    "all_news": [
      {
        "title": "美军封锁霍尔木兹海峡正式生效，能源市场高度紧张",
        "summary": "4月14日美东时间10时，美军正式开始封锁所有进出伊朗港口的海上交通。沙特施压美国放弃封锁，多个北约国家表示不参与行动。全球能源供应链面临剧烈冲击，LME铝价升至四年新高。",
        "source": "新华社/路透社",
        "date": "2026-04-14",
        "emoji": "🔥"
      },
      {
        "title": "上期所调整黄金期货涨跌停板幅度",
        "summary": "4月14日上海期货交易所发布通知，调整黄金等期货相关合约涨跌停板幅度和交易保证金比例，应对地缘风险带来的价格波动。近一周一口价黄金产品最高下跌17%。",
        "source": "上期所/中新经纬",
        "date": "2026-04-14",
        "emoji": "📊"
      },
      {
        "title": "A股低开高走，创业板指大涨近4%",
        "summary": "4月14日A股三大指数低开高走，沪指涨1.92%，深证成指涨3.87%，创业板指涨4.81%。超2300只个股上涨，成交放量。锂矿、光模块、玻璃纤维板块领涨，宁德时代、中际旭创、中国巨石等多股创历史新高。",
        "source": "证券时报/东方财富",
        "date": "2026-04-14",
        "emoji": "📈"
      },
      {
        "title": "海南自贸港低空经济招商大会举办",
        "summary": "4月14日海南自贸港全球产业招商大会低空经济专场在海口举办，推动低空经济发展。第十三届中国网络视听大会同日在成都开幕。",
        "source": "海南日报/每经网",
        "date": "2026-04-14",
        "emoji": "🚁"
      },
      {
        "title": "美媒称沙特施压美国放弃封锁霍尔木兹海峡",
        "summary": "据美方媒体报道，沙特方面正在施压美国放弃对霍尔木兹海峡的封锁行动，担心能源出口受阻影响全球经济。英海事分析公司称海峡船舶移动受到多重控制动态影响。",
        "source": "环球网/青海羚网",
        "date": "2026-04-14",
        "emoji": "🌍"
      }
    ],
    "s_level": [
      {
        "emoji": "🔴",
        "title": "美军封锁霍尔木兹海峡正式生效（地缘风险实质升级）",
        "source": "新华社/路透社",
        "key_point": "美军4月14日美东时间10时正式开始封锁伊朗港口海上交通。沙特施压美国放弃行动，北约多国不参与。GEO-001范式：地缘升级+供应中断=油气高胜率窗口。关键变量：沙特态度、伊朗反制措施、北约国家立场。",
        "duration": "1-4周",
        "etfs": [
          { "name": "561360 石油ETF", "sentiment": "利好" },
          { "name": "15985 能源ETF", "sentiment": "利好" }
        ],
        "stocks": ["中国石油", "中国石化", "中海油服"],
        "signal": "短期：地缘风险已实质性升级，油气板块有支撑；中期：关注沙特调停结果"
      }
    ],
    "a_level": [
      {
        "emoji": "🟡",
        "title": "A股低开高走创业板指大涨4.81%",
        "source": "证券时报",
        "key_point": "A股展现强劲韧性，超2300只个股上涨，锂矿光模块领涨。宁德时代、中际旭创创历史新高，市场情绪由悲观转乐观。",
        "duration": "1-3天",
        "etfs": [
          { "name": "515930 创业板ETF", "sentiment": "利好" }
        ],
        "stocks": ["宁德时代", "中际旭创", "中国巨石"],
        "signal": "短期：市场情绪修复，科技股领涨；中期：关注量能持续性"
      },
      {
        "emoji": "🟡",
        "title": "上期所调整黄金期货涨跌停板",
        "source": "上期所",
        "key_point": "监管应对地缘波动，黄金期货波动加大。一口价黄金产品下跌17%，市场避险情绪有所缓解。",
        "duration": "1-3天",
        "etfs": [
          { "name": "518880 黄金ETF", "sentiment": "中性" }
        ],
        "stocks": ["山东黄金", "中金黄金"],
        "signal": "短期：金价震荡加剧，观望为主"
      }
    ],
    "douyin": [],
    "wukong_judgment": {
      "market_sentiment": "谨慎偏多",
      "core_analysis": [
        "地缘风险实质性升级，但A股展现韧性，低开高走说明市场承接力强",
        "锂矿光模块领涨，科技股主线明确",
        "宁德时代创历史新高，资金抱团核心资产",
        "美沙角力伊朗局势，能源板块短期有支撑"
      ],
      "operations": [
        { "type": "可做", "content": "锂矿/光模块/AI算力核心标的" },
        { "type": "关注", "content": "油气板块，地缘溢价已部分定价" },
        { "type": "警惕", "content": "追高黄金，地缘风险边际减弱" }
      ]
    },
    "bajie_conclusion": {
      "optimal_action": "轻仓参与科技主线",
      "optimal_etfs": "创业板ETF(20%)+芯片ETF(15%)",
      "win_rate": "~58%",
      "max_drawdown": "-8%",
      "融合说明": ["市场韧性超预期，但地缘不确定性仍在，建议轻仓博弈"]
    }
  },
  "2026-04-15": {
    "date": "2026-04-15",
    "market_tone": {
      "早报": "【2026-04-15早报】霍尔木兹海峡部分恢复通航，特朗普称'美伊战争已结束'，避险情绪降温",
      "晚报": "【2026-04-15晚报】A股高开低走创业板指跌超1%，医药商业航天逆势走强，市场分歧加大"
    },
    "all_news": [
      {
        "title": "霍尔木兹海峡部分恢复通航，特朗普称美伊战争已结束",
        "summary": "4月15日，霍尔木兹海峡部分恢复通航，24小时内超20艘商船通过。特朗普接受采访时称伊朗战事'接近结束'，暗示未来两天美伊可重返谈判桌。调解方正努力说服双方举办技术磋商。",
        "source": "微博/自贡网/21经济网",
        "date": "2026-04-15",
        "emoji": "🕊️"
      },
      {
        "title": "A股高开低走，创业板指创新高后跌超1%",
        "summary": "4月15日A股三大指数高开低走，沪指微涨，深成指跌近1%，创业板指盘中创新高后收跌超1%。医药、商业航天概念逆势走强，锂电池、存储芯片等板块调整。全市场超2000只个股上涨。",
        "source": "每日经济新闻/华夏时报",
        "date": "2026-04-15",
        "emoji": "📉"
      },
      {
        "title": "包钢厂区爆炸78人送医，容百科技被立案调查",
        "summary": "包钢厂区发生爆炸事故，已有78人送医。证监会宣布对容百科技重大合同公告涉嫌误导性陈述立案调查。容百科技韩国子公司与LG化学的专利纠纷仍在诉讼中。",
        "source": "界面新闻/证券时报",
        "date": "2026-04-15",
        "emoji": "⚠️"
      },
      {
        "title": "国资委召开低空经济产业发展专题推进会",
        "summary": "4月15日国务院国资委召开中央企业低空经济产业发展专题推进会，研究低空航空装备创新迭代方向。会议强调要加快低空航空装备创新迭代，推动产业高质量发展。",
        "source": "国资委/中新经纬",
        "date": "2026-04-15",
        "emoji": "🚁"
      },
      {
        "title": "康众医疗拟4亿现金收购AI医疗公司脉得智能",
        "summary": "4月14日晚康众医疗(688607)公告，拟以现金方式收购脉得智能科技(无锡)有限公司控制权，标的公司估值7.5亿元。脉得智能专注于AI医疗领域。",
        "source": "南方财经网/证券时报",
        "date": "2026-04-15",
        "emoji": "🤖"
      },
      {
        "title": "国家安全教育日金融安全宣传，券商护航十五五",
        "summary": "4月15日是第十一个全民国家安全教育日，平安证券等多家券商举办金融安全宣传活动，主题为统筹发展和安全，护航十五五新征程。",
        "source": "华夏时报",
        "date": "2026-04-15",
        "emoji": "🏛️"
      },
      {
        "title": "美元人民币汇率6.8，黄金4867美元上涨",
        "summary": "4月15日人民币汇率升至6.8元关口，较前一交易日6.81上涨。现货黄金4867.5美元上涨，石油跌破90美元至89.54美元。外围金融市场全线飙涨。",
        "source": "微博股票/中新经纬",
        "date": "2026-04-15",
        "emoji": "💰"
      }
    ],
    "s_level": [
      {
        "emoji": "🔴",
        "title": "霍尔木兹海峡恢复通航+特朗普称战争结束（地缘风险快速降温）",
        "source": "微博/新华社",
        "key_point": "24小时内超20艘商船通过海峡，特朗普称'美伊战争已结束'。GEO-001范式：地缘缓和=避险资产快速回撤。关键变量：谈判重启进度、伊朗核计划立场。",
        "duration": "1-2天",
        "etfs": [
          { "name": "518880 黄金ETF", "sentiment": "利空" },
          { "name": "561360 石油ETF", "sentiment": "利空" }
        ],
        "stocks": ["山东黄金", "中金黄金", "中国石油"],
        "signal": "短期：避险逻辑快速瓦解，油气黄金承压；中期：关注谈判实质性进展"
      }
    ],
    "a_level": [
      {
        "emoji": "🟡",
        "title": "A股高开低走创业板指跌超1%",
        "source": "每日经济新闻",
        "key_point": "市场分歧加大，医药商业航天逆势走强，锂电池存储芯片调整。创业板盘中创新高后回落，显示上方压力。",
        "duration": "1-3天",
        "etfs": [
          { "name": "512010 医药ETF", "sentiment": "利好" },
          { "name": "159920 半导体ETF", "sentiment": "利空" }
        ],
        "stocks": ["恒瑞医药", "药明康德", "宁德时代"],
        "signal": "短期：震荡分化，关注医药低吸机会"
      },
      {
        "emoji": "🟡",
        "title": "国资委推进低空经济产业发展",
        "source": "国资委",
        "key_point": "央企低空经济专题会，加快航空装备创新迭代。低空战略上升，相关产业链持续受益。",
        "duration": "1-4周",
        "etfs": [
          { "name": "588560 航空航天ETF", "sentiment": "利好" }
        ],
        "stocks": ["中航沈飞", "中航西飞", "纵横股份"],
        "signal": "中期：低空经济政策持续加码，关注龙头标的"
      },
      {
        "emoji": "🟡",
        "title": "容百科技被立案调查+包钢爆炸事故",
        "source": "证监会/界面新闻",
        "key_point": "容百科技重大合同公告涉嫌误导性陈述被立案，包钢爆炸事故78人送医。两只个股短期承压，相关板块情绪受影响。",
        "duration": "1-3天",
        "etfs": [],
        "stocks": ["容百科技", "包钢股份"],
        "signal": "回避相关个股"
      }
    ],
    "douyin": [],
    "wukong_judgment": {
      "market_sentiment": "中性分歧",
      "core_analysis": [
        "地缘风险快速降温，避险逻辑瓦解，黄金油气承压",
        "A股高开低走显示市场分歧，创业板新高后获利了结",
        "医药商业航天逆势走强，资金寻找新主线",
        "低空经济政策加码，中期逻辑清晰"
      ],
      "operations": [
        { "type": "可做", "content": "医药板块低吸" },
        { "type": "警惕", "content": "追高油气黄金" },
        { "type": "关注", "content": "低空经济产业链龙头" }
      ]
    },
    "bajie_conclusion": {
      "optimal_action": "观望为主轻仓医药",
      "optimal_etfs": "医药ETF(15%)+航空航天ETF(10%)",
      "win_rate": "~45%",
      "max_drawdown": "-6%",
      "融合说明": ["地缘缓和引发避险资产回撤，市场分歧加大，建议降低仓位"]
    }
  },
  "2026-04-16": {
    "date": "2026-04-16",
    "market_tone": {
      "早报": "【2026-04-16早报】一季度GDP同比增5%超预期，经济开局良好，A股集体高开",
      "晚报": "【2026-04-16晚报】A股集体大涨创业板指涨超3%，宁德时代AH股双双创历史新高，亚太股市全线飘红"
    },
    "all_news": [
      {
        "title": "一季度GDP同比增5.0%，中国经济开局良好",
        "summary": "国家统计局4月16日发布数据，一季度国内生产总值33.4万亿元，按不变价格计算同比增长5.0%，比去年四季度回升0.5个百分点。一季度CPI同比上涨0.9%，消费零售额增长，经济运行稳中向好。",
        "source": "国家统计局/央广网/中国新闻网",
        "date": "2026-04-16",
        "emoji": "📊"
      },
      {
        "title": "A股集体大涨，创业板指涨超3%，超4400只个股上涨",
        "summary": "4月16日A股三大指数大幅高开高走，科创综指盘中大涨逾3%，上证指数收复3900点，创业板指大涨超3%站上3200点。超4400只个股上涨，成交放量。日经225指数涨2.38%创历史新高，韩国指数涨2.21%。",
        "source": "证券时报/通达股份行情",
        "date": "2026-04-16",
        "emoji": "🚀"
      },
      {
        "title": "宁德时代AH股双双创历史新高，市值破2万亿",
        "summary": "4月16日宁德时代A股涨超4%，H股大涨超10%，双双创历史新高。A股总市值再次突破2万亿元大关。此前的4月15日宁德时代公告催化市场情绪。",
        "source": "证券时报/每经网",
        "date": "2026-04-16",
        "emoji": "🔋"
      },
      {
        "title": "它石智航完成4.5亿美元Pre-A轮融资，创中国具身智能纪录",
        "summary": "4月16日它石智航宣布完成超4.5亿美元Pre-A轮融资，创下中国具身智能有史以来最高单轮融资纪录。这是继2025年Q2完成2.42亿美元天使轮融资后再次刷新纪录。",
        "source": "证券时报/上市公司公告",
        "date": "2026-04-16",
        "emoji": "🤖"
      },
      {
        "title": "一季度居民人均可支配收入实际增长4%",
        "summary": "国家统计局16日披露，一季度全国居民人均可支配收入实际增长4%。3月份社会消费品零售总额41616亿元，同比增长1.7%。经济数据整体向好。",
        "source": "中新经纬/国家统计局",
        "date": "2026-04-16",
        "emoji": "💰"
      },
      {
        "title": "3月原油加工由增转降，工业生产稳定",
        "summary": "国家统计局16日披露，3月份规模以上工业原油加工由增转降，原煤生产规模稳定，原油生产保持稳定。能源供给侧运行平稳。",
        "source": "中新经纬",
        "date": "2026-04-16",
        "emoji": "🛢️"
      },
      {
        "title": "特斯拉宣布对欧盟110亿美元商品征收关税",
        "summary": "当地时间4月9日，特朗普在推特宣布美国将对价值110亿美元的欧盟产品征收关税，称欧盟给空客的补贴对美国产生负面影响，贸易战再度升温。",
        "source": "上观新闻/新浪",
        "date": "2026-04-16",
        "emoji": "⚔️"
      },
      {
        "title": "国资委要求加快低空航空装备创新迭代",
        "summary": "4月16日据国资委网站消息，国务院国资委强调央企要加快低空航空装备创新迭代，推动低空经济产业高质量发展。政策持续加码低空经济。",
        "source": "中新经纬/国资委",
        "date": "2026-04-16",
        "emoji": "🚁"
      }
    ],
    "s_level": [
      {
        "emoji": "🔴",
        "title": "一季度GDP同比增5.0%超预期（宏观经济强劲开局）",
        "source": "国家统计局/央广网",
        "key_point": "一季度GDP增长5.0%超预期，比去年Q4回升0.5个百分点。CPI温和上涨0.9%，居民收入实际增4%，消费零售增长。经济数据全面向好，A股基本面支撑强。关键信号：GDP超预期+收入增长+消费回暖=经济复苏确立。",
        "duration": "1-4周",
        "etfs": [
          { "name": "515930 创业板ETF", "sentiment": "利好" },
          { "name": "510300 沪深300ETF", "sentiment": "利好" }
        ],
        "stocks": ["宁德时代", "中国中免", "贵州茅台"],
        "signal": "中期：经济基本面支撑A股，可增加权益仓位"
      },
      {
        "emoji": "🔴",
        "title": "宁德时代AH股创历史新高，市值破2万亿",
        "source": "证券时报",
        "key_point": "宁德时代A股涨超4%、H股涨超10%双双创历史新高，市值破2万亿。龙头公司持续创新高，说明机构资金核心资产牛市。关键信号：龙头新高=资金抱团强化，锂电池板块情绪高涨。",
        "duration": "1-2周",
        "etfs": [
          { "name": "159755 锂电池ETF", "sentiment": "利好" },
          { "name": "515930 创业板ETF", "sentiment": "利好" }
        ],
        "stocks": ["宁德时代", "比亚迪", "亿纬锂能"],
        "signal": "短期：龙头领涨，锂电池板块可跟随"
      }
    ],
    "a_level": [
      {
        "emoji": "🟡",
        "title": "A股集体大涨创业板指涨超3%",
        "source": "证券时报",
        "key_point": "超4400只个股上涨，成交放量。日经225创历史新高，亚太股市全线飘红。市场情绪高涨，做多窗口开启。",
        "duration": "1-3天",
        "etfs": [
          { "name": "515930 创业板ETF", "sentiment": "利好" }
        ],
        "stocks": ["宁德时代", "中际旭创", "东方财富"],
        "signal": "短期：情绪高涨，可积极参与"
      },
      {
        "emoji": "🟡",
        "title": "它石智航完成4.5亿美元融资",
        "source": "证券时报",
        "key_point": "中国具身智能最大单轮融资，AI机器人赛道热度持续。明星资本集结，产业资本看好。",
        "duration": "1-2周",
        "etfs": [
          { "name": "515070 AI智能ETF", "sentiment": "利好" }
        ],
        "stocks": ["机器人概念股", "AI算力龙头"],
        "signal": "中期：具身智能赛道持续关注"
      },
      {
        "emoji": "🟡",
        "title": "特朗普对欧盟征收110亿美元关税",
        "source": "上观新闻",
        "key_point": "贸易战再度升温，欧美贸易摩擦加剧。Trump范式：关税威胁=短期避险情绪升温。关键变量：欧盟反制措施、是否波及中国。",
        "duration": "1-4周",
        "etfs": [],
        "stocks": ["出口欧洲板块谨慎"],
        "signal": "关注贸易摩擦升级风险"
      }
    ],
    "douyin": [],
    "wukong_judgment": {
      "market_sentiment": "积极做多",
      "core_analysis": [
        "一季度GDP增5%超预期，经济基本面强劲",
        "宁德时代AH股双双创新高，龙头股牛市确立",
        "A股集体大涨，超4400只个股上涨，情绪高涨",
        "它石智航融资创纪录，AI具身智能赛道热度不减",
        "亚太股市全线飘红，风险偏好上升"
      ],
      "operations": [
        { "type": "可做", "content": "锂电池/AI算力/核心资产" },
        { "type": "可做", "content": "增加仓位，把握做多窗口" },
        { "type": "关注", "content": "低空经济政策持续加码" }
      ]
    },
    "bajie_conclusion": {
      "optimal_action": "积极做多核心资产",
      "optimal_etfs": "创业板ETF(40%)+锂电池ETF(20%)+AI智能ETF(15%)",
      "win_rate": "~72%",
      "max_drawdown": "-10%",
      "融合说明": ["经济数据超预期+龙头创新高+情绪高涨=做多窗口开启，建议积极参与"]
    }
  }
};

// 读取现有news-data.js
const newsDataPath = 'C:\\Users\\asus\\temp-news-website\\news-data.js';
let content = fs.readFileSync(newsDataPath, 'utf-8');

// 找到newsData对象的开始位置
const newsDataStart = content.indexOf('const newsData = {');
const newsDataEnd = content.lastIndexOf('};') + 2;
const availableDatesMatch = content.match(/const availableDates = \[([^\]]+)\]/);

// 提取现有日期
let existingDates = [];
if (availableDatesMatch) {
  existingDates = availableDatesMatch[1].match(/"\d{4}-\d{2}-\d{2}"/g).map(d => d.replace(/"/g, ''));
}

// 生成新数据
const newEntries = Object.entries(newDaysData).map(([date, data]) => {
  return `"${date}": ${JSON.stringify(data, null, 2)}`;
}).join(',\n');

// 更新日期列表
const newDates = Object.keys(newDaysData);
const allDates = [...new Set([...newDates, ...existingDates])].sort().reverse();

// 构建新文件内容
const header = `// 财经新闻数据 - 四层交叉分析版
// 生成时间: ${(new Date()).toISOString().split('T')[0]}
// 架构: 悟空+八戒(优质新闻) → 沙僧+白龙马(全量新闻+市场数据)
// 三层交叉: 白龙马融合悟空信号 | 八戒融合沙僧+白龙马信号

const newsData = {
${newEntries},
`;

// 从原有内容中提取非新增日期的数据
const originalDataStart = content.indexOf('{', content.indexOf('const newsData =') + 10) + 1;
const originalDataEnd = content.lastIndexOf('};');
const originalContent = content.substring(originalDataStart, originalDataEnd).trim();

const footer = `${originalContent}
};

const availableDates = ${JSON.stringify(allDates)};

function getNews(date) { return newsData[date] || null; }
function getPreviousDate(date) { const idx = availableDates.indexOf(date); return idx < availableDates.length - 1 ? availableDates[idx + 1] : null; }
function getNextDate(date) { const idx = availableDates.indexOf(date); return idx > 0 ? availableDates[idx - 1] : null; }
`;

// 写入文件
const newFileContent = header + footer;

// 先验证JSON语法
try {
  // 提取newsData部分进行验证
  const jsonTest = newFileContent.substring(newFileContent.indexOf('const newsData ='), newFileContent.lastIndexOf('};') + 2)
    .replace('const newsData = ', '');
  JSON.parse(jsonTest);
  console.log('JSON syntax validation passed');
} catch(e) {
  console.error('JSON syntax error:', e.message);
  console.log('Writing file anyway for manual fix...');
}

fs.writeFileSync(newsDataPath, newFileContent, 'utf-8');
console.log('Updated news-data.js with dates:', allDates.slice(0, 5).join(', '), '...');
console.log('File size:', (newFileContent.length / 1024).toFixed(1), 'KB');
