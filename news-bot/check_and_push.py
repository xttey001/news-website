# -*- coding: utf-8 -*-
"""
新闻推送检查器 - 开机后检测是否需要补发
"""
import os
import json
from datetime import datetime, time as dt_time
import sys

# 添加当前目录到路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from news_fetcher import format_news_for_push

STATE_FILE = r"C:\Users\asus\.qclaw\workspace\news-bot\push_state.json"

def load_state():
    """加载推送状态"""
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def save_state(state):
    """保存推送状态"""
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(state, f, ensure_ascii=False, indent=2)

def should_push_today(state, push_time):
    """检查今天该时段是否已推送"""
    today = datetime.now().strftime('%Y-%m-%d')
    key = f"{today}_{push_time}"
    return state.get(key, False)

def mark_pushed(push_time):
    """标记已推送"""
    state = load_state()
    today = datetime.now().strftime('%Y-%m-%d')
    key = f"{today}_{push_time}"
    state[key] = True
    save_state(state)

def get_current_push_slot():
    """获取当前应该推送的时段"""
    now = datetime.now().time()
    
    # 推送时段定义
    slots = [
        (dt_time(9, 0), dt_time(12, 0), '09:00'),   # 9点档
        (dt_time(13, 0), dt_time(21, 0), '13:00'),  # 13点档
        (dt_time(22, 0), dt_time(23, 59), '22:00'), # 22点档
    ]
    
    for start, end, slot_name in slots:
        if start <= now <= end:
            return slot_name
    
    return None

def check_and_push():
    """检查并补发新闻"""
    print("=" * 50)
    print("   新闻推送检查器")
    print(f"   时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    # 检查是否是工作日
    if datetime.now().weekday() >= 5:  # 周六=5, 周日=6
        print("[跳过] 今天是周末，不推送")
        return False
    
    # 获取当前时段
    slot = get_current_push_slot()
    if not slot:
        print("[跳过] 当前不在推送时段内")
        return False
    
    # 检查是否已推送
    state = load_state()
    if should_push_today(state, slot):
        print(f"[跳过] 今天 {slot} 时段已推送")
        return False
    
    # 需要补发
    print(f"[补发] 今天 {slot} 时段未推送，开始补发...")
    
    try:
        result = format_news_for_push()
        print("\n[成功] 新闻已抓取，准备推送...")
        
        # 标记已推送
        mark_pushed(slot)
        
        return result
    except Exception as e:
        print(f"[错误] 补发失败: {e}")
        return False

if __name__ == "__main__":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    result = check_and_push()
    if result:
        print("\n" + result)
