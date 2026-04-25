with open(r"C:\Users\asus\temp-news-website\news-data.js", "r", encoding="utf-8") as f:
    content = f.read()

lines = content.split('\n')
print(f"Total lines: {len(lines)}")
print(f'Total chars: {len(content)}')

# Count occurrences of key strings
print(f'"2026-04-24" occurrences: {content.count("2026-04-24")}')
print(f'"2026-04-22" occurrences: {content.count("2026-04-22")}')

# Check availableDates
import re
ad_match = re.search(r'const availableDates = \[([^\]]+)\]', content)
if ad_match:
    dates_str = ad_match.group(1)
    first_few = ', '.join(dates_str.split(',')[:5])
    print(f"First 5 availableDates: {first_few}")
else:
    print("availableDates not found")

# Check first 5 lines (raw bytes check)
print("\nFirst 5 lines (repr):")
for i, l in enumerate(lines[:5], 1):
    print(f"  {i}: {repr(l[:100])}")

# Check last 10 lines
print("\nLast 10 lines (repr):")
for i, l in enumerate(lines[-10:], len(lines)-9):
    print(f"  {i}: {repr(l)}")

# Check lines around the new entry start
print("\nLines 6-15 (after newsData = {):")
for i, l in enumerate(lines[5:16], 6):
    print(f"  {i}: {repr(l[:120])}")

# Check around line 600 (end area)
print("\nLines 598-609:")
for i, l in enumerate(lines[597:], 598):
    print(f"  {i}: {repr(l[:120])}")
