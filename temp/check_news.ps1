$matches = Select-String -Path 'C:\Users\asus\temp-news-website\news-data.js' -Pattern '2026-04-24'
foreach ($m in $matches) {
    Write-Host "Line $($m.LineNumber): $($m.Line.Substring(0, [Math]::Min(130, $m.Line.Length)))"
}
Write-Host ""
Write-Host "Total: $($matches.Count) matches"
Write-Host ""

# Check the start of availableDates
$lines = Get-Content 'C:\Users\asus\temp-news-website\news-data.js'
$dateLine = $lines | Where-Object { $_ -match 'availableDates' }
$idx = ($lines.IndexOf($dateLine))
Write-Host "availableDates at line: $idx"
Write-Host $dateLine.Substring(0, [Math]::Min(200, $dateLine.Length))
