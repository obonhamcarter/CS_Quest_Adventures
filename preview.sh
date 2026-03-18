#!/bin/bash

# Preview script for CS Quest Adventures
# This script starts a live preview server with auto-reload

set -e  # Exit on error

PROJECT_DIR="/Users/obonhamcarter/Desktop/0_/tutorialSites/CS_Quest_Adventures"
VENV_PYTHON="$PROJECT_DIR/venv/bin/python"

echo "🔍 CS Quest Adventures - Preview Server"
echo "======================================="
echo ""

# Check if venv exists
if [ ! -f "$VENV_PYTHON" ]; then
    echo "❌ Error: Virtual environment not found at $VENV_PYTHON"
    echo "Please run: python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt"
    exit 1
fi

# Change to project directory
cd "$PROJECT_DIR"

# Start preview server
echo "🌐 Starting preview server..."
echo "   The site will open in your browser automatically"
echo "   Press Ctrl+C to stop the server"
echo ""
echo "Preview URL: http://localhost:4321"
echo ""

QUARTO_PYTHON="$VENV_PYTHON" quarto preview
