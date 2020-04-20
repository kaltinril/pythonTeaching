# THis is going to be as simple as possible
import sys
import pygame
from pygame.locals import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
fps = 60.0

# List of points for the snake
snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]

# initialize everything for drawing
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fps_clock = pygame.time.Clock()

# loop
while True:

    # Clear screen
    screen.fill((0, 0, 0))  # Fill the screen with black.

    # draw snake

    # Check for directional input
    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # move snake by adding another point with the velociy/direction, to the last position and adding it to the list
    # remove the last point

    # Force to 60 FPS
    fps_clock.tick(fps)

