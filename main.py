import pygame
import random

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()
running = True
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
apple_pos = pygame.Vector2(random.randint(1,1280),random.randint(1,720))
dt = 0


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("green")
    
# Fruit Logic  
    pygame.draw.circle(screen, "black", apple_pos, 40)




    pygame.display.flip()
    dt = clock.tick(60) / 1000

    
    
    
    
    
    
    
    
    
    
    
    
    
    clock.tick(60)
pygame.quit()