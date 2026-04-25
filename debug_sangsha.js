const fs = require('fs');
const c = fs.readFileSync('C:\\Users\\asus\\temp-news-website\\news-data.js', 'utf-8');

// 检查 04-16 的 sangsha_module
const d16 = c.indexOf('"2026-04-16":');
const sg = c.indexOf('sangsha_module', d16);
const sgEnd = c.indexOf('},', sg + 1000);

const sgBlock = c.substring(sg, sgEnd + 20);
console.log('=== 04-16 sangsha_module 前500字符 ===');
console.log(sgBlock.substring(0, 500));

// 提取 analysis_results 的第一条
const arStart = sgBlock.indexOf('"analysis_results":');
const firstTitle = sgBlock.match(/"title":"([^"]+)"/);
const firstFullTitle = sgBlock.match(/"full_title":"([^"]+)"/);

console.log('\n=== 第一条新闻 ===');
console.log('title:', firstTitle ? firstTitle[1].substring(0, 50) : 'NOT FOUND');
console.log('full_title:', firstFullTitle ? firstFullTitle[1].substring(0, 50) : 'NOT FOUND');
