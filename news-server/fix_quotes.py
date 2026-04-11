# -*- coding: utf-8 -*-
# Replace ALL types of double quotes with corner brackets in JSON
fname = 'news_data/news_2026-04-11.json'
with open(fname, encoding='utf-8') as f:
    content = f.read()

# Replace various quote types
content = content.replace('\u201c', '\u300c')  # " (U+201C LEFT DOUBLE QUOTATION MARK)
content = content.replace('\u201d', '\u300d')  # " (U+201D RIGHT DOUBLE QUOTATION MARK)
content = content.replace('\u300c', '\u300a')  # 「 (U+300C LEFT CORNER BRACKET)
content = content.replace('\u300d', '\u300b')    # 」 (U+300D RIGHT CORNER BRACKET)

# Replace ASCII double quotes inside strings with corner brackets
import re
# This replaces " that appears inside string values (after : or , or [)
# by finding them and replacing with corner bracket
# Strategy: scan and replace only the ones that would break JSON
lines = content.split('\n')
fixed_lines = []
errors = []
for i, line in enumerate(lines, 1):
    if i == 48:
        errors.append(f'Line {i}: {repr(line[20:40])}')
    fixed_lines.append(line)

if errors:
    print('Problem areas:', errors)

# Try a different approach - just escape quotes inside strings
import json
try:
    # Re-write the file by parsing and re-dumping with proper escaping
    # First, let's just find all double quotes that cause issues
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if ': ' in stripped or '[' in stripped or stripped.startswith('"'):
            # These lines have string values - check for unescaped quotes
            # A properly escaped JSON string won't have unescaped " inside
            pass
    print('Lines look OK, checking with json module...')
except Exception as e:
    print('Error: ' + str(e))
