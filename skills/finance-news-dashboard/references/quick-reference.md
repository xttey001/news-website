# 快速参考

## 网站地址
```
https://xttey001.github.io/news-website/
```

## 核心目录
```
C:\Users\asus\.qclaw\workspace\news-server\
├── news_data/                          # 新闻数据
├── github-pages-deploy/                # GitHub Pages 部署
├── generate_static_with_history.py     # 生成网站
├── daily_update.py                     # 日常更新
└── push_to_github.py                   # 推送脚本
```

## 常用命令

### 手动更新新闻
```bash
cd C:\Users\asus\.qclaw\workspace\news-server
python generate_static_with_history.py
python push_to_github.py
```

### 查看定时任务
```bash
cron list
```

### 修改定时任务时间
```bash
cron update <jobId> --schedule "0 10 * * *"
```

### 立即运行任务
```bash
cron run <jobId>
```

### 查看任务执行日志
```bash
cron runs <jobId>
```

## 新闻分类

| 级别 | 标记 | 影响时长 | 例子 |
|------|------|---------|------|
| S级 | 🔴 | 1-3 个月 | 美联储政策、央行流动性 |
| A级 | 🟡 | 1-2 周 | 新能源政策、券商研报 |
| 抖音 | 📱 | 3-7 天 | 创业 IPO、融资新闻 |

## 新闻数据格式

```json
{
  "date": "2026-03-29",
  "market_tone": "📈 市场情绪描述",
  "s_level": [
    {
      "emoji": "🌍",
      "title": "新闻标题",
      "summary": "新闻摘要",
      "duration": "1-3 个月",
      "etfs": [{"name": "ETF 名称", "sentiment": "利好"}],
      "stocks": ["个股代码"],
      "signal": "资金信号"
    }
  ],
  "a_level": [...],
  "douyin": [...]
}
```

## 定时任务

| 时间 | 任务 ID | 状态 |
|------|--------|------|
| 10:00 | 35b33942-7aee-44d0-b664-a08e786978a1 | ✅ |
| 17:00 | 4dbb86d5-ffc7-4f0f-bc53-cdf3ad78b256 | ✅ |
| 23:00 | 2d910a43-5204-4bf5-b984-d22cd554c4b4 | ✅ |

## 故障排除

### 网站没有更新
1. 检查 `news_data/` 目录中是否有新文件
2. 运行 `generate_static_with_history.py`
3. 检查 `github-pages-deploy/` 目录
4. 清除浏览器缓存

### 定时任务没有执行
1. 运行 `cron list` 检查任务状态
2. 运行 `cron runs <jobId>` 查看日志
3. 确认 OpenClaw 服务正在运行

### 微信推送没有收到
1. 检查微信账号配置
2. 查看任务执行日志
3. 确认推送权限已开启

## 文件位置

| 文件 | 位置 |
|------|------|
| 新闻数据 | `news_data/news_YYYY-MM-DD.json` |
| 网站首页 | `github-pages-deploy/index.html` |
| 新闻数据 JS | `github-pages-deploy/news-data.js` |
| 生成脚本 | `generate_static_with_history.py` |
| 更新脚本 | `daily_update.py` |
| 推送脚本 | `push_to_github.py` |

## 微信推送配置

- **频道**：weixin
- **账号 ID**：d73bbcd779f4-im-bot
- **用户 ID**：o9cq807dwW0H1oaoEkmj7r8hfVeU@im.wechat
- **推送方式**：direct

## 时区

所有时间都使用 `Asia/Shanghai`（GMT+8）

## 下一次自动更新

- 🕙 2026-03-30 10:00
- 🕔 2026-03-30 17:00
- 🕛 2026-03-30 23:00
