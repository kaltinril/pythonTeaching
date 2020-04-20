# THis is going to be as simple as possible
import sys
import pygame
from pygame.locals import *
import random
import math

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

fruit_colors = [RED, GREEN, BLUE]

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
fps = 60.0

# List of points for the snake
snake = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
snake_v = (0, 0)
snake_size = 2

# List of "fruit" to eat
fruit = [(50, 50, 3, GREEN)]
fruit_total = 4
fruit_size = 3

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
        pygame.draw.circle(screen, f[3], (f[0], f[1]), f[2])

    # draw snake
    for point in snake:
        pygame.draw.circle(screen, WHITE, point, snake_size) #screen.set_at(point, WHITE) # This was to draw a single pixel

    pygame.display.flip()

    # move snake by adding another point with the velociy/direction, to the last position and adding it to the list
    last_point = snake[-1]
    new_point = (last_point[0] + (snake_v[0] * snake_size), last_point[1] + (snake_v[1] * snake_size))
    snake.append(new_point)

    # Check if the snake collided with the fruit
    eaten = False
    for i in range(0, len(fruit)):
        f = fruit[i]
        distance = math.sqrt((f[0] - last_point[0])**2 + (f[1] - last_point[1])**2)
        if distance < (snake_size + f[2]):
            fruit.pop(i)
            eaten = True
            break

    # remove the last point
    if not eaten:
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
        snake_v = (0, 0)
        fruit.clear()

    # spawn another fruit every 2 seconds
    if time_elapsed_since_last_action > 2000 or len(fruit) == 0:
        x = random.randint(10, SCREEN_WIDTH - 10)
        y = random.randint(10, SCREEN_HEIGHT - 10)
        s = random.randint(2, 7)
        c = random.randint(0, 2)

        fruit.append((x, y, s, fruit_colors[c]))
        time_elapsed_since_last_action = 0

    # Only keep so many
    if len(fruit) > fruit_total:
        fruit.pop(0)

    # Force to 60 FPS
    dt = fps_clock.tick(fps)
    time_elapsed_since_last_action += dt

