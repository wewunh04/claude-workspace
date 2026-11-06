# Restore Downloads cleanup (2026-11-05) using downloads-move-log.csv
# Default = dry-run (nothing moves). Add -Execute to actually move back.
# Never overwrites: if a file already exists at the original location, it is skipped.
param([switch]$Execute)

$log = Import-Csv -LiteralPath (Join-Path $PSScriptRoot 'downloads-move-log.csv')
$result = foreach ($r in $log) {
    if ($r.Status -ne 'MOVED') { continue }
    $status =
        if (-not (Test-Path -LiteralPath $r.To))  { 'MISSING (moved/deleted since)' }
        elseif (Test-Path -LiteralPath $r.From)   { 'SKIP-EXISTS' }
        elseif ($Execute) {
            try { Move-Item -LiteralPath $r.To -Destination $r.From -ErrorAction Stop; 'RESTORED' }
            catch { 'ERROR: ' + $_.Exception.Message }
        } else { 'WOULD-RESTORE' }
    [pscustomobject]@{ File = Split-Path $r.From -Leaf; Status = $status }
}

"MODE: " + $(if ($Execute) { 'EXECUTE' } else { 'DRY-RUN (nothing moved)' })
$result | Group-Object Status | ForEach-Object { "{0,-32} {1}" -f $_.Name, $_.Count }
$result | Where-Object { $_.Status -notin 'RESTORED','WOULD-RESTORE' } | Select-Object -First 20 | Format-Table -AutoSize
