const fs = require('fs');

const content = fs.readFileSync('C:\\Users\\asus\\temp-news-website\\news-data.js', 'utf-8');

function generateSangsha(newsItem, date) {
  const title = newsItem.title || '';
  const emoji = newsItem.emoji || '';
  
  let 追高 = 5, 抄底 = 5, 恐慌 = 5, 观望 = 85;
  let 情绪 = [], 总结 = '平稳', 含义 = '中性';
  
  if (title.includes('封锁') || title.includes('霍尔木兹') || emoji === '🔥') {
    追高 = 15; 恐慌 = 45; 观望 = 40; 情绪 = ['恐慌']; 总结 = '散户恐慌'; 含义 = '风险';
  } else if (title.includes('谈判') || title.includes('停火') || title.includes('恢复通航')) {
    追高 = 25; 抄底 = 15; 恐慌 = 5; 观望 = 55; 情绪 = ['谨慎']; 总结 = '散户谨慎'; 含义 = '修复';
  } else if (title.includes('GDP') || title.includes('超预期') || title.includes('创新高')) {
    追高 = 65; 恐慌 = 3; 观望 = 22; 情绪 = ['乐观','亢奋']; 总结 = '散户亢奋'; 含义 = '利好';
  } else if (title.includes('创业板') || title.includes('宁德') || emoji === '📈') {
    追高 = 55; 恐慌 = 5; 观望 = 40; 情绪 = ['积极']; 总结 = '散户积极'; 含义 = '做多';
  } else if (title.includes('医药')) {
    追高 = 45; 恐慌 = 8; 观望 = 47; 情绪 = ['关注']; 总结 = '散户关注'; 含义 = '轮动';
  } else if (title.includes('黄金') || title.includes('原油') || emoji === '📊') {
    追高 = 35; 恐慌 = 25; 观望 = 40; 情绪 = ['避险']; 总结 = '散户避险'; 含义 = '避险';
  } else {
    情绪 = ['观望'];
  }
  
  return {
    news: title.substring(0,80), title, full_title: title, summary: '',
    追高买入概率: 追高, 抄底买入概率: 抄底, 恐慌卖出概率: 恐慌, 观望概率: 观望,
    情绪标签: 情绪, 韭菜行为总结: 总结, 市场含义: 含义,
    买入概率: Math.round((追高+抄底)/2), is_long_term: false, date, decay: 1.0,
    weighted_buy_prob: Math.round((追高+抄底)/2)
  };
}

function addSangsha(dateStr, content) {
  const keyPos = content.indexOf('"' + dateStr + '": {');
  if (keyPos < 0) return content;
  
  // Windows CRLF: }, 然后 \r\n  "s_level":
  const endPattern = '},\r\n  "s_level":';
  const endIdx = content.indexOf(endPattern, keyPos);
  if (endIdx < 0) {
    console.log(dateStr + ': 找不到插入点');
    return content;
  }
  
  // 提取标题
  const block = content.substring(keyPos, endIdx);
  const titles = block.match(/"title":\s*"([^"]+)"/g) || [];
  const newsItems = titles.map(t => ({ title: t.match(/"title":\s*"([^"]+)"/)[1] }));
  console.log(dateStr + ': ' + newsItems.length + '条');
  
  const results = newsItems.map(n => generateSangsha(n, dateStr));
  const avgBuy = Math.round(results.reduce((s,r) => s+r.追高买入概率,0)/results.length);
  const avgPanic = Math.round(results.reduce((s,r) => s+r.恐慌卖出概率,0)/results.length);
  
  let sentiment = '平稳', advice = '观望';
  if (avgBuy > 40) { sentiment = '亢奋'; advice = '防追高'; }
  else if (avgBuy > 25) { sentiment = '积极'; advice = '可参与'; }
  else if (avgPanic > 30) { sentiment = '恐慌'; advice = '谨慎'; }
  
  const sangshaModule = `
        "sangsha_module": {
            "overall_sentiment": "${sentiment}",
            "advice": "${advice}",
            "avg_buy_prob": ${avgBuy},
            "avg_panic_prob": ${avgPanic},
            "analysis_results": ${JSON.stringify(results)}
        }`;
  
  // 在 }, 之后插入
  const insertAt = endIdx + 2;
  return content.substring(0, insertAt) + sangshaModule + content.substring(insertAt);
}

let newContent = content;
newContent = addSangsha('2026-04-14', newContent);
newContent = addSangsha('2026-04-15', newContent);
newContent = addSangsha('2026-04-16', newContent);

fs.writeFileSync('C:\\Users\\asus\\temp-news-website\\news-data.js', newContent, 'utf-8');
console.log('Done!');
