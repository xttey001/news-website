# -*- coding: utf-8 -*-
"""Debug why sangsha_module is not in 2026-04-10 section"""
import json

with open('C:\\Users\\asus\\.qclaw\\workspace\\news-server\\github-pages-deploy\\test-news-data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find all occurrences of 2026-04-10
import re
matches = list(re.finditer(r'"2026-04-10"', content))
print(f'Found {len(matches)} occurrences of "2026-04-10"')

# Find first occurrence of sangsha_module after 2026-04-10
idx_0410 = content.find('"2026-04-10"')
idx_sangsha = content.find('"sangsha_module"', idx_0410)
idx_0409 = content.find('"2026-04-09"', idx_0410)

print(f'\nPositions:')
print(f'  2026-04-10 starts at: {idx_0410}')
print(f'  sangsha_module found at: {idx_sangsha}')
print(f'  2026-04-09 starts at: {idx_0409}')

if idx_sangsha > 0:
    if idx_0409 > 0 and idx_sangsha < idx_0409:
        print(f'\n✓ sangsha_module is BEFORE 2026-04-09 (correct position)')
    elif idx_0409 > 0 and idx_sangsha > idx_0409:
        print(f'\n✗ sangsha_module is AFTER 2026-04-09 (wrong position!)')
    else:
        print(f'\n? sangsha_module position unclear')

# Show the structure around 2026-04-10
print(f'\nStructure around 2026-04-10:')
section = content[idx_0410:idx_0410+2000]
print(section[:500])