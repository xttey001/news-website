# -*- coding: utf-8 -*-
import re

c = open(r'C:\Users\asus\.qclaw\workspace\news-server\github-pages-deploy\news-data.js', 'r', encoding='utf-8').read()
m = re.findall(r"'\d{4}-\d{2}-\d{2}':", c)
print("Dates found:", m[:5])
print("2026-04-15 in file:", '2026-04-15' in c)
print("availableDates in file:", 'const availableDates' in c)
print("File size:", len(c))
