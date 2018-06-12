class: center, middle

# Week 08 - Game workshop
---

## Last Week's Challenge
### `game_classes.py`

```python
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
```
---
```python
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
  
```
---

```python
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
```
---

## Drawing a tank
* Find an image online suitable to use for our tank.
    - PNG files are good because they usually have transparency.
* Modify our `Tank` class to load the image using the `pygame.image.load(...)` command.
* Modify our `Tank` class to draw the image on the screen using the `screen.blit(...)` command.
---

## Rotating our tank
* When we change direction, we want to rotate the image of our tank.
* We can get the orientation of our tank using the `math.atan2(...)` function.
* Take a copy of the image of our tank, and rotate it to the correct orientation each tick using the `pygame.transform.rotate(...)` command.
---

## Drawing a background
* We need a background for our tank to drive on!
* Find a background image off the internet that is suitable.
* Use the `pygame.image.load(...)` function to load the image, and the
`screen.blit(...)` function to draw it on the screen.

---

## Limiting the speed of the game
* The game will update at different speeds on different computers. This is because computers are faster / slower than each other.
* We want our game to run at the same speed everywhere, so that it behaves as expected.
* We can limit the speed of our game by limiting the frames per second.
* Create a pygame `Clock` and use the `clock.tick(...)` method in our main loop to limit the speed of our game.

## Challenge: game extensions
* Make some modification to the game that you think would be fun!
* For example, make the tank drive faster if you're holding the SHIFT key.
---

## That's all, folks!
* You've finished the eighth workshop!