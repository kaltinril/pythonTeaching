# Using template from:
# https://gist.github.com/MatthewJA/7544830

import sys

import pygame
from pygame.locals import *

# define some colors (R, G, B)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
FUCHSIA = (255, 0, 255)
GRAY = (128, 128, 128)
LIME = (0, 128, 0)
MAROON = (128, 0, 0)
NAVYBLUE = (0, 0, 128)
OLIVE = (128, 128, 0)
PURPLE = (128, 0, 128)
RED = (255, 0, 0)
SILVER = (192, 192, 192)
TEAL = (0, 128, 128)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
CYAN = (0, 255, 255)

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

# Start the player positions, 0 is player1, 1 is player2
PLAYER1 = [20, 240]
PLAYER2 = [600, 240]
PLAYER_HEIGHT = 50
PLAYER_WIDTH = 10
PLAYER_SPEED = 5

BALL = [int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)]
BALL_SPEED = 5
BALL_SIZE = 10
BALL_V_X = 1
BALL_V_Y = 1


def draw_bumper(screen, position):
    x_draw = position[0] - (PLAYER_WIDTH / 2)
    y_draw = position[1] - (PLAYER_HEIGHT / 2)
    draw_rect = pygame.Rect(x_draw, y_draw, 10, 50)
    pygame.draw.rect(screen, WHITE, draw_rect)


def draw_ball(screen, position, size):
    pygame.draw.circle(screen, WHITE, position, size)


def update(dt):
    """
    Update game. Called once per frame.
    dt is the amount of time passed since last frame.
    If you want to have constant apparent movement no matter your framerate,
    what you can do is something like

    x += v * dt

    and this will scale your velocity based on time. Extend as necessary."""

    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        PLAYER1[1] -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        PLAYER1[1] += PLAYER_SPEED

    # Restrict the player bounds
    if PLAYER1[1] > (SCREEN_HEIGHT - 25):
        PLAYER1[1] = SCREEN_HEIGHT - 25
    if PLAYER1[1] < 25:
        PLAYER1[1] = 25

    BALL[0] += (BALL_V_X * BALL_SPEED)
    BALL[1] += (BALL_V_Y * BALL_SPEED)

    #if BALL[0] > (SCREEN_HEIGHT - BALL_SIZE[0]):
        #BALL_V_X *= -1

def draw(screen):
    """
    Draw things to the window. Called once per frame.
    """
    screen.fill((0, 0, 0))  # Fill the screen with black.

    draw_bumper(screen, PLAYER1)
    draw_bumper(screen, PLAYER2)
    draw_ball(screen, BALL, BALL_SIZE)

    # Flip the display so that the things we drew actually show up.
    pygame.display.flip()


def run_game():
    # Initialise PyGame.
    pygame.init()

    fps = 60.0
    fps_clock = pygame.time.Clock()

    # Set up the window.

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Main game loop.
    dt = 1 / fps  # dt is the time since last frame.
    while True:  # Loop forever!
        update(dt)
        draw(screen)

        dt = fps_clock.tick(fps)


# This is the entry point to the game
if __name__ == "__main__":
    run_game()
