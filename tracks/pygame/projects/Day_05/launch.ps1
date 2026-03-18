# Launch script for Day 05: Flappy Bird

$ErrorActionPreference = "Stop"

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Day 05: Flappy Bird Clone" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

Write-Host "📦 Installing dependencies..." -ForegroundColor Yellow
uv sync
Write-Host ""
Write-Host "🎮 Launching Flappy Bird..." -ForegroundColor Yellow
Write-Host ""
uv run python src_instr/flappy_bird.py
