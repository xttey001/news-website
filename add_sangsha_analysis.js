const fs = require('fs');

// 读取现有 news-data.js
const content = fs.readFileSync('C:\\Users\\asus\\temp-news-website\\news-data.js', 'utf-8');

// 沙僧分析函数 - 为每条新闻生成韭菜直觉分析
function generateSangshaAnalysis(newsItem, date) {
  const title = newsItem.title || '';
  const emoji = newsItem.emoji || '';
  const text = title;
  
  // 基于关键词判断情绪
  let 追高买入概率 = 5;
  let 抄底买入概率 = 5;
  let 恐慌卖出概率 = 5;
  let 观望概率 = 85;
  let 情绪标签 = [];
  let 韭菜行为总结 = '散户情绪平稳，观望为主';
  let 市场含义 = '中性';

  // 地缘危机相关
  if (text.includes('封锁') || text.includes('霍尔木兹') || text.includes('伊朗') || text.includes('美军') || emoji === '🔥') {
    追高买入概率 = 15;
    恐慌卖出概率 = 45;
    观望概率 = 40;
    情绪标签.push('恐慌', '观望');
    韭菜行为总结 = '散户恐慌，部分抛售观望';
    市场含义 = '风险';
  }
  
  // 谈判/缓和相关
  if (text.includes('谈判') || text.includes('停火') || text.includes('和平') || text.includes('恢复通航')) {
    追高买入概率 = 25;
    抄底买入概率 = 15;
    恐慌卖出概率 = 5;
    观望概率 = 55;
    情绪标签.push('谨慎', '观望');
    韭菜行为总结 = '散户谨慎，部分抄底';
    市场含义 = '修复';
  }
  
  // GDP/经济利好
  if (text.includes('GDP') || text.includes('超预期') || text.includes('增长') || text.includes('创新高')) {
    追高买入概率 = 65;
    抄底买入概率 = 10;
    恐慌卖出概率 = 3;
    观望概率 = 22;
    情绪标签.push('乐观', '亢奋');
    韭菜行为总结 = '散户亢奋，追高买入';
    市场含义 = '利好';
  }
  
  // 科技股/新能源
  if (text.includes('创业板') || text.includes('宁德') || text.includes('新能源') || text.includes('锂矿') || text.includes('光模块') || emoji === '📈') {
    追高买入概率 = 55;
    恐慌卖出概率 = 5;
    观望概率 = 40;
    情绪标签.push('积极');
    韭菜行为总结 = '散户积极跟进';
    市场含义 = '做多';
  }
  
  // 医药
  if (text.includes('医药') || text.includes('创新药') || text.includes('疫苗')) {
    追高买入概率 = 45;
    恐慌卖出概率 = 8;
    观望概率 = 47;
    情绪标签.push('关注');
    韭菜行为总结 = '散户关注医药机会';
    市场含义 = '轮动';
  }
  
  // 黄金/避险
  if (text.includes('黄金') || text.includes('避险') || text.includes('原油') || emoji === '📊') {
    追高买入概率 = 35;
    恐慌卖出概率 = 25;
    观望概率 = 40;
    情绪标签.push('避险');
    韭菜行为总结 = '散户避险情绪升温';
    市场含义 = '避险';
  }
  
  // 默认
  if (情绪标签.length === 0) {
    情绪标签.push('观望');
  }

  return {
    news: text.substring(0, 100),
    title: title,
    full_title: title,
    summary: '',
    追高买入概率,
    抄底买入概率,
    恐慌卖出概率,
    观望概率,
    情绪标签,
    韭菜行为总结,
    市场含义,
    买入概率: Math.round((追高买入概率 + 抄底买入概率) / 2),
    is_long_term: false,
    date: date,
    decay: 1.0,
    weighted_buy_prob: Math.round((追高买入概率 + 抄底买入概率) / 2)
  };
}

