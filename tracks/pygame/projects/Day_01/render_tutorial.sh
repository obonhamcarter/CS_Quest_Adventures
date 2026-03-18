#!/bin/bash
# Render Quarto tutorial for Day 01
# Sets up Python environment and renders to HTML

set -e

echo "================================"
echo "Rendering Day 01 Tutorial"
echo "================================"
echo ""

# Check if Quarto is installed
if ! command -v quarto &> /dev/null; then
    echo "❌ Quarto is not installed!"
    echo ""
    echo "Install Quarto from: https://quarto.org/docs/get-started/"
    echo ""
    exit 1
fi

echo "✓ Quarto is installed"

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

# Check if tutorial directory exists
if [ ! -d "tutorial" ]; then
    echo "❌ Tutorial directory not found!"
    exit 1
fi

cd tutorial

echo "✓ Found tutorial directory"
echo ""

# Create a temporary Python virtual environment for Quarto
echo "📦 Setting up Python environment for Quarto..."

# Create venv if it doesn't exist
if [ ! -d ".venv_quarto" ]; then
    python3 -m venv .venv_quarto
fi

# Activate virtual environment
source .venv_quarto/bin/activate

# Install required packages for Quarto
pip install --quiet --upgrade pip
pip install --quiet jupyter matplotlib plotly pandas numpy

echo "✓ Python environment ready"
echo ""

# Render the tutorial
echo "📄 Rendering Quarto document..."
echo ""

quarto render day01_tutorial.qmd

echo ""
echo "✓ Tutorial rendered successfully!"
echo ""
echo "📂 Output file: tutorial/day01_tutorial.html"
echo ""
echo "To view:"
echo "  open tutorial/day01_tutorial.html        (macOS)"
echo "  xdg-open tutorial/day01_tutorial.html    (Linux)"
echo ""

# Deactivate virtual environment
deactivate

# Ask if user wants to open the file
read -p "Open the tutorial in browser? [y/N]: " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    if [[ "$OSTYPE" == "darwin"* ]]; then
        open day01_tutorial.html
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        xdg-open day01_tutorial.html
    fi
fi

echo "Done!"
