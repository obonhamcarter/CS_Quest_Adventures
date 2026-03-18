#!/bin/bash
# Launch script for Day 05: Flappy Bird

set -e

echo "================================"
echo "Day 05: Flappy Bird Clone"
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
echo "🎮 Launching Flappy Bird..."
echo ""
uv run python src_instr/flappy_bird.py
