# -*- coding: utf-8 -*-
with open(r'C:\Users\asus\.qclaw\workspace\news-server\github-pages-deploy\news-data.js', 'rb') as f:
    data = f.read()
import re
dates = re.findall(b'"(2026-[0-9][0-9]-[0-9][0-9])"', data)
unique = sorted(set(dates))
print(len(unique), 'dates:', [d.decode() for d in unique])
print('File size:', len(data))
print('Has availableDates:', b'availableDates' in data)
print('Has 04-08:', b'"2026-04-08"' in data)
