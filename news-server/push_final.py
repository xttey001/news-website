import subprocess
import os

os.chdir("github-pages-deploy")

# 检查是否有更改
result = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
if result.stdout.strip():
    print("[*] Changes detected, committing...")
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "Update with 5 days of news"], check=True)
    print("[OK] Committed")
else:
    print("[*] No changes to commit")

# 推送
print("[*] Pushing to GitHub...")
result = subprocess.run(["git", "push"], capture_output=True, text=True)
if result.returncode == 0:
    print("[OK] Pushed successfully!")
    print("\nYour website is updated at:")
    print("https://xttey001.github.io/news-website/")
else:
    print(f"[ERROR] {result.stderr}")
