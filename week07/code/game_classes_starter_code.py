# imports
import pygame, sys
from pygame.locals import *

# setup constant variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hello, pygame!')

# handles pygame events
def handle_pygame_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 

# the Tank class represents a real-life tank!
class Tank:
    # constructor
    def __init__(self):
        self.color = (255, 255, 255)
        self.pos = (175, 125)
        self.radius = 50
        self.speed = 2

    # handles keyboard input
    def handle_input(self):
        # NOTE: copy handle_keyboard_input code form previous challenge here 

    # handles screen wrapping
    def handle_wrapping(self):
        # NOTE: copy handle_wrapping code from previous challenge here

    # updates the Tank
    def update(self):
        self.handle_input()
        self.handle_wrapping()

    # draws the Tank
    def draw(self):
        # NOTE: copy drawing code from previous challenge here


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
