"""
Day 06: Frogger Clone - Instructor Complete Version
Help the frog cross the road and river!
"""

import pygame
import sys
import random

pygame.init()

# Constants
WINDOW_WIDTH = 700
WINDOW_HEIGHT = 700
GRID_SIZE = 50
FPS = 60

# Colors
GRASS_GREEN = (50, 200, 50)
ROAD_GRAY = (80, 80, 80)
WATER_BLUE = (50, 100, 255)
FROG_GREEN = (0, 255, 0)
CAR_COLORS = [(255, 0, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]
LOG_BROWN = (139, 90, 43)


class Frog:
    """Represents the player frog."""
    
    def __init__(self):
        """Initialize frog at starting position."""
        self.reset()
        
    def reset(self):
        """Reset frog to starting position."""
        self.grid_x = 6
        self.grid_y = 13
        self.x = self.grid_x * GRID_SIZE
        self.y = self.grid_y * GRID_SIZE
        
    def move(self, dx, dy, obstacles):
        """Move frog if valid."""
        new_grid_x = self.grid_x + dx
        new_grid_y = self.grid_y + dy
        
        # Check boundaries
        if 0 <= new_grid_x < 14 and 0 <= new_grid_y < 14:
            self.grid_x = new_grid_x
            self.grid_y = new_grid_y
            self.x = self.grid_x * GRID_SIZE
            self.y = self.grid_y * GRID_SIZE
            return True
        return False
        
    def draw(self, surface):
        """Draw the frog."""
        rect = pygame.Rect(self.x + 5, self.y + 5, GRID_SIZE - 10, GRID_SIZE - 10)
        pygame.draw.rect(surface, FROG_GREEN, rect)
        pygame.draw.rect(surface, (0, 200, 0), rect, 3)
        
        # Eyes
        eye1_pos = (self.x + 15, self.y + 15)
        eye2_pos = (self.x + 35, self.y + 15)
        pygame.draw.circle(surface, (255, 255, 255), eye1_pos, 5)
        pygame.draw.circle(surface, (255, 255, 255), eye2_pos, 5)
        pygame.draw.circle(surface, (0, 0, 0), eye1_pos, 3)
        pygame.draw.circle(surface, (0, 0, 0), eye2_pos, 3)


class Car:
    """Represents a car obstacle."""
    
    def __init__(self, lane, speed):
        """Initialize car in a lane."""
        self.lane = lane
        self.speed = speed
        self.width = GRID_SIZE * random.choice([1, 2])
        
        if speed > 0:
            self.x = -self.width
        else:
            self.x = WINDOW_WIDTH
            
        self.y = lane * GRID_SIZE
        self.color = random.choice(CAR_COLORS)
        
    def update(self):
        """Move car."""
        self.x += self.speed
        
    def draw(self, surface):
        """Draw the car."""
        rect = pygame.Rect(self.x, self.y + 10, self.width, GRID_SIZE - 20)
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, (0, 0, 0), rect, 2)
        
    def off_screen(self):
        """Check if car is off screen."""
        if self.speed > 0:
            return self.x > WINDOW_WIDTH
        else:
            return self.x + self.width < 0
            
    def collides_with(self, frog):
        """Check collision with frog."""
        frog_rect = pygame.Rect(frog.x, frog.y, GRID_SIZE, GRID_SIZE)
        car_rect = pygame.Rect(self.x, self.y, self.width, GRID_SIZE)
        return frog_rect.colliderect(car_rect)


class Log:
    """Represents a log platform."""
    
    def __init__(self, lane, speed):
        """Initialize log in a lane."""
        self.lane = lane
        self.speed = speed
        self.width = GRID_SIZE * random.choice([2, 3])
        
        if speed > 0:
            self.x = -self.width
        else:
            self.x = WINDOW_WIDTH
            
        self.y = lane * GRID_SIZE
        
    def update(self):
        """Move log."""
        self.x += self.speed
        
    def draw(self, surface):
        """Draw the log."""
        rect = pygame.Rect(self.x, self.y + 15, self.width, GRID_SIZE - 30)
        pygame.draw.rect(surface, LOG_BROWN, rect, border_radius=10)
        pygame.draw.rect(surface, (100, 60, 30), rect, 3, border_radius=10)
        
    def off_screen(self):
        """Check if log is off screen."""
        if self.speed > 0:
            return self.x > WINDOW_WIDTH
        else:
            return self.x + self.width < 0
            
    def is_on(self, frog):
        """Check if frog is on this log."""
        if frog.grid_y != self.lane:
            return False
        frog_x = frog.x + GRID_SIZE // 2
        return self.x < frog_x < self.x + self.width


