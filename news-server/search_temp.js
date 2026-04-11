// 临时搜索脚本
const path = require('path');
const prosearch = require('D:/QCLaw/resources/openclaw/config/skills/online-search/scripts/prosearch.cjs');
const kw = process.argv[2] || '今日A股财经新闻';
prosearch(`{"keyword":"${kw}"}`);
