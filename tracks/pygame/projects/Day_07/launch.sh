#!/bin/bash
# Launch script for Day 07: Dungeon Crawler

set -e

echo "================================"
echo "Day 07: Dungeon Crawler"
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
echo "🎮 Launching Dungeon Crawler..."
echo ""
uv run python src_instr/dungeon_crawler.py
