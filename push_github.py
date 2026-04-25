# -*- coding: utf-8 -*-
"""GitHub API push without git CLI"""
import base64, json, requests

REPO = "xttey001/news-website"
BRANCH = "main"
FILE_PATH = "news-data.js"
TOKEN_FILE = r"C:\Users\asus\.qclaw\workspace\github_token.txt"

# Try to read token from env first
token = None
for path in [
    r"C:\Users\asus\.qclaw\workspace\.github_token",
    r"C:\Users\asus\AppData\Local\GitHubDesktop\github_credentials",
]:
    try:
        with open(path, "r") as f:
            token = f.read().strip()
            break
    except:
        pass

if not token:
    # Try gh auth
    import subprocess
    r = subprocess.run(
        [r"C:\Program Files\GitHub CLI\gh.exe", "auth", "token"],
        capture_output=True, text=True
    )
    if r.returncode == 0:
        token = r.stdout.strip()

if not token:
    print("ERROR: No GitHub token found. Please login with: gh auth login")
    exit(1)

HEADERS = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github.v3+json",
    "User-Agent": "QClaw-Python/1.0"
}

def api_get(url):
    r = requests.get(f"https://api.github.com{url}", headers=HEADERS, timeout=10)
    r.raise_for_status()
    return r.json()

def api_post(url, data):
    r = requests.post(f"https://api.github.com{url}", headers=HEADERS, json=data, timeout=10)
    r.raise_for_status()
    return r.json()

def api_put(url, data):
    r = requests.put(f"https://api.github.com{url}", headers=HEADERS, json=data, timeout=10)
    r.raise_for_status()
    return r.json()

print("Reading file...")
with open(r"C:\Users\asus\.qclaw\workspace\news-data.js", "rb") as f:
    content = f.read()
print(f"File size: {len(content)} bytes")

print("Getting latest commit...")
latest = api_get(f"/repos/{REPO}/branches/{BRANCH}")
commit_sha = latest["commit"]["sha"]
tree_sha = latest["commit"]["commit"]["tree"]["sha"]
print(f"Latest commit: {commit_sha[:8]}")

print("Creating blob...")
blob = api_post(f"/repos/{REPO}/git/blobs", {
    "content": content.decode("utf-8"),
    "encoding": "utf-8"
})
blob_sha = blob["sha"]
print(f"Blob: {blob_sha[:8]}")

print("Creating tree...")
tree = api_post(f"/repos/{REPO}/git/trees", {
    "base_tree": tree_sha,
    "tree": [{
        "path": FILE_PATH,
        "mode": "100644",
        "type": "blob",
        "sha": blob_sha
    }]
})
tree_sha = tree["sha"]
print(f"Tree: {tree_sha[:8]}")

print("Creating commit...")
commit = api_post(f"/repos/{REPO}/git/commits", {
    "message": "更新新闻: 2026-04-15 高开低走分化 医药爆发 原油暴跌",
    "tree": tree_sha,
    "parents": [commit_sha]
})
commit_sha = commit["sha"]
print(f"Commit: {commit_sha[:8]}")

print("Updating branch...")
api_put(f"/repos/{REPO}/git/refs/heads/{BRANCH}", {
    "sha": commit_sha,
    "force": False
})
print("Done! https://xttey001.github.io/news-website/")
