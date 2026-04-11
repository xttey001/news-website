@echo off
chcp 65001 >nul

echo Creating cron job: 财经新闻-早报...
"D:\QCLaw\resources\openclaw\config\skills\qclaw-openclaw\scripts\openclaw-win.cmd" cron add --name="财经新闻-早报" --cron="0 9 * * 1-5" --tz="Asia/Shanghai" --session=isolated --message="执行 Python 脚本获取财经新闻：python -c \"import sys; sys.stdout.reconfigure(encoding='utf-8'); exec(open(r'C:/Users/asus/.qclaw/workspace/news-bot/news_scheduler_v2.py', encoding='utf-8').read())\" 然后读取 C:\\Users\\asus\\.qclaw\\workspace\\news-bot\\latest_news.txt 的内容，通过 message 工具发送到微信频道（channel: weixin, to: o9cq807dwW0H1oaoEkmj7r8hfVeU@im.wechat）。只发送新闻内容，不要其他解释。" --announce --channel=weixin --to="o9cq807dwW0H1oaoEkmj7r8hfVeU@im.wechat"

echo.
echo Creating cron job: 财经新闻-午报...
"D:\QCLaw\resources\openclaw\config\skills\qclaw-openclaw\scripts\openclaw-win.cmd" cron add --name="财经新闻-午报" --cron="0 13 * * 1-5" --tz="Asia/Shanghai" --session=isolated --message="执行 Python 脚本获取财经新闻：python -c \"import sys; sys.stdout.reconfigure(encoding='utf-8'); exec(open(r'C:/Users/asus/.qclaw/workspace/news-bot/news_scheduler_v2.py', encoding='utf-8').read())\" 然后读取 C:\\Users\\asus\\.qclaw\\workspace\\news-bot\\latest_news.txt 的内容，通过 message 工具发送到微信频道（channel: weixin, to: o9cq807dwW0H1oaoEkmj7r8hfVeU@im.wechat）。只发送新闻内容，不要其他解释。" --announce --channel=weixin --to="o9cq807dwW0H1oaoEkmj7r8hfVeU@im.wechat"

echo.
echo Creating cron job: 财经新闻-晚报...
"D:\QCLaw\resources\openclaw\config\skills\qclaw-openclaw\scripts\openclaw-win.cmd" cron add --name="财经新闻-晚报" --cron="0 22 * * 1-5" --tz="Asia/Shanghai" --session=isolated --message="执行 Python 脚本获取财经新闻：python -c \"import sys; sys.stdout.reconfigure(encoding='utf-8'); exec(open(r'C:/Users/asus/.qclaw/workspace/news-bot/news_scheduler_v2.py', encoding='utf-8').read())\" 然后读取 C:\\Users\\asus\\.qclaw\\workspace\\news-bot\\latest_news.txt 的内容，通过 message 工具发送到微信频道（channel: weixin, to: o9cq807dwW0H1oaoEkmj7r8hfVeU@im.wechat）。只发送新闻内容，不要其他解释。" --announce --channel=weixin --to="o9cq807dwW0H1oaoEkmj7r8hfVeU@im.wechat"

echo.
echo Done!
pause
