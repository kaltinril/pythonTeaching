# Pygame - Shapes

This lesson will introduce the Pygame library.  This is a library that allows us to play sound, draw shapes and pictures, get keyboard and mouse input, and much more.

We will not describe how everything works in this lesson, but instead will provide a template and let the user work with that template to draw shapes.

## Purpose:

Learn how to draw dots, lines, rectangles, and circles.

## References:
- Free online Editor and IDE: https://repl.it/languages/python3
- Free online help about Python:  https://www.w3schools.com/python/
- These lessons: https://github.com/kaltinril/pythonTeaching/tree/master/assignments/4thgrade
- Pygame information: https://www.pygame.org/docs
- Pygame Draw: https://www.pygame.org/docs/ref/draw.html

## Template Pygame with pixel, line, rectangle, and circle

```python
import pygame, sys
from pygame.locals import *
import random

# set up pygame
pygame.init()

# set up the window
screen = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption('My Game')

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

# Define the clock
clock = pygame.time.Clock()

# Loop forever
while True:
  # Clear background to gray
  screen.fill(GRAY)
  
  # Draw 4 red dots (pixels)
  screen.set_at((10, 10), RED)
  screen.set_at((11, 11), RED)
  screen.set_at((10, 11), RED)
  screen.set_at((11, 10), RED)
  
  # Draw a white lines
  pygame.draw.line(screen, WHITE, (70, 20), (30, 90), 1)
  
  # Draw a GREEN rectangle
  pygame.draw.rect(screen, GREEN, (170, 120, 130, 190))
  
  # Draw a BLUE circle
  pygame.draw.circle(screen, BLUE, (300, 200), 30, 0)
  
  # Flip the display so that the things we drew actually show up.
  pygame.display.flip()

  # Check for events like quit, or keyboard
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()

  # Limit to 60 frames per second
  clock.tick(60)

```


