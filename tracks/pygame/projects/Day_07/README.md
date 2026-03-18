# Day 07: Dungeon Crawler ⚔️

Explore dungeons, collect treasures, and avoid enemies!

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
cd Day_07
uv sync
uv run python src_instr/dungeon_crawler.py
```

## Game Controls

- **Arrow Keys** or **WASD**: Move player
- **ESC** or **Close Window**: Quit

## Learning Objectives

- ✅ Tile-based map system (2D arrays)
- ✅ Camera system (viewport following player)
- ✅ Basic enemy AI (pathfinding)
- ✅ Item collection system
- ✅ Health management
- ✅ Multiple room navigation
- ✅ Locked doors and keys

## Key Concepts

### Tile Map
```python
# Map as 2D array
dungeon_map = [
    [1, 1, 1, 1, 1],  # 1 = wall
    [1, 0, 0, 0, 1],  # 0 = floor
    [1, 0, 2, 0, 1],  # 2 = door
    [1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1],
]
```

### Camera System
```python
# Center camera on player
camera_x = player.x - SCREEN_WIDTH // 2
camera_y = player.y - SCREEN_HEIGHT // 2

# Draw with offset
draw_x = object.x - camera_x
draw_y = object.y - camera_y
```

### Simple Pathfinding
```python
# Move toward player
if abs(player.x - enemy.x) > abs(player.y - enemy.y):
    move_horizontal_toward_player()
else:
    move_vertical_toward_player()
```

## Customization Ideas

- Design custom dungeon layouts
- Add more enemy types
- Implement combat system
- Add inventory system
- Create multiple floors/levels
- Add boss battles
- Implement save/load system
- Add different weapons/items

## Course Complete! 🎉

Congratulations on completing all 7 days! You now know:
- Game loops and architecture
- Physics simulation
- AI implementation
- Data structures for games
- Procedural generation
- Complex collision systems
- RPG mechanics

**Next:** Create your own original game combining these concepts!

---

**Happy Coding! 🎮**
