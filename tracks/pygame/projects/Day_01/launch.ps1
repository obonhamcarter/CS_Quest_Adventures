# Launch script for Day 01: Maze Explorer
# Works on Windows PowerShell

$ErrorActionPreference = "Stop"

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Day 01: Maze Explorer" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Check if uv is installed
$uvInstalled = Get-Command uv -ErrorAction SilentlyContinue
if (-not $uvInstalled) {
    Write-Host "❌ UV is not installed!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Install UV with:"
    Write-Host '  powershell -c "irm https://astral.sh/uv/install.ps1 | iex"'
    Write-Host ""
    exit 1
}

Write-Host "✓ UV is installed" -ForegroundColor Green

# Get script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

Write-Host "✓ Working directory: $scriptDir" -ForegroundColor Green
Write-Host ""

# Install dependencies
Write-Host "📦 Installing dependencies..." -ForegroundColor Yellow
uv sync
Write-Host "✓ Dependencies installed" -ForegroundColor Green
Write-Host ""

# Show menu
Write-Host "Select what to run:" -ForegroundColor Yellow
Write-Host "1) Complete instructor version (src_instr/maze_game.py)"
Write-Host "2) Student template (src_template/maze_game.py)"
Write-Host "3) Run tests"
Write-Host "4) Exit"
Write-Host ""

$choice = Read-Host "Enter choice [1-4]"

switch ($choice) {
    "1" {
        Write-Host ""
        Write-Host "🎮 Launching complete game..." -ForegroundColor Yellow
        Write-Host ""
        uv run python src_instr/maze_game.py
    }
    "2" {
        Write-Host ""
        Write-Host "🎮 Launching student template..." -ForegroundColor Yellow
        Write-Host ""
        uv run python src_template/maze_game.py
    }
    "3" {
        Write-Host ""
        Write-Host "🧪 Running tests..." -ForegroundColor Yellow
        Write-Host ""
        uv run pytest tests/ -v
    }
    "4" {
        Write-Host "Goodbye!" -ForegroundColor Green
        exit 0
    }
    default {
        Write-Host "❌ Invalid choice" -ForegroundColor Red
        exit 1
    }
}

Write-Host ""
Write-Host "✓ Done!" -ForegroundColor Green
