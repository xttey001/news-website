let fs = require('fs');
let content = fs.readFileSync('news-data.js', 'utf8');
console.log('File size:', content.length);

// Find "2026-04-05": appearances
let all = [];
let idx = 0;
while ((idx = content.indexOf('"2026-04-05":', idx)) !== -1) {
    all.push(idx);
    idx += 1;
}
console.log('"2026-04-05": appears at positions:', all);

// Find "2026-04-06": appearances
let all6 = [];
idx = 0;
while ((idx = content.indexOf('"2026-04-06":', idx)) !== -1) {
    all6.push(idx);
    idx += 1;
}
console.log('"2026-04-06": appears at positions:', all6);

// Check around position 1000 (should be in the object)
console.log('\nAround position 1000:');
console.log(content.slice(990, 1050));
