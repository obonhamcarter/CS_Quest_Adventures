# Day 01: Maze Explorer 🎯

Navigate a dot through a maze using arrow keys!

## Prerequisites

- Python 3.10 or higher
- UV package manager

### Install UV

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Windows (PowerShell):**
```powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

## Quick Start

### Using the Launch Script (Recommended)

**macOS / Linux:**
```bash
chmod +x launch.sh
./launch.sh
```

**Windows (Git Bash or WSL):**
```bash
bash launch.sh
```

**Windows (PowerShell):**
```powershell
.\launch.ps1
```

### Manual Setup and Run

#### macOS / Linux

```bash
# Navigate to project directory
cd Day_01

# Install dependencies
uv sync

# Run the complete game
uv run python src_instr/maze_game.py

# Or run student template
uv run python src_template/maze_game.py

# Run tests
uv run pytest tests/ -v
```

#### Windows (Command Prompt)

```cmd
REM Navigate to project directory
cd Day_01

REM Install dependencies
uv sync

REM Run the complete game
uv run python src_instr/maze_game.py

REM Or run student template
uv run python src_template/maze_game.py

REM Run tests
uv run pytest tests/ -v
```

#### Windows (PowerShell)

```powershell
# Navigate to project directory
cd Day_01

# Install dependencies
uv sync

# Run the complete game
uv run python src_instr/maze_game.py

# Or run student template
uv run python src_template/maze_game.py

# Run tests
uv run pytest tests/ -v
```

## Game Controls

- **Arrow Keys** or **WASD**: Move the player dot
- **ESC** or **Close Window**: Quit game

## Project Structure

```
Day_01/
├── README.md                 # This file
├── pyproject.toml           # UV project configuration
├── launch.sh                # Launch script (Mac/Linux)
├── launch.ps1               # Launch script (Windows)
├── render_tutorial.sh       # Quarto rendering script
├── src_instr/              # Complete instructor code
│   └── maze_game.py
├── src_template/           # Student template with TODOs
│   └── maze_game.py
├── tests/                  # Unit tests
│   └── test_maze_game.py
├── tutorial/               # Tutorial documentation
│   └── day01_tutorial.qmd
├── docs/                   # Teaching guides
│   └── README.md
└── assets/                 # Game assets
    ├── images/
    └── sounds/
```

## Development

### Running Tests

**All Operating Systems:**
```bash
uv run pytest tests/ -v              # Verbose output
uv run pytest tests/ -v --cov        # With coverage
uv run pytest tests/ -k test_player  # Specific test
```

### Code Style

```bash
# Format code (if black is installed)
uv run black src_instr/ src_template/

# Lint code (if ruff is installed)
uv run ruff check src_instr/ src_template/
```

## Rendering Tutorial

To render the Quarto tutorial document to HTML:

**macOS / Linux:**
```bash
chmod +x render_tutorial.sh
./render_tutorial.sh
```

**Windows (PowerShell):**
```powershell
.\render_tutorial.ps1
```

**Manual Rendering:**
```bash
cd tutorial
quarto render day01_tutorial.qmd
# Output: day01_tutorial.html
```

> **Note:** Requires [Quarto](https://quarto.org/) to be installed

## Troubleshooting

### "Command not found: uv"

**Solution:** UV not installed or not in PATH
```bash
# macOS/Linux: Restart terminal or run
source ~/.bashrc  # or ~/.zshrc

# Windows: Restart PowerShell/Command Prompt
```

### "No module named 'pygame'"

**Solution:** Dependencies not installed
```bash
uv sync
```

### Game window doesn't appear

**Solution:** Check pygame initialization
- Ensure `pygame.init()` is called
- Verify display is created: `pygame.display.set_mode((width, height))`
- Check game loop is running

### Tests fail

**Solution:** Run from project root
```bash
cd Day_01
uv run pytest tests/ -v
```

### Permission denied on launch.sh

**Solution:** Make script executable
```bash
chmod +x launch.sh
```

## Learning Objectives

After completing this tutorial, you will understand:

- ✅ Setting up Python projects with UV
- ✅ Pygame initialization and game loop
- ✅ RGB color system
- ✅ Screen coordinates (x, y)
- ✅ Keyboard input handling
- ✅ Collision detection with rectangles
- ✅ Game state management
- ✅ Testing with pytest

## Customization Ideas

- Change colors and sizes
- Design your own maze layout
- Add a timer
- Create multiple levels
- Add sound effects
- Implement a high score system

## Next Steps

After completing Day 01, move on to:
- **Day 02: Bouncing Ball** - Learn physics simulation and gravity

## Resources

- [Pygame Documentation](https://www.pygame.org/docs/)
- [UV Documentation](https://github.com/astral-sh/uv)
- [Python Tutorial](https://docs.python.org/3/tutorial/)

## Support

- Check [../QUICKSTART.md](../QUICKSTART.md) for setup help
- Review [../TEACHER_GUIDE.md](../TEACHER_GUIDE.md) for teaching tips
- See [docs/README.md](docs/README.md) for detailed teaching guide

## License

Educational use. Feel free to modify and share!

---

**Happy Coding! 🎮**
