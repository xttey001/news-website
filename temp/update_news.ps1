$origPath = "C:\Users\asus\temp-news-website\news-data.js"
$entryPath = "C:\Users\asus\.qclaw\workspace\temp\_new_entry.js"
$outPath   = "C:\Users\asus\temp-news-website\news-data.js"

# Load both files
$content  = Get-Content $origPath -Raw
$newEntry = Get-Content $entryPath -Raw

# --- 1. Update header timestamp ---
$content = $content -replace '// 生成时间: \d{4}-\d{2}-\d{2} \d{2}:\d{2}', '// 生成时间: 2026-04-24 08:00'

# --- 2. Replace 2026-04-22 block with new 2026-04-24 block ---
# Pattern: find "2026-04-22": { ... "douyin": []\n\t}\n," then insert new entry before
# Since the file ends with a trailing comma after each date block, we replace the whole 2026-04-22 block
$oldDatePattern = '"2026-04-22": \{[\s\S]*?},\s*\n\t\}'
$content = $content -replace $oldDatePattern, ($newEntry.Trim() + "`n`n" + '          "content": "成交量配合，若不放大则冲高回落风险"' + "`n" + '        }' + "`n" + '    }' + "`n" + '  }' + "`n" + '};')

# --- 3. Update availableDates array ---
# Replace the array to put 2026-04-24 at the front
$content = $content -replace '"2026-04-22"(,\s*)', '"2026-04-24"$1"2026-04-22"$1'

# --- 4. Also update first availableDates entry (it should list 2026-04-24 first) ---
$content = $content -replace '(\["2026-04-22")', ('["2026-04-24",' + "`n" + '        "2026-04-22"')

# Write output
$content | Set-Content $outPath -NoNewline

Write-Host "Done. Checking..."
# Quick sanity: count lines
$lines = (Get-Content $outPath).Count
Write-Host "Lines: $lines"
$has2026 = Select-String -Path $outPath -Pattern "2026-04-24"
Write-Host "Found 2026-04-24: $($has2026.Count) times"
