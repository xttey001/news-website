
const FROM_TIME = Math.floor(Date.now()/1000) - 86400;
const TO_TIME = Math.floor(Date.now()/1000);
const {execSync} = require('child_process');
const kw = '今日财经要闻 A股 2026年4月11日';
const body = JSON.stringify({keyword:kw, from_time:FROM_TIME, to_time:TO_TIME, industry:'news'});
const result = execSync('node "D:/QCLaw/resources/openclaw/config/skills/online-search/scripts/prosearch.cjs"', {input:body, encoding:'utf8'});
console.log(result);
