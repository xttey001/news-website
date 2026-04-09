// 注入4.05悟空/八戒到news-data.js
const fs = require('fs');

// 读取悟空/八戒数据
const wkData = JSON.parse(fs.readFileSync('orig_20260405_full.json', 'utf8'));
const wk = wkData.wukong_judgment;
const bj = wkData.bajie_conclusion;
console.log('悟空:', wk?.market_sentiment || wk?.emotion || 'N/A');
console.log('八戒:', bj?.optimal_action || 'N/A');

// 读取 news-data.js
const content = fs.readFileSync('news-data.js', 'utf8');

// 找到 newsData = ... const availableDates
const match = content.match(/const newsData = ({[\s\S]*?});?\s*const availableDates/);
if (!match) { console.log('Cannot find newsData!'); process.exit(1); }

const jsonStr = match[1]
    .replace(/,\s*([}\]])/g, '$1')  // 移除尾随逗号
    .replace(/'([^']+)'/g, '"$1"')  // 单引号转双引号
    .replace(/"/g, '"')
    .replace(/\u201C/g, '"')
    .replace(/\u201D/g, '"');

let newsData;
try {
    newsData = JSON.parse(jsonStr);
} catch(e) {
    console.log('JSON parse failed:', e.message);
    // 尝试提取4.05单独更新
    const idx050 = content.indexOf('"2026-04-05":');
    const idx040 = content.indexOf('"2026-04-04":');
    const block = content.slice(idx050, idx040);
    console.log('4.05 block has wukong:', block.includes('wukong_judgment'));
    process.exit(1);
}

console.log(`Parsed: ${Object.keys(newsData).length} dates`);

// 更新4.05
if (newsData['2026-04-05']) {
    newsData['2026-04-05'].wukong_judgment = wk;
    newsData['2026-04-05'].bajie_conclusion = bj;
    console.log('Updated 2026-04-05');
} else {
    console.log('2026-04-05 not found!');
    process.exit(1);
}

// 生成新文件
const sortedDates = Object.keys(newsData).sort().reverse();
const newContent = 'const newsData = ' + JSON.stringify(newsData, null, 2) + ';\n\n'
    + 'const availableDates = ' + JSON.stringify(sortedDates) + ';\n\n'
    + 'function getNews(date) { return newsData[date] || null; }\n'
    + 'function getPreviousDate(date) { const idx = availableDates.indexOf(date); return idx < availableDates.length - 1 ? availableDates[idx + 1] : null; }\n'
    + 'function getNextDate(date) { const idx = availableDates.indexOf(date); return idx > 0 ? availableDates[idx - 1] : null; }';

fs.writeFileSync('news-data.js', newContent, 'utf8');
console.log('Saved news-data.js');

// 验证
const { execSync } = require('child_process');
try {
    execSync('node --check news-data.js', { encoding: 'utf8' });
    console.log('JS语法验证: OK');
} catch(e) {
    console.log('JS语法错误:', e.stderr || e.message);
}

// 最终验证4.05
const d = newsData['2026-04-05'];
console.log('\n2026-04-05 验证:');
console.log('  悟空:', !!d.wukong_judgment, '- sentiment:', d.wukong_judgment?.market_sentiment || d.wukong_judgment?.emotion);
console.log('  八戒:', !!d.bajie_conclusion, '- action:', d.bajie_conclusion?.optimal_action?.slice(0,30));
