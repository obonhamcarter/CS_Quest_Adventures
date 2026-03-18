# Launch script for Day 03: Pong Game

$ErrorActionPreference = "Stop"

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Day 03: Pong Game" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

Write-Host "📦 Installing dependencies..." -ForegroundColor Yellow
uv sync
Write-Host ""
Write-Host "🎮 Launching Pong..." -ForegroundColor Yellow
Write-Host ""
uv run python src_instr/pong_game.py
