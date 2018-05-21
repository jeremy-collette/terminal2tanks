# imports
import pygame, sys
from pygame.locals import *

# setup variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
color = (255, 255, 255)
pos = (175, 125)
radius = 50
x_vel = 0
y_vel = 0
speed = 2

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hello, pygame!')

# main game loop
while True:
    # event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        
    # keyboard input
    keys = pygame.key.get_pressed()
    x_vel = keys[K_LEFT] * -speed + keys[K_RIGHT] * speed
    y_vel = keys[K_UP] * -speed + keys[K_DOWN] * speed
    pos = (pos[0] + x_vel, pos[1] + y_vel)
   
    # wrap x-axis around the screen
    min_x = -radius
    max_x = SCREEN_WIDTH + radius
    if (pos[0] < min_x):
        pos = (max_x, pos[1])
    if (pos[0] > max_x):
        pos = (min_x, pos[1])

    # wrap y-axis around the screen
    min_y = -radius
    max_y = SCREEN_HEIGHT + radius
    if (pos[1] < min_y):
        pos = (pos[0], max_y)
    if (pos[1] > max_y):
        pos = (pos[0], min_y)

    # drawing
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, color, pos, radius)
    pygame.display.update()
