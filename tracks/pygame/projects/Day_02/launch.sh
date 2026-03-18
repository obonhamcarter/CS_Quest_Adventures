#!/bin/bash
# Launch script for Day 02: Bouncing Ball Physics

set -e

echo "================================"
echo "Day 02: Bouncing Ball Physics"
echo "================================"
echo ""

if ! command -v uv &> /dev/null; then
    echo "❌ UV is not installed!"
    echo "Install: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "📦 Installing dependencies..."
uv sync
echo "✓ Dependencies installed"
echo ""
echo "🎮 Launching game..."
echo ""
uv run python src_instr/bouncing_ball.py
