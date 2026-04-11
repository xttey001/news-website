const http = require('http');

const PROXY_PORT = process.env.AUTH_GATEWAY_PORT || '19000';
const PROXY_HOST = '127.0.0.1';
const API_PATH = '/proxy/prosearch/search';
const REQUEST_TIMEOUT = 15000;

// 搜索关键词
const keywords = [
  'A股 上证指数 深证成指 今日行情',
  '科技股 芯片 人工智能 今日',
  '新能源 锂电池 光伏 今日',
  '金融 银行 保险 券商 今日',
  '黄金 原油 大宗商品 今日'
];

async function search(keyword) {
  const body = JSON.stringify({ keyword, industry: 'news' });
  
  return new Promise((resolve, reject) => {
    const req = http.request(
      {
        host: PROXY_HOST,
        port: Number(PROXY_PORT),
        path: API_PATH,
        method: 'POST',
        timeout: REQUEST_TIMEOUT,
        headers: {
          'Content-Type': 'application/json',
          'Content-Length': Buffer.byteLength(body),
        },
      },
      (res) => {
        let data = '';
        res.setEncoding('utf8');
        res.on('data', (chunk) => { data += chunk; });
        res.on('end', () => {
          try {
            const result = JSON.parse(data);
            resolve(result);
          } catch (e) {
            resolve({ success: false, message: e.message });
          }
        });
      }
    );

    req.on('timeout', () => {
      req.destroy();
      resolve({ success: false, message: 'timeout' });
    });

    req.on('error', (err) => {
      resolve({ success: false, message: err.message });
    });

    req.write(body);
    req.end();
  });
}

async function main() {
  const allResults = [];
  
  for (const keyword of keywords) {
    console.log(`\n搜索: ${keyword}`);
    const result = await search(keyword);
    
    if (result.success) {
      console.log('成功');
      allResults.push({ keyword, result });
    } else {
      console.log('失败:', result.message);
    }
  }
  
  // 保存结果
  const fs = require('fs');
  fs.writeFileSync('search_results.json', JSON.stringify(allResults, null, 2), 'utf-8');
  console.log('\n结果已保存到 search_results.json');
}

main();
