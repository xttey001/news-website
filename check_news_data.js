const fs = require('fs');
const vm = require('vm');
const code = fs.readFileSync('C:\\Users\\asus\\temp-news-website\\news-data.js', 'utf-8');

// 使用vm执行代码并获取newsData
const context = { console, exports: {}, module: { exports: {} } };
vm.createContext(context);
vm.runInContext(code, context);

const newsData = context.newsData;

console.log('=== 2026-04-16 数据检查 ===');
const d = newsData['2026-04-16'];
console.log('Keys:', Object.keys(d).join(', '));
console.log('Has bayes_analysis:', d.s_level && d.s_level[0] && d.s_level[0].bayes_analysis ? 'YES' : 'NO');
console.log('Has decision_matrix:', d.decision_matrix ? 'YES' : 'NO');
console.log('Has sangsha_module:', d.sangsha_module ? 'YES' : 'NO');
console.log('Has white_dragon:', d.white_dragon ? 'YES' : 'NO');
console.log('Has tang_sanzang:', d.tang_sanzang ? 'YES' : 'NO');

if (d.s_level && d.s_level[0] && d.s_level[0].bayes_analysis) {
  console.log('\n=== 第一条S级新闻贝叶斯分析 ===');
  console.log('Prior prob:', d.s_level[0].bayes_analysis.prior_prob);
  console.log('Posterior:', d.s_level[0].bayes_analysis.posterior);
  console.log('Expected return:', d.s_level[0].bayes_analysis.expected_return);
}

if (d.decision_matrix) {
  console.log('\n=== 决策矩阵 ===');
  d.decision_matrix.forEach(row => {
    console.log(`${row.新闻}: ${row.做多概率} → ${row.建议}`);
  });
}

if (d.tang_sanzang) {
  console.log('\n=== 唐僧仲裁 ===');
  console.log('仓位:', d.tang_sanzang.仓位);
  console.log('行动:', d.tang_sanzang.最终行动);
}
