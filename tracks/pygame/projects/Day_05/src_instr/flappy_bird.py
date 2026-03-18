"""
Day 05: Flappy Bird Clone - Instructor Complete Version
Jump through pipes in this infinite scrolling game.
"""

import pygame
import sys
import random

pygame.init()

# Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
FPS = 60

# Colors
SKY_BLUE = (135, 206, 235)
GROUND_BROWN = (139, 90, 43)
PIPE_GREEN = (100, 200, 100)
BIRD_YELLOW = (255, 255, 100)
WHITE = (255, 255, 255)

# Game settings
GRAVITY = 0.5
JUMP_STRENGTH = -10
BIRD_SIZE = 30
PIPE_WIDTH = 70
PIPE_GAP = 200
PIPE_SPEED = 3
SPAWN_PIPE_TIME = 1500  # milliseconds


class Bird:
    """Represents the player bird."""
    
    def __init__(self):
        """Initialize bird."""
        self.x = 80
        self.y = WINDOW_HEIGHT // 2
        self.velocity = 0
        self.radius = BIRD_SIZE // 2
        
    def jump(self):
        """Make bird jump."""
        self.velocity = JUMP_STRENGTH
        
    def update(self):
        """Update bird position."""
        self.velocity += GRAVITY
        self.y += self.velocity
        
    def draw(self, surface):
        """Draw the bird."""
        # Draw bird body
        pygame.draw.circle(surface, BIRD_YELLOW, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(surface, (255, 200, 0), (int(self.x), int(self.y)), self.radius, 3)
        
        # Draw eye
        eye_x = int(self.x + 10)
        eye_y = int(self.y - 5)
        pygame.draw.circle(surface, WHITE, (eye_x, eye_y), 5)
        pygame.draw.circle(surface, (0, 0, 0), (eye_x, eye_y), 3)
        
    def check_collision(self, pipes):
        """Check if bird hit pipes or boundaries."""
        # Check boundaries
        if self.y - self.radius <= 0 or self.y + self.radius >= WINDOW_HEIGHT - 50:
            return True
            
        # Check pipe collision
        for pipe in pipes:
            # Check if bird is in pipe's x range
            if pipe.x < self.x + self.radius and pipe.x + PIPE_WIDTH > self.x - self.radius:
                # Check if bird hit pipe
                if self.y - self.radius < pipe.top_height or self.y + self.radius > pipe.top_height + PIPE_GAP:
                    return True
                    
        return False


class Pipe:
    """Represents a pair of pipes (top and bottom)."""
    
    def __init__(self, x):
        """Initialize pipe at x position."""
        self.x = x
        self.top_height = random.randint(100, WINDOW_HEIGHT - 50 - PIPE_GAP - 100)
        self.passed = False
        
    def update(self):
        """Move pipe left."""
        self.x -= PIPE_SPEED
        
    def draw(self, surface):
        """Draw top and bottom pipes."""
        # Top pipe
        top_rect = pygame.Rect(self.x, 0, PIPE_WIDTH, self.top_height)
        pygame.draw.rect(surface, PIPE_GREEN, top_rect)
        pygame.draw.rect(surface, (80, 160, 80), top_rect, 4)
        
        # Bottom pipe
        bottom_y = self.top_height + PIPE_GAP
        bottom_height = WINDOW_HEIGHT - 50 - bottom_y
        bottom_rect = pygame.Rect(self.x, bottom_y, PIPE_WIDTH, bottom_height)
        pygame.draw.rect(surface, PIPE_GREEN, bottom_rect)
        pygame.draw.rect(surface, (80, 160, 80), bottom_rect, 4)
        
    def off_screen(self):
        """Check if pipe is off screen."""
        return self.x + PIPE_WIDTH < 0


def main():
    """Main game loop."""
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Day 05: Flappy Bird")
    clock = pygame.time.Clock()
    
    # Game objects
    bird = Bird()
    pipes = [Pipe(WINDOW_WIDTH + 200)]
    
    # Game state
    score = 0
    game_over = False
    game_started = False
    
    # Timing
    last_pipe_time = pygame.time.get_ticks()
    
    # Fonts
    font = pygame.font.Font(None, 48)
    small_font = pygame.font.Font(None, 36)
    
    running = True
    while running:
        current_time = pygame.time.get_ticks()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not game_started:
                        game_started = True
                    elif not game_over:
                        bird.jump()
                    else:
                        # Restart
                        bird = Bird()
                        pipes = [Pipe(WINDOW_WIDTH + 200)]
                        score = 0
                        game_over = False
                        game_started = False
                        last_pipe_time = current_time
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not game_started:
                    game_started = True
                elif not game_over:
                    bird.jump()
                    
        if game_started and not game_over:
            # Update bird
            bird.update()
            
            # Spawn new pipes
            if current_time - last_pipe_time > SPAWN_PIPE_TIME:
                pipes.append(Pipe(WINDOW_WIDTH))
                last_pipe_time = current_time
                
            # Update pipes
            for pipe in pipes:
                pipe.update()
                
                # Check if passed pipe
                if not pipe.passed and pipe.x + PIPE_WIDTH < bird.x:
                    pipe.passed = True
                    score += 1
                    
            # Remove off-screen pipes
            pipes = [pipe for pipe in pipes if not pipe.off_screen()]
            
            # Check collisions
            if bird.check_collision(pipes):
                game_over = True
                
        # Draw
        screen.fill(SKY_BLUE)
        
        # Draw pipes
        for pipe in pipes:
            pipe.draw(screen)
            
        # Draw bird
        bird.draw(screen)
        
        # Draw ground
        ground_rect = pygame.Rect(0, WINDOW_HEIGHT - 50, WINDOW_WIDTH, 50)
        pygame.draw.rect(screen, GROUND_BROWN, ground_rect)
        
        # Draw score
        score_text = font.render(str(score), True, WHITE)
        screen.blit(score_text, (WINDOW_WIDTH // 2 - score_text.get_width() // 2, 30))
        
        # Draw start message
        if not game_started:
            start_text = small_font.render("Press SPACE or Click to Start", True, WHITE)
            screen.blit(start_text, (WINDOW_WIDTH // 2 - start_text.get_width() // 2, WINDOW_HEIGHT // 2))
            
        # Draw game over
        if game_over:
            game_over_text = font.render("Game Over!", True, WHITE)
            restart_text = small_font.render("Press SPACE to Restart", True, WHITE)
            screen.blit(game_over_text, (WINDOW_WIDTH // 2 - game_over_text.get_width() // 2, WINDOW_HEIGHT // 2 - 50))
            screen.blit(restart_text, (WINDOW_WIDTH // 2 - restart_text.get_width() // 2, WINDOW_HEIGHT // 2 + 10))
            
        pygame.display.flip()
        clock.tick(FPS)
        
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
