const fs = require('fs');
const content = fs.readFileSync('C:\\Users\\asus\\temp-news-website\\news-data.js', 'utf-8');

// 检查是否包含新的关键字段
console.log('=== 检查news-data.js内容 ===');
console.log('文件大小:', (content.length / 1024).toFixed(1), 'KB');

// 检查2026-04-16的数据
const hasDate = content.includes('"2026-04-16"');
console.log('包含2026-04-16:', hasDate ? 'YES' : 'NO');

const hasBayes = content.includes('"bayes_analysis"');
console.log('包含bayes_analysis:', hasBayes ? 'YES' : 'NO');

const hasDecisionMatrix = content.includes('"decision_matrix"');
console.log('包含decision_matrix:', hasDecisionMatrix ? 'YES' : 'NO');

const hasSangsha = content.includes('"sangsha_module"');
console.log('包含sangsha_module:', hasSangsha ? 'YES' : 'NO');

const hasWhiteDragon = content.includes('"white_dragon"');
console.log('包含white_dragon:', hasWhiteDragon ? 'YES' : 'NO');

const hasTangSanzang = content.includes('"tang_sanzang"');
console.log('包含tang_sanzang:', hasTangSanzang ? 'YES' : 'NO');

// 提取availableDates
const datesMatch = content.match(/const availableDates = \[([^\]]+)\]/);
if (datesMatch) {
  console.log('\navailableDates:', datesMatch[1].substring(0, 200));
}

// 检查2026-04-16的决策矩阵
if (hasDecisionMatrix) {
  const dmMatch = content.match(/"decision_matrix":\s*\[([^\]]+\])/);
  if (dmMatch) {
    console.log('\n决策矩阵样例:', dmMatch[0].substring(0, 300));
  }
}
