const fs = require('fs');

const content = fs.readFileSync('C:\\Users\\asus\\temp-news-website\\news-data.js', 'utf-8');

// 先恢复到干净的版本（从 a411616 恢复）
// 然后重新生成完整的 sangsha_module

function generateSangshaItem(newsItem, date) {
  const title = newsItem.title || '';
  const emoji = newsItem.emoji || '';
  
  // 基于标题关键词生成更真实的韭菜分析
  let 追高 = 15, 抄底 = 10, 恐慌 = 10, 观望 = 65;
  let 情绪 = ['观望'], 总结 = '散户观望', 含义 = '中性';
  
  // 地缘风险类
  if (title.includes('封锁') || title.includes('霍尔木兹') || emoji === '🔥') {
    追高 = 25; 抄底 = 5; 恐慌 = 55; 观望 = 15;
    情绪 = ['恐慌', '避险']; 总结 = '散户恐慌抛售'; 含义 = '风险加剧';
  }
  // 谈判/缓和类
  else if (title.includes('谈判') || title.includes('停火') || title.includes('恢复') || title.includes('施压')) {
    追高 = 35; 抄底 = 25; 恐慌 = 8; 观望 = 32;
    情绪 = ['谨慎', '关注']; 总结 = '散户谨慎观望，部分尝试抄底'; 含义 = '情绪修复';
  }
  // 科技/新能源利好
  else if (title.includes('宁德') || title.includes('创业板') || title.includes('锂矿') || title.includes('光模块') || emoji === '📈') {
    追高 = 75; 抄底 = 15; 恐慌 = 3; 观望 = 7;
    情绪 = ['FOMO', '亢奋']; 总结 = '散户疯了，都在追！'; 含义 = '顶部风险';
  }
  // GDP/经济数据
  else if (title.includes('GDP') || title.includes('超预期') || title.includes('创新高')) {
    追高 = 65; 抄底 = 20; 恐慌 = 5; 观望 = 10;
    情绪 = ['乐观', '积极']; 总结 = '散户情绪高涨，积极做多'; 含义 = '利好兑现';
  }
  // 黄金/原油/商品
  else if (title.includes('黄金') || title.includes('原油') || title.includes('铝') || emoji === '📊') {
    追高 = 40; 抄底 = 15; 恐慌 = 25; 观望 = 20;
    情绪 = ['避险', '纠结']; 总结 = '散户纠结，部分避险'; 含义 = '分歧加大';
  }
  // 医药
  else if (title.includes('医药') || title.includes('医疗')) {
    追高 = 45; 抄底 = 25; 恐慌 = 10; 观望 = 20;
    情绪 = ['关注', '轮动']; 总结 = '散户关注轮动机会'; 含义 = '板块轮动';
  }
  // 低空经济/新题材
  else if (title.includes('低空') || title.includes('招商')) {
    追高 = 55; 抄底 = 20; 恐慌 = 5; 观望 = 20;
    情绪 = ['兴奋', '新题材']; 总结 = '散户对新题材兴奋'; 含义 = '题材炒作';
  }
  // 默认
  else {
    情绪 = ['观望', '中性']; 总结 = '无明显情绪变化'; 含义 = '中性';
  }
  
  const 买入概率 = Math.round((追高 + 抄底) / 2);
  
  return {
    news: title,
    title: title,
    full_title: title,
    summary: '',
    追高买入概率: 追高,
    抄底买入概率: 抄底,
    恐慌卖出概率: 恐慌,
    观望概率: 观望,
    情绪标签: 情绪,
    韭菜行为总结: 总结,
    市场含义: 含义,
    买入概率: 买入概率,
    is_long_term: false,
    date: date,
    decay: 1.0,
    weighted_buy_prob: 买入概率
  };
}

