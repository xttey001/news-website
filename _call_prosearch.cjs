const { execSync } = require('child_process');
const path = require('path');

const FROM_TIME = Math.floor(Date.now()/1000) - 86400;
const TO_TIME = Math.floor(Date.now()/1000);

const searches = [
  '今日财经要闻 A股 2026年4月11日',
  '今日A股市场行情 2026年4月11日',
  '今日经济政策新闻 2026年4月',
  '黄金原油价格 2026年4月11日',
  '美股收盘 2026年4月10日'
];

const scriptPath = path.join('D:/QCLaw/resources/openclaw/config/skills/online-search/scripts/prosearch.cjs');

for (const kw of searches) {
  const body = JSON.stringify({ keyword: kw, from_time: FROM_TIME, to_time: TO_TIME, industry: 'news' });
  try {
    const result = execSync(`node "${scriptPath}" "${body.replace(/"/g, '\\"')}"`, { encoding: 'utf8', timeout: 15000 });
    console.log('=== SEARCH:', kw, '===');
    console.log(result);
  } catch (e) {
    console.error('ERROR for', kw, ':', e.message);
  }
}
