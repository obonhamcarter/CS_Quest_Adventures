# Launch script for Day 07: Dungeon Crawler

$ErrorActionPreference = "Stop"

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Day 07: Dungeon Crawler" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

Write-Host "📦 Installing dependencies..." -ForegroundColor Yellow
uv sync
Write-Host ""
Write-Host "🎮 Launching Dungeon Crawler..." -ForegroundColor Yellow
Write-Host ""
uv run python src_instr/dungeon_crawler.py
