# Using template from:
# https://gist.github.com/MatthewJA/7544830

import sys

import pygame
from pygame.locals import *
import random

# define some colors (R, G, B)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
CYAN = (0, 255, 255)

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 480

PLAYER1 = [20, 240]
PLAYER2 = [600, 240]
PLAYER_HEIGHT = 50
PLAYER_WIDTH = 10
PLAYER_SPEED = 5

BALL = [int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)]
BALL_SPEED = 3
BALL_SIZE = 10
BALL_V_X = 0
BALL_V_Y = 0

SCORES = [0, 0]


def draw_bumper(screen, position):
    x_draw = position[0] - (PLAYER_WIDTH / 2)
    y_draw = position[1] - (PLAYER_HEIGHT / 2)
    draw_rect = pygame.Rect(x_draw, y_draw, PLAYER_WIDTH, PLAYER_HEIGHT)
    pygame.draw.rect(screen, WHITE, draw_rect)


def draw_ball(screen, position, size):
    pygame.draw.circle(screen, WHITE, position, size)


def reset_board():
    global BALL_V_X, BALL_V_Y

    BALL_V_X = 0
    BALL_V_Y = 0
    BALL[0] = int(SCREEN_WIDTH / 2)
    BALL[1] = int(SCREEN_HEIGHT / 2)

    PLAYER1[1] = 240
    PLAYER2[1] = 240


def draw_scores(screen, font):
    score_str = font.render(str(SCORES[0]), True, WHITE)
    screen.blit(score_str, (30, 30))

    score_str = font.render(str(SCORES[1]), True, WHITE)
    screen.blit(score_str, ((SCREEN_WIDTH - (30 + (score_str.get_width() // 2))), 30))


def update(dt):

    # Until we convert to using classes
    global BALL_V_X, BALL_V_Y

    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                BALL_V_X = -1 + (random.randint(0, 1) * 2)
                BALL_V_Y = -1 + (random.randint(0, 1) * 2)

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        PLAYER1[1] -= PLAYER_SPEED
    if keys[pygame.K_s]:
        PLAYER1[1] += PLAYER_SPEED
    # Player 2
    if keys[pygame.K_UP]:
        PLAYER2[1] -= PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        PLAYER2[1] += PLAYER_SPEED

    # Restrict the player bounds
    if PLAYER1[1] > (SCREEN_HEIGHT - 25):
        PLAYER1[1] = SCREEN_HEIGHT - 25
    if PLAYER1[1] < 25:
        PLAYER1[1] = 25

    if PLAYER2[1] > (SCREEN_HEIGHT - 25):
        PLAYER2[1] = SCREEN_HEIGHT - 25
    if PLAYER2[1] < 25:
        PLAYER2[1] = 25

    # Move the ball
    BALL[0] += (BALL_V_X * BALL_SPEED)
    BALL[1] += (BALL_V_Y * BALL_SPEED)

    if BALL[1] > (SCREEN_HEIGHT - BALL_SIZE) or BALL[1] < BALL_SIZE:
        BALL_V_Y *= -1

    # Do simple position check, not real collision check
    # If the ball is to the LEFT of player1
    if BALL[0] <= PLAYER1[0] + (PLAYER_WIDTH / 2):
        # If the ball is within the Y value of the player
        if PLAYER1[1] + (PLAYER_HEIGHT / 2) >= BALL[1] >= PLAYER1[1] - (PLAYER_HEIGHT / 2):
            BALL_V_X *= -1

    if BALL[0] >= PLAYER2[0] - (PLAYER_WIDTH / 2):
        # If the ball is within the Y value of the player
        if PLAYER2[1] + (PLAYER_HEIGHT / 2) >= BALL[1] >= PLAYER2[1] - (PLAYER_HEIGHT / 2):
            BALL_V_X *= -1

    # Give points
    if BALL[0] < BALL_SIZE:
        SCORES[1] += 1
        reset_board()
    elif BALL[0] > SCREEN_WIDTH - BALL_SIZE:
        SCORES[0] += 1
        reset_board()


def draw(screen, font):
    screen.fill((0, 0, 0))  # Fill the screen with black.

    draw_bumper(screen, PLAYER1)
    draw_bumper(screen, PLAYER2)
    draw_ball(screen, BALL, BALL_SIZE)
    draw_scores(screen, font)

    # Flip the display so that the things we drew actually show up.
    pygame.display.flip()


def run_game():
    # Initialise PyGame.
    pygame.init()

    fps = 60.0
    fps_clock = pygame.time.Clock()

    # Set up the window.
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    font = pygame.font.SysFont("comicsansms", 36)

    # Main game loop.
    dt = 1 / fps  # dt is the time since last frame.
    while True:  # Loop forever!
        update(dt)
        draw(screen, font)

        dt = fps_clock.tick(fps)


# This is the entry point to the game
if __name__ == "__main__":
    run_game()
