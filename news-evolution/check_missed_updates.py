# -*- coding: utf-8 -*-
"""
错过更新检查脚本

功能：在WorkBuddy启动时自动检查是否需要补执行
- 检查今天是否已更新
- 如果错过，自动执行更新

使用方法：
1. 在WorkBuddy启动时自动运行此脚本
2. 或手动运行：python check_missed_updates.py
"""

import os
import json
from datetime import datetime, timedelta
from pathlib import Path
import subprocess
import sys

# 路径配置
EVOLUTION_DIR = Path(__file__).parent
WNEWS_DIR = Path(r'c:\Users\asus\wnews')
NEWS_DATA_FILE = WNEWS_DIR / 'news-data.js'

def get_last_update_date():
    """获取最后更新日期"""
    if not NEWS_DATA_FILE.exists():
        print(f"❌ news-data.js 不存在: {NEWS_DATA_FILE}")
        return None
    
    try:
        with open(NEWS_DATA_FILE, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取 availableDates
        import re
        match = re.search(r'availableDates\s*=\s*(\[[^\]]+\])', content)
        if match:
            dates = json.loads(match.group(1))
            if dates:
                # 返回最新日期
                return dates[-1]
    except Exception as e:
        print(f"❌ 读取news-data.js失败: {e}")
    
    return None

def should_update():
    """判断是否需要更新"""
    last_date = get_last_update_date()
    
    if not last_date:
        print("⚠️ 无法获取最后更新日期，建议更新")
        return True
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    if last_date < today:
        print(f"📅 最后更新: {last_date}, 今天: {today}")
        print(f"⏭️ 需要更新（错过了 {last_date} 到 {today} 的更新）")
        return True
    elif last_date == today:
        # 检查是否是早上还是晚上
        hour = datetime.now().hour
        if hour >= 20:
            # 晚上8点后检查今天是否已更新晚报
            print(f"✅ 今天已更新（{last_date}），当前时间 {hour}:00")
            return False
        else:
            print(f"✅ 今天已更新（{last_date}）")
            return False
    else:
        print(f"✅ 数据已是最新（{last_date}）")
        return False
    
    return False

def run_update():
    """执行更新"""
    print("\n" + "="*50)
    print("🚀 开始执行更新...")
    print("="*50 + "\n")
    
    os.chdir(EVOLUTION_DIR)
    result = subprocess.run(
        [sys.executable, 'daily_update_v4.py'],
        capture_output=True,
        text=True,
        encoding='utf-8'
    )
    
    print(result.stdout)
    if result.stderr:
        print("⚠️ 错误信息:")
        print(result.stderr)
    
    if result.returncode == 0:
        print("\n✅ 更新完成！")
    else:
        print(f"\n❌ 更新失败（退出码: {result.returncode}）")
    
    return result.returncode == 0

def main():
    print("="*50)
    print("🔍 wnews 错过更新检查")
    print("="*50 + "\n")
    
    print(f"当前时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    if should_update():
        print("\n" + "-"*50)
        user_input = input("是否现在执行更新？(y/n): ").strip().lower()
        
        if user_input == 'y':
            run_update()
        else:
            print("⏭️ 跳过更新")
    else:
        print("\n✅ 无需更新")

if __name__ == '__main__':
    main()
