# Using template from:
# https://gist.github.com/MatthewJA/7544830

import sys

import pygame
from pygame.locals import *


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


def draw(screen):
    """
    Draw things to the window. Called once per frame.
    """
    screen.fill((0, 0, 0))  # Fill the screen with black.

    # Flip the display so that the things we drew actually show up.
    pygame.display.flip()


def run_game():
    # Initialise PyGame.
    pygame.init()

    fps = 60.0
    fps_clock = pygame.time.Clock()

    # Set up the window.
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))

    # Main game loop.
    dt = 1 / fps  # dt is the time since last frame.
    while True:  # Loop forever!
        update(dt)
        draw(screen)

        dt = fps_clock.tick(fps)


# This is the entry point to the game
if __name__ == "__main__":
    run_game()
