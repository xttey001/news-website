const fs = require('fs');
const content = fs.readFileSync('C:\\Users\\asus\\temp-news-website\\news-data.js', 'utf-8');

// 找到 04-16 区块
const d16Start = content.indexOf('"2026-04-16":');
const d13Start = content.indexOf('"2026-04-13":');
const d16Block = content.substring(d16Start, d13Start);

// 找到第一个和第二个 sangsha_module
const first = d16Block.indexOf('sangsha_module');
const second = d16Block.indexOf('sangsha_module', first + 20);

console.log('Block length:', d16Block.length);
console.log('First sangsha_module at:', first);
console.log('Second sangsha_module at:', second);

// 检查第一个 sangsha_module 的内容
const firstEnd = d16Block.indexOf('},', first + 100);
console.log('\n=== First sangsha_module (前500字符) ===');
console.log(d16Block.substring(first, first + 500));

// 检查第二个 sangsha_module 的内容
const secondEnd = d16Block.indexOf('},', second + 100);
console.log('\n=== Second sangsha_module (前500字符) ===');
console.log(d16Block.substring(second, second + 500));
