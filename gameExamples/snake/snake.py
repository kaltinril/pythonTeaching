# THis is going to be as simple as possible
import sys
import pygame
from pygame.locals import *
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
fps = 60.0

# List of points for the snake
snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
snake_v = (0, 0)
snake_size = 2

# List of "fruit" to eat
fruit = [(50, 50)]

# initialize everything for drawing
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fps_clock = pygame.time.Clock()
time_elapsed_since_last_action = 0

# loop
while True:
    # Check for directional input
    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_v[1] == 0:
                snake_v = (0, -1)
            elif event.key == pygame.K_DOWN and snake_v[1] == 0:
                snake_v = (0, 1)
            elif event.key == pygame.K_LEFT and snake_v[0] == 0:
                snake_v = (-1, 0)
            elif event.key == pygame.K_RIGHT and snake_v[0] == 0:
                snake_v = (1, 0)

    # Clear screen
    screen.fill(BLACK)  # Fill the screen with black.

    # Draw the fruit
    for f in fruit:
        pygame.draw.circle(screen, GREEN, f, 2)

    # draw snake
    for point in snake:
        pygame.draw.circle(screen, WHITE, point, snake_size) #screen.set_at(point, WHITE) # This was to draw a single pixel

    pygame.display.flip()

    # move snake by adding another point with the velociy/direction, to the last position and adding it to the list
    last_point = snake[-1]
    new_point = (last_point[0] + (snake_v[0] * snake_size), last_point[1] + (snake_v[1] * snake_size))
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

    # Move the fruit every 10 seconds
    if time_elapsed_since_last_action > 10000:
        x = random.randint(10, SCREEN_WIDTH - 10)
        y = random.randint(10, SCREEN_HEIGHT - 10)
        fruit.pop()
        fruit.append((x, y))
        time_elapsed_since_last_action = 0

    # Force to 60 FPS
    dt = fps_clock.tick(fps)
    time_elapsed_since_last_action += dt

