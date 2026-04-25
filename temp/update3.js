// update-news.js - Clean update of news-data.js
const fs = require('fs');
const path = require('path');

const origPath = 'C:\\Users\\asus\\temp-news-website\\news-data.js';
const entryPath = 'C:\\Users\\asus\\.qclaw\\workspace\\temp\\_new_entry.js';
const outPath = 'C:\\Users\\asus\\temp-news-website\\news-data.js';

let content = fs.readFileSync(origPath, 'utf8');
let newEntry = fs.readFileSync(entryPath, 'utf8');

console.log(`Original: ${content.length} chars`);
console.log(`New entry: ${newEntry.length} chars`);

// 1. Update header timestamp
content = content.replace(
  /\/\/ 生成时间: \d{4}-\d{2}-\d{2} \d{2}:\d{2}/,
  '// 生成时间: 2026-04-24 08:00'
);

// 2. Find and replace "2026-04-22" block
// The block starts with "2026-04-22": { and ends with:
//     "douyin": []
//   },
const markerStart = '"2026-04-22": {';
const markerEnd = '    "douyin": []\n  },';

let idxStart = content.indexOf(markerStart);
let idxEnd = content.lastIndexOf(markerEnd);

if (idxStart === -1 || idxEnd === -1) {
  console.log(`ERROR: start=${idxStart}, end=${idxEnd}`);
  process.exit(1);
}

console.log(`Block start: ${idxStart}, end: ${idxEnd}`);

// The block we want to replace: from idxStart to idxEnd + markerEnd.length
let oldBlock = content.substring(idxStart, idxEnd + markerEnd.length);
console.log(`Old block: ${oldBlock.length} chars`);

// New entry already ends with "},\n" - need to add proper closing
// After the block, the content should end with "  }\n};\n"
let remaining = content.substring(idxEnd + markerEnd.length);
console.log(`Remaining: "${remaining.substring(0, 50)}"`);

// Verify remaining ends with the closing
if (remaining.trim() !== '};\n' && !remaining.trim().startsWith('}')) {
  // It might have more content
  console.log(`Remaining content: "${remaining.substring(0, 100)}"`);
}

// Build new content
let newContent = content.substring(0, idxStart) + newEntry + remaining;

fs.writeFileSync(outPath, newContent, 'utf8');
console.log(`Written: ${newContent.length} chars`);

// 3. Update availableDates - first occurrence of 2026-04-22 -> 2026-04-24,2026-04-22
newContent = fs.readFileSync(outPath, 'utf8');
newContent = newContent.replace(
  /"2026-04-22"(,\s*"?)/,
  '"2026-04-24",\n        "2026-04-22"$1'
);
fs.writeFileSync(outPath, newContent, 'utf8');

// Verification
let lines = newContent.split('\n');
console.log(`\nTotal lines: ${lines.length}`);
console.log(`2026-04-24 count: ${(newContent.match(/"2026-04-24"/g) || []).length}`);
console.log(`2026-04-22 count: ${(newContent.match(/"2026-04-22"/g) || []).length}`);

console.log('\nFirst 6 lines:');
lines.slice(0, 6).forEach((l, i) => console.log(`  ${i+1}: ${l.substring(0, 80)}`));

console.log('\nLast 6 lines:');
lines.slice(-6).forEach((l, i) => console.log(`  ${lines.length-5+i}: ${l.substring(0, 80)}`));

// Check availableDates
let adMatch = newContent.match(/const availableDates = \[([^\]]+)\]/);
if (adMatch) {
  let dates = adMatch[1].split(',').slice(0, 3).map(d => d.trim().replace(/"/g, ''));
  console.log(`\nFirst 3 availableDates: ${dates.join(', ')}`);
}
