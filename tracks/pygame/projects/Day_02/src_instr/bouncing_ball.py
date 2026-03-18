"""
Day 02: Bouncing Ball Physics - Instructor Complete Version
A simulation of bouncing balls with realistic physics including gravity.
"""

import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 100, 100)
BLUE = (100, 150, 255)
GREEN = (100, 255, 150)
PURPLE = (200, 100, 255)
YELLOW = (255, 255, 100)
ORANGE = (255, 165, 100)

COLORS = [RED, BLUE, GREEN, PURPLE, YELLOW, ORANGE]

# Physics constants
GRAVITY = 0.5  # Acceleration due to gravity (pixels/frame²)
FRICTION = 0.99  # Energy loss on bounce (coefficient of restitution)
MIN_BOUNCE_VELOCITY = 0.5  # Minimum velocity to keep bouncing


class Ball:
    """Represents a bouncing ball with physics."""
    
    def __init__(self, x, y, radius, color):
        """
        Initialize a ball.
        
        Args:
            x: Initial x position
            y: Initial y position
            radius: Ball radius
            color: Ball color (RGB tuple)
        """
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        
        # Velocity (speed and direction)
        self.vx = random.uniform(-10, 10)  # Horizontal velocity
        self.vy = random.uniform(-15, -5)  # Vertical velocity (negative = upward)
        
    def update(self):
        """Update ball position and apply physics."""
        # Apply gravity
        self.vy += GRAVITY
        
        # Update position based on velocity
        self.x += self.vx
        self.y += self.vy
        
        # Bounce off left and right walls
        if self.x - self.radius <= 0:
            self.x = self.radius
            self.vx = abs(self.vx) * FRICTION
        elif self.x + self.radius >= WINDOW_WIDTH:
            self.x = WINDOW_WIDTH - self.radius
            self.vx = -abs(self.vx) * FRICTION
        
        # Bounce off floor
        if self.y + self.radius >= WINDOW_HEIGHT:
            self.y = WINDOW_HEIGHT - self.radius
            
            # Only bounce if moving fast enough
            if abs(self.vy) > MIN_BOUNCE_VELOCITY:
                self.vy = -abs(self.vy) * FRICTION
            else:
                self.vy = 0
                
            # Apply friction to horizontal movement
            self.vx *= 0.95
        
        # Bounce off ceiling
        if self.y - self.radius <= 0:
            self.y = self.radius
            self.vy = abs(self.vy) * FRICTION
            
    def draw(self, surface):
        """Draw the ball on the given surface."""
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)
        
        # Draw velocity vector (for visualization)
        end_x = int(self.x + self.vx * 3)
        end_y = int(self.y + self.vy * 3)
        pygame.draw.line(surface, WHITE, (int(self.x), int(self.y)), (end_x, end_y), 2)
        
    def is_resting(self):
        """Check if ball has come to rest."""
        return abs(self.vy) < MIN_BOUNCE_VELOCITY and self.y + self.radius >= WINDOW_HEIGHT - 1


def create_random_ball():
    """Create a ball with random properties."""
    radius = random.randint(15, 40)
    x = random.randint(radius, WINDOW_WIDTH - radius)
    y = random.randint(radius, WINDOW_HEIGHT // 3)
    color = random.choice(COLORS)
    return Ball(x, y, radius, color)


def main():
    """Main game loop."""
    # Create the game window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Day 02: Bouncing Ball Physics")
    
    # Create clock for controlling frame rate
    clock = pygame.time.Clock()
    
    # Create initial balls
    balls = [create_random_ball() for _ in range(5)]
    
    # Font for instructions
    font = pygame.font.Font(None, 36)
    small_font = pygame.font.Font(None, 24)
    
    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Create new ball at mouse position
                x, y = event.pos
                radius = random.randint(15, 40)
                color = random.choice(COLORS)
                balls.append(Ball(x, y, radius, color))
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Add random ball
                    balls.append(create_random_ball())
                elif event.key == pygame.K_c:
                    # Clear all balls
                    balls = []
                elif event.key == pygame.K_r:
                    # Reset with 5 random balls
                    balls = [create_random_ball() for _ in range(5)]
        
        # Update all balls
        for ball in balls:
            ball.update()
        
        # Drawing
        screen.fill(BLACK)
        
        # Draw all balls
        for ball in balls:
            ball.draw(screen)
        
        # Draw instructions
        instructions = [
            "Click: Add ball at mouse",
            "SPACE: Add random ball",
            "C: Clear all",
            "R: Reset"
        ]
        
        y_offset = 10
        for instruction in instructions:
            text = small_font.render(instruction, True, WHITE)
            screen.blit(text, (10, y_offset))
            y_offset += 25
        
        # Draw ball count
        count_text = font.render(f"Balls: {len(balls)}", True, WHITE)
        screen.blit(count_text, (WINDOW_WIDTH - 150, 10))
        
        # Update display
        pygame.display.flip()
        
        # Control frame rate
        clock.tick(FPS)
    
    # Quit
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
