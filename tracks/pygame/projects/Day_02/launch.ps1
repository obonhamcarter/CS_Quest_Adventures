# Launch script for Day 02: Bouncing Ball Physics

$ErrorActionPreference = "Stop"

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Day 02: Bouncing Ball Physics" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

$uvInstalled = Get-Command uv -ErrorAction SilentlyContinue
if (-not $uvInstalled) {
    Write-Host "❌ UV is not installed!" -ForegroundColor Red
    exit 1
}

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

Write-Host "📦 Installing dependencies..." -ForegroundColor Yellow
uv sync
Write-Host "✓ Dependencies installed" -ForegroundColor Green
Write-Host ""
Write-Host "🎮 Launching game..." -ForegroundColor Yellow
Write-Host ""
uv run python src_instr/bouncing_ball.py
