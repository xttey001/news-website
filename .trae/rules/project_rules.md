---
alwaysApply: true
---

# 悟空财经新闻分析系统 - Always Applied Rules

> ⚠️ **重要**：此文件包含项目核心规则，每次对话开始时 AI 必须首先阅读并遵循！

## 1. 项目基本信息

### 1.1 项目概述
| 属性 | 值 |
|------|-----|
| **项目名称** | 悟空财经新闻分析系统 (Wukong Finance News Analysis) |
| **项目类型** | 财经新闻智能分析 + 投资决策辅助 |
| **线上地址** | https://xttey001.github.io/news-website/ |
| **仓库地址** | https://github.com/xttey001/news-website |
| **核心架构** | 五维智能体交叉分析系统 |

### 1.2 技术栈
| 层级 | 技术 |
|------|------|
| **前端** | 纯 HTML5 + CSS3 + Vanilla JavaScript (无框架) |
| **样式方案** | CSS Variables (主题色系统) |
| **自动化** | Python 3.14+ |
| **部署** | GitHub Pages |
| **数据格式** | JavaScript 对象 (news-data.js) |
| **CI/CD** | GitHub Actions (.github/workflows/deploy.yml) |

### 1.3 五维智能体架构
```
┌─────────────────────────────────────────────────────────────┐
│                    五层交叉分析架构                          │
├──────────────┬──────────────────────────────────────────────┤
│ 🐵 悟空      │ 市场深度判断：地缘非线性/Trump量化/财报分级   │
├──────────────┼──────────────────────────────────────────────┤
│ 🧅 沙僧      │ 散户情绪监测：FOMO预警/恐慌逆向/拐点预判      │
├──────────────┼──────────────────────────────────────────────┤
│ 🐉 白龙马    │ 主力行为识别：Trump-主力模式/出货vs洗盘       │
├──────────────┼──────────────────────────────────────────────┤
│ 🐷 八戒      │ 贝叶斯概率校准：先验库/信号权重/地缘有效期    │
├──────────────┼──────────────────────────────────────────────┤
│ 🙏 唐僧      │ 跨层矛盾仲裁：全局风控/仓位决策               │
└──────────────┴──────────────────────────────────────────────┘
```

---

## 2. 核心约束

### 2.1 代码规范

#### JavaScript
- **使用双引号** `"` 而非单引号
- **使用 Tab 缩进**（而非空格）
- **对象属性缩进**：使用 1 个 Tab 层级
- **数组项缩进**：使用 1 个 Tab 层级
- **末尾逗号**：对象/数组最后一项不加逗号
- **文件编码**：UTF-8 (无 BOM)

#### Python
- **遵循 PEP 8**
- **使用 4 空格缩进**
- **函数命名**：snake_case
- **类命名**：PascalCase
- **常量**：UPPER_SNAKE_CASE

#### HTML/CSS
- **CSS 变量命名**：--kebab-case
- **类名命名**：kebab-case
- **使用语义化标签**

### 2.2 命名规则

| 类型 | 规范 | 示例 |
|------|------|------|
| **变量/函数** | camelCase | `newsData`, `getAnalysis()` |
| **常量** | UPPER_SNAKE_CASE | `MAX_NEWS_ITEMS` |
| **CSS 变量** | --kebab-case | `--bg-start`, `--text-dim` |
| **CSS 类名** | kebab-case | `.page-nav`, `.market-tone` |
| **文件名** | snake_case | `news-data.js`, `daily_update_v4.py` |
| **日期格式** | YYYY-MM-DD | `2026-04-25` |

### 2.3 文件组织
```
workspace/
├── index.html              # 主页面（线上版）
├── local_news.html         # 本地离线版
├── review.html             # 复盘分析页面 ⚠️ 需同步更新
├── news-data.js            # 核心数据文件 ⚠️ 所有数据在此
├── create_local_version.py # 生成本地HTML
├── update_newsdata.py      # 旧版更新脚本
├── news-evolution/         # 自动化系统目录
│   ├── daily_update_v4.py  # 每日更新主脚本
│   ├── weekly_review.py    # 周复盘脚本
│   ├── market_agents_evolution/  # 五维智能体模块
│   │   ├── wukong_enhanced.py
│   │   ├── sangsha_enhanced.py
│   │   ├── white_dragon_enhanced.py
│   │   ├── bajie_enhanced.py
│   │   └── tang_seng_arbiter.py
│   └── data/               # 验证数据
├── memory/                 # 每日记忆日志
│   └── YYYY-MM-DD.md
├── .github/workflows/      # CI/CD
│   └── deploy.yml          # GitHub Pages 部署
└── .trae/rules/            # AI 规则文件
    └── project_rules.md    # 本文件
```

