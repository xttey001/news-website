const http = require('http');

const PROXY_PORT = process.env.AUTH_GATEWAY_PORT || '19000';
const PROXY_HOST = '127.0.0.1';
const API_PATH = '/proxy/prosearch/search';
const REQUEST_TIMEOUT = 15000;

const params = {
  keyword: 'A股 2026年4月8日',
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