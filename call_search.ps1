# UTF-8 with BOM
$PSDefaultParameterValues['Out-File:Encoding'] = 'utf8'
$nodePath = "D:\QCLaw\resources\openclaw\config\skills\online-search\scripts\prosearch.cjs"
$paramsFile = "C:\Users\asus\.qclaw\workspace\search_params.json"

# Read params as UTF-8
$paramsContent = Get-Content -Path $paramsFile -Raw -Encoding UTF8
$paramsContent = $paramsContent.Trim()

Write-Host "Params: $paramsContent"

# Try calling with various methods
$result = & node $nodePath $paramsContent 2>&1
Write-Host "Exit code: $LASTEXITCODE"
Write-Host "Output length: $($result.Length)"
Write-Host "First 500 chars: $($result | Select-Object -First 1 | ForEach-Object { $_.ToString().Substring(0, [Math]::Min(500, $_.ToString().Length)) })"
