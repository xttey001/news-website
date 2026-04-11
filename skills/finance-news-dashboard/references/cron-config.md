# 定时任务配置指南

## 当前配置

### 三个定时任务

| 任务 ID | 时间 | 频率 | 状态 |
|--------|------|------|------|
| 35b33942-7aee-44d0-b664-a08e786978a1 | 10:00 | 每天 | ✅ 启用 |
| 4dbb86d5-ffc7-4f0f-bc53-cdf3ad78b256 | 17:00 | 每天 | ✅ 启用 |
| 2d910a43-5204-4bf5-b984-d22cd554c4b4 | 23:00 | 每天 | ✅ 启用 |

## 任务内容

每个定时任务都会执行以下步骤：

```
1. 搜索最新的财经新闻
   - A股热点
   - 新能源政策
   - 金融市场
   - 科技行业

2. 按照分类整理
   - S级新闻（主线级）
   - A级新闻（轮动级）
   - 抖音相关

3. 更新数据文件
   - 保存到 news_data/news_YYYY-MM-DD.json

4. 生成网站
   - 运行 generate_static_with_history.py
   - 扫描所有 news_data/*.json 文件
   - 生成 index.html + news-data.js

5. 推送到 GitHub
   - 复制文件到 github-pages-deploy/
   - 执行 git add/commit/push
   - 网站 3 分钟内自动更新

6. 推送微信通知
   - 发送更新结果
   - 发送网站链接
```

## 修改定时任务

### 查看所有任务

```bash
cron list
```

### 修改任务时间

例如，将 10:00 的任务改为 09:00：

```bash
cron update 35b33942-7aee-44d0-b664-a08e786978a1 --schedule "0 9 * * *"
```

### 禁用任务

```bash
cron update <jobId> --enabled false
```

### 启用任务

```bash
cron update <jobId> --enabled true
```

### 删除任务

```bash
cron remove <jobId>
```

### 添加新任务

```bash
cron add \
  --name "财经新闻自动更新 - 每天 12:00" \
  --schedule "0 12 * * *" \
  --payload '{"kind":"agentTurn","message":"...","timeoutSeconds":300}' \
  --delivery '{"mode":"announce","channel":"weixin","to":"..."}'
```

## Cron 表达式

### 格式
```
分 小时 日 月 周几
0   10   *  *  *
```

### 常见表达式

| 表达式 | 说明 |
|--------|------|
| `0 10 * * *` | 每天 10:00 |
| `0 17 * * *` | 每天 17:00 |
| `0 23 * * *` | 每天 23:00 |
| `0 9 * * 1-5` | 周一到周五 09:00 |
| `0 0 1 * *` | 每月 1 号 00:00 |
| `0 0 * * 0` | 每周日 00:00 |
| `*/15 * * * *` | 每 15 分钟 |

### 时区
所有任务使用 `Asia/Shanghai` 时区（GMT+8）

## 推送配置

### 微信推送

**配置**：
- 频道：`weixin`
- 账号 ID：`d73bbcd779f4-im-bot`
- 用户 ID：`o9cq807dwW0H1oaoEkmj7r8hfVeU@im.wechat`
- 推送方式：`direct`

**验证**：
- 检查微信是否收到通知
- 检查通知内容是否完整

### 飞书推送（可选）

如果需要添加飞书推送，修改任务的 `delivery` 配置：

```json
{
  "mode": "announce",
  "channel": "feishu",
  "to": "<飞书用户 ID>"
}
```

## 故障排除

### 问题：定时任务没有执行

**检查清单**：
1. 确认任务已启用
   ```bash
   cron list
   ```
   查看 `enabled` 字段是否为 `true`

2. 检查下一次运行时间
   ```bash
   cron list
   ```
   查看 `nextRunAtMs` 字段

3. 查看任务执行日志
   ```bash
   cron runs <jobId>
   ```

4. 确认 OpenClaw 服务正在运行
   ```bash
   openclaw status
   ```

### 问题：任务执行失败

**检查清单**：
1. 查看任务执行日志
   ```bash
   cron runs <jobId>
   ```

2. 检查错误信息
   - 网络连接问题
   - 文件权限问题
   - GitHub 认证问题

3. 手动运行任务测试
   ```bash
   cron run <jobId>
   ```

### 问题：微信推送没有收到

**检查清单**：
1. 确认微信账号已正确配置
2. 检查任务的 `delivery` 配置
3. 查看任务执行日志
4. 确认微信通知权限已开启

## 高级配置

### 添加周末任务

如果只想在工作日更新新闻：

```bash
cron update <jobId> --schedule "0 10 * * 1-5"
```

### 添加多个时间点

创建多个任务，每个任务对应一个时间点：

```bash
# 早上 08:00
cron add --name "财经新闻 - 08:00" --schedule "0 8 * * *" ...

# 中午 12:00
cron add --name "财经新闻 - 12:00" --schedule "0 12 * * *" ...

# 下午 16:00
cron add --name "财经新闻 - 16:00" --schedule "0 16 * * *" ...

# 晚上 20:00
cron add --name "财经新闻 - 20:00" --schedule "0 20 * * *" ...
```

### 条件执行

如果需要在特定条件下执行（例如，只在市场开盘时间），可以在任务的 `message` 中添加条件检查。

## 监控和维护

### 定期检查

每周检查一次任务执行情况：

```bash
cron list
cron runs <jobId> --limit 10
```

### 日志分析

查看最近 10 次执行的日志：

```bash
cron runs <jobId> --limit 10
```

### 性能优化

- 如果任务执行时间过长，考虑增加 `timeoutSeconds`
- 如果网络不稳定，考虑添加重试机制
- 如果推送失败，考虑添加备用推送方式

## 参考资源

- **OpenClaw Cron 文档**：https://docs.openclaw.ai/cron
- **Cron 表达式生成器**：https://crontab.guru/
- **时区列表**：https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
