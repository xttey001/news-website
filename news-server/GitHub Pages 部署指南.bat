@echo off
chcp 65001 >nul
echo.
echo ================================================
echo GitHub Pages 部署指南
echo ================================================
echo.
echo 步骤 1：检查 Git
echo -------------------------------------------
git --version
echo.
echo ================================================
echo 步骤 2：创建 GitHub 仓库
echo ================================================
echo.
echo 1. 打开：https://github.com/new
echo 2. Repository name: news-website
echo 3. 选择 Public
echo 4. 点击 Create repository
echo.
echo ================================================
echo 步骤 3：在 GitHub 创建仓库后
echo ================================================
echo.
echo 复制你的 GitHub 用户名，然后运行：
echo.
echo cd C:\Users\asus\.qclaw\workspace\news-server\github-pages-deploy
echo git remote add origin https://github.com/YOUR_USERNAME/news-website.git
echo git branch -M main
echo git push -u origin main
echo.
echo ================================================
echo 步骤 4：启用 GitHub Pages
echo ================================================
echo.
echo 1. 进入仓库 Settings
echo 2. 左侧菜单点击 Pages
echo 3. Source 选择 Deploy from a branch
echo 4. Branch 选择 main
echo 5. 点击 Save
echo.
echo ================================================
echo 步骤 5：访问你的网站
echo ================================================
echo.
echo 网址：https://YOUR_USERNAME.github.io/news-website/
echo.
echo ================================================
echo.
pause
