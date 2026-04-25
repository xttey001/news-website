import re

orig_path = r"C:\Users\asus\temp-news-website\news-data.js"
entry_path = r"C:\Users\asus\.qclaw\workspace\temp\_new_entry.js"
out_path   = r"C:\Users\asus\temp-news-website\news-data.js"

with open(orig_path, "r", encoding="utf-8") as f:
    content = f.read()

with open(entry_path, "r", encoding="utf-8") as f:
    new_entry = f.read()

# 1. Update header timestamp
content = re.sub(
    r'// 生成时间: \d{4}-\d{2}-\d{2} \d{2}:\d{2}',
    '// 生成时间: 2026-04-24 08:00',
    content
)

# 2. Find the end marker of the 2026-04-22 block
# The block ends with:     ],
#     "douyin": []
#   },
# then followed by the newsData closing
old_end_marker = '    "douyin": []\n  },\n'
idx_old_end = content.rfind(old_end_marker)
if idx_old_end == -1:
    print("ERROR: Could not find old block end marker")
    exit(1)
print(f"Found end marker at char {idx_old_end}")

# The start of the 2026-04-22 block
old_start_marker = '"2026-04-22": {'
idx_old_start = content.find(old_start_marker)
if idx_old_start == -1:
    print("ERROR: Could not find old block start marker")
    exit(1)
print(f"Found start marker at char {idx_old_start}")

# Replace the whole 2026-04-22 block (from start to end_marker inclusive)
old_block = content[idx_old_start:idx_old_end + len(old_end_marker)]
print(f"Old block length: {len(old_block)} chars")

# Construct new content: before + new entry + newsData closing
# new_entry already has a trailing comma at the end
# But we need: new_entry (already ends with "},\n") 
# then: "  }\n};\n"
new_content = content[:idx_old_start] + new_entry + "  }\n};\n"

with open(out_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("File written. Checking...")

# Sanity checks
lines = new_content.split('\n')
print(f"Total lines: {len(lines)}")
date_count = new_content.count('"2026-04-24"')
print(f'2026-04-24 occurrences: {date_count}')

# Check first few lines
for i, l in enumerate(lines[:5], 1):
    print(f"  {i}: {l[:100]}")

# Check last few lines
for i, l in enumerate(lines[-6:], len(lines)-5):
    print(f"  {i}: {l[:100]}")

# Verify availableDates has 2026-04-24 first
ad_match = re.search(r'const availableDates = \[([^\]]+)\]', new_content)
if ad_match:
    first_date = ad_match.group(1).strip().split(',')[0].strip('"')
    print(f"First availableDate: {first_date}")
