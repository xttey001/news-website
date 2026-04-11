@echo off
chcp 65001 >nul
cls

echo.
echo ================================================
echo   财经新闻网站 - 快速启动指南
echo ================================================
echo.
echo 你的网站已部署到 GitHub Pages！
echo.
echo 网址：https://xttey001.github.io/news-website/
echo.
echo ================================================
echo   功能
echo ================================================
echo.
echo ✅ 时间线视图（显示最近 30 天）
echo ✅ 日期切换（点击日期快速查看）
echo ✅ 前一天/后一天导航
echo ✅ 历史新闻存档
echo ✅ 完整的新闻内容（S/A/抖音分类）
echo.
echo ================================================
echo   每日更新（3 种方式）
echo ================================================
echo.
echo 方式 1：一键更新（最简单）
echo   cd C:\Users\asus\.qclaw\workspace\news-server
echo   python daily_update.py
echo.
echo 方式 2：手动步骤（最灵活）
echo   python generate_static_with_history.py
echo   copy index.html github-pages-deploy\
echo   copy news-data.js github-pages-deploy\
echo   cd github-pages-deploy
echo   git add . && git commit -m "Update" && git push
echo.
echo 方式 3：自动定时更新（最省心）
echo   python setup_daily_cron.py
echo   openclaw gateway restart
echo   （之后每天 23:00 自动更新）
echo.
echo ================================================
echo   快速命令
echo ================================================
echo.
echo 更新网站：
echo   python daily_update.py
echo.
echo 生成网站：
echo   python generate_static_with_history.py
echo.
echo 推送到 GitHub：
echo   python push_to_github.py
echo.
echo 设置自动更新：
echo   python setup_daily_cron.py
echo.
echo ================================================
echo   文档
echo ================================================
echo.
echo 快速参考：快速参考.md
echo 详细说明：历史新闻功能说明.md
echo 部署指南：GitHub Pages 完整指南.md
echo 完成总结：完成总结.md
echo.
echo ================================================
echo.
echo 现在就访问你的网站吧！
echo https://xttey001.github.io/news-website/
echo.
pause