function addCompleteSangsha(dateStr, content) {
  // 找到日期块
  const dateKey = '"' + dateStr + '": {';
  const datePos = content.indexOf(dateKey);
  if (datePos < 0) {
    console.log(dateStr + ': 找不到日期块');
    return content;
  }
  
  // 提取 all_news 数组中的所有新闻
  const allNewsStart = content.indexOf('"all_news": [', datePos);
  if (allNewsStart < 0) {
    console.log(dateStr + ': 找不到 all_news');
    return content;
  }
  
  // 找到 all_news 结束位置
  const allNewsEnd = content.indexOf('],', allNewsStart);
  if (allNewsEnd < 0) {
    console.log(dateStr + ': 找不到 all_news 结束');
    return content;
  }
  
  // 提取 all_news 块
  const allNewsBlock = content.substring(allNewsStart, allNewsEnd + 2);
  
  // 解析标题
  const titleMatches = allNewsBlock.match(/"title":\s*"([^"]+)"/g) || [];
  const emojiMatches = allNewsBlock.match(/"emoji":\s*"([^"]+)"/g) || [];
  
  const newsItems = titleMatches.map((t, i) => {
    const titleMatch = t.match(/"title":\s*"([^"]+)"/);
    const emojiMatch = emojiMatches[i] ? emojiMatches[i].match(/"emoji":\s*"([^"]+)"/) : null;
    return {
      title: titleMatch ? titleMatch[1] : '',
      emoji: emojiMatch ? emojiMatch[1] : ''
    };
  });
  
  console.log(dateStr + ': 提取到 ' + newsItems.length + ' 条 all_news');
  
  // 生成分析结果
  const analysisResults = newsItems.map(n => generateSangshaItem(n, dateStr));
  
  // 计算平均值
  const avgBuy = Math.round(analysisResults.reduce((s, r) => s + r.追高买入概率, 0) / analysisResults.length);
  const avgPanic = Math.round(analysisResults.reduce((s, r) => s + r.恐慌卖出概率, 0) / analysisResults.length);
  
  // 判断整体情绪
  let overall_sentiment = '平稳';
  let advice = '观望';
  if (avgBuy > 50) {
    overall_sentiment = '亢奋';
    advice = '注意追高风险';
  } else if (avgBuy > 35) {
    overall_sentiment = '积极';
    advice = '可适度参与';
  } else if (avgPanic > 40) {
    overall_sentiment = '恐慌';
    advice = '谨慎为主，等待企稳';
  }
  
  // 找到 s_level 位置插入（兼容 LF 和 CRLF）
  let sLevelPattern = '],\n  "s_level":';
  let sLevelPos = content.indexOf(sLevelPattern, datePos);
  if (sLevelPos < 0) {
    sLevelPattern = '],\r\n  "s_level":';
    sLevelPos = content.indexOf(sLevelPattern, datePos);
  }
  if (sLevelPos < 0) {
    console.log(dateStr + ': 找不到 s_level 插入点');
    return content;
  }
  
  // 构建完整的 sangsha_module（使用 LF 换行）
  // 注意：], 已经有逗号了，所以 sangsha_module 不需要开头加逗号
  // 但 sangsha_module 结尾需要逗号，因为后面还有 s_level
  const sangshaModule = `
  "sangsha_module": {
    "overall_sentiment": "${overall_sentiment}",
    "advice": "${advice}",
    "avg_buy_prob": ${avgBuy},
    "avg_panic_prob": ${avgPanic},
    "total_news_count": ${newsItems.length},
    "time_window": "当日全量",
    "analysis_results": ${JSON.stringify(analysisResults)}
  },`;
  
  // 在 ], 之后插入（], 后面已经有换行，直接插入 sangsha_module）
  // ],\n  "s_level": -> ],\n  "sangsha_module": {...},\n  "s_level":
  const insertAt = sLevelPos + 2; // 跳过 ],
  // sangshaModule 开头已有逗号，所以直接插入
  return content.substring(0, insertAt) + sangshaModule + content.substring(insertAt);
}

// 执行
let newContent = content;
newContent = addCompleteSangsha('2026-04-14', newContent);
newContent = addCompleteSangsha('2026-04-15', newContent);
newContent = addCompleteSangsha('2026-04-16', newContent);

fs.writeFileSync('C:\\Users\\asus\\temp-news-website\\news-data.js', newContent, 'utf-8');
console.log('Done! 文件已更新');
