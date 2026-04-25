const fs = require('fs');
const c = fs.readFileSync('C:\\Users\\asus\\temp-news-website\\news-data.js', 'utf-8');

// 检查三个日期的 sangsha_module
const dates = ['2026-04-14', '2026-04-15', '2026-04-16'];

dates.forEach(d => {
  const datePos = c.indexOf('"' + d + '"');
  const sgPos = c.indexOf('sangsha_module', datePos);
  
  if (sgPos > 0) {
    // 提取 sangsha_module 的关键字段
    const sgBlock = c.substring(sgPos, sgPos + 800);
    
    const totalMatch = sgBlock.match(/"total_news_count":\s*(\d+)/);
    const resultsMatch = sgBlock.match(/"analysis_results":\s*\[/);
    
    console.log(d + ':');
    console.log('  total_news_count:', totalMatch ? totalMatch[1] : 'NOT FOUND');
    console.log('  has analysis_results:', resultsMatch ? 'YES' : 'NO');
    
    // 检查第一条分析
    const firstResult = sgBlock.match(/"韭菜行为总结":\s*"([^"]+)"/);
    console.log('  韭菜行为总结样例:', firstResult ? firstResult[1] : 'NOT FOUND');
  } else {
    console.log(d + ': NOT FOUND');
  }
});