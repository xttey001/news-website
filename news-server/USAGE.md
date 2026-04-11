# 财经新闻网站 - 完整使用指南

## 📌 概述

这是一个专为你设计的财经新闻网站，具有以下特点：

✅ **日期切换** - 查看任何日期的新闻  
✅ **历史保存** - 所有新闻永久保存，不会丢失  
✅ **在线访问** - 其他人可以通过链接访问  
✅ **自动更新** - 与你的 cron job 自动集成  
✅ **专业排版** - 深色主题，清晰易读  

---

## 🚀 快速开始（3 步）

### 第 1 步：安装依赖

```bash
cd C:\Users\asus\.qclaw\workspace\news-server
pip install -r requirements.txt
```

### 第 2 步：启动服务器

```bash
python run_server.py
```

你会看到：
```
╔════════════════════════════════════════════════════════════╗
║         财经新闻网站服务器已启动                            ║
╠════════════════════════════════════════════════════════════╣
║  🌐 本地访问: http://localhost:5000                        ║
║  📱 局域网访问: http://[你的IP]:5000                       ║
```

### 第 3 步：打开浏览器

访问 `http://localhost:5000`

---

## 📊 功能说明

### 1. 日期选择

页面顶部有多种方式选择日期：

- **日期输入框**：直接输入日期
- **快捷按钮**：
  - 📅 **今天** - 查看今天的新闻
  - 📅 **昨天** - 查看昨天的新闻
  - 📅 **上周** - 查看一周前的新闻
- **历史日期列表**：点击下方的日期按钮查看历史新闻

### 2. 新闻内容

每条新闻包含：

- **标题** - 新闻主题（带 emoji）
- **要点** - 一句话核心内容
- **影响时长** - 预期影响周期
- **映射 ETF** - 相关 ETF（标注利好/利空）
- **映射个股** - 相关个股
- **资金信号** - 市场情绪和资金流向

### 3. 新闻分类

- **S 级（红色）** - 主线级新闻，结构性叙事
- **A 级（金色）** - 轮动级新闻，阶段性叙事
- **抖音相关（蓝色）** - 平台相关新闻

---

## 🔗 与 Cron Job 集成

你的 cron job 现在可以自动保存新闻到网站。

### 更新 Cron Job Payload

在你的 cron job 中添加以下步骤：

```python
# 在生成 HTML 后，调用 API 保存数据
import requests
import json

news_data = {
    "date": "2026-03-29",
    "market_tone": "市场基调...",
    "s_level": [...],
    "a_level": [...],
    "douyin": [...]
}

# 保存到网站
response = requests.post(
    "http://localhost:5000/api/news",
    json=news_data
)
```

### 自动推送脚本

创建一个脚本 `push_news.py`：

```python
#!/usr/bin/env python3
import requests
import json
from datetime import datetime

def push_news_to_website(news_data):
    """推送新闻到网站"""
    url = "http://localhost:5000/api/news"
    
    try:
        response = requests.post(url, json=news_data)
        if response.status_code == 200:
            print("✅ 新闻已保存到网站")
            return True
    except Exception as e:
        print(f"❌ 保存失败: {e}")
        return False

# 使用示例
if __name__ == "__main__":
    news_data = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "market_tone": "...",
        "s_level": [...],
        "a_level": [...],
        "douyin": [...]
    }
    push_news_to_website(news_data)
```

---

## 🌐 公网访问方案

### 方案 1：Ngrok（最简单，推荐）

**优点**：无需配置，一条命令即可  
**缺点**：免费版本有限制，重启后 URL 会变

```bash
# 1. 下载 ngrok
# 从 https://ngrok.com/download 下载对应系统版本

# 2. 解压并运行
ngrok http 5000

# 3. 你会看到：
# Forwarding    https://abc123.ngrok.io -> http://localhost:5000

# 4. 分享这个 URL 给其他人
```

**分享链接示例**：
```
https://abc123.ngrok.io
https://abc123.ngrok.io?date=2026-03-28
```

### 方案 2：Cloudflare Tunnel

**优点**：免费，URL 稳定  
**缺点**：需要 Cloudflare 账户

```bash
# 1. 安装 cloudflared
# 从 https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/install-and-setup/installation/ 下载

# 2. 运行
cloudflared tunnel --url http://localhost:5000

# 3. 获得公网 URL
```

### 方案 3：内网穿透（ZeroTier）

**优点**：安全，速度快  
**缺点**：需要安装客户端

```bash
# 1. 安装 ZeroTier
# 从 https://www.zerotier.com/download/ 下载

# 2. 加入网络
zerotier-cli join <network-id>

# 3. 其他人可以通过 ZeroTier IP 访问
```

### 方案 4：部署到云服务器（推荐长期使用）

#### 使用 Heroku（免费）

