const http = require('http');

const PORT = process.env.AUTH_GATEWAY_PORT || '19000';
const HOST = '127.0.0.1';
const API_PATH = '/proxy/prosearch/search';
const FROM_TIME = Math.floor(Date.now()/1000) - 86400;
const TO_TIME = Math.floor(Date.now()/1000);

const searches = [
  '今日财经要闻 A股 2026年4月11日',
  '今日A股市场行情 2026年4月11日',
  '黄金原油价格 2026年4月11日',
  '美股收盘 2026年4月10日',
  '人民币汇率 2026年4月11日',
  '央行货币政策 2026年4月',
  'A股板块涨跌 2026年4月11日',
  '北向资金 2026年4月11日'
];

function doSearch(keyword) {
  return new Promise((resolve, reject) => {
    const body = JSON.stringify({ keyword, from_time: FROM_TIME, to_time: TO_TIME, industry: 'news' });
    const req = http.request({
      host: HOST,
      port: Number(PORT),
      path: API_PATH,
      method: 'POST',
      timeout: 15000,
      headers: { 'Content-Type': 'application/json', 'Content-Length': Buffer.byteLength(body) }
    }, (res) => {
      let data = '';
      res.on('data', d => data += d);
      res.on('end', () => resolve(data));
    });
    req.on('error', reject);
    req.setTimeout(15000, () => { req.destroy(); reject(new Error('timeout')); });
    req.write(body);
    req.end();
  });
}

(async () => {
  for (const kw of searches) {
    try {
      const result = await doSearch(kw);
      const parsed = JSON.parse(result);
      console.log('\n=== SEARCH:', kw, '===');
      if (parsed.success) {
        console.log(parsed.message || JSON.stringify(parsed.data).slice(0, 1000));
      } else {
        console.log('Error:', parsed.message);
      }
    } catch (e) {
      console.error('ERROR for', kw, ':', e.message);
    }
  }
})();
