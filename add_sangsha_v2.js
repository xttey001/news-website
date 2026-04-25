const fs = require('fs');

// 读取现有 news-data.js
const content = fs.readFileSync('C:\\Users\\asus\\temp-news-website\\news-data.js', 'utf-8');

// 沙僧分析函数
function generateSangshaAnalysis(newsItem, date) {
  const title = newsItem.title || '';
  const emoji = newsItem.emoji || '';
  const text = title;
  
  let 追高买入概率 = 5;
  let 抄底买入概率 = 5;
  let 恐慌卖出概率 = 5;
  let 观望概率 = 85;
  let 情绪标签 = [];
  let 韭菜行为总结 = '散户情绪平稳，观望为主';
  let 市场含义 = '中性';

  if (text.includes('封锁') || text.includes('霍尔木兹') || text.includes('伊朗') || emoji === '🔥') {
    追高买入概率 = 15; 恐慌卖出概率 = 45; 观望概率 = 40;
    情绪标签 = ['恐慌', '观望']; 韭菜行为总结 = '散户恐慌，部分抛售'; 市场含义 = '风险';
  }
  else if (text.includes('谈判') || text.includes('停火') || text.includes('和平') || text.includes('恢复通航')) {
    追高买入概率 = 25; 抄底买入概率 = 15; 恐慌卖出概率 = 5; 观望概率 = 55;
    情绪标签 = ['谨慎']; 韭菜行为总结 = '散户谨慎'; 市场含义 = '修复';
  }
  else if (text.includes('GDP') || text.includes('超预期') || text.includes('增长') || text.includes('创新高')) {
    追高买入概率 = 65; 恐慌卖出概率 = 3; 观望概率 = 22;
    情绪标签 = ['乐观', '亢奋']; 韭菜行为总结 = '散户亢奋追高'; 市场含义 = '利好';
  }
  else if (text.includes('创业板') || text.includes('宁德') || text.includes('新能源') || text.includes('锂矿') || emoji === '📈') {
    追高买入概率 = 55; 恐慌卖出概率 = 5; 观望概率 = 40;
    情绪标签 = ['积极']; 韭菜行为总结 = '散户积极跟进'; 市场含义 = '做多';
  }
  else if (text.includes('医药') || text.includes('创新药')) {
    追高买入概率 = 45; 恐慌卖出概率 = 8; 观望概率 = 47;
    情绪标签 = ['关注']; 韭菜行为总结 = '散户关注医药'; 市场含义 = '轮动';
  }
  else if (text.includes('黄金') || text.includes('避险') || text.includes('原油') || emoji === '📊') {
    追高买入概率 = 35; 恐慌卖出概率 = 25; 观望概率 = 40;
    情绪标签 = ['避险']; 韭菜行为总结 = '散户避险'; 市场含义 = '避险';
  }
  else {
    情绪标签 = ['观望'];
  }

  return {
    news: text.substring(0, 80), title, full_title: title, summary: '',
    追高买入概率, 抄底买入概率, 恐慌卖出概率, 观望概率,
    情绪标签, 韭菜行为总结, 市场含义,
    买入概率: Math.round((追高买入概率 + 抄底买入概率) / 2),
    is_long_term: false, date, decay: 1.0,
    weighted_buy_prob: Math.round((追高买入概率 + 抄底买入概率) / 2)
  };
}

function addSangshaForDate(dateStr, content) {
  const keyPattern = '"' + dateStr + '": {';
  const keyPos = content.indexOf(keyPattern);
  if (keyPos < 0) return content;
  
  // 找到这个日期块的边界
  let rest = content.substring(keyPos + 20);
  const nextKeyMatch = rest.match(/"2026-\d{2}-\d{2}":\s*\{/);
  let endPos = content.length;
  if (nextKeyMatch) endPos = keyPos + 20 + nextKeyMatch.index;
  
  let block = content.substring(keyPos, endPos);
  
  // 查找 all_news 数组结束位置（在 block 内）
  const allNewsEndIdx = block.indexOf('],\n        "s_level"');
  if (allNewsEndIdx < 0) {
    console.log(dateStr + ': 找不到插入点');
    return content;
  }
  
  // 提取新闻标题
  const titleMatches = block.match(/"title":\s*"([^"]+)"/g) || [];
  const newsItems = titleMatches.map(m => ({ title: m.match(/"title":\s*"([^"]+)"/)[1] }));
  console.log(dateStr + ': ' + newsItems.length + '条新闻');
  
  const analysisResults = newsItems.map(item => generateSangshaAnalysis(item, dateStr));
  
  const avgBuy = Math.round(analysisResults.reduce((sum, r) => sum + r.追高买入概率, 0) / analysisResults.length);
  const avgPanic = Math.round(analysisResults.reduce((sum, r) => sum + r.恐慌卖出概率, 0) / analysisResults.length);
  
  let overallSentiment = '平稳';
  let advice = '观望为主';
  if (avgBuy > 40) { overallSentiment = '亢奋'; advice = '注意追高风险'; }
  else if (avgBuy > 25) { overallSentiment = '积极'; advice = '可以适度参与'; }
  else if (avgPanic > 30) { overallSentiment = '恐慌'; advice = '保持谨慎'; }
  
  const sangshaModule = `
        "sangsha_module": {
            "overall_sentiment": "${overallSentiment}",
            "advice": "${advice}",
            "avg_buy_prob": ${avgBuy},
            "avg_panic_prob": ${avgPanic},
            "analysis_results": ${JSON.stringify(analysisResults)}
        }`;
  
  // 在 all_news 结束后插入
  const insertAt = keyPos + allNewsEndIdx + 4; // 跳过 "],\n  "
  return content.substring(0, insertAt) + sangshaModule + content.substring(insertAt);
}

let newContent = content;
newContent = addSangshaForDate('2026-04-14', newContent);
newContent = addSangshaForDate('2026-04-15', newContent);
newContent = addSangshaForDate('2026-04-16', newContent);

fs.writeFileSync('C:\\Users\\asus\\temp-news-website\\news-data.js', newContent, 'utf-8');
console.log('Done!');
