# Day 05: Flappy Bird Clone 🐦

Navigate through pipes in this infinite scrolling game!

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
cd Day_05
uv sync
uv run python src_instr/flappy_bird.py
```

## Game Controls

- **SPACE** or **Click**: Flap / Jump
- **ESC** or **Close Window**: Quit

## Learning Objectives

- ✅ Jumping mechanics (impulse physics)
- ✅ Infinite scrolling backgrounds
- ✅ Procedural pipe generation
- ✅ Gap randomization
- ✅ Game state management (menu, playing, game over)
- ✅ Timing and spawn systems

## Key Concepts

### Jump Mechanic
```python
def jump():
    velocity_y = JUMP_STRENGTH  # Negative = upward

def update():
    velocity_y += GRAVITY  # Always pulling down
    y += velocity_y
```

### Procedural Generation
```python
# Spawn pipes at intervals
if time_since_last_pipe > SPAWN_INTERVAL:
    gap_y = random.randint(min_height, max_height)
    pipes.append(Pipe(x=SCREEN_WIDTH, gap_y=gap_y))
```

## Customization Ideas

- Different bird sprites/animations
- Varying pipe widths
- Day/night cycle
- Weather effects
- Difficulty modes
- Obstacles besides pipes
- Parallax scrolling backgrounds

## Next Steps

**Day 06: Frogger** - Multi-lane platformer with complex collision

---

**Happy Coding! 🎮**
