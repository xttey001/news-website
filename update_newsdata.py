# -*- coding: utf-8 -*-
import json, re, shutil

# Read today's analysis
with open(r'C:\Users\asus\.qclaw\workspace\today_analysis.json', 'r', encoding='utf-8') as f:
    today = json.load(f)

# Read current news-data.js
nd_path = r'C:\Users\asus\.qclaw\workspace\news-data.js'
with open(nd_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Check if date already exists
date_key = "'" + today['date'] + "':"
if date_key in content:
    print("Date already exists, will replace")
    # Remove old entry
    pattern = r",?\s*'" + today['date'] + r"':\s*\{[^}]*(?:\{[^}]*\}[^}]*)*\},?"
    content = re.sub(pattern, '', content, flags=re.DOTALL)
else:
    print("Date does not exist, will add")

# Backup
shutil.copy(nd_path, nd_path + '.bak')

# Serialize new entry
new_entry = json.dumps(today, ensure_ascii=False, indent=2)
new_entry_lines = new_entry.split('\n')
# Indent each line
new_entry_indented = '\n'.join('  ' + line for line in new_entry_lines)
# Wrap with date key
new_entry_text = "  '" + today['date'] + "': " + new_entry_indented[2:]  # remove extra indent

# Find insertion point (before the last "};" or "const availableDates")
# Find the position of "const availableDates"
av_pos = content.rfind('const availableDates')
if av_pos == -1:
    # Find last closing brace of an entry
    print("Finding insertion point...")
    av_pos = content.rfind('}')

# Insert before availableDates
insert_pos = content.rfind(',', 0, av_pos) + 1
if insert_pos == 0:
    insert_pos = av_pos

new_content = content[:insert_pos] + "\n" + new_entry_text + ",\n" + content[insert_pos:]

# Verify syntax
try:
    json.loads('{' + new_content.split('const newsData')[0].split('{', 1)[1].rsplit('}', 1)[0] + '}')
    print("Syntax check passed")
except Exception as e:
    print("Syntax error:", e)

# Write
with open(nd_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done. File updated.")

# Verify availableDates still exists
with open(nd_path, 'r', encoding='utf-8') as f:
    final = f.read()
if 'const availableDates' in final:
    print("availableDates: OK")
else:
    print("ERROR: availableDates missing!")
