# imports
import pygame, sys
from pygame.locals import *

# setup variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hello, pygame!')

def handle_pygame_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 

class Tank:
    def __init__(self):
        self.color = (255, 255, 255)
        self.pos = (175, 125)
        self.radius = 50
        self.speed = 2

    def handle_input(self):
        keys = pygame.key.get_pressed()
        x_vel = keys[K_LEFT] * -self.speed + keys[K_RIGHT] * self.speed
        y_vel = keys[K_UP] * -self.speed + keys[K_DOWN] * self.speed
        self.pos = (self.pos[0] + x_vel, self.pos[1] + y_vel)    

    def handle_wrapping(self):
        min_x = -self.radius
        max_x = SCREEN_WIDTH + self.radius
        if (self.pos[0] < min_x):
            self.pos = (max_x, self.pos[1])
        if (self.pos[0] > max_x):
            self.pos = (min_x, self.pos[1])

        min_y = -self.radius
        max_y = SCREEN_HEIGHT + self.radius
        if (self.pos[1] < min_y):
            self.pos = (self.pos[0], max_y)
        if (self.pos[1] > max_y):
            self.pos = (self.pos[0], min_y)

    def update(self):
        self.handle_input()
        self.handle_wrapping()

    def draw(self):
        screen.fill((0, 0, 0))
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
        pygame.display.update()
  

# create Tank
t = Tank()

# main game loop
while True:
    # handle pygame events
    handle_pygame_events()

    # update Tank
    t.update()

    # draw Tank
    t.draw()
