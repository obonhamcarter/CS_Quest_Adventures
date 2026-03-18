# Launch script for Day 04: Snake Game

$ErrorActionPreference = "Stop"

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Day 04: Snake Game" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

Write-Host "📦 Installing dependencies..." -ForegroundColor Yellow
uv sync
Write-Host ""
Write-Host "🎮 Launching Snake..." -ForegroundColor Yellow
Write-Host ""
uv run python src_instr/snake_game.py
