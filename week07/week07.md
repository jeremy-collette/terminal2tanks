class: center, middle

# Week 07 - Intro to classes
---

## Last Week's Challenge
### `game_functions.py`
```python
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
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()   

def handle_keyboard_input(pos): 
```
---
```python
    keys = pygame.key.get_pressed()
    x_vel = keys[K_LEFT] * -speed + keys[K_RIGHT] * speed
    y_vel = keys[K_UP] * -speed + keys[K_DOWN] * speed
    pos = (pos[0] + x_vel, pos[1] + y_vel)
    return pos

def handle_wrapping(pos):
    min_x = -radius
    max_x = SCREEN_WIDTH + radius
    if (pos[0] < min_x):
        pos = (max_x, pos[1])
    if (pos[0] > max_x):
        pos = (min_x, pos[1])

    min_y = -radius
    max_y = SCREEN_HEIGHT + radius
    if (pos[1] < min_y):
        pos = (pos[0], max_y)
    if (pos[1] > max_y):
        pos = (pos[0], min_y)
    return pos

def drawing():
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, color, pos, radius)
    pygame.display.update()

# main game loop
while True:
    # event handling
    handle_events()
        
    # keyboard input
```
---
```python
    pos = handle_keyboard_input(pos)
   
    # handle wrapping
    pos = handle_wrapping(pos)

    # drawing
    drawing()


```
---

## What is a class?
* Previously, we've been using `string`, `float`, `integer`, and even `list`. These are 'built-in types'.
* A class is a 'user-defined type'. A type that we create ourselves!
* This is because we often find the need for more complicated functionality, that built-in types cannot provide.
* Often, a class will represent a real-world concept.
* For example, lets create the `Point` class to hold a coordinate on a 2D plane.

```python
class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

p = Point()
p.x = 50
p.y = 100

print('Point at (' + str(p.x) + ', ' + str(p.y) + ')')
```

---
## Constructors
* The `__init__` method (similar to a function) is a _constructor_. 
* Constructors are used to initialise our class. Here we create the data members (variables) that our class needs.
* Constructors can also take arguments, that we can use to further customise our class.
* Let's create the `Point` class again, with a constructor that takes arguments.

```python
class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

p = Point(50, 100)

print('Point at (' + str(p.x) + ', ' + str(p.y) + ')')
```
---

## Class methods
* A function that is owned by a class is called a _method_.
* Methods allow us to operate on the data members of a class.
* The first argument for class methods is always `self`, which is a reference to the class that owns the method.
* We need to use `self` to access our classes data members.
* Let's create the `Point` class again, with the `reset` and `distance` methods.

```python
class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def reset(self):
        self.x = 0
        self.y = 0

    def distance(self, other):
        return math.sqrt(math.pow(self.x - other.x, 2) + math.pow(self.y - other.y, 2))

p = Point(50, 100)
p2 = Point(75, 150)

print('Distance between points: ' + str(p.distance(p2)))
p.reset()
p2.reset()
print('Distance between resetted points: ' + str(p.distance(p2)))
```
---

## Challenge: `game_classes.py`
* Modify our game so that the circle is represented by a class called `Tank`.
* Copy the code from our functions in the previous challenge to functions in the Tank class.
* Here is some starter code:

```python
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
```
---
```python
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
        # NOTE: copy handle_keyboard_input code from previous challenge here 

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
```
---
```python
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

## That's all, folks!
* You've finished the seventh workshop!