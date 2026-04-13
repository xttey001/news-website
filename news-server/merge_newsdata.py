# -*- coding: utf-8 -*-
"""合并 news_data/ 到 news-data.js（只合并已有数据，保留悟空/八戒分析）
"""
import os, json, glob, sys
sys.stdout.reconfigure(encoding='utf-8', errors='replace')

print("=== 合并 news_data 到 news-data.js ===\n")

# Step 1: 收集所有数据
all_dates = {}

# 1a. news_data/*.json
for f in sorted(glob.glob("news_data/news_*.json"), reverse=True):
    name = os.path.basename(f)
    size = os.path.getsize(f)
    if size == 0:
        print(f"  [跳过-空文件] {name}")
        continue
    try:
        with open(f, "r", encoding="utf-8") as fp:
            d = json.load(fp)
        date = d.get("date", "")
        if date:
            all_dates[date] = d
            src = "悟空+八戒" if d.get("wukong_judgment") else "仅S级"
            print(f"  [news_data] {date} → {src}")
    except Exception as e:
        print(f"  [跳过-错误] {name}: {e}")

# 1b. orig_2026*.json（有悟空+八戒的旧数据，优先级高）
for f in sorted(glob.glob("orig_2026*.json")):
    name = os.path.basename(f)
    size = os.path.getsize(f)
    if size == 0:
        print(f"  [跳过-空文件] {name}")
        continue
    try:
        with open(f, "r", encoding="utf-8") as fp:
            d = json.load(fp)
        date = d.get("date", "")
        if date and d.get("wukong_judgment"):
            all_dates[date] = d
            print(f"  [orig补充] {date} → 悟空+八戒 (覆盖news_data)")
    except Exception as e:
        print(f"  [跳过-错误] {name}: {e}")

print(f"\n总计合并: {len(all_dates)} 个日期")

# 按日期排序（最新在前）
sorted_dates = sorted(all_dates.keys(), reverse=True)
print("可用日期:", sorted_dates[:10], "...")

# Step 2: 生成 news-data.js
os.chdir(os.path.dirname(os.path.abspath(__file__)) or ".")

js_lines = []
js_lines.append("// 新闻数据 - 自动生成")
js_lines.append("const newsData = {")

for i, (date, data) in enumerate(sorted(all_dates.items(), reverse=True)):
    comma = "," if i > 0 else ""
    js_lines.append(f'  {comma}"{date}": {json.dumps(data, ensure_ascii=False, indent=2)}')

js_lines.append("};")
js_lines.append("")
js_lines.append(f"const availableDates = {json.dumps(sorted_dates, ensure_ascii=False)};")

# 加上辅助函数
js_lines.append("")
js_lines.append("// 获取前一天")
js_lines.append("function getPreviousDate(date) {")
js_lines.append("    const idx = availableDates.indexOf(date);")
js_lines.append("    return idx < availableDates.length - 1 ? availableDates[idx + 1] : null;")
js_lines.append("}")
js_lines.append("")
js_lines.append("// 获取后一天")
js_lines.append("function getNextDate(date) {")
js_lines.append("    const idx = availableDates.indexOf(date);")
js_lines.append("    return idx > 0 ? availableDates[idx - 1] : null;")
js_lines.append("}")

content = "\n".join(js_lines) + "\n"

# Step 3: 写文件（UTF-8 无 BOM）
with open("news-data.js", "w", encoding="utf-8") as f:
    f.write(content)

print(f"\n✅ news-data.js 已写入 ({len(content)} 字符)")

# Step 4: 验证
print("\n=== 验证语法 ===")
import subprocess
r = subprocess.run(["node", "--check", "news-data.js"], capture_output=True, text=True)
if r.returncode == 0:
    print("✅ JS 语法检查通过")
else:
    print(f"❌ 语法错误: {r.stderr}")
