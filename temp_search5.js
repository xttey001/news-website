const http = require('http');

const PROXY_PORT = process.env.AUTH_GATEWAY_PORT || '19000';
const PROXY_HOST = '127.0.0.1';
const API_PATH = '/proxy/prosearch/search';

// 计算今天和昨天的时间戳
const now = Date.now();
const oneDayAgo = now - 86400 * 1000;
const twoDaysAgo = now - 86400 * 2 * 1000;

const params = {
  keyword: 'A股 今日收盘 4月',
  from_time: Math.floor(twoDaysAgo / 1000),
  to_time: Math.floor(now / 1000),
  industry: 'news'
};

const body = JSON.stringify(params);

const options = {
  hostname: PROXY_HOST,
  port: PROXY_PORT,
  path: API_PATH,
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': Buffer.byteLength(body)
  }
};

const req = http.request(options, (res) => {
  let data = '';
  res.on('data', (chunk) => data += chunk);
  res.on('end', () => console.log(data));
});

req.on('error', (e) => console.log(JSON.stringify({success: false, message: e.message})));
req.write(body);
req.end();