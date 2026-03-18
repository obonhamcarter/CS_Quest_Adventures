"""
Day 07: Simple Dungeon Crawler - Instructor Complete Version
Explore dungeons, collect treasures, and avoid enemies!
"""

import pygame
import sys
import random

pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
TILE_SIZE = 40
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WALL_GRAY = (60, 60, 60)
FLOOR_BROWN = (139, 90, 43)
PLAYER_BLUE = (100, 150, 255)
ENEMY_RED = (255, 50, 50)
TREASURE_GOLD = (255, 215, 0)
DOOR_GREEN = (50, 255, 50)

# Tile types
FLOOR = 0
WALL = 1
DOOR = 2

# Sample dungeon map
DUNGEON_MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1, 1, 2, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]


class Player:
    """Represents the player character."""
    
    def __init__(self, x, y):
        """Initialize player."""
        self.grid_x = x
        self.grid_y = y
        self.health = 100
        self.max_health = 100
        self.treasures = 0
        self.has_key = False
        
    def move(self, dx, dy, dungeon_map, enemies):
        """Move player if valid."""
        new_x = self.grid_x + dx
        new_y = self.grid_y + dy
        
        # Check bounds
        if 0 <= new_y < len(dungeon_map) and 0 <= new_x < len(dungeon_map[0]):
            tile = dungeon_map[new_y][new_x]
            
            # Check walls
            if tile == WALL:
                return False
                
            # Check doors (need key)
            if tile == DOOR and not self.has_key:
                return False
                
            # Check enemy collision
            for enemy in enemies:
                if enemy.grid_x == new_x and enemy.grid_y == new_y:
                    # Attack enemy
                    self.health -= 10
                    return False
                    
            # Valid move
            self.grid_x = new_x
            self.grid_y = new_y
            return True
            
        return False
        
    def draw(self, surface, camera_x, camera_y):
        """Draw the player."""
        x = self.grid_x * TILE_SIZE - camera_x
        y = self.grid_y * TILE_SIZE - camera_y
        
        rect = pygame.Rect(x + 5, y + 5, TILE_SIZE - 10, TILE_SIZE - 10)
        pygame.draw.rect(surface, PLAYER_BLUE, rect, border_radius=5)
        pygame.draw.rect(surface, (50, 100, 200), rect, 3, border_radius=5)


class Enemy:
    """Represents an enemy character."""
    
    def __init__(self, x, y):
        """Initialize enemy."""
        self.grid_x = x
        self.grid_y = y
        self.move_timer = 0
        
    def update(self, player, dungeon_map, dt):
        """Simple AI movement towards player."""
        self.move_timer += dt
        
        if self.move_timer > 0.5:  # Move every 0.5 seconds
            self.move_timer = 0
            
            # Simple pathfinding
            dx = 0
            dy = 0
            
            if abs(player.grid_x - self.grid_x) > abs(player.grid_y - self.grid_y):
                if player.grid_x > self.grid_x:
                    dx = 1
                elif player.grid_x < self.grid_x:
                    dx = -1
            else:
                if player.grid_y > self.grid_y:
                    dy = 1
                elif player.grid_y < self.grid_y:
                    dy = -1
                    
            new_x = self.grid_x + dx
            new_y = self.grid_y + dy
            
            # Check if move is valid
            if 0 <= new_y < len(dungeon_map) and 0 <= new_x < len(dungeon_map[0]):
                if dungeon_map[new_y][new_x] == FLOOR:
                    self.grid_x = new_x
                    self.grid_y = new_y
                    
    def draw(self, surface, camera_x, camera_y):
        """Draw the enemy."""
        x = self.grid_x * TILE_SIZE - camera_x
        y = self.grid_y * TILE_SIZE - camera_y
        
        rect = pygame.Rect(x + 5, y + 5, TILE_SIZE - 10, TILE_SIZE - 10)
        pygame.draw.rect(surface, ENEMY_RED, rect, border_radius=5)
        pygame.draw.rect(surface, (200, 0, 0), rect, 3, border_radius=5)


class Treasure:
    """Represents collectible treasure."""
    
    def __init__(self, x, y, is_key=False):
        """Initialize treasure."""
        self.grid_x = x
        self.grid_y = y
        self.is_key = is_key
        self.collected = False
        
    def check_collection(self, player):
        """Check if player collected this treasure."""
        if not self.collected and player.grid_x == self.grid_x and player.grid_y == self.grid_y:
            self.collected = True
            if self.is_key:
                player.has_key = True
            else:
                player.treasures += 1
            return True
        return False
        
    def draw(self, surface, camera_x, camera_y):
        """Draw the treasure."""
        if self.collected:
            return
            
        x = self.grid_x * TILE_SIZE - camera_x
        y = self.grid_y * TILE_SIZE - camera_y
        
        if self.is_key:
            # Draw key
            rect = pygame.Rect(x + 10, y + 15, 20, 10)
            pygame.draw.rect(surface, TREASURE_GOLD, rect, border_radius=3)
            pygame.draw.circle(surface, TREASURE_GOLD, (x + 30, y + 20), 8)
            pygame.draw.circle(surface, FLOOR_BROWN, (x + 30, y + 20), 5)
        else:
            # Draw treasure
            points = [
                (x + 20, y + 10),
                (x + 25, y + 20),
                (x + 35, y + 25),
                (x + 25, y + 30),
                (x + 20, y + 40),
                (x + 15, y + 30),
                (x + 5, y + 25),
                (x + 15, y + 20),
            ]
            pygame.draw.polygon(surface, TREASURE_GOLD, points)
            pygame.draw.polygon(surface, (200, 170, 0), points, 2)


