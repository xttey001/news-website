# -*- coding: utf-8 -*-
import re

with open('github-pages-deploy/news-data.js', encoding='utf-8') as f:
    content = f.read()

start = content.find('"2026-04-11": {')
if start == -1:
    print("NOT FOUND")
    exit()

brace_count = 0
end = start
for i in range(start, len(content)):
    if content[i] == '{':
        brace_count += 1
    elif content[i] == '}':
        brace_count -= 1
        if brace_count == 0:
            end = i + 1
            break
block = content[start:end]

# Top-level fields
fields = re.findall(r'"(\w+)":\s*\{', block)
print("Top-level fields:", fields)

# Check s_level items
sl = re.search(r'"s_level":\s*\[(.*?)\]', block, re.DOTALL)
if sl:
    if 'bayes_analysis' in sl.group(1):
        print("S-level has bayes_analysis: YES")
    else:
        print("S-level has bayes_analysis: NO")

# Check bajie_conclusion
bj_fields = re.findall(r'"bajie_conclusion":\s*\{(.*?)(?=\n\s*"[^"]+":|$)', block, re.DOTALL)
if bj_fields:
    print("bajie_conclusion key fields:", [f for f in re.findall(r'"(\w+)":', bj_fields[0]) if f][:15])

# Check overall
if '"overall":' in block:
    print("overall field: EXISTS")
else:
    print("overall field: MISSING")

# Check tang_sanzang
if 'tang_sanzang' in block:
    print("tang_sanzang: EXISTS")
    ts = re.search(r'"tang_sanzang":\s*\{(.*?)\}', block, re.DOTALL)
    if ts:
        ts_fields = re.findall(r'"([^"]+)":', ts.group(1))
        print("  tang_sanzang fields:", ts_fields[:10])
else:
    print("tang_sanzang: MISSING")
