const fs = require('fs');
const content = fs.readFileSync('C:\\Users\\asus\\temp-news-website\\news-data.js', 'utf-8');

const dates = ['2026-04-14', '2026-04-15', '2026-04-16'];

dates.forEach((date, di) => {
  const keyPattern = '"' + date + '": {';
  const keyPos = content.indexOf(keyPattern);
  if (keyPos < 0) { console.log(date + ': NOT FOUND'); return; }
  
  // Find next date key to bound this block
  let endPos = content.length;
  const nextDates = dates.filter((_, i) => i > di).map(d => '"' + d + '":');
  const otherDates = ['"2026-04-13":', '"2026-04-12":', '"2026-04-11":', '"2026-04-10":'];
  [...nextDates, ...otherDates].forEach(nd => {
    const p = content.indexOf(nd, keyPos + 20);
    if (p > 0 && p < endPos) endPos = p;
  });
  
  const block = content.substring(keyPos, endPos);
  const hasSangsha = block.includes('"sangsha_module"');
  const hasAnalysisResults = block.includes('"analysis_results"');
  const hasZhuigao = block.includes('追高买入概率');
  const allNewsCount = (block.match(/"title":/g) || []).length;
  
  console.log(date + ':');
  console.log('  block size: ' + block.length);
  console.log('  sangsha_module: ' + hasSangsha);
  console.log('  analysis_results: ' + hasAnalysisResults);
  console.log('  has 追高买入概率: ' + hasZhuigao);
  console.log('  news items (title count): ' + allNewsCount);
});