def main():
    """Main game loop."""
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Day 07: Dungeon Crawler")
    clock = pygame.time.Clock()
    
    # Create game objects
    player = Player(1, 1)
    
    # Create enemies in random floor positions
    enemies = []
    for _ in range(5):
        while True:
            x = random.randint(1, len(DUNGEON_MAP[0]) - 2)
            y = random.randint(1, len(DUNGEON_MAP) - 2)
            if DUNGEON_MAP[y][x] == FLOOR and (x != 1 or y != 1):
                enemies.append(Enemy(x, y))
                break
                
    # Create treasures
    treasures = []
    # Add key
    treasures.append(Treasure(18, 13, is_key=True))
    # Add regular treasures
    for _ in range(8):
        while True:
            x = random.randint(1, len(DUNGEON_MAP[0]) - 2)
            y = random.randint(1, len(DUNGEON_MAP) - 2)
            if DUNGEON_MAP[y][x] == FLOOR and (x != 1 or y != 1):
                treasures.append(Treasure(x, y))
                break
                
    # Camera position
    camera_x = 0
    camera_y = 0
    
    # Fonts
    font = pygame.font.Font(None, 32)
    
    running = True
    while running:
        dt = clock.tick(FPS) / 1000.0
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_UP, pygame.K_w):
                    player.move(0, -1, DUNGEON_MAP, enemies)
                elif event.key in (pygame.K_DOWN, pygame.K_s):
                    player.move(0, 1, DUNGEON_MAP, enemies)
                elif event.key in (pygame.K_LEFT, pygame.K_a):
                    player.move(-1, 0, DUNGEON_MAP, enemies)
                elif event.key in (pygame.K_RIGHT, pygame.K_d):
                    player.move(1, 0, DUNGEON_MAP, enemies)
                    
        # Update enemies
        for enemy in enemies:
            enemy.update(player, DUNGEON_MAP, dt)
            
        # Check treasure collection
        for treasure in treasures:
            treasure.check_collection(player)
            
        # Update camera (center on player)
        camera_x = player.grid_x * TILE_SIZE - WINDOW_WIDTH // 2 + TILE_SIZE // 2
        camera_y = player.grid_y * TILE_SIZE - WINDOW_HEIGHT // 2 + TILE_SIZE // 2
        
        # Clamp camera
        map_width = len(DUNGEON_MAP[0]) * TILE_SIZE
        map_height = len(DUNGEON_MAP) * TILE_SIZE
        camera_x = max(0, min(camera_x, map_width - WINDOW_WIDTH))
        camera_y = max(0, min(camera_y, map_height - WINDOW_HEIGHT))
        
        # Draw
        screen.fill(BLACK)
        
        # Draw dungeon
        for y, row in enumerate(DUNGEON_MAP):
            for x, tile in enumerate(row):
                screen_x = x * TILE_SIZE - camera_x
                screen_y = y * TILE_SIZE - camera_y
                
                rect = pygame.Rect(screen_x, screen_y, TILE_SIZE, TILE_SIZE)
                
                if tile == WALL:
                    pygame.draw.rect(screen, WALL_GRAY, rect)
                    pygame.draw.rect(screen, (40, 40, 40), rect, 2)
                elif tile == FLOOR:
                    pygame.draw.rect(screen, FLOOR_BROWN, rect)
                    pygame.draw.rect(screen, (100, 70, 30), rect, 1)
                elif tile == DOOR:
                    pygame.draw.rect(screen, DOOR_GREEN, rect)
                    pygame.draw.rect(screen, (30, 180, 30), rect, 3)
                    
        # Draw treasures
        for treasure in treasures:
            treasure.draw(screen, camera_x, camera_y)
            
        # Draw enemies
        for enemy in enemies:
            enemy.draw(screen, camera_x, camera_y)
            
        # Draw player
        player.draw(screen, camera_x, camera_y)
        
        # Draw UI
        health_text = font.render(f"Health: {player.health}/{player.max_health}", True, (255, 50, 50))
        treasure_text = font.render(f"Treasures: {player.treasures}/8", True, TREASURE_GOLD)
        key_text = font.render(f"Key: {'Yes' if player.has_key else 'No'}", True, DOOR_GREEN)
        
        screen.blit(health_text, (10, 10))
        screen.blit(treasure_text, (10, 45))
        screen.blit(key_text, (10, 80))
        
        # Draw controls
        controls_text = font.render("WASD/Arrows to move", True, WHITE)
        screen.blit(controls_text, (WINDOW_WIDTH - 280, WINDOW_HEIGHT - 40))
        
        # Win condition
        uncollected = sum(1 for t in treasures if not t.collected and not t.is_key)
        if uncollected == 0:
            win_text = font.render("You collected all treasures!", True, TREASURE_GOLD)
            screen.blit(win_text, (WINDOW_WIDTH // 2 - 200, WINDOW_HEIGHT // 2))
            
        # Game over
        if player.health <= 0:
            game_over_text = font.render("Game Over!", True, (255, 0, 0))
            screen.blit(game_over_text, (WINDOW_WIDTH // 2 - 100, WINDOW_HEIGHT // 2))
            
        pygame.display.flip()
        
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
