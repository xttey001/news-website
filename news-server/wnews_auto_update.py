# -*- coding: utf-8 -*-
"""wnews 自动更新脚本 - 推送到 wnews 仓库

与 daily_update_with_models.py 不同，此脚本推送到 wnews 仓库：
- 仓库：git@github.com:xttey001/wnews.git
- 本地：c:\Users\asus\wnews
- 网站：https://xttey001.github.io/wnews/
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

import os
import json
import shutil
from datetime import datetime

print('=== wnews Auto Update - 四层交叉分析版 ===')

# 路径配置
WNEWS_DIR = r'c:\Users\asus\wnews'
NEWS_SERVER_DIR = r'c:\Users\asus\.qclaw\workspace\news-server'

# 1. 在 news-server 目录运行 generate_full_newsdata.py
print('\nStep 1: Generating full news data with cross-analysis...')
os.chdir(NEWS_SERVER_DIR)
import subprocess
result = subprocess.run([sys.executable, 'generate_full_newsdata.py'], 
                       capture_output=True, text=True, timeout=120)
if result.returncode != 0:
    print(f'  Warning: generate_full_newsdata.py failed: {result.stderr[:200]}')
else:
    print(f'  OK: {result.stdout[-200:]}')

# 2. 复制生成的文件到 wnews 仓库
print('\nStep 2: Copying to wnews repository...')
src_js = os.path.join(NEWS_SERVER_DIR, 'github-pages-deploy', 'news-data.js')
src_html = os.path.join(NEWS_SERVER_DIR, 'github-pages-deploy', 'index.html')

# 检查新闻数据文件
if not os.path.exists(src_js):
    # 备选：从 news-server 根目录找
    src_js = os.path.join(NEWS_SERVER_DIR, 'news-data.js')
    if not os.path.exists(src_js):
        print('  ERROR: news-data.js not found!')
        sys.exit(1)

# 复制 news-data.js
dst_js = os.path.join(WNEWS_DIR, 'news-data.js')
shutil.copy2(src_js, dst_js)
print(f'  Copied news-data.js ({os.path.getsize(dst_js)} bytes)')

# 复制 index.html（如果存在更新的版本）
if os.path.exists(src_html):
    dst_html = os.path.join(WNEWS_DIR, 'index.html')
    shutil.copy2(src_html, dst_html)
    print(f'  Copied index.html')

# 3. JS 语法检查
print('\nStep 3: Validating JS syntax...')
check = subprocess.run(['node', '--check', dst_js], capture_output=True, text=True)
if check.returncode == 0:
    print('  JS syntax: OK ✅')
else:
    print(f'  JS syntax ERROR ❌: {check.stderr[:200]}')
    print('  Aborting push!')
    sys.exit(1)

# 4. Git 推送到 wnews 仓库
today = datetime.now().strftime('%Y-%m-%d')
print(f'\nStep 4: Pushing to wnews repository...')
os.chdir(WNEWS_DIR)

# git add
subprocess.run(['git', 'add', '-A'])

# 检查是否有变更
status = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
if not status.stdout.strip():
    print('  No changes to commit')
else:
    # git commit
    commit_msg = f'Auto update: {today} with 4-layer cross analysis'
    subprocess.run(['git', 'commit', '-m', commit_msg])
    
    # git push
    push_result = subprocess.run(['git', 'push', 'origin', 'main'], 
                                capture_output=True, text=True)
    if push_result.returncode == 0:
        print(f'  Pushed successfully ✅')
    else:
        print(f'  Push failed: {push_result.stderr[:200]}')

print(f'\n=== wnews Update Complete ({today}) ===')
print(f'Website: https://xttey001.github.io/wnews/')
