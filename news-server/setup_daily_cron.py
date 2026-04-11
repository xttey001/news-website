"""
创建定时任务：每天 23:00 自动更新新闻到 GitHub Pages
"""
import json
import os

# 读取现有的 cron 配置
cron_file = "cron/jobs.json"
with open(cron_file, 'r', encoding='utf-8') as f:
    jobs = json.load(f)

# 创建新的定时任务
new_job = {
    "name": "Daily GitHub Pages Update",
    "schedule": {
        "kind": "cron",
        "expr": "0 23 * * *",  # 每天 23:00
        "tz": "Asia/Shanghai"
    },
    "payload": {
        "kind": "systemEvent",
        "text": "执行每日新闻更新到 GitHub Pages：cd C:\\Users\\asus\\.qclaw\\workspace\\news-server && python daily_update.py"
    },
    "delivery": {
        "mode": "announce",
        "channel": "weixin",
        "to": "o9cq807dwW0H1oaoEkmj7r8hfVeU@im.wechat"
    },
    "sessionTarget": "main",
    "enabled": True
}

# 添加到 jobs 列表
jobs.append(new_job)

# 保存
with open(cron_file, 'w', encoding='utf-8') as f:
    json.dump(jobs, f, ensure_ascii=False, indent=2)

print("[OK] Created daily update cron job")
print("[OK] Schedule: Every day at 23:00 (Asia/Shanghai)")
print("[OK] Job will automatically update GitHub Pages")
