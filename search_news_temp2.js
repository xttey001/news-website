const { spawnSync } = require('child_process');
const path = require('path');
const scriptPath = path.join('D:', 'QCLaw', 'resources', 'openclaw', 'config', 'skills', 'online-search', 'scripts', 'prosearch.cjs');

const ft = Math.floor(Date.now()/1000) - 259200;
const tt = Math.floor(Date.now()/1000);

function search(keyword) {
  const args = JSON.stringify({ keyword, from_time: ft, to_time: tt, industry: 'news' });
  const result = spawnSync('node', [scriptPath, args], { encoding: 'utf-8', maxBuffer: 10*1024*1024 });
  return result.stdout || result.stderr;
}

const queries = [
  '一季度GDP 经济数据 4月16日 2026',
  '宁德时代 历史新高 4月16日',
  '霍尔木兹海峡 恢复通航 4月14日 2026',
  'A股 创业板 大涨 4月16日',
  '黄金价格 4月14日 4月15日 2026',
  '包钢 爆炸 容百科技 4月 2026',
  '低空经济 国资委 4月15日 2026',
  '特斯拉 半导体 AI 4月 2026',
];

for (const q of queries) {
  console.log(`\n=== ${q} ===`);
  const r = search(q);
  try {
    const parsed = JSON.parse(r);
    if (parsed.results) {
      parsed.results.slice(0, 5).forEach((item, i) => {
        console.log(`${i+1}. [${item.title}] ${(item.snippet||item.summary||'').substring(0,200)}`);
      });
    } else if (parsed.message) {
      console.log(parsed.message.substring(0, 500));
    }
  } catch(e) {
    console.log(r.substring(0, 500));
  }
}