---

## 3. 关键配置

### 3.1 主题色彩系统 (CSS Variables)
```css
:root {
  --bg-start: #0d1117;        /* 背景渐变起点 */
  --bg-end: #161b22;          /* 背景渐变终点 */
  --green: #3fb950;           /* 上涨/利好 */
  --green-bg: rgba(63,185,80,0.12);
  --orange: #f0883e;          /* 警告/中性 */
  --red: #f85149;             /* 下跌/利空 */
  --blue: #58a6ff;            /* 信息/链接 */
  --gold: #d29922;            /* 重点/高亮 */
  --purple: #a371f7;          /* 特色功能 */
  --card-bg: rgba(255,255,255,0.04);
  --card-border: rgba(255,255,255,0.1);
  --text: #e6edf3;            /* 主文字 */
  --text-dim: #8b949e;        /* 次要文字 */
}
```

### 3.2 新闻等级定义
| 等级 | 标识 | 含义 | 持续时间 |
|------|------|------|----------|
| **S级** | 🔴 红色 | 结构性机会/重大事件 | 1-2周 |
| **A级** | 🟢 绿色 | 阶段性机会 | 1-3天 |
| **B级** | 🟡 黄色 | 普通新闻/观察 | 当日 |

### 3.3 ETF 代码映射
| 名称 | 代码 | 类型 |
|------|------|------|
| 纳指ETF | 512930 | 美股科技 |
| 芯片ETF | 512760 | A股半导体 |
| 医药ETF | 512010 | A股医药 |
| 创业板ETF | 159915 | A股成长 |
| 科创50ETF | 588000 | A股科技 |

---

## 4. 禁止事项 🚫

### 绝对不能做的事

1. **❌ 禁止修改 .trae/rules/project_rules.md**
   - 此文件是 AI 行为规范，只有用户能修改
   - AI 只能读取，禁止写入

2. **❌ 禁止遗漏五维模块**
   - 每个日期数据必须包含：悟空/沙僧/白龙马/八戒/唐僧
   - 最容易遗漏：沙僧模块、白龙马模块、唐僧模块

3. **❌ 禁止 availableDates 顺序错误**
   - 新日期必须放在数组最前面 `[0]` 位置
   - 错误顺序会导致新闻不显示

4. **❌ 禁止忘记更新 review.html**
   - 每次更新 news-data.js 后必须同步更新 review.html
   - 复盘页面需要手动更新逐日准确率表格

5. **❌ 禁止破坏数据格式**
   - 不要改变 news-data.js 的结构
   - 每个模块的字段必须完整保留

6. **❌ 禁止使用框架/库**
   - 前端保持纯 Vanilla JS，不引入 React/Vue/Angular
   - 不引入 jQuery 等外部库

7. **❌ 禁止硬编码敏感信息**
   - API 密钥、密码等必须环境变量化
   - 不提交到 Git 仓库

8. **❌ 禁止破坏性删除**
   - 删除文件前必须确认无引用
   - 优先使用注释而非删除

---

## 5. 开发流程

### 5.1 标准更新流程 (每日新闻)
```
1. 查看当前数据
   → 阅读 news-data.js 最新日期结构

2. 添加新日期数据
   → 确保包含完整五维模块
   → 复制已有日期结构修改

3. 更新 availableDates
   → 新日期放在数组 [0] 位置

4. 语法验证
   → 运行: node -c news-data.js

5. 生成本地HTML
   → 运行: python create_local_version.py

6. 更新复盘页面
   → 修改 review.html 逐日准确率表格

7. Git 提交推送
   → git add .
   → git commit -m "Update: YYYY-MM-DD 新闻"
   → git push

8. 验证部署
   → 访问 https://xttey001.github.io/news-website/
```

