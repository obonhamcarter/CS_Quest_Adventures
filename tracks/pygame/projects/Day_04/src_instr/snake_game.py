"""
Day 04: Snake Game - Instructor Complete Version
Classic snake game with growing body and food collection.
"""

import pygame
import sys
import random
from collections import deque

pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (0, 180, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)


class Snake:
    """Represents the snake."""
    
    def __init__(self):
        """Initialize snake in center."""
        center_x = GRID_WIDTH // 2
        center_y = GRID_HEIGHT // 2
        self.body = deque([(center_x, center_y), (center_x - 1, center_y), (center_x - 2, center_y)])
        self.direction = RIGHT
        self.grow_pending = False
        
    def move(self):
        """Move snake in current direction."""
        head_x, head_y = self.body[0]
        new_head = (head_x + self.direction[0], head_y + self.direction[1])
        
        self.body.appendleft(new_head)
        
        if not self.grow_pending:
            self.body.pop()
        else:
            self.grow_pending = False
            
    def grow(self):
        """Mark snake to grow on next move."""
        self.grow_pending = True
        
    def change_direction(self, new_direction):
        """Change direction if not opposite."""
        # Can't go backwards
        opposite = {UP: DOWN, DOWN: UP, LEFT: RIGHT, RIGHT: LEFT}
        if new_direction != opposite[self.direction]:
            self.direction = new_direction
            
    def check_collision(self):
        """Check if snake hit itself or wall."""
        head = self.body[0]
        
        # Wall collision
        if not (0 <= head[0] < GRID_WIDTH and 0 <= head[1] < GRID_HEIGHT):
            return True
            
        # Self collision
        if head in list(self.body)[1:]:
            return True
            
        return False
        
    def draw(self, surface):
        """Draw the snake."""
        for i, (x, y) in enumerate(self.body):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            color = GREEN if i == 0 else DARK_GREEN
            pygame.draw.rect(surface, color, rect)
            pygame.draw.rect(surface, BLACK, rect, 1)


class Food:
    """Represents food for the snake."""
    
    def __init__(self, snake_body):
        """Place food at random position not on snake."""
        self.position = self.generate_position(snake_body)
        
    def generate_position(self, snake_body):
        """Generate random position not on snake."""
        while True:
            pos = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if pos not in snake_body:
                return pos
                
    def draw(self, surface):
        """Draw the food."""
        x, y = self.position
        rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, RED, rect)
        pygame.draw.rect(surface, YELLOW, rect, 2)


def main():
    """Main game loop."""
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Day 04: Snake Game")
    clock = pygame.time.Clock()
    
    # Game objects
    snake = Snake()
    food = Food(snake.body)
    
    # Game state
    score = 0
    game_over = False
    
    # Fonts
    font = pygame.font.Font(None, 48)
    small_font = pygame.font.Font(None, 36)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and not game_over:
                if event.key in (pygame.K_UP, pygame.K_w):
                    snake.change_direction(UP)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    snake.change_direction(DOWN)
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    snake.change_direction(LEFT)
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    snake.change_direction(RIGHT)
            elif event.type == pygame.KEYDOWN and game_over:
                if event.key == pygame.K_SPACE:
                    # Restart
                    snake = Snake()
                    food = Food(snake.body)
                    score = 0
                    game_over = False
                    
        if not game_over:
            # Update
            snake.move()
            
            # Check food collision
            if snake.body[0] == food.position:
                snake.grow()
                score += 10
                food = Food(snake.body)
                
            # Check game over
            if snake.check_collision():
                game_over = True
                
        # Draw
        screen.fill(BLACK)
        
        # Draw grid
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            pygame.draw.line(screen, (30, 30, 30), (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, (30, 30, 30), (0, y), (WINDOW_WIDTH, y))
            
        # Draw game objects
        snake.draw(screen)
        food.draw(screen)
        
        # Draw score
        score_text = small_font.render(f"Score: {score}", True, WHITE)
        screen.blit(score_text, (10, 10))
        
        # Draw game over
        if game_over:
            game_over_text = font.render("Game Over!", True, RED)
            restart_text = small_font.render("Press SPACE to restart", True, WHITE)
            screen.blit(game_over_text, (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, WINDOW_HEIGHT // 2 - 50))
            screen.blit(restart_text, (WINDOW_WIDTH // 2 - restart_text.get_width() // 2, WINDOW_HEIGHT // 2 + 10))
            
        pygame.display.flip()
        clock.tick(FPS)
        
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
