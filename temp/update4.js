// update-news.js - Clean update of news-data.js
const fs = require('fs');

const origPath = 'C:\\Users\\asus\\temp-news-website\\news-data.js';
const entryPath = 'C:\\Users\\asus\\.qclaw\\workspace\\temp\\_new_entry.js';
const outPath = 'C:\\Users\\asus\\temp-news-website\\news-data.js';

let content = fs.readFileSync(origPath, 'utf8');
let newEntry = fs.readFileSync(entryPath, 'utf8');

console.log('Original: ' + content.length + ' chars');
console.log('New entry: ' + newEntry.length + ' chars');
console.log('Has CRLF: ' + content.includes('\r\n'));

// 1. Update header timestamp
content = content.replace(
  /\/\/ 生成时间: \d{4}-\d{2}-\d{2} \d{2}:\d{2}/,
  '// 生成时间: 2026-04-24 08:00'
);

// 2. Find and replace "2026-04-22" block (CRLF-aware)
const markerStart = '"2026-04-22": {';
const markerEnd = '    "douyin": []\r\n  },';

let idxStart = content.indexOf(markerStart);
let idxEnd = content.lastIndexOf(markerEnd);

if (idxStart === -1 || idxEnd === -1) {
  console.log('ERROR: start=' + idxStart + ', end=' + idxEnd);
  process.exit(1);
}

console.log('Block start: ' + idxStart + ', end: ' + idxEnd);

// Fix newEntry line endings to CRLF
newEntry = newEntry.replace(/\n/g, '\r\n');

let remaining = content.substring(idxEnd + markerEnd.length);
console.log('Remaining starts: ' + JSON.stringify(remaining.substring(0, 50)));

// Build new content
let newContent = content.substring(0, idxStart) + newEntry + remaining;

fs.writeFileSync(outPath, newContent, 'utf8');
console.log('Written: ' + newContent.length + ' chars');

// 3. Update availableDates - first occurrence of 2026-04-22 -> 2026-04-24,2026-04-22
newContent = fs.readFileSync(outPath, 'utf8');
newContent = newContent.replace(
  /"2026-04-22",\r\n/,
  '"2026-04-24",\r\n        "2026-04-22",\r\n'
);
fs.writeFileSync(outPath, newContent, 'utf8');

// Verification
newContent = fs.readFileSync(outPath, 'utf8');
let lines = newContent.split('\n');
console.log('\nTotal lines: ' + lines.length);
console.log('2026-04-24 count: ' + (newContent.match(/"2026-04-24"/g) || []).length);
console.log('2026-04-22 count: ' + (newContent.match(/"2026-04-22"/g) || []).length);

console.log('\nFirst 6 lines:');
lines.slice(0, 6).forEach(function(l, i) { console.log('  ' + (i+1) + ': ' + l.substring(0, 80)); });

console.log('\nLast 6 lines:');
lines.slice(-6).forEach(function(l, i) { console.log('  ' + (lines.length-5+i) + ': ' + l.substring(0, 80)); });

// Check availableDates
let adMatch = newContent.match(/const availableDates = \[([^\]]+)\]/);
if (adMatch) {
  let dates = adMatch[1].split(',').slice(0, 3).map(function(d) { return d.trim().replace(/"/g, ''); });
  console.log('\nFirst 3 availableDates: ' + dates.join(', '));
}
