const fs = require('fs');
const c = fs.readFileSync('C:\\Users\\asus\\temp-news-website\\news-data.js', 'utf8');
console.log('Has CRLF:', c.includes('\r\n'));
console.log('Index of start:', c.indexOf('"2026-04-22": {'));
console.log('LastIndexOf end (LF):', c.lastIndexOf('    "douyin": []\n  },'));
console.log('LastIndexOf end (CRLF):', c.lastIndexOf('    "douyin": []\r\n  },'));
// Check bytes around that area
let idx = c.lastIndexOf('    "douyin": []\r\n  },');
console.log('CRLF index:', idx);
if (idx > 0) {
  console.log('Chars before:', JSON.stringify(c.substring(idx-10, idx+20)));
}
