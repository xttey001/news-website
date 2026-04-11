@echo off
chcp 65001 >nul
echo ========================================
echo    财经新闻定时推送脚本
echo    设置: 09:00 / 13:00 / 22:00
echo ========================================

:loop
echo [%date% %time%] 检查新闻...

REM 获取当前小时
for /f "tokens=1-4 delims=/ " %%a in ('date /t') do set yy=%%a&set mo=%%b&set dd=%%c
for /f "tokens=5-8 delims=:." %%a in ('echo %time%') do set hh=%%a

echo 当前时间: %hh% 点

REM 检查是否需要推送 (只在9点、13点、22点)
if "%hh%"=="09" goto push
if "%hh%"=="13" goto push
if "%hh%"=="22" goto push

echo 跳过推送，等待下次检查...
timeout /t 3600 /nobreak >nul
goto loop

:push
echo 开始抓取新闻...
python -c "import sys; sys.stdout.reconfigure(encoding='utf-8'); exec(open('C:/Users/asus/.qclaw/workspace/news-bot/news_scheduler.py', encoding='utf-8').read())"

echo [%date% %time%] 推送完成
echo 等待下一次推送...
timeout /t 7200 /nobreak >nul
goto loop
