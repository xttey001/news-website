#!/usr/bin/env node
/**
 * news-data.js 语法检查工具
 * 用法: node check-json.js [path/to/news-data.js]
 * 
 * 检查项:
 * 1. JavaScript 语法错误
 * 2. 中文引号（会导致 JSON 解析失败）
 * 3. 其他常见问题
 */

const fs = require('fs');
const path = require('path');
const { execSync } = require('child_process');

// 获取文件路径
const newsDataPath = process.argv[2] || path.join(__dirname, '..', 'github-pages-deploy', 'news-data.js');

console.log('🔍 检查文件:', newsDataPath);
console.log('');

let hasError = false;

// 1. 检查文件是否存在
if (!fs.existsSync(newsDataPath)) {
  console.error('❌ 文件不存在:', newsDataPath);
  process.exit(1);
}

// 2. JavaScript 语法检查
console.log('📋 步骤1: JavaScript 语法检查...');
try {
  execSync(`node --check "${newsDataPath}"`, { stdio: 'pipe' });
  console.log('✅ 语法检查通过');
} catch (err) {
  console.error('❌ 语法错误:');
  console.error(err.stderr?.toString() || err.message);
  hasError = true;
}

// 3. 中文引号检查
console.log('');
console.log('📋 步骤2: 中文引号检查...');
const content = fs.readFileSync(newsDataPath, 'utf-8');

// 检查中文引号（使用 Unicode 码点避免自身解析问题）
const chineseQuotes = [
  { char: '\u201C', name: '中文左双引号', code: 'U+201C' },
  { char: '\u201D', name: '中文右双引号', code: 'U+201D' },
  { char: '\u2018', name: '中文左单引号', code: 'U+2018' },
  { char: '\u2019', name: '中文右单引号', code: 'U+2019' },
];

const lines = content.split('\n');
const problematicLines = [];

lines.forEach((line, idx) => {
  chineseQuotes.forEach(({ char, name }) => {
    if (line.includes(char)) {
      problematicLines.push({
        line: idx + 1,
        char: name,
        content: line.trim().substring(0, 80)
      });
    }
  });
});

if (problematicLines.length > 0) {
  console.error('❌ 发现中文引号（会导致 JSON 解析失败）:');
  problematicLines.slice(0, 5).forEach(item => {
    console.error(`   行 ${item.line}: ${item.char}`);
    console.error(`   内容: "${item.content}..."`);
  });
  if (problematicLines.length > 5) {
    console.error(`   ... 还有 ${problematicLines.length - 5} 处`);
  }
  console.error('');
  console.error('💡 解决方案: 将中文引号 " " 替换为 「 」 或转义为 \"');
  hasError = true;
} else {
  console.log('✅ 未发现中文引号问题');
}

// 4. 检查 availableDates 是否包含最新日期
console.log('');
console.log('📋 步骤3: availableDates 检查...');
try {
  // 提取 availableDates 数组
  const match = content.match(/var availableDates\s*=\s*(\[[\s\S]*?\]);/);
  if (match) {
    const datesStr = match[1];
    const dates = eval(datesStr); // 安全：已通过语法检查
    
    if (dates.length === 0) {
      console.error('❌ availableDates 为空');
      hasError = true;
    } else {
      console.log(`✅ availableDates 包含 ${dates.length} 个日期`);
      console.log(`   最新日期: ${dates[0]}`);
      
      // 检查是否是今天或最近的交易日
      const today = new Date().toISOString().split('T')[0];
      if (dates[0] === today) {
        console.log('   ✅ 最新日期是今天');
      } else {
        console.log(`   ⚠️ 最新日期不是今天（${today}），请确认是否正常`);
      }
    }
  }
} catch (err) {
  console.error('⚠️ 无法解析 availableDates:', err.message);
}

// 5. 总结
console.log('');
console.log('═'.repeat(50));
if (hasError) {
  console.error('❌ 检查未通过，请修复上述问题后再提交');
  process.exit(1);
} else {
  console.log('✅ 所有检查通过，可以安全提交');
  process.exit(0);
}