```bash
# 1. 注册 https://www.heroku.com

# 2. 安装 Heroku CLI
# 从 https://devcenter.heroku.com/articles/heroku-cli 下载

# 3. 登录
heroku login

# 4. 创建应用
heroku create your-news-app

# 5. 部署
git push heroku main

# 6. 获得 URL
# https://your-news-app.herokuapp.com
```

#### 使用 PythonAnywhere（免费）

1. 注册 https://www.pythonanywhere.com
2. 上传代码到 Files
3. 创建 Web 应用
4. 配置 WSGI 文件
5. 获得公网 URL

#### 使用 VPS（推荐，需付费）

```bash
# 在 VPS 上（如 DigitalOcean、Linode）

# 1. 安装 Python
sudo apt-get install python3 python3-pip

# 2. 克隆代码
git clone your-repo
cd news-server

# 3. 安装依赖
pip3 install -r requirements.txt

# 4. 使用 Gunicorn 启动
pip3 install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# 5. 配置 Nginx 反向代理
# 配置 SSL 证书
# 设置自启动
```

---

## 📱 分享给其他人

### 本地网络分享

如果其他人在同一个 WiFi 网络：

```
http://[你的电脑IP]:5000
```

查看你的 IP：
```bash
# Windows
ipconfig

# 找到 IPv4 Address，如 192.168.1.100
```

### 公网分享

使用上面的公网访问方案，分享 URL：

```
https://your-domain.com
https://your-domain.com?date=2026-03-28
```

### 创建二维码

使用在线工具（如 https://qr-code-generator.com/）生成二维码，方便扫描访问。

---

## 🔧 API 文档

### 获取新闻

```bash
GET /api/news/<date>

# 例：
curl http://localhost:5000/api/news/2026-03-29

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

# 返回：
{
  "status": "success",
  "date": "2026-03-29"
}
```

### 获取所有日期

```bash
GET /api/dates

# 返回：
{
  "dates": ["2026-03-29", "2026-03-28", "2026-03-27", ...]
}
```

### 删除新闻

```bash
DELETE /api/news/<date>

# 例：
curl -X DELETE http://localhost:5000/api/news/2026-03-29
```

---

## 💾 数据备份

所有新闻数据存储在 `news_data/` 目录：

```
news_data/
├── news_2026-03-29.json
├── news_2026-03-28.json
└── ...
```

### 备份数据

```bash
# 复制整个 news_data 目录
cp -r news_data news_data_backup
```

### 恢复数据

```bash
# 将备份复制回来
cp -r news_data_backup/* news_data/
```

---

## 🔐 安全建议

### 1. 添加密码保护

编辑 `app.py`，添加认证：

```python
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

@auth.verify_password
def verify_password(username, password):
    return username == "admin" and password == "your-password"

@app.route('/api/news', methods=['POST'])
@auth.login_required
def save_news_api():
    # ...
```

### 2. 使用 HTTPS

如果部署到公网，必须使用 HTTPS：

```bash
# 使用 Let's Encrypt 获得免费证书
certbot certonly --standalone -d your-domain.com
```

### 3. 限制访问

```python
from flask_limiter import Limiter

limiter = Limiter(app, key_func=lambda: request.remote_addr)

@app.route('/api/news', methods=['POST'])
@limiter.limit("10 per hour")
def save_news_api():
    # ...
```

---

## 🐛 故障排查

### 问题 1：无法访问 localhost:5000

**解决方案**：
1. 确认服务器正在运行
2. 检查防火墙设置
3. 尝试 `http://127.0.0.1:5000`

### 问题 2：数据丢失

**解决方案**：
1. 检查 `news_data/` 目录是否存在
2. 运行 `python migrate.py` 恢复初始数据
3. 检查文件权限

### 问题 3：无法保存新闻

**解决方案**：
1. 检查 `news_data/` 目录是否可写
2. 查看服务器日志
3. 确认 JSON 格式正确

### 问题 4：公网无法访问

**解决方案**：
1. 检查防火墙是否开放 5000 端口
2. 确认 ngrok/cloudflared 正在运行
3. 检查 URL 是否正确

---

## 📞 常见问题

**Q: 新闻会永久保存吗？**  
A: 是的，所有新闻都保存在 `news_data/` 目录中，除非手动删除。

**Q: 可以修改已保存的新闻吗？**  
A: 可以，通过 API 重新 POST 相同日期的数据会覆盖旧数据。

**Q: 支持多少条新闻？**  
A: 理论上无限制，取决于磁盘空间。

**Q: 可以导出数据吗？**  
A: 可以，直接复制 `news_data/` 目录中的 JSON 文件。

**Q: 支持移动端访问吗？**  
A: 完全支持，页面已优化响应式设计。

---

## 🎉 下一步

1. **启动服务器**：`python run_server.py`
2. **访问网站**：`http://localhost:5000`
3. **分享链接**：使用 ngrok 或部署到云服务器
4. **集成 Cron Job**：自动推送新闻数据
5. **邀请他人**：分享你的新闻网站

---

**祝你使用愉快！** 🚀
