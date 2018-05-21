# imports
import pygame, sys
from pygame.locals import *

# setup variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 300
color = (255, 255, 255)
pos = (175, 125)
radius = 50
speed = 2

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Hello, pygame!')

def handle_events():
    # handle pygame events here

def handle_keyboard_input(pos): 
    # handle keyboard input here

def handle_wrapping(pos):
    # handle x/y pos wrapping here

def drawing():
    # drawing code here

# main game loop
while True:
    # event handling
    handle_events()
        
    # keyboard input
    pos = handle_keyboard_input(pos)
   
    # handle wrapping
    pos = handle_wrapping(pos)

    # drawing
    drawing()
