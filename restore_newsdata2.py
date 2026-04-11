# -*- coding: utf-8 -*-
import subprocess

result = subprocess.run(
    ['git', 'show', 'cd722ac:news-data.js'],
    capture_output=True,
    cwd=r'C:\Users\asus\.qclaw\workspace\news-server\github-pages-deploy'
)
content = result.stdout
print('Bytes from git show:', len(content))

# Remove UTF-8 BOM if present
if content.startswith(b'\xef\xbb\xbf'):
    content = content[3:]
    print('Removed BOM')

with open(r'C:\Users\asus\.qclaw\workspace\news-server\github-pages-deploy\news-data.js', 'wb') as f:
    f.write(content)
print('Written', len(content), 'bytes')

# Verify with Node
import subprocess as sp2
r2 = sp2.run(
    ['node', '-e', 'var d=require(\'./news-data.js\'); console.log(Object.keys(d).length+\' entries\')'],
    capture_output=True, text=True,
    cwd=r'C:\Users\asus\.qclaw\workspace\news-server\github-pages-deploy'
)
print('Node output:', r2.stdout.strip(), r2.stderr.strip()[:100] if r2.stderr else '')
