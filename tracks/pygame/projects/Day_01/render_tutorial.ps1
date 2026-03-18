# Render Quarto tutorial for Day 01 (Windows)
# Sets up Python environment and renders to HTML

$ErrorActionPreference = "Stop"

Write-Host "================================" -ForegroundColor Cyan
Write-Host "Rendering Day 01 Tutorial" -ForegroundColor Cyan
Write-Host "================================" -ForegroundColor Cyan
Write-Host ""

# Check if Quarto is installed
$quartoInstalled = Get-Command quarto -ErrorAction SilentlyContinue
if (-not $quartoInstalled) {
    Write-Host "❌ Quarto is not installed!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Install Quarto from: https://quarto.org/docs/get-started/"
    Write-Host ""
    exit 1
}

Write-Host "✓ Quarto is installed" -ForegroundColor Green

# Get script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

# Check if tutorial directory exists
if (-not (Test-Path "tutorial")) {
    Write-Host "❌ Tutorial directory not found!" -ForegroundColor Red
    exit 1
}

Set-Location tutorial

Write-Host "✓ Found tutorial directory" -ForegroundColor Green
Write-Host ""

# Create a temporary Python virtual environment for Quarto
Write-Host "📦 Setting up Python environment for Quarto..." -ForegroundColor Yellow

# Create venv if it doesn't exist
if (-not (Test-Path ".venv_quarto")) {
    python -m venv .venv_quarto
}

# Activate virtual environment
& .\.venv_quarto\Scripts\Activate.ps1

# Install required packages for Quarto
pip install --quiet --upgrade pip
pip install --quiet jupyter matplotlib plotly pandas numpy

Write-Host "✓ Python environment ready" -ForegroundColor Green
Write-Host ""

# Render the tutorial
Write-Host "📄 Rendering Quarto document..." -ForegroundColor Yellow
Write-Host ""

quarto render day01_tutorial.qmd

Write-Host ""
Write-Host "✓ Tutorial rendered successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "📂 Output file: tutorial\day01_tutorial.html"
Write-Host ""

# Deactivate virtual environment
deactivate

# Ask if user wants to open the file
$response = Read-Host "Open the tutorial in browser? [y/N]"
if ($response -match "^[Yy]$") {
    Start-Process day01_tutorial.html
}

Write-Host "Done!" -ForegroundColor Green
