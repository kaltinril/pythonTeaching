# THis is going to be as simple as possible
import sys
import pygame
from pygame.locals import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
fps = 60.0

# List of points for the snake
snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
xv = 0
yv = 0
snake_size = 2

# List of "fruit" to eat
fruit = [(50, 50)]

# initialize everything for drawing
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fps_clock = pygame.time.Clock()

# loop
while True:
    # Check for directional input
    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and yv == 0:
                yv = -1
                xv = 0
            elif event.key == pygame.K_DOWN and yv == 0:
                yv = 1
                xv = 0
            elif event.key == pygame.K_LEFT and xv == 0:
                yv = 0
                xv = -1
            elif event.key == pygame.K_RIGHT and xv == 0:
                yv = 0
                xv = 1

    # Clear screen
    screen.fill(BLACK)  # Fill the screen with black.

    # draw snake
    for point in snake:
        pygame.draw.circle(screen, WHITE, point, snake_size) #screen.set_at(point, WHITE) # This was to draw a single pixel

    pygame.display.flip()

    # move snake by adding another point with the velociy/direction, to the last position and adding it to the list
    last_point = snake[-1]
    new_point = (last_point[0] + (xv * snake_size), last_point[1] + (yv* snake_size))
    snake.append(new_point)

    # remove the last point
    snake.pop(0)

    # Check if the snake collided with the walls
    if (
        new_point[0] >= SCREEN_WIDTH
        or new_point[0] <= 0
        or new_point[1] >= SCREEN_HEIGHT
        or new_point[1] <= 0
    ):
        snake.clear()
        snake.append((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        xv = 0
        yv = 0


    # Force to 60 FPS
    fps_clock.tick(fps)

