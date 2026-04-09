let fs = require('fs');
let content = fs.readFileSync('news-data.js', 'utf8');

// 找到所有日期的位置
let dates = ['2026-04-09', '2026-04-08', '2026-04-07', '2026-04-06', '2026-04-05', '2026-04-04'];
let positions = {};
for (let d of dates) {
    let idx = content.indexOf('"' + d + '":');
    if (idx !== -1) positions[d] = idx;
}
console.log('Date positions:');
for (let d of dates) {
    console.log(' ', d, ':', positions[d]);
}

// 找到 4.05 块
let idx050 = positions['2026-04-05'];
let idx060 = positions['2026-04-06'];
let idx040 = positions['2026-04-04'];

console.log('\n4.05 block should be from', idx050, 'to', idx060, '(next date after 4.05)');
let block = content.slice(idx050, idx060);
console.log('Block length:', block.length);
console.log('Has wukong:', block.includes('wukong_judgment'));
console.log('Has bajie:', block.includes('bajie_conclusion'));
console.log('First 200 chars:', block.slice(0, 200));
