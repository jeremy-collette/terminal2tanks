# imports
import pygame, sys
from pygame.locals import *

# setup variables
color = (255, 255, 255)
pos = (175, 125)
radius = 50
x_vel = 0
y_vel = 0
speed = 2

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 300))
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

    # drawing
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, color, pos, radius)
    pygame.display.update()
