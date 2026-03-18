# Day 06: Frogger Clone 🐸

Help the frog cross the road and river!

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
cd Day_06
uv sync
uv run python src_instr/frogger_game.py
```

## Game Controls

- **Arrow Keys**: Move frog (grid-based jumping)
- **ESC** or **Close Window**: Quit

## Learning Objectives

- ✅ Multi-lane movement system
- ✅ Complex collision detection (cars, logs, water)
- ✅ Platform riding mechanics (frog on logs)
- ✅ Lives system
- ✅ Multiple zone types (road, river, safe zones)
- ✅ Speed variation per lane

## Key Concepts

### Multi-Zone Collision
```python
# Different behavior per zone
if in_road_zone:
    check_car_collision()
elif in_water_zone:
    if not on_log:
        lose_life()
    else:
        move_with_log()
```

### Platform Riding
```python
# Frog moves with log
if frog.is_on(log):
    frog.x += log.speed
```

## Customization Ideas

- More lane types (trains, lily pads)
- Power-ups (invincibility, speed boost)
- Multiple safe zones to reach
- Time pressure
- Moving obstacles in safe zones
- Different frog types with abilities

## Next Steps

**Day 07: Dungeon Crawler** - Tile-based RPG with exploration

---

**Happy Coding! 🎮**
