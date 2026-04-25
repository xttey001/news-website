/**
 * 财经新闻五层分析系统 - 自动化工作流脚本
 * 
 * 使用方式：
 *   node news-five-layer-workflow.js "<新闻标题>" "<新闻内容>"
 * 
 * 或者在OpenClaw中：
 *   五层分析：Trump施压伊朗，黄金大涨
 */

const AGENT_IDS = {
  wukong: 'agent-acd13225',    // 🐵 悟空：新闻分析师
  bajie: 'agent-64a61d6d',     // 🐷 八戒：贝叶斯概率
  shaseng: 'agent-217acc17',   // 🧅 沙僧：散户情绪
  bailongma: 'agent-f189fdb5' // 🐴 白龙马：主力行为
};

// 第一层：悟空分析Prompt模板
const WUKONG_PROMPT = (news) => `你是悟空，新闻分析师。请分析以下新闻并输出JSON格式：

【新闻】
标题：${news.title}
内容：${news.content}

【分析要求】
1. 判断新闻级别：S级（结构性叙事，影响1-4周）/ A级（阶段性叙事，影响1-3天）/ B级
2. 判断情绪方向：利多/利空/中性
3. 应用Trump jawboning反转定律（如果适用）
4. 输出ETF映射和个股映射

【输出格式】（必须是有效JSON）
{
  "level": "S",
  "emoji": "🔴",
  "title": "简化标题",
  "summary": "一句话核心内容",
  "sentiment": "利多/利空/中性",
  "direction": "看多/看空/震荡",
  "confidence": 75,
  "duration": "1-4周",
  "trump_jawboning": {
    "detected": false,
    "signal_count": 0,
    "reversal_probability": "0%"
  },
  "etf_mapping": {
    "bullish": ["518880 黄金ETF"],
    "bearish": []
  },
  "stock_mapping": {
    "bullish": ["山东黄金"],
    "bearish": []
  },
  "key_variables": ["变量1", "变量2"],
  "reasoning": ["要点1", "要点2", "要点3"],
  "risks": ["风险1", "风险2"]
}`;

// 第二层：八戒分析Prompt模板
const BAJIE_PROMPT = (wukongOutput) => `你是八戒，贝叶斯分析大师。基于悟空的分析输出，计算贝叶斯概率。

【悟空输出】
${JSON.stringify(wukongOutput, null, 2)}

【任务】
1. 设定先验概率（基于历史基准）
2. 计算似然（Trump jawboning信号强度，如有）
3. 输出后验概率（做多ETF的胜率）

【输出格式】（必须是有效JSON）
{
  "prior": {"base": "历史基准", "value": 50, "reason": "基于xxx"},
  "likelihood": {"strength": "信号强度", "value": 0.5, "reason": "xxx"},
  "posterior": {"bullish_prob": 60, "confidence_interval": [55, 65]},
  "expected_return": {"etf": "+2%~+5%", "stock": "+5%~+10%"},
  "decision_matrix": [
    {"scenario": "概率≥75%", "action": "✅ 坚定做多", "position": "70-100%"},
    {"scenario": "概率60-74%", "action": "✅ 可做，轻仓", "position": "30-50%"}
  ],
  "final_conclusion": {
    "optimal_action": "操作建议",
    "win_rate": 60,
    "max_drawdown_alert": "-5%"
  }
}`;

// 第三层：沙僧分析Prompt模板
const SHASENG_PROMPT = (news, wukongOutput) => `你是沙僧，韭菜心理分析师。用小红书姐妹风格预测散户看到这条新闻会有什么反应。

【新闻】
标题：${news.title}

【悟空判断】
- ${wukongOutput.level}级新闻，${wukongOutput.sentiment}

【任务】
预测散户的情绪和行为。

【输出格式】（必须是有效JSON）
{
  "news_title": "${news.title}",
  "追高买入概率": 75,
  "抄底买入概率": 10,
  "恐慌卖出概率": 5,
  "观望概率": 10,
  "情绪标签": ["FOMO", "避险"],
  "韭菜行为总结": "姐妹们！冲冲冲！",
  "市场含义": "顶部风险",
  "综合买入概率": 70,
  "warning": "追高概率偏高，警惕主力出货"
}`;

// 第四层：白龙马分析Prompt模板
const BAILONGMA_PROMPT = (wukongOutput, shasengOutput) => `你是白龙马，主力操盘手模型。判断主力行为。

【悟空分析】
- ${wukongOutput.level}级新闻，${wukongOutput.sentiment}
- ${wukongOutput.direction}

【沙僧分析】
- 散户追高概率：${shasengOutput.追高买入概率}%
- 情绪：${shasengOutput.情绪标签.join('、')}

【任务】
判断主力是否在利用这次"利好"进行出货？

【输出格式】（必须是有效JSON）
{
  "主力状态": "出货|吸筹|拉升|洗盘|观望",
  "行为解释": "基于量价和散户行为的分析",
  "是否利用散户": true,
  "利用方式": "借利好出货",
  "当前阶段": "出货初期",
  "信号强度": "中强",
  "关键观察点": ["点1", "点2"],
  "操作建议": "不追高，观望为主"
}`;

