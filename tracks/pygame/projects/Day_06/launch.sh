#!/bin/bash
# Launch script for Day 06: Frogger

set -e

echo "================================"
echo "Day 06: Frogger Clone"
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
echo "🎮 Launching Frogger..."
echo ""
uv run python src_instr/frogger_game.py
