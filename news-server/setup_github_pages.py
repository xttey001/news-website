"""
GitHub Pages 自动部署脚本
"""
import subprocess
import os
import sys

print("\n" + "="*60)
print("GitHub Pages Deployment")
print("="*60 + "\n")

# 检查是否有 git
try:
    result = subprocess.run(["git", "--version"], capture_output=True, text=True)
    print(f"[OK] Git found: {result.stdout.strip()}\n")
except:
    print("[ERROR] Git not found. Please install Git first:")
    print("https://git-scm.com/download/win\n")
    sys.exit(1)

# 创建 GitHub Pages 目录
gh_pages_dir = "github-pages-deploy"
os.makedirs(gh_pages_dir, exist_ok=True)

# 复制 index.html
import shutil
shutil.copy("index.html", f"{gh_pages_dir}/index.html")

print("[1/5] Created deployment directory\n")

# 进入目录
os.chdir(gh_pages_dir)

# 初始化 git
print("[2/5] Initializing Git repository...")
subprocess.run(["git", "init"], capture_output=True)
print("[OK]\n")

# 创建 .nojekyll 文件（告诉 GitHub 不要用 Jekyll 处理）
with open(".nojekyll", 'w') as f:
    f.write("")
print("[3/5] Created .nojekyll file\n")

# 添加文件
print("[4/5] Adding files to Git...")
subprocess.run(["git", "add", "."], capture_output=True)
subprocess.run(["git", "commit", "-m", f"Update news - {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M')}"], capture_output=True)
print("[OK]\n")

# 提示下一步
print("[5/5] Next Steps:")
print("="*60)
print("\n1. Create a GitHub repository:")
print("   - Go to: https://github.com/new")
print("   - Repository name: news-website")
print("   - Make it PUBLIC")
print("   - Click 'Create repository'\n")

print("2. Push to GitHub:")
print("   cd github-pages-deploy")
print("   git remote add origin https://github.com/YOUR_USERNAME/news-website.git")
print("   git branch -M main")
print("   git push -u origin main\n")

print("3. Enable GitHub Pages:")
print("   - Go to repository Settings")
print("   - Click 'Pages' in left sidebar")
print("   - Source: Deploy from a branch")
print("   - Branch: main")
print("   - Click 'Save'\n")

print("4. Access your website:")
print("   https://YOUR_USERNAME.github.io/news-website/\n")

print("="*60)
print("Alternative: Use GitHub CLI (gh)")
print("="*60)
print("\nIf you have GitHub CLI installed:")
print("  cd github-pages-deploy")
print("  gh repo create news-website --public --source=. --push")
print("  gh api repos/{owner}/news-website/pages -X POST -f source='{\"branch\":\"main\"}'\n")

print("OR run the automated script:\n")
print("  python deploy_to_github.py\n")

print("="*60 + "\n")

# 返回上级目录
os.chdir("..")