/**
 * 唐僧仲裁逻辑
 * 
 * @param {Object} wukongOutput - 悟空输出
 * @param {Object} bajieOutput - 八戒输出
 * @param {Object} shasengOutput - 沙僧输出
 * @param {Object} bailongmaOutput - 白龙马输出
 * @returns {Object} 唐僧最终决策
 */
function tangArbitration(wukongOutput, bajieOutput, shasengOutput, bailongmaOutput) {
  // 矛盾检测
  const contradictions = [];
  
  // 1. 悟空 vs 白龙马
  const wukongVsBailongma = (wukongOutput.sentiment === '利多' && bailongmaOutput.主力状态 === '出货') ||
                           (wukongOutput.direction === '看多' && bailongmaOutput.主力状态 === '出货');
  if (wukongVsBailongma) {
    contradictions.push('悟空看多 vs 白龙马判断主力出货');
  }
  
  // 2. 八戒 vs 沙僧（高胜率+散户狂热）
  const bajieVsShaseng = bajieOutput.posterior.bullish_prob >= 65 && 
                         shasengOutput.追高买入概率 >= 75;
  if (bajieVsShaseng) {
    contradictions.push('八戒高胜率 vs 沙僧散户狂热');
  }
  
  // 3. 三重危险
  const tripleDanger = wukongOutput.sentiment === '利多' && 
                       bailongmaOutput.主力状态 === '出货' &&
                       shasengOutput.追高买入概率 >= 75;
  if (tripleDanger) {
    contradictions.push('三重危险：利多新闻 + 主力出货 + 散户狂热');
  }
  
  // 仓位计算
  let basePosition = 0;
  const bullishProb = bajieOutput.posterior.bullish_prob;
  
  if (bullishProb >= 75) basePosition = 70;
  else if (bullishProb >= 60) basePosition = 50;
  else if (bullishProb >= 50) basePosition = 20;
  else basePosition = 0;
  
  // 唐僧系数
  let tangCoeff = 1.0;
  
  if (tripleDanger) {
    tangCoeff = 0; // 清仓
    contradictions.push('触发风控：三重危险 → 清仓');
  } else if (wukongVsBailongma) {
    tangCoeff = 0.7; // 跨层矛盾
    contradictions.push('触发调整：悟空看多+白龙马出货 → 降至30%');
  } else if (bajieVsShaseng) {
    tangCoeff = 0.5; // 情绪过热
    contradictions.push('触发调整：八戒高胜率+沙僧狂热 → 降至35%');
  }
  
  // 风控系数
  let riskCoeff = 1.0;
  
  // Trump jawboning
  if (wukongOutput.trump_jawboning?.detected && 
      parseInt(wukongOutput.trump_jawboning.reversal_probability) >= 50) {
    riskCoeff *= 0.8;
    contradictions.push('触发风控：Trump jawboning检测');
  }
  
  // 最终仓位
  const finalPosition = Math.round(basePosition * tangCoeff * riskCoeff);
  
  return {
    矛盾检测结果: {
      '悟空vs白龙马': wukongVsBailongma ? '矛盾' : '一致',
      '八戒vs沙僧': bajieVsShaseng ? '矛盾' : '一致',
      '总体一致性': contradictions.length === 0 ? '高' : '低'
    },
    仲裁决策: {
      '主要矛盾': contradictions[0] || '无重大矛盾',
      '仲裁理由': contradictions.length > 0 ? '存在跨层矛盾，需降仓处理' : '五层信号一致，可正常操作',
      '唐僧系数': tangCoeff
    },
    仓位计算: {
      '八戒胜率': bullishProb,
      '基础仓位': basePosition,
      '唐僧系数': tangCoeff,
      '风控系数': riskCoeff,
      '最终仓位': finalPosition
    },
    风控触发: contradictions.filter(c => c.includes('触发')),
    最终行动: {
      '操作': finalPosition >= 30 ? '买入' : (finalPosition > 0 ? '观望' : '不操作'),
      '标的': wukongOutput.etf_mapping.bullish[0] || '无',
      '仓位': finalPosition + '%',
      '止损线': '-3%',
      '止盈目标': '+5%'
    }
  };
}

// 导出
module.exports = {
  AGENT_IDS,
  WUKONG_PROMPT,
  BAJIE_PROMPT,
  SHASENG_PROMPT,
  BAILONGMA_PROMPT,
  tangArbitration
};

console.log('财经新闻五层分析系统 - 工作流模块');
console.log('Agent IDs:', AGENT_IDS);
