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

class Bullet:
    def __init__(self, pos, angle):
        self.color = (255, 255, 255)
        self.pos = pos
        self.image = pygame.image.load('bullet.png')
        self.image = pygame.transform.scale(self.image, (40,20))
        self.rotated_image = self.image
        self.initial_orientation = 90
        theta = (angle + 270) * (math.pi / 180) 
        self.x_vel = math.cos(theta) * 10
        self.y_vel = math.sin(theta) * 10

    def handle_input(self):
        self.pos = (self.pos[0] + self.x_vel, self.pos[1] + self.y_vel)

        if (self.x_vel != 0 or self.y_vel != 0):
            new_orientation = math.atan2(self.x_vel, -self.y_vel) * (180 / math.pi)
            angle_diff = self.initial_orientation - new_orientation
            self.rotated_image = pygame.transform.rotate(self.image, angle_diff)

    def is_offscreen(self):
        min_x = -self.rotated_image.get_width()
        max_x = SCREEN_WIDTH + self.rotated_image.get_width()
        if (self.pos[0] < min_x):
            return True
        if (self.pos[0] > max_x):
            return True

        min_y = -self.rotated_image.get_height()
        max_y = SCREEN_HEIGHT + self.rotated_image.get_height()
        if (self.pos[1] < min_y):
            return True
        if (self.pos[1] > max_y):
            return True
        return False

    def update(self):
        self.handle_input()

    def draw(self):
        image_rect = self.rotated_image.get_rect()
        centred_pos = (self.pos[0] - image_rect[2] / 2., self.pos[1] - image_rect[3] / 2.)
        screen.blit(self.rotated_image, centred_pos)

class Tank:
    def __init__(self):
        self.color = (255, 255, 255)
        self.pos = (175, 125)
        self.speed = 2
        self.image = pygame.image.load('tank.png')
        self.rotated_image = self.image
        self.initial_orientation = 180
        self.orientation = self.initial_orientation
        self.bullets = []
        self.last_bullet = 0
        self.tick = 0

    def handle_input(self):
        keys = pygame.key.get_pressed()
        shift_speed = self.speed * (1 + keys[K_LSHIFT])
        x_vel = keys[K_LEFT] * -shift_speed + keys[K_RIGHT] * shift_speed
        y_vel = keys[K_UP] * -shift_speed + keys[K_DOWN] * shift_speed
        self.pos = (self.pos[0] + x_vel, self.pos[1] + y_vel)

        if (x_vel != 0 or y_vel != 0):
            self.orientation = math.atan2(x_vel, -y_vel) * (180 / math.pi)
            angle_diff = self.initial_orientation - self.orientation
            self.rotated_image = pygame.transform.rotate(self.image, angle_diff)

        if (self.tick - self.last_bullet > 5 and keys[K_SPACE]):
            self.bullets.append(Bullet(self.pos, self.orientation))
            self.last_bullet = self.tick

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
        self.tick += 1
        self.handle_input()
        self.handle_wrapping()

        for b in self.bullets:
            b.update()
            if (b.is_offscreen()):
                self.bullets.remove(b)



    def draw(self):
        image_rect = self.rotated_image.get_rect()
        centred_pos = (self.pos[0] - image_rect[2] / 2., self.pos[1] - image_rect[3] / 2.)
        screen.blit(self.rotated_image, centred_pos)

        for b in self.bullets:
            b.draw()
        pygame.display.update()


# create Tank
t = Tank()

# main game loop
while True:
    # limit speed
    clock.tick(120)

    # handle pygame events
    handle_pygame_events()

    # update Tank
    t.update()

    # draw 
    screen.fill((0, 0, 0))
    screen.blit(background_image, (0,0))
    t.draw()
