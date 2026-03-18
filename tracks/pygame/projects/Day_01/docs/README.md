# Day 01: Maze Explorer

## Overview

Welcome to Day 01 of the Pygame Tutorial Series! In this tutorial, students will create their first game: a simple maze explorer where a player-controlled dot navigates through a maze to reach a goal.

## Learning Objectives

- Set up a Python project using UV
- Understand Pygame basics (initialization, game loop, event handling)
- Learn RGB color system and screen coordinates
- Implement keyboard input handling
- Create collision detection between game objects
- Build a complete, playable game

## Time Allocation (45 minutes)

- Setup and introduction: 5 minutes
- Understanding colors and coordinates: 5 minutes
- Building the game: 25 minutes
- Running and testing: 5 minutes
- Q&A and experimentation: 5 minutes

## Prerequisites

- Python 3.10+ installed
- UV installed (see installation guide)
- A text editor or IDE (VS Code recommended)
- Basic understanding of Python (variables, functions, loops)

## Project Structure

```
Day_01/
├── pyproject.toml              # UV project configuration
├── src_instr/                  # Instructor complete code
│   └── maze_game.py
├── src_template/               # Student template code
│   └── maze_game.py
├── tests/                      # Test files
│   └── test_maze_game.py
├── tutorial/                   # Tutorial documentation
│   └── day01_tutorial.qmd
├── docs/                       # Additional documentation
│   └── README.md
└── assets/                     # Game assets
    └── images/
```

## Setup Instructions

### For Instructors

1. Clone or download the repository
2. Navigate to Day_01 directory
3. Run the complete version:
   ```bash
   cd Day_01
   uv sync
   uv run python src_instr/maze_game.py
   ```
4. Run tests:
   ```bash
   uv run pytest tests/ -v
   ```

### For Students

1. Create a new directory for your project
2. Initialize UV project:
   ```bash
   mkdir day01-maze-explorer
   cd day01-maze-explorer
   uv init
   uv add pygame
   uv add pytest --dev
   ```
3. Copy the template code from `src_template/maze_game.py`
4. Follow the tutorial to complete the game

## Key Concepts Covered

### 1. UV Package Management
- Project initialization
- Dependency management
- Running Python scripts

### 2. Pygame Fundamentals
- Initialization and setup
- Creating a display window
- Game loop structure
- Event handling

### 3. Graphics and Rendering
- RGB color system
- Drawing shapes (rectangles, circles)
- Screen coordinates and positioning

### 4. User Input
- Keyboard event handling
- Continuous key press detection
- Movement controls

### 5. Collision Detection
- Rectangle-based collision
- Wall collision response
- Goal detection

### 6. Game State Management
- Tracking game state (playing, won)
- Conditional rendering
- Win conditions

## Game Features

- **Player Movement**: WASD or arrow keys
- **Maze Navigation**: Walls block movement
- **Goal System**: Reach the goal to win
- **Visual Feedback**: Color changes on win
- **Win Message**: Text display on completion

## Testing

The project includes pytest tests that verify:
- Player initialization
- Movement mechanics
- Collision detection
- Goal existence
- Pygame initialization

Run tests with:
```bash
uv run pytest tests/ -v
```

## Common Issues and Solutions

### Issue: "No module named 'pygame'"
**Solution**: Run `uv add pygame` to install the dependency

### Issue: Game window doesn't open
**Solution**: Check that pygame.init() is called before creating the display

### Issue: Player moves through walls
**Solution**: Verify collision detection logic in the move() method

### Issue: Game runs too fast/slow
**Solution**: Adjust the FPS constant (default is 60)

## Extensions and Challenges

### Easy
- Change colors and sizes
- Adjust player speed
- Modify window dimensions

### Medium
- Design a new maze layout
- Add a timer
- Create multiple goals/checkpoints

### Hard
- Implement multiple levels
- Add moving obstacles
- Create a scoring system

## Teaching Notes

### Key Points to Emphasize

1. **The Game Loop Pattern**: This is fundamental to all game development
2. **Coordinate System**: (0,0) is top-left, not bottom-left
3. **Collision Detection**: Essential for game physics and interaction
4. **Constants**: Using named constants makes code more maintainable

### Common Student Mistakes

1. Forgetting to call `pygame.init()`
2. Not calling `pygame.display.flip()` to update the screen
3. Placing collision check before movement instead of after
4. Confusing x and y coordinates

### Discussion Questions

1. "Why do we need a game loop instead of just running code once?"
2. "How does collision detection work in real games?"
3. "What makes a maze fun vs frustrating?"
4. "How could we make the game more challenging?"

### Engagement Activities

1. **Live Coding**: Build the game together, step by step
2. **Pair Programming**: Students work in pairs
3. **Maze Design Challenge**: Students design unique mazes
4. **Show and Tell**: Students share their customizations

## Next Steps

After completing Day 01, students will be ready for:

**Day 02: Bouncing Ball Physics**
- Velocity and acceleration
- Physics simulation
- Multiple objects
- Gravity effects

## Resources

- [Pygame Documentation](https://www.pygame.org/docs/)
- [UV Documentation](https://github.com/astral-sh/uv)
- [RGB Color Picker](https://www.w3schools.com/colors/colors_picker.asp)
- [Pygame Tutorials](https://www.pygame.org/wiki/tutorials)

## License

This tutorial is provided for educational purposes. Feel free to modify and adapt for your classroom needs.

## Feedback

We welcome feedback to improve these tutorials! Please share:
- What worked well
- What was confusing
- Suggestions for improvement
- Additional features students requested

---

**Happy Teaching! 🎮**
