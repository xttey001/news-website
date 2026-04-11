# 🚀 GitHub Pages 部署完整指南

**优势**：完全免费 + 固定 URL + 无需注册额外服务 + 全球 CDN 加速

---

## 📊 方案对比

| 方案 | 成本 | URL | 配置难度 | 推荐度 |
|------|------|-----|---------|--------|
| **GitHub Pages** | 免费 | 固定 | ⭐⭐ 中等 | ⭐⭐⭐⭐⭐ |
| Ngrok | 免费 | 动态 | ⭐⭐ 中等 | ⭐⭐⭐ |
| 局域网 | 免费 | 固定 | ⭐ 简单 | ⭐⭐⭐ |

---

## 🎯 GitHub Pages 部署步骤

### 第 1 步：准备工作（已完成 ✅）

静态 HTML 已生成：
- 文件：`index.html`
- 大小：9180 字节
- 部署目录：`github-pages-deploy/`

---

### 第 2 步：创建 GitHub 仓库

1. **打开浏览器，访问**：
   ```
   https://github.com/new
   ```

2. **填写信息**：
   - Repository name: `news-website`
   - Description: `财经新闻速览网站`
   - 选择 **Public**（公开）
   - **不要**勾选 "Add a README file"
   - **不要**勾选 ".gitignore"
   - **不要**选择 License

3. **点击** "Create repository"

---

### 第 3 步：推送到 GitHub

在 PowerShell 中运行：

```powershell
# 进入部署目录
cd C:\Users\asus\.qclaw\workspace\news-server\github-pages-deploy

# 添加远程仓库（替换 YOUR_USERNAME）
git remote add origin https://github.com/YOUR_USERNAME/news-website.git

# 切换到 main 分支
git branch -M main

# 推送到 GitHub
git push -u origin main
```

**注意**：第一次推送需要输入 GitHub 用户名和密码（或 token）

---

### 第 4 步：启用 GitHub Pages

1. **打开仓库设置**：
   ```
   https://github.com/YOUR_USERNAME/news-website/settings
   ```

2. **在左侧菜单找到** "Pages"

3. **配置 Pages**：
   - Source: "Deploy from a branch"
   - Branch: "main"
   - Folder: "/ (root)"
   - 点击 "Save"

4. **等待部署**：
   - 通常需要 1-3 分钟
   - 页面会显示绿色提示：✅ Your site is live at ...

---

### 第 5 步：访问你的网站

部署成功后，访问：
```
https://YOUR_USERNAME.github.io/news-website/
```

例如，如果你的 GitHub 用户名是 `johnsmith`：
```
https://johnsmith.github.io/news-website/
```

---

## 🎁 额外功能

### 自定义域名（可选）

如果你有自己的域名：

1. 在仓库根目录创建 `CNAME` 文件
2. 内容写上你的域名，例如：`news.yourdomain.com`
3. 在域名服务商处添加 CNAME 记录指向 `YOUR_USERNAME.github.io`
4. 在 GitHub Pages 设置中启用 HTTPS

---

### 自动更新新闻

每次更新新闻后，运行：

```powershell
# 生成新的静态 HTML
python generate_static.py

# 复制到部署目录
copy index.html github-pages-deploy\

# 进入部署目录
cd github-pages-deploy

# 提交更改
git add .
git commit -m "Update news - 2026-03-29"
git push
```

---

## 🔧 故障排查

### 问题 1：推送失败 "Authentication failed"

**解决方案**：
- 使用 Personal Access Token 代替密码
- 生成 token：https://github.com/settings/tokens
- 勾选 `repo` 权限
- 推送时密码处输入 token

### 问题 2：网站显示 404

**解决方案**：
- 检查文件名是否为 `index.html`
- 检查 GitHub Pages 是否已启用
- 等待 1-3 分钟让部署完成

### 问题 3：样式不显示

**解决方案**：
- 确保所有 CSS 都在 `<style>` 标签内（已处理）
- 检查浏览器控制台是否有错误

---

## 📁 文件结构

```
news-server/
├── index.html                  # 静态 HTML（已生成）
├── generate_static.py          # 生成静态 HTML 的脚本
├── setup_github_pages.py       # GitHub Pages 设置脚本
├── github-pages-deploy/        # 部署目录
│   ├── index.html              # 要部署的 HTML
│   ├── .nojekyll               # 告诉 GitHub 不使用 Jekyll
│   └── .git/                   # Git 仓库
└── GitHub Pages 部署指南.bat    # 部署指南
```

---

## 🎯 快速命令汇总

```powershell
# 1. 生成静态 HTML
cd C:\Users\asus\.qclaw\workspace\news-server
python generate_static.py

# 2. 复制到部署目录
copy index.html github-pages-deploy\

# 3. 进入部署目录
cd github-pages-deploy

# 4. 提交并推送
git add .
git commit -m "Update news"
git push
```

---

## ✅ 优势总结

**GitHub Pages vs Ngrok**：

| 特性 | GitHub Pages | Ngrok |
|------|-------------|-------|
| URL | 固定不变 | 每次变化 |
| 需要注册 | GitHub 账号 | Ngrok 账号 |
| 成本 | 免费 | 免费版够用 |
| 访问速度 | 全球 CDN | 取决于网络 |
| 动态内容 | ❌ 不支持 | ✅ 支持 |
| 适用场景 | 静态展示 | 实时交互 |

---

## 💡 推荐

**如果你的新闻网站只需要展示**（不需要交互功能）：
→ **使用 GitHub Pages**（固定 URL，专业）

**如果需要实时交互**（搜索、筛选、评论）：
→ **使用 Ngrok**（支持动态后端）

**当前情况**：
- 新闻展示 → GitHub Pages ✅
- 未来扩展 → 可以两者结合

---

## 🚀 下一步

1. 创建 GitHub 仓库：https://github.com/new
2. 运行部署命令（见第 3 步）
3. 启用 GitHub Pages（见第 4 步）
4. 分享你的网站 URL！

---

**祝你部署顺利！** 🎉
