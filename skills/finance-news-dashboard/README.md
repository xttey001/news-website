# 财经新闻自动化系统 Skill（悟空+八戒双分析）

## 概述

这是一个完整的财经新闻自动化系统 skill，采用**悟空+八戒双分析体系**：

- 🐵 **悟空** = 新闻分析师：挖掘信息背后的真实含义，给出情绪判断和操作策略
- 🐷 **八戒** = 概率分析师：计算胜率、预期收益率、置信区间，辅助交易决策

### 核心功能
- ✅ 自动抓取财经新闻
- ✅ 智能分类（S级/A级/抖音）
- ✅ **悟空判断**：大盘情绪 + 核心分析 + 操作参考
- ✅ **八戒贝叶斯分析**：每条新闻的胜率/预期收益/置信区间
- ✅ **决策矩阵**：所有新闻的优先级汇总
- ✅ **八戒最终结论**：最优行动 + ETF组合 + 胜率 + 止损线
- ✅ 生成专业 HTML 网站
- ✅ 推送到 GitHub Pages
- ✅ 定时自动更新
- ✅ 微信/飞书推送通知

## 快速开始

### 1. 访问网站
```
https://xttey001.github.io/news-website/
```

### 2. 查看新闻
- 点击时间线上的日期查看对应日期的新闻
- 使用前一天/后一天按钮导航
- 输入日期跳转

### 3. 页面结构
```
📊 今日基调（一句话定性市场情绪）
📈 悟空今日判断（大盘情绪、核心分析、操作参考）
📊 决策矩阵（所有新闻的做多概率/预期收益/建议汇总）
🧠 八戒最终结论（最优行动、ETF组合、胜率、回撤警戒）
=== 分隔 ===
🔴 S级新闻1 + 🧮 八戒贝叶斯分析
🔴 S级新闻2 + 🧮 八戒贝叶斯分析
🟡 A级新闻 + 🧮 八戒贝叶斯分析
📱 抖音相关 + 🧮 八戒贝叶斯分析
```

## 文件结构

```
finance-news-dashboard/
├── SKILL.md                            # Skill 主文档（详细规范）
├── README.md                           # 本文件（快速开始）
├── scripts/                            # 核心脚本
│   ├── generate_static_with_history.py # 生成网站脚本
│   ├── daily_update.py                 # 日常更新脚本
│   └── push_to_github.py               # 推送脚本
├── references/                         # 参考文档
│   ├── news-format.md                  # 新闻数据格式规范
│   ├── cron-config.md                  # 定时任务配置指南
│   └── quick-reference.md              # 快速参考
└── assets/                             # 资源文件
    └── example-news.json               # 示例新闻文件
```

## 双分析体系详解

### 🐵 悟空分析

**核心定位**：新闻分析师 — 不被表面新闻迷惑，精准挖掘信息背后的真实含义

**分析风格**：
- 🔍 **找漏洞**：新闻稿里藏着什么没说的？数据背后的猫腻？
- 🎯 **辨机会**：这条新闻是利好还是利空？市场会怎么反应？
- 📈 **看后续**：短期影响是什么？中长期又会怎么演变？
- 🧠 **独立判断**：不盲从主流解读，用逻辑和数据说话

**输出内容**：
- 📊 今日基调（一句话定性）
- 📈 悟空今日判断
  - 大盘情绪
  - 核心分析（3-5条）
  - 操作参考（✅可做/⚠️警惕/❌回避/📌关注）

### 🐷 八戒贝叶斯分析

**核心定位**：概率分析师 — 为每条新闻计算胜率、预期收益率、置信区间

**分析框架**：
```
📊 贝叶斯概率推断：[新闻标题]
| 维度 | 判断 | 概率 |
|------|------|------|
| 先验（市场基准） | xxx | xx% |
| 似然（数据验证） | xxx | xx% |
| 后验（综合） | 做多概率 | **xx%** |
| 预期收益率 | ETF/个股 | **+x%~+y%** |
| 置信区间 | 95%CI | [+x%, +y%] |
💡 关键变量：xxx
```

**概率阈值**：
- ≥75%：✅ 高胜率，坚定做多
- 60%~74%：✅ 可做，轻仓
- 50%~59%：⚠️ 中性，可博弈
- 40%~49%：⚠️ 观望
- <40%：❌ 不做，回避

**最终输出**：
- 📊 决策矩阵（所有新闻汇总）
- 🧠 八戒最终结论
  - 最优行动
  - 最优ETF组合
  - 胜率（贝叶斯后验）
  - 最大回撤警戒（止损线）

## 新闻数据格式

