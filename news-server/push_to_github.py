"""
推送到 GitHub Pages
"""
import shutil
import subprocess
import os

os.chdir("github-pages-deploy")

# 复制文件
print("[*] Copying files...")
shutil.copy("../index.html", "index.html")
shutil.copy("../news-data.js", "news-data.js")
print("[OK] Files copied")

# Git 操作
print("[*] Adding files to git...")
subprocess.run(["git", "add", "."], check=True)

print("[*] Committing...")
subprocess.run(["git", "commit", "-m", "Add history timeline feature"], check=True)

print("[*] Pushing to GitHub...")
result = subprocess.run(["git", "push"], capture_output=True, text=True)

if result.returncode == 0:
    print("[OK] Pushed successfully!")
    print("\nYour website is updated at:")
    print("https://xttey001.github.io/news-website/")
else:
    print(f"[ERROR] Push failed: {result.stderr}")
