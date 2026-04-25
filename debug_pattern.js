const fs = require('fs');
const c = fs.readFileSync('C:\\Users\\asus\\temp-news-website\\news-data.js', 'utf-8');
const d14 = c.indexOf('2026-04-14');
const sub = c.substring(d14, d14 + 2500);

// Find pattern: ], then CRLF, then 2 spaces, then "
const pattern = '],\r\n  "';
const p = sub.indexOf(pattern);
console.log('Pattern "],\\r\\n  \"" found at:', p);
if (p > 0) {
  console.log('Context:', sub.substring(p, p + 30).replace(/\r\n/g, '\\r\\n'));
}
