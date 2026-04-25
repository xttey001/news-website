const fs = require('fs');
const content = fs.readFileSync('C:\\Users\\asus\\temp-news-website\\review.html', 'utf-8');
const idx = content.indexOf('id="report-apr"');
const start = Math.max(0, idx - 100);
const end = Math.min(content.length, idx + 3000);
console.log('Context around report-apr:');
console.log('---');
console.log(content.substring(start, end));
