# Launch script for Day 06: Frogger

$ErrorActionPreference = "Stop"

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Day 06: Frogger Clone" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

Write-Host "📦 Installing dependencies..." -ForegroundColor Yellow
uv sync
Write-Host ""
Write-Host "🎮 Launching Frogger..." -ForegroundColor Yellow
Write-Host ""
uv run python src_instr/frogger_game.py
