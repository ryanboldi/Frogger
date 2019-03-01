import pygame

pygame.init()

# colors
ROAD = (128,128,128)
GRASS = (124, 252, 0)
YELLOW = (250, 252, 0)
SKY = (0, 250, 252)

#sizes
LANES = 3
ROADHEIGHT = 300

WIDTH = 800
HEIGHT = 500

LANESIZE = ROADHEIGHT/LANES
GRASSHEIGHT = ROADHEIGHT + 2*(LANESIZE) #LANESIZE on each side

screen = pygame.display.set_mode((WIDTH, HEIGHT))
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

    #draws background
    screen.fill(SKY)

    #draw grass
    pygame.draw.rect(screen, GRASS, [0, (HEIGHT-GRASSHEIGHT)/2, WIDTH, GRASSHEIGHT], 0)
    pygame.draw.rect(screen, (0,0,0), [-1, (HEIGHT-GRASSHEIGHT)/2, WIDTH+2, GRASSHEIGHT], 1)

    #draws road
    pygame.draw.rect(screen, ROAD, [0, (HEIGHT-ROADHEIGHT)/2, WIDTH, ROADHEIGHT], 0)
    pygame.draw.rect(screen, (0,0,0), [-1, (HEIGHT-ROADHEIGHT)/2, WIDTH+2, ROADHEIGHT], 1)

    


    # update screen
    pygame.display.flip()

    clock.tick(60)

pygame.quit()