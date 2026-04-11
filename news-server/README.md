# 财经新闻网站 - 部署指南

## 📋 目录结构

```
news-server/
├── app.py                 # Flask 应用主程序
├── run.py                 # 启动脚本
├── migrate.py             # 数据迁移脚本
├── requirements.txt       # Python 依赖
├── templates/
│   └── index.html         # 前端页面
└── news_data/             # 新闻数据存储目录（自动创建）
    ├── news_2026-03-29.json
    ├── news_2026-03-28.json
    └── ...
```

## 🚀 快速开始

### 1. 本地运行

```bash
# 进入目录
cd C:\Users\asus\.qclaw\workspace\news-server

# 安装依赖
pip install -r requirements.txt

# 迁移初始数据
python migrate.py

# 启动服务器
python run.py
```

然后在浏览器打开：`http://localhost:5000`

### 2. 功能说明

- **日期选择**：使用日期输入框或快捷按钮（今天/昨天/上周）
- **历史查看**：点击下方的历史日期按钮查看之前的新闻
- **自动保存**：每天的新闻自动保存为 JSON 文件
- **数据持久化**：关闭服务器后数据不会丢失

## 🌐 公网访问方案

### 方案 1：使用 Ngrok（最简单）

```bash
# 安装 ngrok
# 从 https://ngrok.com/download 下载

# 启动 ngrok
ngrok http 5000

# 会得到一个公网 URL，如：
# https://abc123.ngrok.io
```

### 方案 2：使用 Cloudflare Tunnel

```bash
# 安装 cloudflared
# 从 https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation/ 下载

# 启动隧道
cloudflared tunnel --url http://localhost:5000
```

### 方案 3：部署到云服务器

#### 使用 Heroku（免费）

```bash
# 安装 Heroku CLI
# 从 https://devcenter.heroku.com/articles/heroku-cli 下载

# 登录
heroku login

# 创建应用
heroku create your-app-name

# 部署
git push heroku main

# 查看日志
heroku logs --tail
```

#### 使用 PythonAnywhere（免费）

1. 注册 https://www.pythonanywhere.com
2. 上传代码
3. 配置 Web 应用
4. 获得公网 URL

#### 使用 VPS（推荐）

```bash
# 在 VPS 上安装 Python 3.8+
sudo apt-get install python3 python3-pip

# 克隆代码
git clone your-repo
cd news-server

# 安装依赖
pip3 install -r requirements.txt

# 使用 Gunicorn 启动
pip3 install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# 使用 Systemd 配置自启动
sudo nano /etc/systemd/system/news-server.service
```

## 📊 API 文档

### 获取新闻

```bash
GET /api/news/<date>
# 例：GET /api/news/2026-03-29

# 返回：
{
  "date": "2026-03-29",
  "market_tone": "...",
  "s_level": [...],
  "a_level": [...],
  "douyin": [...]
}
```

### 保存新闻

```bash
POST /api/news
Content-Type: application/json

{
  "date": "2026-03-29",
  "market_tone": "市场基调",
  "s_level": [...],
  "a_level": [...],
  "douyin": [...]
}
```

### 获取所有日期

```bash
GET /api/dates

# 返回：
{
  "dates": ["2026-03-29", "2026-03-28", ...]
}
```

### 删除新闻

```bash
DELETE /api/news/<date>
# 例：DELETE /api/news/2026-03-29
```

## 🔗 与 Cron Job 集成

更新你的 cron job payload，在生成 HTML 后同时保存到数据库：

```json
{
  "kind": "agentTurn",
  "message": "执行以下步骤：\n1. 获取今天的新闻数据\n2. 生成 HTML 页面\n3. 调用 POST /api/news 保存数据\n4. 推送到微信和飞书"
}
```

## 🔐 安全建议

1. **添加认证**：为 API 添加密钥验证
2. **HTTPS**：使用 SSL 证书加密传输
3. **速率限制**：防止滥用
4. **备份**：定期备份 news_data 目录

## 📱 分享链接

部署后，你可以分享以下链接给其他人：

- **本地网络**：`http://[你的IP]:5000`
- **公网**：`https://your-domain.com`
- **特定日期**：`https://your-domain.com?date=2026-03-29`

## 🐛 故障排查

### 端口被占用

```bash
# 查看占用 5000 端口的进程
netstat -ano | findstr :5000

# 杀死进程
taskkill /PID <PID> /F

# 或改用其他端口
python run.py --port 8000
```

### 数据丢失

检查 `news_data` 目录是否存在，如果不存在：

```bash
python migrate.py
```

### 无法访问

1. 检查防火墙设置
2. 确认服务器正在运行
3. 检查 IP 地址和端口是否正确

## 📞 支持

有问题？检查以下文件：
- `app.py` - 后端逻辑
- `templates/index.html` - 前端代码
- `news_data/` - 数据存储

---

**祝你使用愉快！** 🎉
