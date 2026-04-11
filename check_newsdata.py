# -*- coding: utf-8 -*-
import subprocess, re

for commit in ['5c7dbd2', '45e69d9', '16deef2', 'ee76788', 'cd722ac', '1c00560']:
    result = subprocess.run(
        ['git', 'show', f'{commit}:news-data.js'],
        capture_output=True,
        cwd=r'C:\Users\asus\.qclaw\workspace\news-server\github-pages-deploy'
    )
    if result.returncode == 0:
        content_bytes = result.stdout
        try:
            content = content_bytes.decode('utf-8', errors='replace')
        except:
            content = content_bytes.decode('latin-1', errors='replace')
        dates = re.findall(b'"(2026-\\d{2}-\\d{2})"', content_bytes)
        unique = sorted(set(dates))
        print(f'{commit}: {len(unique)} dates - {[d.decode() for d in unique]}')
    else:
        print(f'{commit}: ERROR')
