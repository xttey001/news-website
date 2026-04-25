# WNews Daily Auto-Push Script
param([string]$LogFile = "C:\Users\asus\.qclaw\workspace\news-evolution\logs\update_$(Get-Date -Format 'yyyyMMdd_HHmm').log")

# Setup logging
$LogDir = Split-Path $LogFile -Parent
if (!(Test-Path $LogDir)) { New-Item -ItemType Directory -Path $LogDir -Force | Out-Null }
if (!(Test-Path $LogFile)) { New-Item -ItemType File -Path $LogFile -Force | Out-Null }

function Log($Msg, $Lvl="INFO") {
    $Line = "[$(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')] [$Lvl] $Msg"
    Write-Host $Line
    Add-Content -Path $LogFile -Value $Line
}

Log "=== Start Daily Update ==="

# Go to wnews directory
$Wnews = "d:\WorkBuddy\新闻网站\wnews"
if (!(Test-Path $Wnews)) {
    Log "Directory not found: $Wnews" "ERROR"
    exit 1
}
cd $Wnews
Log "Directory: $Wnews"

# Check Git status
Log "Check Git status..."
$Status = git status --porcelain 2>&1
if ($LASTEXITCODE -ne 0) {
    Log "Git error: $Status" "ERROR"
    exit 1
}

# Push if changes exist
if ($Status) {
    $Date = Get-Date -Format "yyyy-MM-dd"
    $Time = Get-Date -Format "HH:mm"
    Log "Changes found, committing..."
    
    git add -A
    git commit -m "Auto: $Date ($Time)"
    
    git remote set-url origin https://github.com/xttey001/wnews.git 2>$null
    git push origin main 2>&1 | ForEach-Object { Log $_ }
    
    if ($LASTEXITCODE -eq 0) {
        Log "Pushed successfully!"
        Log "URL: https://xttey001.github.io/wnews/"
    } else {
        Log "Push failed" "ERROR"
    }
} else {
    Log "No changes"
}

Log "=== Complete ==="
