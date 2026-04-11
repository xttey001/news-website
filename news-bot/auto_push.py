"""
财经新闻定时推送系统
使用方式: 被 Windows 任务计划程序调用
"""

import subprocess
import sys
import os
import json
from datetime import datetime

# 添加 OpenClaw 的 Python 路径
sys.path.insert(0, r'D:\QCLaw\resources\openclaw')

# 导入 OpenClaw 的 message 模块
try:
    from openclaw.tools.message import MessageTool
    HAS_MESSAGE_TOOL = True
except:
    HAS_MESSAGE_TOOL = False

def main():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] 定时新闻推送开始...")
    
    # 1. 执行新闻抓取
    news_file = r'C:\Users\asus\.qclaw\workspace\news-bot\latest_news.txt'
    
    try:
        import subprocess
        result = subprocess.run(
            ['python', '-c', '''
import sys
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"C:\\Users\\asus\\.qclaw\\workspace\\news-bot")
from news_scheduler import format_push
result = format_push()
with open(r"C:\\Users\\asus\\.qclaw\\workspace\\news-bot\\latest_news.txt", "w", encoding="utf-8") as f:
    f.write(result)
print("News generated successfully")
'''],
            capture_output=True,
            text=True,
            encoding='utf-8',
            timeout=60
        )
        print(result.stdout)
        if result.stderr:
            print(f"Errors: {result.stderr}")
    except Exception as e:
        print(f"抓取失败: {e}")
        return
    
    # 2. 读取新闻内容
    try:
        with open(news_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except:
        content = f"📊 {datetime.now().strftime('%Y年%m月%d日 %H:%M')} 财经新闻\n\n暂无更新"
    
    # 3. 通过 OpenClaw 发送
    if HAS_MESSAGE_TOOL:
        try:
            tool = MessageTool()
            result = tool.execute({
                "action": "send",
                "channel": "weixin",
                "target": "o9cq807dwW0H1oaoEkmj7r8hfVeU@im.wechat",
                "message": content
            })
            print(f"推送结果: {result}")
        except Exception as e:
            print(f"OpenClaw 推送失败: {e}")
            # 保存到待发送队列
            save_to_queue(content)
    else:
        # OpenClaw 不可用时保存到队列
        save_to_queue(content)
        print("已保存到待发送队列")

def save_to_queue(content):
    """保存到待发送队列"""
    queue_file = r'C:\Users\asus\.qclaw\workspace\news-bot\pending_queue.json'
    queue = []
    if os.path.exists(queue_file):
        try:
            with open(queue_file, 'r', encoding='utf-8') as f:
                queue = json.load(f)
        except:
            queue = []
    
    queue.append({
        "time": datetime.now().isoformat(),
        "content": content
    })
    
    with open(queue_file, 'w', encoding='utf-8') as f:
        json.dump(queue, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
