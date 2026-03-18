# Day 02: Bouncing Ball Physics ⚽

Explore physics simulation with gravity and bouncing balls!

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

**Windows (PowerShell):**
```powershell
.\launch.ps1
```

### Manual Setup and Run

#### macOS / Linux

```bash
# Navigate to project directory
cd Day_02

# Install dependencies
uv sync

# Run the complete game
uv run python src_instr/bouncing_ball.py
```

#### Windows (Command Prompt)

```cmd
REM Navigate to project directory
cd Day_02

REM Install dependencies
uv sync

REM Run the complete game
uv run python src_instr/bouncing_ball.py
```

#### Windows (PowerShell)

```powershell
# Navigate to project directory
cd Day_02

# Install dependencies
uv sync

# Run the complete game
uv run python src_instr/bouncing_ball.py
```

## Game Controls

- **Click**: Add ball at mouse position
- **SPACE**: Add random ball
- **C**: Clear all balls
- **R**: Reset with 5 random balls
- **ESC** or **Close Window**: Quit game

## Learning Objectives

After completing this tutorial, you will understand:

- ✅ Physics simulation (gravity, velocity, acceleration)
- ✅ Vector mathematics basics
- ✅ Multiple object management
- ✅ Mouse input handling
- ✅ Energy loss (coefficient of restitution)
- ✅ Dynamic object creation

## Key Concepts

### Physics Equations Used
```python
# Gravity (acceleration)
velocity_y += GRAVITY

# Position update
x += velocity_x
y += velocity_y

# Bounce (energy loss)
velocity_y = -velocity_y * FRICTION
```

## Customization Ideas

- Adjust gravity strength
- Change friction/energy loss
- Add different ball types
- Implement ball-to-ball collisions
- Add obstacles
- Create a "gravity painter" mode

## Next Steps

After completing Day 02, move on to:
- **Day 03: Pong** - Create a classic paddle game with AI opponent

## Resources

- [Pygame Documentation](https://www.pygame.org/docs/)
- [UV Documentation](https://github.com/astral-sh/uv)
- [Physics in Games](https://www.toptal.com/game/video-game-physics-part-i-an-introduction-to-rigid-body-dynamics)

---

**Happy Coding! 🎮**
