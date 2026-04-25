# 📊 复盘 Agent 工作流程

## 概述
这是一个专门负责更新复盘页面的 Agent 工作流程。

---

## 🔄 工作流程

### Phase 1: 数据收集
1. 读取 `news-data.js` 获取本周数据
2. 计算本周日期范围（周一至周五）
3. 加载 `insights.json` 获取范式库

### Phase 2: 分析评估
对每一天：
- 提取市场基调 (market_tone)
- 提取悟空判断 (wukong_judgment)
- 提取八戒结论 (bajie_conclusion)
- 统计 S/A 级新闻数量
- 评估判断准确率

### Phase 3: 生成报告
生成标准复盘报告 HTML：
- 准确率统计
- 逐日准确率表格
- 可复刻经验
- 失败教训

### Phase 4: 更新页面
1. 更新 `review.html`
2. 添加新周按钮和报告内容
3. Git commit + push

### Phase 5: 存档
- 保存复盘数据到 `memory/review/YYYY-WXX.md`

---

## 📝 复盘报告模板

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
            <tr><td>MM-DD</td><td>xxx</td><td class="acc-high">✅ 高</td><td>xxx</td><td>xxx</td></tr>
        </tbody>
    </table>

    <div class="section-title">🏆 本周可复刻经验</div>
    <div class="exp-card">
        <div class="exp-title"><span class="icon">⚡</span> 经验N：经验标题</div>
        <div class="exp-content">
            <ul>
                <li><strong>事件：</strong>xxx</li>
                <li><strong>可复刻公式：</strong>xxx</li>
            </ul>
        </div>
    </div>
</div>
```

---

## 🎯 准确率评估标准

| 评估 | 条件 | CSS类 |
|------|------|-------|
| ✅ 高 | 悟空判断与市场一致，八戒胜率高 | `acc-high` |
| ⚠️ 中 | 部分准确，有改进空间 | `acc-mid` |
| ❌ 失误 | 判断与实际相反 | `acc-low` |

---

## 🔧 快速执行命令

```bash
# 读取本周数据
node -e "
  const data = require('./news-data.js');
  const today = new Date();
  const monday = new Date(today);
  monday.setDate(today.getDate() - today.getDay() + 1);
  const weekDates = [];
  for(let i=0; i<5; i++) {
    const d = new Date(monday);
    d.setDate(monday.getDate() + i);
    weekDates.push(d.toISOString().split('T')[0]);
  }
  console.log('本周:', weekDates.join(', '));
"

# 验证 review.html 语法
node --check review.html 2>&1 || echo "HTML无法用node检查，跳过"

# Git 推送
git add review.html && git commit -m "复盘: 第N周" && git push
```

---

## 📁 文件路径

| 文件 | 绝对路径 |
|------|----------|
| 新闻数据 | `C:\Users\asus\.qclaw\workspace\news-data.js` |
| 复盘页面 | `C:\Users\asus\.qclaw\workspace\review.html` |
| 范式库 | `C:\Users\asus\.qclaw\workspace\news-server\insights.json` |
| 存档目录 | `C:\Users\asus\.qclaw\workspace\memory\review\` |

---

## ⚠️ 注意事项

1. **只基于实际数据** - 不要生成虚构内容
2. **格式必须一致** - 使用标准 HTML 模板
3. **Git push 前检查** - 确认文件正确
4. **保留历史报告** - 不要删除旧周报
5. **更新月度汇总** - 月末更新月度复盘

---

## 🚀 手动触发

在 OpenClaw 中输入：
```
请执行周复盘任务
```
