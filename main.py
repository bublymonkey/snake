import pygame
import random
 
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
 
# --- Grid Setup ---
TILE_SIZE = 40
COLS = screen.get_width() // TILE_SIZE
ROWS = screen.get_height() // TILE_SIZE
 
def to_pixel(grid_pos):
    return (grid_pos[0] * TILE_SIZE, grid_pos[1] * TILE_SIZE)
 
def random_grid_pos():
    return (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
 
# --- Game State ---
snake = [(COLS // 2, ROWS // 2)]
direction = (1, 0)
apple = random_grid_pos()
 
move_timer = 0
MOVE_INTERVAL = 0.15
 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP    and direction != (0,  1): direction = (0, -1)
            if event.key == pygame.K_DOWN  and direction != (0, -1): direction = (0,  1)
            if event.key == pygame.K_LEFT  and direction != (1,  0): direction = (-1, 0)
            if event.key == pygame.K_RIGHT and direction != (-1, 0): direction = (1,  0)
 
    # --- Move ---
    move_timer += dt
    if move_timer >= MOVE_INTERVAL:
        move_timer = 0
        new_head = ((snake[0][0] + direction[0]) % COLS, (snake[0][1] + direction[1]) % ROWS)
        if new_head in snake:
            running = False
        snake.insert(0, new_head)
        if new_head == apple:
            apple = random_grid_pos()
        else:
            snake.pop()
 
    # --- Draw ---
    screen.fill("green")
    pygame.draw.circle(screen, "black", to_pixel(apple), 40)
 
    pygame.display.flip()
    dt = clock.tick(60) / 1000
 
pygame.quit()