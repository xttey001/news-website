const fs = require('fs');
const content = fs.readFileSync('C:\\Users\\asus\\temp-news-website\\news-data.js', 'utf8');

// Find the last date block end
const markerEnd = '    "douyin": []\r\n  },';
const idxEnd = content.lastIndexOf(markerEnd);
console.log('idxEnd:', idxEnd);

// Find the content after
const afterEnd = content.substring(idxEnd + markerEnd.length);
console.log('After end (' + afterEnd.length + ' chars):');
console.log(JSON.stringify(afterEnd.substring(0, 200)));

// Also look for "newsData" closing
const closeIdx = content.indexOf('};\n', idxEnd);
if (closeIdx >= 0) {
  console.log('\nFound }; at:', closeIdx);
  console.log('Chars around };:');
  console.log(JSON.stringify(content.substring(closeIdx - 20, closeIdx + 30)));
}

// Count occurrences of }; in content
let count = 0;
for (let i = content.indexOf('};', idxEnd); i >= 0; i = content.indexOf('};', i + 1)) {
  if (i >= idxEnd) { count++; console.log('}; at:', i, '->', JSON.stringify(content.substring(i, i+20))); }
}
console.log('Total }; after idxEnd:', count);

// Find all lines near the end
let lines = content.split('\n');
console.log('\nLast 20 lines:');
lines.slice(-20).forEach(function(l, i) { console.log('  ' + (lines.length-19+i) + ': |' + l + '|'); });
