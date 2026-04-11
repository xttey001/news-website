# -*- coding: utf-8 -*-
"""Final verification of generated file"""
import re

with open('C:\\Users\\asus\\.qclaw\\workspace\\news-server\\github-pages-deploy\\news-data.js', 'r', encoding='utf-8') as f:
    json_str = f.read()

# Find top-level date keys
pattern = r'"(2026-\d{2}-\d{2})":\s*\{'
matches = list(re.finditer(pattern, json_str))

print('Top-level date keys in generated file:')
for m in matches:
    print(f'  {m.group(1)} at position {m.start()}')

# Find sangsha_module occurrences
sg_matches = list(re.finditer(r'"sangsha_module"', json_str))
print(f'\nFound {len(sg_matches)} sangsha_module occurrences')

# Check each date
results = []
for i, date_match in enumerate(matches):
    date = date_match.group(1)
    start = date_match.start()
    end = matches[i+1].start() if i+1 < len(matches) else len(json_str)
    
    sg_in_range = [m for m in sg_matches if start < m.start() < end]
    wd_in_range = [m for m in re.finditer(r'"white_dragon"', json_str) if start < m.start() < end]
    
    has_sg = len(sg_in_range) > 0
    has_wd = len(wd_in_range) > 0
    results.append((date, has_sg, has_wd))

print('\nVerification results:')
for date, has_sg, has_wd in results:
    status = 'OK' if has_sg and has_wd else 'MISSING'
    print(f'  {date}: sangsha={has_sg}, white_dragon={has_wd} [{status}]')