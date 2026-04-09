// 验证 4.05 数据
let fs = require('fs');
let content = fs.readFileSync('news-data.js', 'utf8');
let idx = content.indexOf('"2026-04-05":');
let nextIdx = content.indexOf('"2026-04-04":');
let block = content.slice(idx, nextIdx);
console.log('wukong_judgment:', block.includes('wukong_judgment') ? 'YES' : 'NO');
console.log('bajie_conclusion:', block.includes('bajie_conclusion') ? 'YES' : 'NO');
console.log('market_sentiment:', (block.match(/"market_sentiment":\s*"([^"]+)"/) || [])[1] || 'N/A');
console.log('optimal_action:', (block.match(/"optimal_action":\s*"([^"]+)"/) || [])[1] || 'N/A');
