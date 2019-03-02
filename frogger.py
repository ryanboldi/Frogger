import pygame
from car import Car

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

#consts to help with runtime
ROADSTART = (HEIGHT-ROADHEIGHT)/2
GRASSSTART = (HEIGHT - GRASSHEIGHT)/2

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('frogger')

# checks if player is alive
alive = True

# clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

LANEARR = [((i*LANESIZE) + ROADSTART) for i in range(0,LANES)]
Car = Car(LANES)



# MAIN PROGRAM LOOP-----------------------
while alive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            alive = False

    #draws background
    screen.fill(SKY)

    #draw grass
    pygame.draw.rect(screen, GRASS, [0, GRASSSTART, WIDTH, GRASSHEIGHT], 0)
    pygame.draw.rect(screen, (10,100,10), [-1, GRASSSTART, WIDTH+2, GRASSHEIGHT], 1)

    
    #draws road
    pygame.draw.rect(screen, ROAD, [0, ROADSTART, WIDTH, ROADHEIGHT], 0)
    pygame.draw.rect(screen, (100,100,100), [-2, ROADSTART, WIDTH+4, ROADHEIGHT], 2)


    #draws yellow line (lane)
    for i in range(1, LANES):
        pygame.draw.line(screen, YELLOW, [0, ROADSTART + (LANESIZE*i) - 0.5],[WIDTH, ROADSTART+(LANESIZE*i) - 0.5], 1)

    # update screen
    pygame.display.flip()

    clock.tick(60)

pygame.quit()