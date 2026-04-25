# 财经新闻五层分析复盘机制

## 一、复盘周期

| 周期 | 触发条件 | 执行内容 |
|------|---------|---------|
| 日复盘 | 每日收盘后 | 验证当日判断vs实际走势 |
| 周复盘 | 周五18:00 | 汇总本周准确率，更新范式 |
| 月复盘 | 月末18:00 | 跨周期规律发现，置信度校准 |

---

## 二、日复盘流程（自动化部分）

### Step 1: 收集判断数据
```javascript
// 从 news-data.js 提取当日判断
const todayNews = newsData.find(n => n.date === today);
const wukongJudgment = todayNews.wukong_judgment;
const bajieJudgment = todayNews.bajie_conclusion;
const shasengJudgment = todayNews.sha_seng_analysis;
const bailongmaJudgment = todayNews.bailongma_analysis;
```

### Step 2: 获取实际走势
```javascript
// 需要外部数据源（如 tushare / akshare）
const actualData = await fetchDailyPrice(targetETF);
const actualReturn = (actualData.close - actualData.open) / actualData.open;
```

### Step 3: 验证判断准确性

| 模块 | 判断 | 验证标准 |
|------|------|---------|
| 🐵 悟空 | direction: 看多/看空/震荡 | 涨跌方向是否一致（±1%容差） |
| 🐷 八戒 | bullish_prob: 65% | 概率校准度（Brier Score） |
| 🧅 沙僧 | 追高买入概率: 78% | 是否出现顶部反转信号 |
| 🐴 白龙马 | 主力状态: 出货/吸筹 | 需要后续K线验证（2-5日） |

---

## 三、周复盘流程（Cron任务执行）

### Step 1: 统计五模块准确率
```javascript
const weeklyStats = {
  wukong: { correct: 0, total: 0 },
  bajie: { calibrationScore: 0 }, // Brier Score
  shaseng: { reversalDetected: 0, total: 0 },
  bailongma: { pending: 0, verified: 0 }
};

// 遍历本周新闻，统计准确率
for (const news of thisWeekNews) {
  // 悟空方向判断
  if (news.wukong_judgment.direction === actualDirection(news)) {
    weeklyStats.wukong.correct++;
  }
  weeklyStats.wukong.total++;
  
  // 八戒概率校准
  weeklyStats.bajie.calibrationScore += brierScore(
    news.bajie_conclusion.posterior.bullish_prob / 100,
    news.actual_return > 0 ? 1 : 0
  );
}
```

### Step 2: 更新insights.json范式置信度
```javascript
// 验证范式是否正确
for (const insight of insights.active) {
  const validationResults = validateInsight(insight, thisWeekNews);
  
  if (validationResults.correct) {
    insight.confidence = Math.min(100, insight.confidence + 5);
  } else {
    insight.confidence = Math.max(0, insight.confidence - 15);
  }
  
  // 记录验证历史
  insight.validationHistory.push({
    date: weekEnd,
    result: validationResults.correct ? 'correct' : 'incorrect',
    confidence: insight.confidence
  });
}
```

### Step 3: 提取可复刻经验
```javascript
const experiences = [];

// 成功范式
for (const news of thisWeekSuccesses) {
  experiences.push({
    type: 'success',
    date: news.date,
    pattern: news.successPattern,
    reason: news.successReason,
    reusable: true
  });
}

// 失败教训
for (const news of thisWeekFailures) {
  experiences.push({
    type: 'failure',
    date: news.date,
    pattern: news.failurePattern,
    reason: news.failureReason,
    lesson: news.lessonLearned,
    reusable: false
  });
}
```

### Step 4: 更新review.html
```javascript
// 添加新的周内容
const weekContent = {
  week: weekNumber,
  dateRange: [startDate, endDate],
  stats: weeklyStats,
  experiences: experiences,
  topInsights: getTopInsights(insights)
};

updateReviewHtml(weekContent);
```

---

## 四、月复盘流程（发现跨周期规律）

### Step 1: 汇总月度数据
```javascript
const monthlyStats = {
  totalNews: 0,
  sLevelNews: 0,
  accuracy: {
    wukong: 0,
    bajie: 0,
    shaseng: 0,
    bailongma: 0
  },
  topPerformingPatterns: [],
  worstPerformingPatterns: []
};
```

### Step 2: 发现跨周期规律
```javascript
// 检测月度级别的主线演变
const themeEvolution = analyzeThemeEvolution(monthNews);
// 例如：AI主线在月初强势 → 月中轮动到消费 → 月末回归科技

// 检测Trump jawboning反转定律的月度有效性
const trumpReversalRate = calculateTrumpReversalRate(monthNews);
```

### Step 3: 更新SKILL.md可复刻经验
```markdown
## 可复刻经验（2026年4月更新）

### 成功范式（置信度≥80%）
1. Trump连续3天喊话 → 反转概率≥70%
2. 散户追高概率≥75% + 主力出货迹象 → 不追高，观望

### 失败教训
1. 线性外推地缘升级 → Trump可能突然放软
2. 忽视持仓等待地缘 → 节假日前应平仓

### 新发现规律
1. （本月新增）...
```

---

## 五、验证数据来源

| 数据类型 | 来源 | API |
|---------|------|-----|
| ETF日行情 | tushare / akshare | `daily()` |
| 个股日行情 | tushare | `daily()` |
| 美股行情 | yfinance | `yf.download()` |
| 汇率 | tushare | `fx_daily()` |
| 新闻舆情 | 腾讯元宝 | 已集成 |

---

## 六、复盘质量标准

| 等级 | 标准 |
|------|------|
| 及格 | 五模块准确率统计 + 每模块1条失败教训 |
| 良好 | + 每模块1条成功范式 |
| 优秀 | + insights.json更新 + 公式可复用 |
| 卓越 | + 跨周期规律 + 唐僧仓位决策评估 + 置信度量化 |

---

## 七、文件位置

- 复盘页面：`C:\Users\asus\temp-news-website\review.html`
- 新闻数据：`C:\Users\asus\temp-news-website\news-data.js`
- 范式库：`C:\Users\asus\.qclaw\workspace\news-server\insights.json`
- 工作流设计：`C:\Users\asus\.qclaw\workspace\news-agent-workflow.md`
- 自动化脚本：`C:\Users\asus\.qclaw\workspace\news-five-layer-workflow.js`

---

## 八、Cron任务状态

| 任务 | 表达式 | 状态 | ID |
|------|--------|------|----|
| 周复盘 | `0 18 * * 5` | ✅ 已创建 | 496652c8-... |
| 月复盘 | `0 18 28-31 * *` | ✅ 已创建 | 945e2722-... |

⚠️ 注意：早报/晚报任务有超时问题，需要增加 timeoutSeconds。
