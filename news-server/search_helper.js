const cp = require('child_process');
const script = 'D:\\QCLaw\\resources\\openclaw\\config\\skills\\online-search\\scripts\\prosearch.cjs';

const ft = Math.floor(Date.now()/1000) - 86400;
const tt = Math.floor(Date.now()/1000);

const searches = [
  {keyword: 'A股 今日财经新闻 4月9日', from_time: ft, to_time: tt, industry: 'news'},
  {keyword: '美股 纳斯达克 道琼斯 4月8日收盘', from_time: ft, to_time: tt, industry: 'news'},
  {keyword: '黄金 原油 大宗商品 4月9日', from_time: ft, to_time: tt, industry: 'news'},
  {keyword: 'AI 芯片 科技股 4月9日', from_time: ft, to_time: tt, industry: 'news'},
  {keyword: '人民币 汇率 北向资金 4月9日', from_time: ft, to_time: tt, industry: 'news'},
];

async function run() {
  for (const s of searches) {
    try {
      const r = cp.execSync(`node "${script}" '${JSON.stringify(s)}'`, {encoding:'utf8', timeout:15000});
      console.log(r);
    } catch(e) {
      console.error('Error for', s.keyword, e.message);
    }
  }
}

run();
