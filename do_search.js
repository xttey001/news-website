const http = require('http');
const fs = require('fs');

const from = Math.floor(Date.now()/1000) - 86400;
const to = Math.floor(Date.now()/1000);

const searches = [
  {keyword:'A股 4月7日 复牌 清明节后',from_time:from,to_time:to,industry:'news'},
  {keyword:'北向资金 今日',from_time:from,to_time:to,industry:'news'},
  {keyword:'美伊停火协议',from_time:from,to_time:to,industry:'news'},
  {keyword:'比特币70000美元',from_time:from,to_time:to,industry:'news'},
  {keyword:'英伟达股价',from_time:from,to_time:to,industry:'news'}
];

const PORT = process.env.AUTH_GATEWAY_PORT || '19000';

async function search(params) {
  return new Promise((resolve) => {
    const body = JSON.stringify(params);
    const req = http.request({
      host: '127.0.0.1',
      port: Number(PORT),
      path: '/proxy/prosearch/search',
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(body),
      },
    }, (res) => {
      let data = '';
      res.setEncoding('utf8');
      res.on('data', (chunk) => { data += chunk; });
      res.on('end', () => { resolve(JSON.parse(data)); });
    });
    req.on('error', (err) => { resolve({success:false,message:err.message}); });
    req.write(body);
    req.end();
  });
}

(async () => {
  const results = [];
  for (const s of searches) {
    const r = await search(s);
    if (r.success && r.data && r.data.docs && r.data.docs.length > 0) {
      results.push({
        keyword: s.keyword,
        count: r.data.docs.length,
        docs: r.data.docs.slice(0, 8).map(d => ({
          title: d.title,
          url: d.url,
          site: d.site,
          date: d.date,
          passage: d.passage?.substring(0, 300)
        }))
      });
    }
  }
  fs.writeFileSync('news_results.json', JSON.stringify(results, null, 2));
  console.log(JSON.stringify(results, null, 2));
})();
