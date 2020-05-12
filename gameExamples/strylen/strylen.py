import pygame, sys
from pygame.locals import *
import random

# set up pygame
pygame.init()

# set up the window
WIDTH = 500
HEIGHT = 400
windowSurface = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Strylen and Mando')

GROUND_POSITION = (HEIGHT / 5) * 4

# set up the colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Define the clock
clock = pygame.time.Clock()

# Load images
ground = pygame.image.load("ground.png")
ground = pygame.transform.scale(ground, (WIDTH, int(HEIGHT / 5)))
groundrect = ground.get_rect()
groundrect.left = 0
groundrect.top = GROUND_POSITION

deadpool = pygame.image.load("deadpool_scaled.png")
deadpool = pygame.transform.scale(deadpool, (60,108))
deadpoolrect = deadpool.get_rect()
deadpoolrect.left = WIDTH - (50 + deadpoolrect.width)
deadpoolrect.top = GROUND_POSITION - deadpoolrect.height

manda = pygame.image.load("mandalorian_scaled.png")
manda = pygame.transform.scale(manda, (60,108))
mandarect = manda.get_rect()
mandarect.left = 50
mandarect.top = GROUND_POSITION - mandarect.height

# run the game loop
game_running = True
speed1 = [0.0, 0.0]
speed2 = [0.0, 0.0]
jumping1 = False
jumping2 = False
fall_speed1 = 0.0
fall_speed2 = 0.0
facing1 = "Right"
facing2 = "Left"
while game_running:
    windowSurface.fill(WHITE)  # Clear the screen
    # pygame.draw.circle(windowSurface, BLUE, (x, y), r, 0)# Draw the circle
    
    windowSurface.blit(ground, groundrect)

    if facing1 == "Right":
        windowSurface.blit(manda, mandarect)
    else:
        windowSurface.blit(pygame.transform.flip(manda, True, False), mandarect)

    if facing2 == "Right":
        windowSurface.blit(deadpool, deadpoolrect)
    else:
        windowSurface.blit(pygame.transform.flip(deadpool, True, False), deadpoolrect)

    
    pygame.display.update()  # Update the screen
    

    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_running = False
                break
            if event.key == pygame.K_SPACE:
                if not jumping1:
                    speed1[1] = -6.0
                    jumping1 = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        facing1 = "Right"
        speed1[0] += 0.5
        if speed1[0] > 5.0:
            speed1[0] = 5.0
    if keys[pygame.K_a]:
        facing1 = "Left"
        speed1[0] += -0.5
        if speed1[0] < -5.0:
            speed1[0] = -5.0
    if keys[pygame.K_w]:
        if not jumping1:
            speed1[1] = -6.0
            jumping1 = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        facing2 = "Right"
        speed2[0] += 0.5
        if speed2[0] > 5.0:
            speed2[0] = 5.0
    if keys[pygame.K_LEFT]:
        facing2 = "Left"
        speed2[0] += -0.5
        if speed2[0] < -5.0:
            speed2[0] = -5.0
    if keys[pygame.K_UP]:
        if not jumping2:
            speed2[1] = -6.0
            jumping2 = True

    # Slow the first player x direction down
    if speed1[0] != 0:
        speed1[0] = speed1[0] + ((-speed1[0] / abs(speed1[0])) / 6)

    # Slow the second player x direction down
    if speed2[0] != 0:
        speed2[0] = speed2[0] + ((-speed2[0] / abs(speed2[0])) / 6)

    # Cause player1 to fall
    fall_speed1 = fall_speed1 + 0.02
    speed1[1] = speed1[1] + fall_speed1

    # Cause player2 to fall
    fall_speed2 = fall_speed2 + 0.02
    speed2[1] = speed2[1] + fall_speed2

    # Move the playerss by the speed
    mandarect = mandarect.move(speed1)
    deadpoolrect = deadpoolrect.move(speed2)

    if mandarect.top >= GROUND_POSITION - mandarect.height:
        mandarect.top = GROUND_POSITION - mandarect.height
        speed1[1] = 0
        fall_speed1 = 0
        jumping1 = False

    if deadpoolrect.top >= GROUND_POSITION - deadpoolrect.height:
        deadpoolrect.top = GROUND_POSITION - deadpoolrect.height
        speed2[1] = 0
        fall_speed2 = 0
        jumping2 = False
