"""
Day 01: Maze Explorer - Instructor Complete Version
A simple game where the player moves a dot through a maze using arrow keys.
"""

import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Colors (RGB)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (50, 150, 255)
GREEN = (50, 255, 150)
RED = (255, 50, 50)
DARK_GRAY = (40, 40, 40)

# Player settings
PLAYER_SIZE = 20
PLAYER_SPEED = 5

# Maze walls (x, y, width, height)
WALLS = [
    pygame.Rect(0, 0, WINDOW_WIDTH, 10),  # Top border
    pygame.Rect(0, 0, 10, WINDOW_HEIGHT),  # Left border
    pygame.Rect(0, WINDOW_HEIGHT - 10, WINDOW_WIDTH, 10),  # Bottom border
    pygame.Rect(WINDOW_WIDTH - 10, 0, 10, WINDOW_HEIGHT),  # Right border
    
    # Internal walls
    pygame.Rect(100, 100, 200, 20),
    pygame.Rect(100, 100, 20, 150),
    pygame.Rect(400, 100, 20, 200),
    pygame.Rect(200, 250, 200, 20),
    pygame.Rect(500, 200, 150, 20),
    pygame.Rect(600, 220, 20, 200),
    pygame.Rect(300, 400, 250, 20),
    pygame.Rect(100, 450, 20, 100),
]

# Goal area
GOAL = pygame.Rect(700, 500, 60, 60)


class Player:
    """Represents the player dot that moves through the maze."""
    
    def __init__(self, x, y):
        """Initialize the player at position (x, y)."""
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)
        self.color = BLUE
        
    def move(self, dx, dy, walls):
        """
        Move the player by dx and dy, checking for wall collisions.
        
        Args:
            dx: Change in x position
            dy: Change in y position
            walls: List of wall rectangles to check collision against
        """
        # Store original position
        original_x = self.rect.x
        original_y = self.rect.y
        
        # Try to move
        self.rect.x += dx
        self.rect.y += dy
        
        # Check for collisions with walls
        for wall in walls:
            if self.rect.colliderect(wall):
                # Collision detected, revert to original position
                self.rect.x = original_x
                self.rect.y = original_y
                break
                
    def draw(self, surface):
        """Draw the player on the given surface."""
        pygame.draw.circle(surface, self.color, self.rect.center, PLAYER_SIZE // 2)


def main():
    """Main game loop."""
    # Create the game window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Day 01: Maze Explorer")
    
    # Create clock for controlling frame rate
    clock = pygame.time.Clock()
    
    # Create player
    player = Player(50, 50)
    
    # Game state
    game_won = False
    
    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Get keyboard input
        if not game_won:
            keys = pygame.key.get_pressed()
            dx, dy = 0, 0
            
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                dx = -PLAYER_SPEED
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                dx = PLAYER_SPEED
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                dy = -PLAYER_SPEED
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                dy = PLAYER_SPEED
            
            # Move player
            player.move(dx, dy, WALLS)
            
            # Check if player reached the goal
            if player.rect.colliderect(GOAL):
                game_won = True
                player.color = GREEN
        
        # Drawing
        screen.fill(BLACK)
        
        # Draw walls
        for wall in WALLS:
            pygame.draw.rect(screen, DARK_GRAY, wall)
        
        # Draw goal
        goal_color = GREEN if game_won else RED
        pygame.draw.rect(screen, goal_color, GOAL)
        
        # Draw player
        player.draw(screen)
        
        # Draw win message
        if game_won:
            font = pygame.font.Font(None, 72)
            text = font.render("You Win!", True, GREEN)
            text_rect = text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
            screen.blit(text, text_rect)
        
        # Update display
        pygame.display.flip()
        
        # Control frame rate
        clock.tick(FPS)
    
    # Quit
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
