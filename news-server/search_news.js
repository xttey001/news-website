const { execSync } = require('child_process');
const args = process.argv.slice(2);
if (args.length === 0) {
  console.log('Usage: node search_news.js <json_string>');
  process.exit(1);
}
const result = execSync(`node "D:\\QCLaw\\resources\\openclaw\\config\\skills\\online-search\\scripts\\prosearch.cjs" ${args[0]}`, { encoding: 'utf8' });
console.log(result);