// 简单方法：直接替换 sangsha_module 部分
function addSangshaModule(dateStr, content) {
  const keyPattern = '"' + dateStr + '": {';
  const keyPos = content.indexOf(keyPattern);
  if (keyPos < 0) {
    console.log(dateStr + ': 未找到');
    return content;
  }
  
  // 找到这个日期块的结束位置（下一个日期的 "date": 或 "2026-" 开始）
  let endPos = content.length;
  const rest = content.substring(keyPos + 20);
  const nextDateMatch = rest.match(/"2026-\d{2}-\d{2}":\s*\{/);
  if (nextDateMatch) {
    endPos = keyPos + 20 + nextDateMatch.index;
  }
  
  let block = content.substring(keyPos, endPos);
  
  // 检查是否已有 sangsha_module
  const hasSangsha = block.includes('"sangsha_module"');
  if (hasSangsha) {
    console.log(dateStr + ': 已有 sangsha_module，检查是否有 analysis_results');
    // 检查是否有 analysis_results
    const hasAnalysis = block.includes('"analysis_results"') && block.includes('追高买入概率');
    if (hasAnalysis) {
      console.log(dateStr + ': 已有完整分析，跳过');
      return content;
    }
    // 删除旧的 sangsha_module
    const sangshaStart = block.indexOf('"sangsha_module"');
    const beforeBlock = block.substring(0, sangshaStart);
    // 找到结束位置
    let deleteEnd = sangshaStart;
    let braceCount = 0;
    let started = false;
    for (let i = sangshaStart; i < block.length; i++) {
      if (block[i] === '{') { braceCount++; started = true; }
      if (block[i] === '}') { braceCount--; }
      if (started && braceCount === 0) { deleteEnd = i + 1; break; }
    }
    block = beforeBlock + block.substring(deleteEnd);
    console.log(dateStr + ': 已删除旧 sangsha_module');
  }
  
  // 提取 all_news 数组
  const newsMatch = block.match(/"all_news":\s*\[([\s\S]*?)(\n\s{4}\]|\n\s{3}\])/);
  if (!newsMatch) {
    console.log(dateStr + ': 未找到 all_news 数组');
    return content;
  }
  
  // 解析新闻项（简单方法：提取 title）
  const newsArrayStr = newsMatch[1];
  const titleMatches = newsArrayStr.match(/"title":\s*"([^"]+)"/g);
  const newsItems = [];
  if (titleMatches) {
    titleMatches.forEach(m => {
      const titleMatch = m.match(/"title":\s*"([^"]+)"/);
      if (titleMatch) {
        newsItems.push({ title: titleMatch[1] });
      }
    });
  }
  console.log(dateStr + ': 找到 ' + newsItems.length + ' 条新闻');
  
  // 生成分析结果
  const analysisResults = newsItems.map(item => generateSangshaAnalysis(item, dateStr));
  
  // 计算整体情绪
  const avgBuy = Math.round(analysisResults.reduce((sum, r) => sum + r.追高买入概率, 0) / analysisResults.length);
  const avgPanic = Math.round(analysisResults.reduce((sum, r) => sum + r.恐慌卖出概率, 0) / analysisResults.length);
  
  let overallSentiment = '平稳';
  let advice = '观望为主';
  if (avgBuy > 40) { overallSentiment = '亢奋'; advice = '注意追高风险'; }
  else if (avgBuy > 25) { overallSentiment = '积极'; advice = '可以适度参与'; }
  else if (avgPanic > 30) { overallSentiment = '恐慌'; advice = '保持谨慎'; }
  
  // 新的 sangsha_module JSON
  const sangshaModule = `,
  "sangsha_module": {
    "overall_sentiment": "${overallSentiment}",
    "advice": "${advice}",
    "avg_buy_prob": ${avgBuy},
    "avg_panic_prob": ${avgPanic},
    "analysis_results": ${JSON.stringify(analysisResults)}
  }`;
  
  // 找到 all_news 数组结束位置
  const allNewsEndPattern = '],\n    ';
  const allNewsEnd = block.indexOf(allNewsEndPattern);
  if (allNewsEnd < 0) {
    console.log(dateStr + ': 找不到插入位置');
    return content;
  }
  
  const insertPos = keyPos + allNewsEnd + allNewsEndPattern.length;
  const before = content.substring(0, insertPos);
  const after = content.substring(insertPos);
  
  return before + sangshaModule + after;
}

// 处理 04-14, 04-15, 04-16
let newContent = content;
newContent = addSangshaModule('2026-04-14', newContent);
newContent = addSangshaModule('2026-04-15', newContent);
newContent = addSangshaModule('2026-04-16', newContent);

// 写回文件
fs.writeFileSync('C:\\Users\\asus\\temp-news-website\\news-data.js', newContent, 'utf-8');
console.log('Done!');
