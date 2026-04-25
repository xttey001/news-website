const fs = require('fs');
let content = fs.readFileSync('C:\\Users\\asus\\temp-news-website\\news-data.js', 'utf-8');

// 处理每个日期：删除第二个 sangsha_module
const dates = ['2026-04-14', '2026-04-15', '2026-04-16'];

dates.forEach(date => {
  const dateStart = content.indexOf(`"${date}":`);
  if (dateStart < 0) {
    console.log(date + ': NOT FOUND');
    return;
  }

  // 找到下一个日期的开始位置
  let nextDateStart = content.length;
  for (let i = dateStart + 10; i < content.length - 15; i++) {
    if (content.substring(i, i + 8).match(/"\d{4}-\d{2}-\d{2}":/)) {
      nextDateStart = content.lastIndexOf('"', i);
      break;
    }
  }

  const block = content.substring(dateStart, nextDateStart);

  // 找到所有 sangsha_module 的位置
  let positions = [];
  let pos = 0;
  while (true) {
    const idx = block.indexOf('sangsha_module', pos);
    if (idx < 0) break;
    positions.push(idx);
    pos = idx + 10;
  }

  if (positions.length > 1) {
    console.log(date + ': Found ' + positions.length + ' sangsha_module');

    // 找到第二个 sangsha_module 的完整内容并删除
    const secondStart = positions[1];
    const secondBlockStart = block.lastIndexOf('"', secondStart);

    // 找到第二个 sangsha_module 的结束位置（下一个逗号和换行）
    let secondEnd = block.indexOf('\n  },', secondStart + 20);
    if (secondEnd < 0) {
      secondEnd = block.indexOf('\n  "white_dragon"', secondStart);
      if (secondEnd > 0) {
        // 回退到前面的 },
        secondEnd = block.lastIndexOf('\n  },', secondEnd);
      }
    }
    if (secondEnd < 0) {
      secondEnd = block.indexOf('\n  "tang_sanzang"', secondStart);
      if (secondEnd > 0) {
        secondEnd = block.lastIndexOf('\n  },', secondEnd);
      }
    }

    if (secondEnd > 0) {
      // 删除第二个 sangsha_module（包括前面的逗号和换行）
      const beforeSecond = block.substring(0, secondBlockStart - 2); // -2 是去掉前面的逗号和空格
      const afterSecond = block.substring(secondEnd + 6); // +6 跳过 \n  },

      // 重建内容
      const beforeDate = content.substring(0, dateStart);
      const afterDate = content.substring(nextDateStart);

      content = beforeDate + beforeSecond + afterSecond + afterDate;
      console.log(date + ': Removed second sangsha_module');
    } else {
      console.log(date + ': Could not find end of second sangsha_module');
    }
  } else if (positions.length === 1) {
    console.log(date + ': Only 1 sangsha_module (OK)');
  } else {
    console.log(date + ': No sangsha_module found');
  }
});

// 验证语法
try {
  eval(content.replace('const newsData = ', 'global.__nd=').replace(/;[\s\S]*$/, ';'));
  console.log('\n✅ Syntax OK');
} catch (e) {
  console.log('\n❌ Syntax Error:', e.message);
}

fs.writeFileSync('C:\\Users\\asus\\temp-news-website\\news-data.js', content, 'utf-8');
console.log('\nDone!');
