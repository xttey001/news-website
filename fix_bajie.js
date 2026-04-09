// 提取完整的4.05八戒数据
const { execSync } = require('child_process');
const fs = require('fs');

const raw = execSync('git show c92c6b7:news-data.js', { encoding: 'utf8', maxBuffer: 50*1024*1024 });

const startIdx = raw.indexOf('"2026-04-05":');
let braceStart = -1;
for (let i = startIdx; i < raw.length; i++) {
    if (raw[i] === '{') { braceStart = i; break; }
}
let depth = 0, endIdx = braceStart;
for (let i = braceStart; i < raw.length; i++) {
    if (raw[i] === '{') depth++;
    else if (raw[i] === '}') { depth--; if (depth === 0) { endIdx = i+1; break; } }
}
const block = raw.slice(braceStart, endIdx);

// 简单直接提取
const bestAction = (block.match(/"best_action":\s*"([^"]+)"/) || [])[1] || '';
const bestEtfs = (block.match(/"best_etfs":\s*"([^"]+)"/) || [])[1] || '';
const winRate = (block.match(/"win_rate":\s*(\d+)/) || [])[1] || '';
const stopLoss = (block.match(/"stop_loss":\s*(-?\d+)/) || [])[1] || '';
const holdingPeriod = (block.match(/"holding_period":\s*"([^"]+)"/) || [])[1] || '';
const conclusion = (block.match(/"conclusion":\s*"([^"]+)"/) || [])[1] || '';

console.log('best_action:', bestAction.slice(0, 80));
console.log('best_etfs:', bestEtfs.slice(0, 80));
console.log('win_rate:', winRate);
console.log('stop_loss:', stopLoss);
console.log('holding_period:', holdingPeriod);
console.log('conclusion:', conclusion.slice(0, 80));

const newBj = {
    optimal_action: bestAction,
    optimal_etfs: bestEtfs,
    win_rate: '~' + winRate + '%',
    max_drawdown: stopLoss + '%',
    holding_period: holdingPeriod,
    conclusion: conclusion
};

const origData = JSON.parse(fs.readFileSync('orig_20260405_full.json', 'utf8'));
origData.bajie_conclusion = newBj;
fs.writeFileSync('orig_20260405_full.json', JSON.stringify(origData, null, 2), 'utf8');
console.log('\nSaved!');
