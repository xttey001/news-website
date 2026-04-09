// 从 c92c6b7 提取 4.05 的悟空/八戒字段
const { execSync } = require('child_process');
const fs = require('fs');

const raw = execSync('git show c92c6b7:news-data.js', { encoding: 'utf8', maxBuffer: 50*1024*1024 });

// 找到 4.05 块
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

function extractObject(str, marker) {
    const idx = str.indexOf(marker);
    if (idx === -1) return null;
    let brace = -1;
    for (let i = idx; i < str.length; i++) {
        if (str[i] === '{') { brace = i; break; }
    }
    if (brace === -1) return null;
    depth = 0;
    for (let i = brace; i < str.length; i++) {
        if (str[i] === '{') depth++;
        else if (str[i] === '}') { depth--; if (depth === 0) return str.slice(brace, i+1); }
    }
    return null;
}

function cleanParse(str) {
    if (!str) return null;
    let clean = str.replace(/\u201C/g, '"').replace(/\u201D/g, '"').replace(/'/g, '"');
    clean = clean.replace(/,(\s*[}\]])/g, '$1');
    try { return JSON.parse(clean); } catch { return null; }
}

const wkStr = extractObject(block, '"wukong_judgment":');
const bjStr = extractObject(block, '"bajie_bayesian":') || extractObject(block, '"bajie_conclusion":');
const sStr = extractObject(block, '"s_level":');
const marketTone = block.match(/"market_tone":\s*"([^"]+)"/)?.[1] || '';

console.log('wukong_judgment:', wkStr ? wkStr.length + ' chars' : 'NOT FOUND');
console.log('bajie_bayesian:', bjStr ? bjStr.length + ' chars' : 'NOT FOUND');
console.log('s_level:', sStr ? sStr.length + ' chars' : 'NOT FOUND');
console.log('market_tone:', marketTone.slice(0, 50));

const wk = cleanParse(wkStr);
const bj = cleanParse(bjStr);
const sLevel = cleanParse(sStr);

console.log('wukong:', wk ? 'OK' : 'FAILED');
console.log('bajie:', bj ? 'OK' : 'FAILED');

if (wk) {
    // 转换旧格式 bajie_bayesian -> bajie_conclusion
    const result = {
        wukong_judgment: wk,
        s_level: Array.isArray(sLevel) ? sLevel : []
    };
    
    if (bj) {
        // bajie_bayesian 旧格式转换为新格式
        result.bajie_conclusion = {
            optimal_action: bj.optimal_action || bj.optimalAction || '',
            optimal_etfs: bj.optimal_etfs || bj.optimalEtfs || '',
            win_rate: bj.win_rate || bj.posterior || bj.winRate || 'N/A',
            max_drawdown: bj.max_drawdown || bj.maxDrawdown || 'N/A',
            holding_period: bj.holding_period || bj.holdingPeriod || ''
        };
    }
    
    fs.writeFileSync('orig_20260405_full.json', JSON.stringify(result, null, 2), 'utf8');
    console.log('\nSaved orig_20260405_full.json!');
    console.log('Market sentiment:', wk.market_sentiment || wk.emotion || 'N/A');
} else {
    console.log('\nFailed to extract wukong_judgment');
}
