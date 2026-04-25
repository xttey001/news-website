const fs = require('fs');
const content = fs.readFileSync('C:\\Users\\asus\\temp-news-website\\news-data.js', 'utf8');

// Count open/close braces in the file
let open = 0, close = 0;
for (let i = 0; i < content.length; i++) {
  if (content[i] === '{') open++;
  if (content[i] === '}') close++;
}
console.log('Opens: ' + open + ', Closes: ' + close);

// Find the structure around line 12293-12306
let lines = content.split('\n');
console.log('\nLines 12288-12310:');
lines.slice(12287, 12310).forEach(function(l, i) {
  console.log('  ' + (12288 + i) + ': ' + l);
});

// Also look at the whole tail
// Find "content" field
let contentIdx = content.indexOf('"content": "成交量');
console.log('\n"content" field at:', contentIdx);
if (contentIdx > 0) {
  console.log('Context: ' + JSON.stringify(content.substring(contentIdx - 100, contentIdx + 150)));
}

// And what comes after the last "}"
let idxEnd = content.lastIndexOf('};\r\n');
console.log('\nLast "};\n" at:', idxEnd);
if (idxEnd > 0) {
  console.log('Context: ' + JSON.stringify(content.substring(idxEnd - 50, idxEnd + 50)));
}

// What's between idxEnd and availableDates?
let afterSemi = content.substring(idxEnd + 3);
console.log('\nAfter "};": ' + JSON.stringify(afterSemi.substring(0, 200)));
