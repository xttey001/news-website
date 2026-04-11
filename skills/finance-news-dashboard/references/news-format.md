# 新闻数据格式规范

## 完整示例

```json
{
  "date": "2026-03-29",
  "market_tone": "📈 市场情绪：谨慎乐观，等待美联储信号",
  "s_level": [
    {
      "emoji": "🌍",
      "title": "美联储鹰派言论推高美元",
      "summary": "美联储官员暗示可能延迟降息，美元指数上升至 105 以上，新兴市场货币承压。",
      "duration": "1-3 个月",
      "etfs": [
        {
          "name": "美元 ETF (UUP)",
          "sentiment": "利好"
        },
        {
          "name": "新兴市场 ETF (EEM)",
          "sentiment": "利空"
        }
      ],
      "stocks": ["美元相关个股"],
      "signal": "风险资产承压，避险情绪升温"
    }
  ],
  "a_level": [
    {
      "emoji": "⚡",
      "title": "新能源政策调整，光伏板块受益",
      "summary": "国家发改委发布新能源补贴政策，光伏企业获得更多支持。",
      "duration": "1-2 周",
      "etfs": [
        {
          "name": "光伏 ETF (TL9)",
          "sentiment": "利好"
        }
      ],
      "stocks": ["隆基绿能", "晶澳科技"],
      "signal": "政策利好，产业链受益"
    }
  ],
  "douyin": [
    {
      "emoji": "📱",
      "title": "月之暗面 IPO 即将启动",
      "summary": "AI 创业公司月之暗面宣布 IPO 计划，融资规模预计 10 亿美元。",
      "duration": "3-7 天",
      "etfs": [],
      "stocks": ["AI 相关个股"],
      "signal": "AI 热度持续，创业融资活跃"
    }
  ]
}
```

## 字段说明

### 顶级字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `date` | string | 日期，格式 YYYY-MM-DD |
| `market_tone` | string | 市场情绪描述，包含 emoji |
| `s_level` | array | S级新闻数组 |
| `a_level` | array | A级新闻数组 |
| `douyin` | array | 抖音相关新闻数组 |

### 新闻项目字段

| 字段 | 类型 | 说明 |
|------|------|------|
| `emoji` | string | 新闻类别 emoji |
| `title` | string | 新闻标题 |
| `summary` | string | 新闻摘要（2-3 句） |
| `duration` | string | 影响时长（如 "1-3 个月"） |
| `etfs` | array | 映射 ETF 数组 |
| `stocks` | array | 映射个股数组 |
| `signal` | string | 资金信号描述 |

### ETF 对象

| 字段 | 类型 | 说明 |
|------|------|------|
| `name` | string | ETF 名称和代码 |
| `sentiment` | string | "利好" 或 "利空" |

## 分类标准

### S级新闻（主线级）
- **定义**：影响整个市场的重大新闻
- **例子**：
  - 美联储政策声明
  - 央行流动性操作
  - 地缘政治事件
  - 重大经济数据发布
- **影响时长**：1-3 个月
- **emoji 建议**：🌍 🏦 📊 ⚠️

### A级新闻（轮动级）
- **定义**：影响特定板块或个股的重要新闻
- **例子**：
  - 新能源政策调整
  - 券商研报发布
  - 个股重组公告
  - 行业政策变化
- **影响时长**：1-2 周
- **emoji 建议**：⚡ 📈 🔧 💡

### 抖音相关
- **定义**：社交媒体热点、创业公司 IPO 等
- **例子**：
  - 创业公司 IPO
  - 融资新闻
  - 社交媒体热点
- **影响时长**：3-7 天
- **emoji 建议**：📱 🚀 💰 🎯

## 颜色约定（反常规）

**注意**：这个系统使用反常规的颜色标记，以便在深色主题中更清晰：

| 情绪 | 颜色 | 说明 |
|------|------|------|
| 利好 | 红色 | 在深色背景中更显眼 |
| 利空 | 绿色 | 在深色背景中更显眼 |

## 创建新闻文件

### 文件名格式
```
news_YYYY-MM-DD.json
```

### 示例
```
news_2026-03-29.json
news_2026-03-28.json
```

### 保存位置
```
C:\Users\asus\.qclaw\workspace\news-server\news_data\
```

## 验证清单

创建新闻文件时，检查以下项目：

- [ ] 日期格式正确（YYYY-MM-DD）
- [ ] 所有必需字段都已填写
- [ ] JSON 格式有效（可用 JSON 验证工具检查）
- [ ] 新闻标题清晰准确
- [ ] 摘要简洁（2-3 句）
- [ ] 影响时长合理
- [ ] ETF 名称和代码正确
- [ ] 个股代码正确
- [ ] sentiment 只包含 "利好" 或 "利空"
- [ ] emoji 选择恰当

## 常见错误

### 错误 1：JSON 格式无效
```json
// ❌ 错误：缺少逗号
{
  "date": "2026-03-29"
  "market_tone": "..."
}

// ✅ 正确
{
  "date": "2026-03-29",
  "market_tone": "..."
}
```

### 错误 2：sentiment 值不正确
```json
// ❌ 错误
{"name": "ETF", "sentiment": "positive"}

// ✅ 正确
{"name": "ETF", "sentiment": "利好"}
```

### 错误 3：数组为空但仍然包含
```json
// ❌ 不推荐
"etfs": [
  {"name": "", "sentiment": ""}
]

// ✅ 推荐
"etfs": []
```

## 工具

### JSON 验证
使用在线工具验证 JSON 格式：
- https://jsonlint.com/
- https://www.json.cn/

### 编辑器
推荐使用支持 JSON 的编辑器：
- VS Code
- Sublime Text
- Notepad++