### 5.2 自动化更新流程
```
1. 运行每日更新脚本
   → python news-evolution/daily_update_v4.py

2. 验证输出
   → 检查生成的数据格式
   → 确认五维模块完整

3. 手动审查并应用
   → 将生成的数据合并到 news-data.js

4. 执行标准流程步骤 3-8
```

### 5.3 文件更新顺序（强制！）
```
news-data.js (数据) 
    ↓
local_news.html (本地页面)
    ↓
review.html (复盘页面) ← 经常被遗漏！
    ↓
GitHub 推送
```

### 5.4 代码检查清单（每次修改必做）
- [ ] **查看本规则** - 确认当前项目上下文
- [ ] **完整五维模块** - 悟空/沙僧/白龙马/八戒/唐僧
- [ ] **availableDates** - 新日期在最前面
- [ ] **语法验证** - `node -c news-data.js`
- [ ] **生成本地HTML** - `python create_local_version.py`
- [ ] **更新复盘页面** - `review.html` 表格
- [ ] **Git提交推送** - add / commit / push

---

## 6. 相关工具/资源引用

### 6.1 内部 Skills
| Skill | 用途 | 触发词 |
|-------|------|--------|
| `project-memory` | 项目核心记忆 | 悟空财经新闻 |
| `wukong-finance-context` | 项目架构详解 | 项目结构 |
| `wukong-news-experience` | 问题记录与经验 | 问题解决 |

### 6.2 常用命令
```bash
# 验证 JavaScript 语法
node -c news-data.js

# 生成本地HTML
python create_local_version.py

# 运行每日更新
python news-evolution/daily_update_v4.py

# Git 操作
git status
git add .
git commit -m "Update: 描述"
git push
git pull
```

### 6.3 关键文件速查
| 用途 | 路径 |
|------|------|
| 核心数据 | `workspace/news-data.js` |
| 主页面 | `workspace/index.html` |
| 复盘页面 | `workspace/review.html` |
| 本地页面 | `workspace/local_news.html` |
| 更新脚本 | `workspace/news-evolution/daily_update_v4.py` |
| 悟空模块 | `workspace/news-evolution/market_agents_evolution/wukong_enhanced.py` |
| 沙僧模块 | `workspace/news-evolution/market_agents_evolution/sangsha_enhanced.py` |
| 白龙马模块 | `workspace/news-evolution/market_agents_evolution/white_dragon_enhanced.py` |
| 八戒模块 | `workspace/news-evolution/market_agents_evolution/bajie_enhanced.py` |
| 唐僧模块 | `workspace/news-evolution/market_agents_evolution/tang_seng_arbiter.py` |
| 部署配置 | `workspace/.github/workflows/deploy.yml` |

### 6.4 数据格式参考
每个日期数据的完整结构参考：`workspace/news-data.js` 中任意已有日期

### 6.5 问题排查
| 问题 | 可能原因 | 解决方案 |
|------|----------|----------|
| 新闻不显示/空白 | availableDates 缺少新日期 | 在数组最前面添加日期 |
| 缺少模块显示 | 沙僧/白龙马/唐僧模块遗漏 | 补全五维模块 |
| 复盘不同步 | 忘记更新 review.html | 同步更新逐日准确率表格 |
| JS 语法错误 | 缺少逗号/括号不匹配 | `node -c news-data.js` 验证 |
| Git 推送冲突 | 远程有本地没有的更新 | 先 `git pull` 再 `git push` |

---

## 7. 记忆与上下文

### 7.1 会话启动必做
每次新对话开始时，AI 必须：
1. **阅读本规则文件** - 了解项目约束
2. **阅读 SKILL.md** - 加载 project-memory skill
3. **查看 memory/YYYY-MM-DD.md** - 了解最近上下文
4. **确认当前工作目录** - 确保在 workspace 目录下

### 7.2 重要记忆点
- **五维模块缺一不可** - 最容易遗漏：沙僧、白龙马、唐僧
- **availableDates 顺序** - 新日期必须在数组最前面 `[0]` 位置
- **复盘页面同步** - 每次更新新闻必须同步更新 review.html
- **语法验证习惯** - 修改后必运行 `node -c news-data.js`

---

> 📌 **最后更新**: 2026-04-25  
> 📝 **维护者**: AI Assistant  
> ⚠️ **版本**: v1.0
