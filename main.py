import pygame
import random
 
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
 
TILE_SIZE = 40
COLS = screen.get_width() // TILE_SIZE
ROWS = screen.get_height() // TILE_SIZE
 
def to_pixel(grid_pos):
    return (grid_pos[0] * TILE_SIZE, grid_pos[1] * TILE_SIZE)
 
def random_grid_pos():
    return (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))

 
snake = [(COLS // 2, ROWS // 2)]
direction = (1, 0)
apple = random_grid_pos()
 
move_timer = 0
MOVE_INTERVAL = 0.15
for x in range(COLS):
        for y in range(ROWS):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, (50, 50, 50), rect, 1)
 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP    and direction != (0,  1): direction = (0, -1)
            if event.key == pygame.K_DOWN  and direction != (0, -1): direction = (0,  1)
            if event.key == pygame.K_LEFT  and direction != (1,  0): direction = (-1, 0)
            if event.key == pygame.K_RIGHT and direction != (-1, 0): direction = (1,  0)
    for segment in snake:
        rect = pygame.Rect(segment[0] * TILE_SIZE, segment[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, (0, 200, 0), rect)


 
    pygame.display.flip()
    dt = clock.tick(60) / 1000


    
 
pygame.quit()