const { spawnSync } = require('child_process');
const path = require('path');
const scriptPath = path.join('D:', 'QCLaw', 'resources', 'openclaw', 'config', 'skills', 'online-search', 'scripts', 'prosearch.cjs');

const ft = Math.floor(Date.now()/1000) - 259200;
const tt = Math.floor(Date.now()/1000);

async function search(keyword) {
  const args = JSON.stringify({ keyword, from_time: ft, to_time: tt, industry: 'news' });
  const result = spawnSync('node', [scriptPath, args], { encoding: 'utf-8', maxBuffer: 10*1024*1024 });
  return result.stdout || result.stderr;
}

(async () => {
  const queries = [
    'A股 财经新闻 4月14日 2026',
    'A股 财经新闻 4月15日 2026',
    'A股 财经新闻 4月16日 2026',
    '美联储 黄金 原油 4月 2026',
    '半导体 AI芯片 特朗普 关税 4月 2026',
    '美伊 地缘 霍尔木兹 4月 2026',
    '港股 数字货币 稳定币 4月 2026',
  ];
  for (const q of queries) {
    console.log(`\n=== ${q} ===`);
    const r = await search(q);
    try {
      const parsed = JSON.parse(r);
      if (parsed.results) {
        parsed.results.slice(0, 8).forEach((item, i) => {
          console.log(`${i+1}. [${item.title}] ${(item.snippet||item.summary||'').substring(0,150)} | ${item.url||''}`);
        });
      } else {
        console.log(r.substring(0, 1000));
      }
    } catch(e) {
      console.log(r.substring(0, 1000));
    }
  }
})();
