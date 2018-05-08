class: center, middle

# Week 05 - Pygame
---

## Last Week's Challenge
### `favourite_foods.py`
```python
food_list = []
food = None
while food != 'quit':
    food = input('Enter a favourite food (or \'quit\' to exit): ')
    if food != 'quit':
        food_list.append(food)

print('\nYour favourite foods are:')
for f in food_list:
    print(f)
```
---

## Pygame
* Pygame is the Python module that we will use to develop our game.
* It allows us to easily read user input (such as keypresses) and to draw on the screen.
* You can install Pygame in Python3 by running the following command in terminal: 
    - `python3 -m pip install -U pygame --user`
---

## Our first game: `hello_pygame.py`
```python
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
```
---
```python
    y_vel = keys[K_UP] * -speed + keys[K_DOWN] * speed
    pos = (pos[0] + x_vel, pos[1] + y_vel)

    # drawing
    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, color, pos, radius)
    pygame.display.update()
```
---

## Imports
```python 
# imports
import pygame, sys
from pygame.locals import *
```

* Your computer has many different Python modules, which are pre-written code we can use in our programs.
* A few slides earlier, we installed the Pygame module on our computer.
* We have to use the `import` command to load a module before we use it.
* For example:

```python
import math
print(math.pi)
```

* If we don't import a module before we use it, we get the error:

```python
>>> print(math.pi)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'math' is not defined
>>> 
```

---

## Variable setup
```python
# setup variables
color = (255, 255, 255)
pos = (175, 125)
radius = 50
x_vel = 0
y_vel = 0
speed = 2
```

* Here we setup some variables for later use.
* Note that the `color` and `pos` variables are tuples.

---

## Pygame setup
```python
# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello, pygame!')
```

* Here we setup pygame.
* The first command initialises pygame.
* The second command creates a screen (and stores it).
* The third command sets the caption for the screen.
---

## The main loop
```python
# main game loop
while True:
    # event handling
    ...
    # keyboard input
    ...
    # drawing
    ...
```

* The main loop of a game is the section of code that continually repeats while the game is running.
* What does `while True` do?

---


## Event handling
```python
# event handling
for event in pygame.event.get():
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
```

* Event handling allows us to detect when certain 'events' happen in our game.
* When the user clicks the quit button on our game, a `QUIT` event will be triggered.
* Here we handle the `QUIT` event and close the game.
---

## Keyboard input
```python
# keyboard input
keys = pygame.key.get_pressed()
x_vel = keys[K_LEFT] * -speed + keys[K_RIGHT] * speed
y_vel = keys[K_UP] * -speed + keys[K_DOWN] * speed
pos = (pos[0] + x_vel, pos[1] + y_vel)
```

* Keyboard input allows the user to control our game.
* Here we store all the current key presses in the `key` variable.
* Each keyboard key has a code. For example, the left arrow is `K_LEFT`.
* We can check if a key has been pressed by using the code as a index in the `keys` variable.
* If the left arrow has been pressed, `keys[K_LEFT]` will be `1`. Otherwise, it will be `0`.
* We can use the key press information for the arrows to change the x and y velocity of our shape.
* We then use the velocity to update the position of our shape.
---

## Drawing
```python
# drawing
screen.fill((0, 0, 0))
pygame.draw.circle(screen, color, pos, radius)
pygame.display.update()
```

* Here we handle drawing.
* Firstly, we clear the screen by filling it with black.
* Then, we draw our circle.
* And update the screen.

---

## Challenge: `wrapping_circle.py`
Adapt the code we saw today so that:
* When the shape goes off the screen, it wraps around the screen and appears on the other side.
---

## That's all, folks!
* You've finished the fifth workshop!