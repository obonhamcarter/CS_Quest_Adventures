#!/bin/bash

# Render script for CS Quest Adventures
# This script activates the virtual environment and renders the site

set -e  # Exit on error

PROJECT_DIR="/Users/obonhamcarter/Desktop/0_/tutorialSites/CS_Quest_Adventures"
VENV_PYTHON="$PROJECT_DIR/venv/bin/python"

echo "🚀 CS Quest Adventures - Render Script"
echo "======================================"
echo ""

# Check if venv exists
if [ ! -f "$VENV_PYTHON" ]; then
    echo "❌ Error: Virtual environment not found at $VENV_PYTHON"
    echo "Please run: python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

# Change to project directory
cd "$PROJECT_DIR"

# Build JupyterLite
echo "🔨 Building JupyterLite environment..."
if [ -d "jupyterlite" ]; then
    cd jupyterlite
    source "$PROJECT_DIR/venv/bin/activate"
    jupyter lite build --contents content
    cp -r _output/* .
    rm -rf _output
    cd "$PROJECT_DIR"
    echo "✅ JupyterLite build complete"
else
    echo "⚠️  JupyterLite directory not found, skipping..."
fi

# Render the site
echo "📝 Rendering site with Quarto..."
QUARTO_PYTHON="$VENV_PYTHON" quarto render

echo ""
echo "✅ Build complete!"
echo ""
echo "To preview the site, run:"
echo "  cd $PROJECT_DIR"
echo "  quarto preview"
echo ""
echo "Output location: $PROJECT_DIR/_site/"
