#!/bin/bash
# Launch script for Day 03: Pong Game

set -e

echo "================================"
echo "Day 03: Pong Game"
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
echo ""
echo "🎮 Launching Pong..."
echo ""
uv run python src_instr/pong_game.py
