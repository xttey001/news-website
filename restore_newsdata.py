# -*- coding: utf-8 -*-
import subprocess, os

# Restore news-data.js from cd722ac (which has all 14 dates)
result = subprocess.run(
    ['git', 'show', 'cd722ac:news-data.js'],
    capture_output=True,
    cwd=r'C:\Users\asus\.qclaw\workspace\news-server\github-pages-deploy'
)
if result.returncode == 0:
    content = result.stdout
    # Save to file
    with open(r'C:\Users\asus\.qclaw\workspace\news-server\github-pages-deploy\news-data.js', 'wb') as f:
        f.write(content)
    print('Restored from cd722ac. Size:', len(content), 'bytes')
    
    # Verify
    import re
    dates = re.findall(b'"(2026-\\d{2}-\\d{2})"', content)
    unique = sorted(set(dates))
    print('Dates restored:', len(unique), unique)
else:
    print('ERROR:', result.returncode)
