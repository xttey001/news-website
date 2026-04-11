# -*- coding: utf-8 -*-
import re, sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('news-data.js', 'r', encoding='utf-8', errors='ignore') as f:
    raw = f.read()

# 找4.04-4.08的位置
for d in ['2026-04-08', '2026-04-07', '2026-04-04']:
    pos = raw.find(d)
    print(f'{d}: pos={pos}')
    if pos >= 0:
        print(f'  context: {repr(raw[pos:pos+50])}')