def main():
    """Main game loop."""
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Day 06: Frogger")
    clock = pygame.time.Clock()
    
    # Game objects
    frog = Frog()
    cars = []
    logs = []
    
    # Lane configurations (lane_number, speed)
    car_lanes = [(8, 2), (9, -2.5), (10, 1.5), (11, -2)]
    log_lanes = [(1, 1.2), (2, 1.5), (3, -1), (4, 2), (5, -1.5), (6, -1.2)]
    
    # Pre-spawn initial logs for better playability
    for lane, speed in log_lanes:
        # Spawn 2-3 logs per lane at different positions
        for i in range(3):
            log = Log(lane, speed)
            log.x = i * 250 + random.randint(0, 100)
            logs.append(log)
    
    # Game state
    lives = 3
    score = 0
    level = 1
    
    # Timing
    car_spawn_timer = 0
    log_spawn_timer = 0
    
    # Fonts
    font = pygame.font.Font(None, 36)
    
    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if frog.move(0, -1, []):
                        if frog.grid_y == 0:
                            # Reached goal!
                            score += 100
                            frog.reset()
                elif event.key == pygame.K_DOWN:
                    frog.move(0, 1, [])
                elif event.key == pygame.K_LEFT:
                    frog.move(-1, 0, [])
                elif event.key == pygame.K_RIGHT:
                    frog.move(1, 0, [])
                    
        # Spawn cars
        car_spawn_timer += dt
        if car_spawn_timer > 2:
            lane, speed = random.choice(car_lanes)
            cars.append(Car(lane, speed))
            car_spawn_timer = 0
            
        # Spawn logs
        log_spawn_timer += dt
        if log_spawn_timer > 1.5:  # Spawn more frequently for better playability
            lane, speed = random.choice(log_lanes)
            logs.append(Log(lane, speed))
            log_spawn_timer = 0
            
        # Update cars
        for car in cars:
            car.update()
        cars = [car for car in cars if not car.off_screen()]
        
        # Update logs
        for log in logs:
            log.update()
        logs = [log for log in logs if not log.off_screen()]
        
        # Check car collisions
        for car in cars:
            if car.collides_with(frog):
                lives -= 1
                frog.reset()
                if lives == 0:
                    # Game over
                    lives = 3
                    score = 0
                    
        # Check if frog is in water
        if 1 <= frog.grid_y <= 6:
            on_log = any(log.is_on(frog) for log in logs)
            if not on_log:
                lives -= 1
                frog.reset()
                if lives == 0:
                    lives = 3
                    score = 0
                    
            # Move frog with log
            else:
                for log in logs:
                    if log.is_on(frog):
                        frog.x += log.speed
                        frog.grid_x = int(frog.x / GRID_SIZE)
                        
                        # Check if fell off edge
                        if frog.x < 0 or frog.x >= WINDOW_WIDTH:
                            lives -= 1
                            frog.reset()
                            if lives == 0:
                                lives = 3
                                score = 0
                        break
                        
        # Draw
        screen.fill(GRASS_GREEN)
        
        # Draw zones
        # Goal zone
        goal_rect = pygame.Rect(0, 0, WINDOW_WIDTH, GRID_SIZE)
        pygame.draw.rect(screen, (100, 255, 100), goal_rect)
        
        # Water zone
        water_rect = pygame.Rect(0, GRID_SIZE, WINDOW_WIDTH, 6 * GRID_SIZE)
        pygame.draw.rect(screen, WATER_BLUE, water_rect)
        
        # Safe middle
        safe_rect = pygame.Rect(0, 7 * GRID_SIZE, WINDOW_WIDTH, GRID_SIZE)
        pygame.draw.rect(screen, GRASS_GREEN, safe_rect)
        
        # Road zone
        road_rect = pygame.Rect(0, 8 * GRID_SIZE, WINDOW_WIDTH, 5 * GRID_SIZE)
        pygame.draw.rect(screen, ROAD_GRAY, road_rect)
        
        # Draw lanes
        for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.line(screen, (200, 200, 200), (0, y), (WINDOW_WIDTH, y), 1)
            
        # Draw objects
        for log in logs:
            log.draw(screen)
        for car in cars:
            car.draw(screen)
        frog.draw(screen)
        
        # Draw UI
        lives_text = font.render(f"Lives: {lives}", True, (255, 255, 255))
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        screen.blit(lives_text, (10, WINDOW_HEIGHT - 40))
        screen.blit(score_text, (WINDOW_WIDTH - 150, WINDOW_HEIGHT - 40))
        
        pygame.display.flip()
        
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
