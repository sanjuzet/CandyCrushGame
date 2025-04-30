import pygame
import random

# Constants
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 8
TILE_SIZE = WIDTH // GRID_SIZE
FPS = 30

# Colors
COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 165, 0)]

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Match-3 Game")
clock = pygame.time.Clock()

# Create the grid
grid = [[random.choice(COLORS) for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def draw_grid():
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            pygame.draw.rect(screen, grid[y][x], (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            pygame.draw.rect(screen, (0, 0, 0), (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

def check_matches():
    matches = []
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            if x < GRID_SIZE - 2 and grid[y][x] == grid[y][x + 1] == grid[y][x + 2]:
                matches.append((y, x))
                matches.append((y, x + 1))
                matches.append((y, x + 2))
            if y < GRID_SIZE - 2 and grid[y][x] == grid[y + 1][x] == grid[y + 2][x]:
                matches.append((y, x))
                matches.append((y + 1, x))
                matches.append((y + 2, x))
    return set(matches)

def remove_matches(matches):
    for y, x in matches:
        grid[y][x] = None

def drop_tiles():
    for x in range(GRID_SIZE):
        column = [grid[y][x] for y in range(GRID_SIZE) if grid[y][x] is not None]
        column = [None] * (GRID_SIZE - len(column)) + column
        for y in range(GRID_SIZE):
            grid[y][x] = column[y]

# Main game loop
running = True
while running:
    screen.fill((255, 255, 255))
    draw_grid()
    
    matches = check_matches()
    if matches:
        remove_matches(matches)
        drop_tiles()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