```javascript
{
  "date": "2026-04-03",
  "market_tone": "清明假期A股休市，海外市场剧烈分化...",
  
  // 悟空判断
  "wukong_judgment": {
    "market_sentiment": "震荡分化，结构性机会为主",
    "core_analysis": ["...", "...", "..."],
    "operations": [
      {"type": "可做", "content": "AI芯片、存储半导体"},
      {"type": "警惕", "content": "黄金贵金属"}
    ]
  },
  
  // 八戒最终结论
  "bajie_conclusion": {
    "optimal_action": "轻仓过节，节后布局AI芯片+医药防御组合",
    "optimal_etfs": "512760芯片ETF(30%) + 512010医药ETF(30%) + ...",
    "win_rate": "~65%（贝叶斯后验）",
    "max_drawdown": "-8%（止损线）"
  },
  
  // S级新闻（每条含贝叶斯分析）
  "s_level": [
    {
      "emoji": "🔴",
      "title": "黄金暴跌原油飞天...",
      "summary": "...",
      "duration": "1-2周",
      "etfs": [{"name": "518880 黄金ETF", "sentiment": "利空"}],
      "stocks": ["中国石油", "中国海油"],
      "signal": "...",
      "bayes_analysis": {
        "prior_judgment": "地缘冲突支撑避险资产",
        "prior_prob": 60,
        "likelihood_judgment": "特朗普威胁打击伊朗...",
        "likelihood_prob": 75,
        "posterior": 72,
        "expected_return": "+3%~+8%",
        "confidence_interval": "[+1%, +12%]",
        "key_variables": "美伊谈判进展、OPEC+产量政策..."
      }
    }
  ],
  
  "a_level": [...],
  "douyin": [...]
}
```

详见 `references/news-format.md`

## 手动更新新闻

### 1. 搜索新闻
```bash
cd C:\Users\asus\.qclaw\workspace\news-server
python search_latest.py
```

### 2. 整理分析
- 按悟空风格整理（market_tone + wukong_judgment）
- 按八戒风格计算贝叶斯分析（每条新闻的胜率/预期收益）
- 生成八戒最终结论

### 3. 更新数据文件
编辑 `github-pages-deploy/news-data.js`

### 4. 推送 GitHub
```bash
cd C:\Users\asus\.qclaw\workspace\news-server\github-pages-deploy
git add news-data.js
git commit -m "更新MM-DD财经新闻：..."
git push origin main
```

### 5. 等待部署
GitHub Pages 约 1-3 分钟后自动更新

## 定时任务配置

### 当前配置
| 时间 | 任务 | Cron ID |
|------|------|---------|
| 09:00 | 早报 | `5f14e80b-b659-4ef8-9dd0-8f5735ae1fe8` |
| 13:00 | 午报 | `c58eee66-8163-4563-b39a-676648e5ea90` |
| 22:00 | 晚报 | `4196ff0d-101a-4e15-a067-4ecbb580bcaf` |
| 10:00 | 自动更新 | `35b33942-7aee-44d0-b664-a08e786978a1` |
| 17:00 | 自动更新 | `4dbb86d5-ffc7-4f0f-bc53-cdf3ad78b256` |
| 23:00 | 自动更新 | `2d910a43-5204-4bf5-b984-d22cd554c4b4` |

### 查看任务
```bash
cron list
```

### 查看日志
```bash
cron runs <jobId>
```

详见 `references/cron-config.md`

## 故障排除

### 网站显示空白/只有标题
**排查步骤**：
1. F12 打开开发者工具 → Console 查看红色报错
2. 常见错误：
   - `ReferenceError: xxx is not defined` → 变量作用域问题
   - `Uncaught SyntaxError` → 括号/花括号不匹配

**预防措施**：
1. 编辑 `index.html` 后立即检查语法
2. `git diff` 审查确保只有预期改动
3. 禁止大段复制粘贴代码块
4. 注意 `const` 变量作用域

### 网站没有更新
1. 确认 `news-data.js` 已更新
2. `git push origin main` 成功
3. 等待 1-3 分钟 GitHub Pages 构建
4. 清除浏览器缓存

### 样式错乱
检查 CSS 类名与 HTML 结构是否匹配：
- `.wukong-judgment` / `.judgment-content` / `.judgment-item`
- `.decision-matrix` / `.matrix-table`
- `.bajie-conclusion` / `.conclusion-item`
- `.bayes-analysis` / `.bayes-table`

## 历史问题记录

**2026-04-03 空白页面 Bug**：
- 原因：编辑时误将渲染代码复制两次，导致变量作用域错误
- 修复：删除重复代码块

**2026-04-04 CSS 类名不匹配 Bug**：
- 原因：CSS 类名与 HTML 结构不匹配
- 修复：统一 CSS 类名

## 参考资源

- **网站地址**：https://xttey001.github.io/news-website/
- **GitHub 仓库**：https://github.com/xttey001/news-website
- **详细规范**：`SKILL.md`
- **数据格式**：`references/news-format.md`
- **定时任务**：`references/cron-config.md`
- **快速参考**：`references/quick-reference.md`

## 许可证

MIT License
