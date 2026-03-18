#!/bin/bash
# Launch script for Day 04: Snake Game

set -e

echo "================================"
echo "Day 04: Snake Game"
echo "================================"
echo ""

if ! command -v uv &> /dev/null; then
    echo "❌ UV is not installed!"
    exit 1
fi

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "📦 Installing dependencies..."
uv sync
echo ""
echo "🎮 Launching Snake..."
echo ""
uv run python src_instr/snake_game.py
