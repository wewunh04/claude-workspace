# 포트폴리오를 내 컴퓨터에서 테스트하는 스크립트
# 사용법: 이 파일을 오른쪽 클릭 → "PowerShell에서 실행"
#        또는 터미널에서: powershell -ExecutionPolicy Bypass -File start-local.ps1
# 끝낼 때: 이 창에서 Ctrl + C

$ErrorActionPreference = 'Stop'
Set-Location -LiteralPath $PSScriptRoot
$port = 5500

Write-Host "1) .env.local → config.js 만드는 중..."
node scripts/gen-config.mjs
if ($LASTEXITCODE -ne 0) { Write-Host "설정 파일을 만들지 못했어요. 위 메시지를 확인하세요."; Read-Host "Enter 를 누르면 닫혀요"; exit 1 }

Write-Host "2) 로컬 서버 시작: http://localhost:$port  (내 컴퓨터에서만 접속 가능)"
Start-Process "http://localhost:$port"
python -m http.server $port --bind 127.0.0.1
