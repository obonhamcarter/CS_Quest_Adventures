"""
Day 03: Pong Game - Instructor Complete Version
Classic paddle game with AI opponent.
"""

import pygame
import sys
import random

pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Game settings
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
PADDLE_SPEED = 7
BALL_SIZE = 15
BALL_SPEED_X = 6
BALL_SPEED_Y = 6
AI_SPEED = 5

class Paddle:
    """Represents a paddle controlled by player or AI."""
    
    def __init__(self, x, y, color):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.color = color
        self.speed = 0
        
    def move(self):
        """Move paddle and keep it on screen."""
        self.rect.y += self.speed
        # Keep on screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > WINDOW_HEIGHT:
            self.rect.bottom = WINDOW_HEIGHT
            
    def draw(self, surface):
        """Draw the paddle."""
        pygame.draw.rect(surface, self.color, self.rect)
        # Add glow effect
        glow_rect = self.rect.inflate(4, 4)
        pygame.draw.rect(surface, self.color, glow_rect, 2)


class Ball:
    """Represents the game ball."""
    
    def __init__(self):
        self.rect = pygame.Rect(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, BALL_SIZE, BALL_SIZE)
        self.speed_x = BALL_SPEED_X * random.choice([-1, 1])
        self.speed_y = BALL_SPEED_Y * random.choice([-1, 1])
        
    def move(self):
        """Move ball and handle wall bounces."""
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        # Bounce off top and bottom
        if self.rect.top <= 0 or self.rect.bottom >= WINDOW_HEIGHT:
            self.speed_y *= -1
            
    def reset(self):
        """Reset ball to center."""
        self.rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.speed_x = BALL_SPEED_X * random.choice([-1, 1])
        self.speed_y = BALL_SPEED_Y * random.choice([-1, 1])
        
    def draw(self, surface):
        """Draw the ball with trail effect."""
        pygame.draw.ellipse(surface, WHITE, self.rect)
        # Trail effect
        trail_rect = self.rect.inflate(4, 4)
        pygame.draw.ellipse(surface, WHITE, trail_rect, 2)


def main():
    """Main game loop."""
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Day 03: Pong")
    clock = pygame.time.Clock()
    
    # Create game objects
    player = Paddle(30, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, CYAN)
    ai = Paddle(WINDOW_WIDTH - 30 - PADDLE_WIDTH, WINDOW_HEIGHT // 2 - PADDLE_HEIGHT // 2, MAGENTA)
    ball = Ball()
    
    # Scores
    player_score = 0
    ai_score = 0
    
    # Fonts
    font = pygame.font.Font(None, 74)
    small_font = pygame.font.Font(None, 36)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        # Player input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            player.speed = -PADDLE_SPEED
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player.speed = PADDLE_SPEED
        else:
            player.speed = 0
            
        # Simple AI
        if ai.rect.centery < ball.rect.centery:
            ai.speed = AI_SPEED
        elif ai.rect.centery > ball.rect.centery:
            ai.speed = -AI_SPEED
        else:
            ai.speed = 0
            
        # Update
        player.move()
        ai.move()
        ball.move()
        
        # Paddle collision
        if ball.rect.colliderect(player.rect) or ball.rect.colliderect(ai.rect):
            ball.speed_x *= -1
            # Add spin based on where ball hits paddle
            if ball.rect.colliderect(player.rect):
                offset = (ball.rect.centery - player.rect.centery) / (PADDLE_HEIGHT / 2)
            else:
                offset = (ball.rect.centery - ai.rect.centery) / (PADDLE_HEIGHT / 2)
            ball.speed_y += offset * 2
            
        # Score points
        if ball.rect.left <= 0:
            ai_score += 1
            ball.reset()
        elif ball.rect.right >= WINDOW_WIDTH:
            player_score += 1
            ball.reset()
            
        # Draw
        screen.fill(BLACK)
        
        # Draw center line
        for y in range(0, WINDOW_HEIGHT, 20):
            pygame.draw.rect(screen, WHITE, (WINDOW_WIDTH // 2 - 2, y, 4, 10))
            
        # Draw game objects
        player.draw(screen)
        ai.draw(screen)
        ball.draw(screen)
        
        # Draw scores
        player_text = font.render(str(player_score), True, CYAN)
        ai_text = font.render(str(ai_score), True, MAGENTA)
        screen.blit(player_text, (WINDOW_WIDTH // 4, 20))
        screen.blit(ai_text, (3 * WINDOW_WIDTH // 4 - ai_text.get_width(), 20))
        
        # Draw controls
        controls = small_font.render("W/S or Arrow Keys to move", True, WHITE)
        screen.blit(controls, (WINDOW_WIDTH // 2 - controls.get_width() // 2, WINDOW_HEIGHT - 40))
        
        pygame.display.flip()
        clock.tick(FPS)
        
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
