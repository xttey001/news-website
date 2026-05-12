# 📊 板块轮动监控提醒系统

自动监控芯片/医药/电网设备等板块轮动信号，实时提醒买卖机会。

## 🚀 快速开始

### 1. 运行监控（最简单方式）

双击运行：
```
run_sector_monitor.bat
```

### 2. 命令行运行

```bash
# 单次监控测试
python sector_rotation_monitor.py

# 持续监控（默认每30分钟）
python sector_rotation_monitor.py
```

## 📁 文件说明

| 文件 | 说明 |
|------|------|
| `sector_rotation_monitor.py` | 核心监控程序 |
| `notification_extensions.py` | 通知扩展模块（微信/钉钉/邮件） |
| `sector_monitor_config.json` | 配置文件 |
| `run_sector_monitor.bat` | Windows一键启动脚本 |
| `monitor_state.json` | 监控状态（自动保存） |
| `sector_monitor.log` | 运行日志 |

## ⚙️ 配置说明

编辑 `sector_monitor_config.json`：

```json
{
    "monitor": {
        "interval_minutes": 30,      // 监控间隔（分钟）
        "market_hours_only": true     // 只在交易时间监控
    },
    "signals": {
        "rsi_overbought": 75,        // RSI超买阈值
        "rsi_oversold": 30,          // RSI超卖阈值
        "change_threshold": 3.0      // 涨跌幅关注阈值
    }
}
```

## 📱 通知方式配置

### 企业微信通知

1. 在企业微信群中添加机器人，获取 webhook URL
2. 编辑 `sector_monitor_config.json`：
```json
"wechat_work": {
    "enabled": true,
    "webhook_url": "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=YOUR_KEY"
}
```

### 钉钉通知

1. 在钉钉群中添加机器人，获取 webhook URL 和 secret
2. 编辑配置：
```json
"dingtalk": {
    "enabled": true,
    "webhook_url": "https://oapi.dingtalk.com/robot/send?access_token=YOUR_TOKEN",
    "secret": "YOUR_SECRET"
}
```

### 邮件通知

```json
"email": {
    "enabled": true,
    "smtp_server": "smtp.qq.com",
    "smtp_port": 587,
    "sender": "your_email@qq.com",
    "password": "your_auth_code",
    "receiver": "receiver@example.com"
}
```

## 🎯 监控信号说明

### 个股信号

| 信号 | 触发条件 | 建议操作 |
|------|---------|---------|
| ⚠️ RSI超买 | RSI > 75 | 考虑减仓 |
| ✅ RSI超卖 | RSI < 30 | 关注买入 |
| 🔴 均线死叉 | M5下穿M10 | 减仓或观望 |
| 🟢 均线金叉 | M5上穿M10 | 关注加仓 |
| 📈 大涨 | 涨幅 > 3% | 观察持续性 |
| 📉 大跌 | 跌幅 > 3% | 评估止损 |

### 轮动信号

| 信号 | 触发条件 | 建议操作 |
|------|---------|---------|
| 🔄 高风险→低风险 | 高风险跌2%+，低风险涨1%+ | 减仓高风险，加仓低风险 |
| 🔄 低风险→高风险 | 低风险跌1%+，高风险涨2%+ | 关注高风险机会 |

## 📊 监控标的

### 高风险（成长型）
- 芯片ETF (512760)
- 科创50 (588000)

### 中风险（平衡型）
- 医药ETF (512010)
- 创业板ETF (159915)

### 低风险（防御型）
- 银行ETF (512800)
- 红利ETF (510880)

## 🛠️ 高级用法

### 自定义监控标的

编辑 `sector_rotation_monitor.py` 中的 `watch_list`：

```python
self.watch_list = {
    "high_risk": {
        "您的ETF": {"code": "shXXXXXX", "rsi_threshold": 75}
    }
}
```

### 修改信号阈值

```python
self.thresholds = {
    "rsi_overbought": 80,    // 调整为80
    "rsi_oversold": 25,      // 调整为25
    "change_threshold": 5.0  // 调整为5%
}
```

## 📝 日志查看

```bash
# 实时查看日志
tail -f sector_monitor.log

# Windows
type sector_monitor.log
```

## ⚠️ 注意事项

1. **数据延迟**：实时数据可能有1-5分钟延迟
2. **信号去重**：同一信号每天只提醒一次
3. **技术指标**：需要积累至少20天数据才能计算MA/RSI
4. **交易时间**：默认只在 9:30-15:00 监控

## 🔧 故障排除

### 无法获取数据
- 检查网络连接
- 确认腾讯API可访问

### 没有信号提醒
- 检查阈值设置是否过于严格
- 确认价格历史数据已积累足够天数

### 通知发送失败
- 检查 webhook URL 是否正确
- 确认网络可以访问微信/钉钉服务器

## 📄 更新日志

### v1.0 (2026-05-12)
- ✅ 基础监控功能
- ✅ RSI/MA技术指标计算
- ✅ 板块轮动信号检测
- ✅ 控制台/微信/钉钉/邮件通知
- ✅ 状态持久化

## 🤝 贡献

欢迎提交 Issue 和 PR！

## 📜 License

MIT License
