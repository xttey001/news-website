const fs = require('fs');
const content = fs.readFileSync('C:\\Users\\asus\\temp-news-website\\news-data.js', 'utf-8');

['2026-04-14', '2026-04-15', '2026-04-16'].forEach(date => {
  const dateStart = content.indexOf(`"${date}":`);
  const nextDateStart = content.indexOf('"2026-04-13":', dateStart);

  let nextDate = nextDateStart;
  if (date === '2026-04-16') {
    // 04-16 后面是 04-13
    nextDate = nextDateStart;
  } else if (date === '2026-04-15') {
    nextDate = content.indexOf('"2026-04-16":', dateStart);
  } else {
    nextDate = content.indexOf('"2026-04-15":', dateStart);
  }

  const block = content.substring(dateStart, nextDate < 0 ? content.length : nextDate);

  // 检查 sangsha_module 数量
  const matches = block.match(/sangsha_module/g);
  console.log(date + ': sangsha_module count =', matches ? matches.length : 0);

  // 检查是否有 title 字段
  if (block.includes('sangsha_module')) {
    const sgStart = block.indexOf('sangsha_module');
    const sgEnd = block.indexOf('},', sgStart + 500);
    const sgBlock = block.substring(sgStart, sgEnd > 0 ? sgEnd + 5 : sgStart + 1000);

    const hasTitle = sgBlock.includes('"title"');
    const hasFullTitle = sgBlock.includes('"full_title"');
    const has韭菜总结 = sgBlock.includes('韭菜行为总结');

    console.log('  has title:', hasTitle);
    console.log('  has full_title:', hasFullTitle);
    console.log('  has 韭菜行为总结:', has韭菜总结);

    // 提取第一条新闻标题
    const titleMatch = sgBlock.match(/"title":"([^"]+)"/);
    if (titleMatch) {
      console.log('  first news title:', titleMatch[1].substring(0, 30) + '...');
    }
  }
});
