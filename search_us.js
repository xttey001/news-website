const http = require('http');

const PROXY_PORT = process.env.AUTH_GATEWAY_PORT || '19000';
const PROXY_HOST = '127.0.0.1';
const API_PATH = '/proxy/prosearch/search';
const REQUEST_TIMEOUT = 15000;

const body = {
  keyword: "美股行情 科技股 最新",
  industry: "news"
};

const requestBody = JSON.stringify(body);

const req = http.request(
  {
    host: PROXY_HOST,
    port: Number(PROXY_PORT),
    path: API_PATH,
    method: 'POST',
    timeout: REQUEST_TIMEOUT,
    headers: {
      'Content-Type': 'application/json',
      'Content-Length': Buffer.byteLength(requestBody),
    },
  },
  (res) => {
    let data = '';
    res.setEncoding('utf8');
    res.on('data', (chunk) => {
      data += chunk;
    });
    res.on('end', () => {
      console.log(data);
    });
  }
);

req.on('timeout', () => {
  req.destroy();
  console.log(JSON.stringify({ success: false, message: '搜索请求超时' }));
  process.exit(1);
});

req.on('error', (err) => {
  console.log(JSON.stringify({ success: false, message: err.message }));
  process.exit(1);
});

req.write(requestBody);
req.end();
