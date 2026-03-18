# Day 03: Pong Game 🏓

Classic paddle game - Player vs AI!

## Prerequisites

- Python 3.10 or higher
- UV package manager

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
cd Day_03
uv sync
uv run python src_instr/pong_game.py
```

## Game Controls

- **W/S** or **Up/Down Arrows**: Move your paddle
- **ESC** or **Close Window**: Quit game

## Learning Objectives

- ✅ Two-player game mechanics (player vs computer)
- ✅ Simple AI implementation (tracking)
- ✅ Score tracking and display
- ✅ Ball-paddle collision angles
- ✅ Speed progression over time
- ✅ Game feel and polish

## Key Concepts

### AI Logic
```python
# Simple tracking AI
if ai_paddle.center < ball.center:
    move_paddle_down()
else:
    move_paddle_up()
```

### Collision with Spin
```python
# Add spin based on hit location
offset = (ball.y - paddle.center_y) / (paddle.height / 2)
ball.velocity_y += offset * 2
```

## Customization Ideas

- Add difficulty levels
- Implement two-player mode
- Add power-ups
- Create tournament mode
- Add paddle sizes that change
- Implement curve balls

## Next Steps

**Day 04: Snake Game** - Grid-based movement and growing mechanics

---

**Happy Coding! 🎮**
