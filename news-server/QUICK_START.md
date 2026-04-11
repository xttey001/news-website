# 🚀 财经新闻网站 - 快速启动指南

**状态**：✅ 服务器已启动并正常运行

---

## 📊 当前进度

| 任务 | 状态 | 说明 |
|------|------|------|
| 后端服务器 | ✅ | Flask 应用正常运行 |
| 前端页面 | ✅ | HTML 时间线页面已创建 |
| API 接口 | ✅ | 所有 REST API 正常工作 |
| 本地访问 | ✅ | http://localhost:5000 |
| 局域网访问 | ✅ | http://192.168.1.12:5000 |
| **公网访问** | ⏳ | 需要配置（见下文） |

---

## 🎯 3 步启用公网访问

### 步骤 1：下载 Ngrok（推荐）

访问：https://ngrok.com/download

选择你的操作系统，下载并解压。

### 步骤 2：运行公网分享脚本

```bash
# 方式 1：使用 Ngrok（推荐）
双击：share_public.bat

# 方式 2：使用 Cloudflare Tunnel
python share_cloudflare.py
```

### 步骤 3：分享公网 URL

Ngrok 或 Cloudflare 会显示一个公网 URL，例如：

```
https://abc123.ngrok.io
```

**分享这个 URL 给其他人**，他们就可以访问你的新闻网站了！

---

## 🌐 访问方式对比

| 方式 | 地址 | 谁能访问 | 配置难度 |
|------|------|---------|---------|
| 本地 | http://localhost:5000 | 只有你 | ✅ 无需配置 |
| 局域网 | http://192.168.1.12:5000 | 同一 WiFi | ✅ 无需配置 |
| **Ngrok** | https://abc123.ngrok.io | 全世界 | 🟡 简单 |
| **Cloudflare** | https://xxx.trycloudflare.com | 全世界 | 🟡 简单 |
| **VPS** | https://yourdomain.com | 全世界 | 🔴 复杂 |

---

## 🚀 立即启用公网访问

### 方案 A：Ngrok（最简单）

1. **下载 Ngrok**
   ```
   https://ngrok.com/download
   ```

2. **解压到任意目录**
   ```
   例如：C:\ngrok\
   ```

3. **运行公网分享脚本**
   ```
   双击：C:\Users\asus\.qclaw\workspace\news-server\share_public.bat
   ```

4. **获得公网 URL**
   ```
   Ngrok 会显示：
   https://abc123.ngrok.io
   
   复制这个 URL 分享给其他人
   ```

### 方案 B：Cloudflare Tunnel（无需下载）

1. **运行 Cloudflare 脚本**
   ```
   python C:\Users\asus\.qclaw\workspace\news-server\share_cloudflare.py
   ```

2. **获得公网 URL**
   ```
   Cloudflare 会显示：
   https://xxx.trycloudflare.com
   
   复制这个 URL 分享给其他人
   ```

---

## 📱 其他人如何访问

### 本地网络（同一 WiFi）

```
http://192.168.1.12:5000
```

### 公网（任何地方）

```
https://abc123.ngrok.io
或
https://xxx.trycloudflare.com
```

---

## 🎮 使用演示

### 查看新闻

1. 打开网站
2. 看到新闻时间线（最近 30 天）
3. 点击任何日期查看该天新闻

### 切换日期

- **点击时间线** - 点击任何圆形按钮
- **使用日期输入框** - 直接输入日期
- **快捷按钮** - 今天/昨天/上周

---

## 📊 新闻内容

每条新闻包含：

```
📰 标题（带 emoji）
├─ 📌 要点 - 一句话核心内容
├─ ⏱️ 影响时长 - 预期影响周期
├─ 📈 映射 ETF - 相关 ETF（标注利好/利空）
├─ ✨ 映射个股 - 相关个股
└─ 💡 资金信号 - 市场情绪和资金流向
```

### 新闻分类

- **🔴 S 级** - 主线级新闻（结构性叙事）
- **🟡 A 级** - 轮动级新闻（阶段性叙事）
- **📱 抖音相关** - 平台相关新闻

---

## 🔗 API 接口

### 获取新闻

```bash
GET /api/news/<date>

# 例：
curl http://localhost:5000/api/news/2026-03-29
```

### 保存新闻

```bash
POST /api/news
Content-Type: application/json

{
  "date": "2026-03-29",
  "market_tone": "市场基调...",
  "s_level": [...],
  "a_level": [...],
  "douyin": [...]
}
```

### 获取所有日期

```bash
GET /api/dates
```

---

## 🔧 故障排查

### 问题：其他人无法访问

**原因**：
- 没有配置公网访问
- Ngrok/Cloudflare 未启动
- 防火墙阻止

**解决**：
1. 确保服务器正在运行
2. 运行 `share_public.bat` 或 `share_cloudflare.py`
3. 检查防火墙设置

### 问题：Ngrok 无法启动

**原因**：
- Ngrok 未正确安装
- 网络连接问题

**解决**：
1. 重新下载 Ngrok
2. 检查网络连接
3. 尝试 Cloudflare Tunnel

---

## 📁 文件清单

```
news-server/
├── start_simple.py              # 启动服务器
├── share_public.bat             # Ngrok 公网分享
├── share_cloudflare.py          # Cloudflare 公网分享
├── app.py                       # Flask 后端
├── templates/index.html         # 前端页面
├── news_data/                   # 新闻数据
└── 其他文档...
```

---

## 🎁 功能特点

- ✅ 新闻时间线（最近 30 天）
- ✅ 日期切换查看历史新闻
- ✅ 响应式设计（手机/平板/电脑）
- ✅ 深色主题（护眼）
- ✅ 数据永久保存
- ✅ API 接口完整
- ✅ 公网访问支持

---

## 🚀 下一步

1. ✅ 服务器已启动
2. ⏳ **启用公网访问**（见上文）
3. ⏳ 集成 Cron Job（自动推送新闻）
4. ⏳ 长期部署（VPS 或域名）

---

## 💡 提示

- Ngrok 免费版本每次启动会生成新的 URL
- Cloudflare Tunnel 提供固定 URL（免费）
- 建议先用 Ngrok 快速测试
- 长期使用考虑 VPS 或自己的域名

---

## 🎉 总结

**现在你可以**：
- ✅ 在本地访问新闻网站
- ✅ 在局域网内分享给其他人
- ⏳ 配置公网访问后，全世界都能访问

**立即启用公网访问**：
1. 下载 Ngrok：https://ngrok.com/download
2. 运行：`share_public.bat`
3. 分享公网 URL 给其他人

---

**祝你使用愉快！** 🎉
