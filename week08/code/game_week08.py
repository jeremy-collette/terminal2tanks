# imports
import pygame, sys, math
from pygame.locals import *

# setup variables
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# pygame setup
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tanks!')
background_image = pygame.image.load('background.jpg')
clock = pygame.time.Clock()

def handle_pygame_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit() 

class Tank:
    def __init__(self):
        self.color = (255, 255, 255)
        self.pos = (175, 125)
        self.speed = 2
        self.image = pygame.image.load('tank.png')
        self.rotated_image = self.image
        self.initial_orientation = 180

    def handle_input(self):
        keys = pygame.key.get_pressed()
        x_vel = keys[K_LEFT] * -self.speed + keys[K_RIGHT] * self.speed
        y_vel = keys[K_UP] * -self.speed + keys[K_DOWN] * self.speed
        self.pos = (self.pos[0] + x_vel, self.pos[1] + y_vel)

        if (x_vel != 0 or y_vel != 0):
            new_orientation = math.atan2(x_vel, -y_vel) * (180 / math.pi)
            angle_diff = self.initial_orientation - new_orientation
            self.rotated_image = pygame.transform.rotate(self.image, angle_diff)

    def handle_wrapping(self):
        min_x = -self.rotated_image.get_width()
        max_x = SCREEN_WIDTH + self.rotated_image.get_width()
        if (self.pos[0] < min_x):
            self.pos = (max_x, self.pos[1])
        if (self.pos[0] > max_x):
            self.pos = (min_x, self.pos[1])

        min_y = -self.rotated_image.get_height()
        max_y = SCREEN_HEIGHT + self.rotated_image.get_height()
        if (self.pos[1] < min_y):
            self.pos = (self.pos[0], max_y)
        if (self.pos[1] > max_y):
            self.pos = (self.pos[0], min_y)

    def update(self):
        self.handle_input()
        self.handle_wrapping()

    def draw(self):
        image_rect = self.rotated_image.get_rect()
        centred_pos = (self.pos[0] - image_rect[2] / 2., self.pos[1] - image_rect[3] / 2.)
        screen.blit(self.rotated_image, centred_pos)
        pygame.display.update()


# create Tank
t = Tank()

# main game loop
while True:
    # limit speed
    clock.tick(60)

    # handle pygame events
    handle_pygame_events()

    # update Tank
    t.update()

    # draw 
    screen.fill((0, 0, 0))
    screen.blit(background_image, (0,0))
    t.draw()
