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
GRAY = (128, 128, 128)

fruit_colors = [RED, GREEN, BLUE]

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
fps = 60.0

# List of points for the snake
snake = [[SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 2]]
snake_v = (0, 0)
snake_size = 2
snake_length = 3
snake_speed = 2

# List of "fruit" to eat
fruit = [[50, 50, 5, GREEN]]
fruit_total = 5

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

    # draw snake
    for i in range(0, len(snake)):
        p = snake[i]
        v = (i / len(snake)) * 255
        print(v)
        pygame.draw.circle(screen, (v, v, v), p[0:2], p[2]) #screen.set_at(point, WHITE) # This was to draw a single pixel

    # Draw the fruit after, so we can see them above the tail
    for f in fruit:
        pygame.draw.circle(screen, f[3], (f[0], f[1]), f[2])

    pygame.display.flip()

    # move snake by adding another point with the velocity/direction, to the last position and adding it to the list
    last_point = snake[-1]
    new_point = [last_point[0] + (snake_v[0] * snake_speed), last_point[1] + (snake_v[1] * snake_speed), snake_size]
    snake.append(new_point)

    # Check if the snake collided with the fruit
    for i in range(0, len(fruit)):
        f = fruit[i]
        distance = math.sqrt((f[0] - last_point[0])**2 + (f[1] - last_point[1])**2)

        # Remove the fruit and increase the length of the snake
        if distance < (last_point[2] + f[2]):
            fruit.pop(i)
            # Increase by the size of the fruit * 2
            snake_length = snake_length + (f[2] * 2)
            if f[3] == RED:
                snake_size += 2
            break

    # remove the last point
    if len(snake) > snake_length:
        snake.pop(0)

    # Check if the snake collided with the walls
    if (
        new_point[0] >= SCREEN_WIDTH
        or new_point[0] <= 0
        or new_point[1] >= SCREEN_HEIGHT
        or new_point[1] <= 0
    ):
        snake.clear()
        snake.append([SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, snake_size])
        snake_v = (0, 0)
        fruit.clear()

    # spawn another fruit every 2 seconds
    if time_elapsed_since_last_action > 2000 or len(fruit) == 0:
        x = random.randint(10, SCREEN_WIDTH - 10)
        y = random.randint(10, SCREEN_HEIGHT - 10)
        s = random.randint(5, 15) # Fruit size
        c = random.randint(0, 2)  # Fruit color index

        # Slowly shrink the fruit size
        for i in range(0, len(fruit)):
            fruit[i][2] += -1
            if fruit[i][2] < 1:
                fruit[i][2] = 1

        fruit.append([x, y, s, fruit_colors[c]])
        time_elapsed_since_last_action = 0

    # Only keep so many
    if len(fruit) > fruit_total:
        fruit.pop(0)

    # Force to 60 FPS
    dt = fps_clock.tick(fps)
    time_elapsed_since_last_action += dt

