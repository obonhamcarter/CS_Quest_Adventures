#!/bin/bash
# Launch script for Day 01: Maze Explorer
# Works on macOS and Linux

set -e  # Exit on error

echo "================================"
echo "Day 01: Maze Explorer"
echo "================================"
echo ""

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "❌ UV is not installed!"
    echo ""
    echo "Install UV with:"
    echo "  curl -LsSf https://astral.sh/uv/install.sh | sh"
    echo ""
    exit 1
fi

echo "✓ UV is installed"

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "✓ Working directory: $SCRIPT_DIR"
echo ""

# Install dependencies
echo "📦 Installing dependencies..."
uv sync
echo "✓ Dependencies installed"
echo ""

# Show menu
echo "Select what to run:"
echo "1) Complete instructor version (src_instr/maze_game.py)"
echo "2) Student template (src_template/maze_game.py)"
echo "3) Run tests"
echo "4) Exit"
echo ""
read -p "Enter choice [1-4]: " choice

case $choice in
    1)
        echo ""
        echo "🎮 Launching complete game..."
        echo ""
        uv run python src_instr/maze_game.py
        ;;
    2)
        echo ""
        echo "🎮 Launching student template..."
        echo ""
        uv run python src_template/maze_game.py
        ;;
    3)
        echo ""
        echo "🧪 Running tests..."
        echo ""
        uv run pytest tests/ -v
        ;;
    4)
        echo "Goodbye!"
        exit 0
        ;;
    *)
        echo "❌ Invalid choice"
        exit 1
        ;;
esac

echo ""
echo "✓ Done!"
