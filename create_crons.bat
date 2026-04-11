@echo off
chcp 65001 >nul
set "SCRIPT=D:\QCLaw\resources\openclaw\config\skills\qclaw-openclaw\scripts\openclaw-win.cmd"

set "MSG=执行 Python 脚本获取财经新闻：python -c \"import sys; sys.stdout.reconfigure(encoding='utf-8'); exec(open(r'C:/Users/asus/.qclaw/workspace/news-bot/news_scheduler_v2.py', encoding='utf-8').read())\"，然后读取 C:/Users/asus/.qclaw/workspace/news-bot/latest_news.txt 的内容，通过 message 工具发送到微信频道（channel: weixin, to: o9cq807dwW0H1oaoEkmj7r8hfVeU@im.wechat）。只发送新闻内容，不要其他解释。不要回复HEARTBEAT_OK，不要解释你是谁。"

echo === Creating Cron 1: 财经新闻-早报 (0 9 * * 1-5) ===
call "%SCRIPT%" cron add --name "财经新闻-早报" --cron "0 9 * * 1-5" --tz "Asia/Shanghai" --session isolated --message "%MSG%" --channel weixin --to "o9cq807dwW0H1oaoEkmj7r8hfVeU@im.wechat" --announce

echo.
echo === Creating Cron 2: 财经新闻-午报 (0 13 * * 1-5) ===
call "%SCRIPT%" cron add --name "财经新闻-午报" --cron "0 13 * * 1-5" --tz "Asia/Shanghai" --session isolated --message "%MSG%" --channel weixin --to "o9cq807dwW0H1oaoEkmj7r8hfVeU@im.wechat" --announce

echo.
echo === Creating Cron 3: 财经新闻-晚报 (0 22 * * 1-5) ===
call "%SCRIPT%" cron add --name "财经新闻-晚报" --cron "0 22 * * 1-5" --tz "Asia/Shanghai" --session isolated --message "%MSG%" --channel weixin --to "o9cq807dwW0H1oaoEkmj7r8hfVeU@im.wechat" --announce

echo.
echo === Listing all cron jobs ===
call "%SCRIPT%" cron list

echo.
echo Done.
