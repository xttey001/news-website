let fs = require('fs');
let content = fs.readFileSync('news-data.js', 'utf8');
let idx = content.indexOf('"2026-04-05":');
let nextIdx = content.indexOf('"2026-04-04":');
console.log('idx:', idx, 'nextIdx:', nextIdx);
if (nextIdx === -1) {
    // 找下一个日期
    let after = content.indexOf('"2026-04-06":');
    console.log('4.06 at:', after);
    let after2 = content.indexOf('"2026-04-08":');
    console.log('4.08 at:', after2);
}
