import pygame
import random
 
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0
game_over = False
 
TILE_SIZE = 40
COLS = screen.get_width() // TILE_SIZE
ROWS = screen.get_height() // TILE_SIZE
 
def to_pixel(grid_pos):
    return (grid_pos[0] * TILE_SIZE, grid_pos[1] * TILE_SIZE)
 

def random_grid_pos(snake_body=None):
    while True:
        pos = (random.randint(0, COLS - 1), random.randint(0, ROWS - 1))
        if snake_body is None or pos not in snake_body:
            return pos

snake = [(COLS // 2, ROWS // 2)]
direction = (1, 0)
apple = random_grid_pos(snake)

score = 0
 
move_timer = 0
MOVE_INTERVAL = 0.15
 
while running:
    screen.fill((20, 20, 20))

    
    for x in range(COLS):
        for y in range(ROWS):
            rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, (50, 50, 50), rect, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w    and direction != (0,  1): direction = (0, -1)
            if event.key == pygame.K_s  and direction != (0, -1): direction = (0,  1)
            if event.key == pygame.K_a  and direction != (1,  0): direction = (-1, 0)
            if event.key == pygame.K_d and direction != (-1, 0): direction = (1,  0)

    if not game_over:
        move_timer += dt
        if move_timer >= MOVE_INTERVAL:
            move_timer = 0
            head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

            if head in snake:
                game_over = True
            else:
                snake.insert(0, head)
                if head == apple:
                    score += 1
                    apple = random_grid_pos(snake)
                else:
                    snake.pop()  

    for segment in snake:
        rect = pygame.Rect(segment[0] * TILE_SIZE, segment[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        pygame.draw.rect(screen, (0, 200, 0), rect)

    apple_rect = pygame.Rect(apple[0] * TILE_SIZE, apple[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE)
    pygame.draw.rect(screen, (200, 0, 0), apple_rect)
 
    pygame.display.flip()
    dt = clock.tick(60) / 1000
 
pygame.quit()