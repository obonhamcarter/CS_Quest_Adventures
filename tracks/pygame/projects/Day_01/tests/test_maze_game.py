"""
Tests for Day 01: Maze Explorer
These tests verify that the game components work correctly.
"""

import pytest
import pygame
import sys
import os

# Add src_instr to path to import the game
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src_instr'))

from maze_game import Player, WALLS, GOAL, PLAYER_SIZE


class TestPlayer:
    """Test the Player class."""
    
    def setup_method(self):
        """Set up test fixtures."""
        pygame.init()
        self.player = Player(50, 50)
    
    def teardown_method(self):
        """Clean up after tests."""
        pygame.quit()
    
    def test_player_initialization(self):
        """Test that player initializes correctly."""
        assert self.player.rect.x == 50
        assert self.player.rect.y == 50
        assert self.player.rect.width == PLAYER_SIZE
        assert self.player.rect.height == PLAYER_SIZE
    
    def test_player_move_no_collision(self):
        """Test that player can move when there's no collision."""
        original_x = self.player.rect.x
        self.player.move(10, 0, [])
        assert self.player.rect.x == original_x + 10
    
    def test_player_collision_with_wall(self):
        """Test that player stops at walls."""
        wall = pygame.Rect(60, 50, 100, 20)
        original_x = self.player.rect.x
        self.player.move(50, 0, [wall])
        # Player should not have moved through the wall
        assert self.player.rect.x == original_x
    
    def test_player_reaches_goal(self):
        """Test that player can reach the goal."""
        player = Player(GOAL.x, GOAL.y)
        assert player.rect.colliderect(GOAL)


class TestMaze:
    """Test the maze structure."""
    
    def test_walls_exist(self):
        """Test that walls are defined."""
        assert len(WALLS) > 0
    
    def test_borders_exist(self):
        """Test that border walls exist."""
        pygame.init()
        # Should have at least 4 border walls
        assert len(WALLS) >= 4
        pygame.quit()
    
    def test_goal_exists(self):
        """Test that goal is defined."""
        assert GOAL is not None
        assert GOAL.width > 0
        assert GOAL.height > 0


def test_pygame_initialization():
    """Test that Pygame initializes without errors."""
    pygame.init()
    assert pygame.get_init()
    pygame.quit()


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
