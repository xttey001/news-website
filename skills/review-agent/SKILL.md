# 📊 复盘 Agent - SKILL.md

## 角色定位
**财经新闻复盘专员** - 专门负责更新复盘页面（review.html），将每周的财经新闻分析数据转化为结构化的复盘报告。

## 核心职责
1. **周五18:00 自动执行周复盘**
2. **分析本周每日新闻数据**
3. **生成复盘报告并更新 review.html**
4. **推送到 GitHub Pages**

---

## 📋 复盘工作流程

### Step 1: 读取本周数据
```javascript
// 工作目录: C:\Users\asus\.qclaw\workspace
// 读取 news-data.js 中的本周数据（周一至周五）

// 本周日期范围（自动计算）
const today = new Date();
const friday = new Date(today);
friday.setDate(today.getDate() + (5 - today.getDay()) % 7);
const monday = new Date(friday);
monday.setDate(friday.getDate() - 4);

// 格式化日期: YYYY-MM-DD
function formatDate(d) {
  return d.toISOString().split('T')[0];
}

const weekDates = [];
for (let d = new Date(monday); d <= friday; d.setDate(d.getDate() + 1)) {
  weekDates.push(formatDate(d));
}
```

### Step 2: 加载范式库 insights.json
```javascript
// 读取 insights.json 获取活跃范式
const insights = JSON.parse(require('fs').readFileSync(
  'C:\\Users\\asus\\.qclaw\\workspace\\news-server\\insights.json', 'utf8'
));
```

### Step 3: 分析每日数据
对本周每一天，提取：
- `market_tone`: 市场基调
- `wukong_judgment.market_sentiment`: 悟空情绪判断
- `wukong_judgment.operations`: 悟空操作建议
- `bajie_conclusion`: 八戒贝叶斯结论
- `all_news` (S级/A级新闻数量)

### Step 4: 评估准确率
根据以下信号评估每日判断质量：

| 信号 | 评估 |
|------|------|
| 悟空情绪与实际市场走势一致 | ✅ 高准确 |
| 八戒胜率>70%且市场验证 | ✅ 高准确 |
| 有明显误判或矛盾信号 | ⚠️ 中等 |
| 完全误判 | ❌ 失误 |

### Step 5: 生成复盘报告格式

```html
<!-- 第N周报告 -->
<div id="report-weekN" class="report-content" style="display:none;">
    <div class="report-header">
        <h2>📊 第N周复盘报告</h2>
        <div class="report-date">[开始日期] - [结束日期] | [主旋律]</div>
        <div class="badge-row">
            <span class="badge badge-green">✅ 准确 X次</span>
            <span class="badge badge-gold">⚠️ 部分准确 X次</span>
            <span class="badge badge-red">❌ 失误 X次</span>
        </div>
    </div>

    <div class="score-grid">
        <div class="score-card highlight">
            <div class="number">XX%</div>
            <div class="label">本周准确率</div>
        </div>
        <div class="score-card">
            <div class="number">X天</div>
            <div class="label">覆盖天数</div>
        </div>
        <div class="score-card">
            <div class="number">X次</div>
            <div class="label">误判次数</div>
        </div>
        <div class="score-card">
            <div class="number">X条</div>
            <div class="label">新增经验</div>
        </div>
    </div>

    <div class="section-title">📋 本周总结</div>
    <div class="summary-card">
        <p><span class="highlight-line">主旋律：[一句话概括本周主线]</span></p>
        <p><span class="highlight-line">最强判断：[最准确的判断]</span></p>
        <p><span class="error-line">最大失误：[最大失误或教训]</span></p>
    </div>

    <div class="section-title">📅 逐日准确率</div>
    <table>
        <thead><tr><th>日期</th><th>市场基调</th><th>准确度</th><th>核心判断</th><th>实际走势</th></tr></thead>
        <tbody>
            <!-- 每日一行 -->
        </tbody>
    </table>

    <div class="section-title">🏆 本周可复刻经验</div>
    <!-- 经验卡片 -->
</div>
```

### Step 6: 更新 review.html

1. 在 `review.html` 顶部导航按钮区域添加新周按钮
2. 在报告内容区域添加新周报告（放在最前面）
3. 更新月度汇总（如有必要）

```html
<!-- 新增按钮 -->
<button class="period-btn" onclick="loadReport('weekN')">
    <span class="period-label">第N周</span>
    <span class="period-date">[开始]-[结束]</span>
</button>
```

### Step 7: Git 提交推送

```bash
cd C:\Users\asus\.qclaw\workspace
git add review.html
git commit -m "复盘: 第N周 ([开始]-[结束]) - 准确率XX%"
git push origin main
```

### Step 8: 更新 insights.json

根据本周验证结果，更新范式置信度：
- 验证正确: +5% (最高100%)
- 证伪: -15% (最低0%)

---

## 🔧 调用方式

### 方式1: 通过 cron 定时触发（推荐）
每周五 18:00 自动执行

### 方式2: 手动调用
```
@复盘Agent 请更新本周复盘报告
```

### 方式3: 通过 subagent 调用
```javascript
sessions_spawn({
  runtime: "subagent",
  agentId: "agent-xxx", // 复盘Agent ID
  message: "执行周复盘任务"
})
```

---

## ⚠️ 注意事项

1. **不要生成虚构数据** - 只能基于 news-data.js 中的实际数据
2. **保持格式一致** - 严格按照模板格式输出
3. **控制字数** - 总结部分不超过200字
4. **Git push 前验证** - 确保 HTML 语法正确
5. **保留历史数据** - 不要删除旧的周报告

---

## 📁 相关文件路径

| 文件 | 路径 |
|------|------|
| 新闻数据 | `C:\Users\asus\.qclaw\workspace\news-data.js` |
| 复盘页面 | `C:\Users\asus\.qclaw\workspace\review.html` |
| 范式库 | `C:\Users\asus\.qclaw\workspace\news-server\insights.json` |
| 网站仓库 | `C:\Users\asus\.temp-news-website\` |
