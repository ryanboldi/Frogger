import pygame
import random
import math

pygame.init()

FRAMERATE = 60

# colors
BLACK = (0, 0, 0)
ROAD = (128, 128, 128)
GRASS = (124, 252, 0)
YELLOW = (250, 252, 0)
SKY = (0, 250, 252)
CAR_COLORS = [(178, 34, 34), (255, 165, 0),
              (255, 215, 0), (0, 250, 154),
              (0, 255, 255), (0, 0, 128),
              (65, 105, 225), (138, 43, 226),
              (75, 0, 130), (128, 0, 128),
              (255, 0, 255), (199, 21, 133)]
PLAYER = (0, 90, 90)


# sizes
LANES = 4
ROADHEIGHT = 300

# screen sizes
WIDTH = 800
HEIGHT = 500

LANESIZE = ROADHEIGHT/LANES
GRASSHEIGHT = ROADHEIGHT + (2 * (LANESIZE))  # LANESIZE on each side


# consts to help with runtime
ROADSTART = (HEIGHT-ROADHEIGHT)/2
GRASSSTART = (HEIGHT - GRASSHEIGHT)/2

CAR_LENGTH_SCALE = 12  # scale from road length to car length
CAR_WIDTH_SCALE = 2  # scale from lane width to car width

CAR_SPEED = 7
X_SPEED = 20
CAR_SPAWN_DELAY = 20

CAR_WHEEL_SCALE = 3

LANEARR = [((i * LANESIZE) + ROADSTART) for i in range(0, LANES)]
CARS = [[] for i in LANEARR]

playerLanes = []
playerLanes = list.copy(LANEARR)

print (LANEARR)
print(playerLanes)

playerLanes.append((LANEARR[-1] + LANESIZE))
playerLanes.insert(0, (LANEARR[0] - LANESIZE))

print("lane array = {}".format(LANEARR))
print(playerLanes)

playerX = WIDTH/2
playerlane = len(playerLanes)-1
print(playerlane)
playerY = playerLanes[playerlane]

class Car(object):
    def __init__(self, lane):
        self.lane = (lane)
        self.length = WIDTH/CAR_LENGTH_SCALE
        # cars will ocupy half the lane
        self.width = (LANESIZE/CAR_WIDTH_SCALE)

        # spawns car slightly off screen
        self.y = LANEARR[self.lane] + (LANESIZE-self.width)/2
        self.x = -((self.length)*2)

        self.wheelDif = self.width/CAR_WHEEL_SCALE
        self.wheelLength = self.wheelDif
        self.wheelWidth = self.wheelLength/2  # 2:1 aspect ratio of wheels

        self.color = random.choice(CAR_COLORS)

    def Draw(self):
        pygame.draw.rect(screen, self.color, [
                         self.x, self.y, self.length, self.width], 0)
        # wheels
        pygame.draw.rect(screen, BLACK, [
                         self.x + (self.wheelDif/2), self.y-(self.wheelWidth/2), self.wheelLength, self.wheelWidth])
        pygame.draw.rect(screen, BLACK, [self.x + self.length - (self.wheelDif/2) -
                                         self.wheelLength, self.y-(self.wheelWidth/2), self.wheelLength, self.wheelWidth])
        pygame.draw.rect(screen, BLACK, [self.x + (self.wheelDif/2), self.y + self.width - (
            self.wheelWidth/2), self.wheelLength, self.wheelWidth])
        pygame.draw.rect(screen, BLACK, [self.x + self.length - (self.wheelDif/2) - self.wheelLength,
                                         self.y + self.width - (self.wheelWidth/2), self.wheelLength, self.wheelWidth])
        self.x += CAR_SPEED

def spawnCar():
    lane = math.floor(random.random() * len(LANEARR))
    c = Car(lane)
    CARS[lane].append(c)

def deleteCars():
    #deletes all cars that are fully off-screen
    for lane in CARS:
        ind = 0
        for car in lane:
            if (car.x - car.width) > WIDTH:
                del lane[ind]
            ind+=1

def drawPlayer():
    playerWidth = LANESIZE/1.5
    pygame.draw.rect(screen, PLAYER, [playerX + (LANESIZE - playerWidth)/2,  playerY +(LANESIZE - playerWidth)/2, playerWidth/1.5, playerWidth])


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Frogger')

# checks if player is alive
alive = True
MoveAble = False
# clock will be used to control how fast the screen updates
clock = pygame.time.Clock()
frameCount = 0
count = 0
# MAIN PROGRAM LOOP-----------------------
while alive:
    frameCount += 1

    #for i in range(0, len(CARS)):
    #    print("lane {} has {} cars".format(i, len(CARS[i])))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            alive = False
        if event.type == pygame.KEYDOWN:
            if MoveAble:
                if event.key == pygame.K_UP:
                    if(playerlane > 0):
                        playerlane -= 1
                if event.key == pygame.K_DOWN:
                    if(playerlane  < len(playerLanes)-1):
                        playerlane += 1
                if event.key == pygame.K_RIGHT:
                    playerX += X_SPEED
                if event.key == pygame.K_LEFT:
                    playerX -= X_SPEED

    # draws background
    screen.fill(SKY)

    # draw grass
    pygame.draw.rect(screen, GRASS, [0, GRASSSTART, WIDTH, GRASSHEIGHT], 0)
    pygame.draw.rect(screen, (10, 100, 10),
                     [-1, GRASSSTART, WIDTH+2, GRASSHEIGHT], 1)

    # draws road
    pygame.draw.rect(screen, ROAD, [0, ROADSTART, WIDTH, ROADHEIGHT], 0)
    pygame.draw.rect(screen, (100, 100, 100),
                     [-2, ROADSTART, WIDTH+4, ROADHEIGHT], 2)

    # draws yellow line (lane)
    for i in range(1, LANES):
        pygame.draw.line(screen, YELLOW, [
                         0, ROADSTART + (LANESIZE*i) - 0.5], [WIDTH, ROADSTART+(LANESIZE*i) - 0.5], 1)

    for lane in CARS:
        for car in lane:
            car.Draw()

    playerY = playerLanes[playerlane]
    drawPlayer()

    if (frameCount == CAR_SPAWN_DELAY):
        spawnCar()
        deleteCars()
        frameCount = 0
        if count < 5:
            count += 1
        
        print(count)
        if count == 5:
            print(MoveAble)
            MoveAble = True

    # update screen
    pygame.display.flip()

    clock.tick(FRAMERATE)

pygame.quit()
