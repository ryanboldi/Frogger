import pygame

pygame.init()

# colors
ROAD = (128,128,128)
GRASS = (124, 252, 0)
YELLOW = (250, 252, 0)
SKY = (0, 250, 252)

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('frogger')

# checks if player is alive
alive = True

# clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

# MAIN PROGRAM LOOP-----------------------
while alive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            alive = False

    screen.fill(SKY)

    pygame.draw.rect(screen, ROAD, [0, 30, 800, 300], 0)

    # update screen
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
