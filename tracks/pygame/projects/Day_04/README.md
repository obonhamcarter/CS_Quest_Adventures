# Day 04: Snake Game 🐍

Classic snake game with growing body and food collection!

## Quick Start

**macOS / Linux:**
```bash
chmod +x launch.sh && ./launch.sh
```

**Windows (PowerShell):**
```powershell
.\launch.ps1
```

**Manual:**
```bash
cd Day_04
uv sync
uv run python src_instr/snake_game.py
```

## Game Controls

- **Arrow Keys** or **WASD**: Change snake direction
- **SPACE** (when game over): Restart
- **ESC** or **Close Window**: Quit

## Learning Objectives

- ✅ Grid-based movement system
- ✅ Deque data structure for body segments
- ✅ Self-collision detection
- ✅ Food spawning logic
- ✅ Growing mechanics
- ✅ Score and game over handling

## Key Concepts

### Snake Body Management
```python
from collections import deque

# Snake as list of (x, y) positions
snake = deque([(5, 5), (5, 6), (5, 7)])

# Move: add new head, remove tail
snake.appendleft(new_head)
if not growing:
    snake.pop()
```

### Direction Control
```python
# Can't go opposite direction
opposite = {UP: DOWN, DOWN: UP, LEFT: RIGHT, RIGHT: LEFT}
if new_direction != opposite[current_direction]:
    current_direction = new_direction
```

## Customization Ideas

- Different snake colors/patterns
- Obstacles in the grid
- Multiple food types (different points)
- Speed increases as snake grows
- Walls that wrap around
- Two-player snake battle

## Next Steps

**Day 05: Flappy Bird** - Infinite scrolling and procedural generation

---

**Happy Coding! 🎮**
