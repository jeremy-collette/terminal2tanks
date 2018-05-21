class: center, middle

# Week 06 - Functions
---

## Last Week's Challenge
### `wrapping_circle.py`
```python
...

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

...

```
---

## What is a function?
* A function allows us to repeat code in different sections of our code without copying and pasting.
* It takes in arguments, and can (optionally) return a value.
* Consider the following example:

```python
def say_hello(name):
    print('Hello, ' + name + '!')

say_hello('Colt')
say_hello('Trent')
say_hello('Isaac')
```

* All of the 'commands' that we've been using are actually functions!
* Remember the `print()` command? Function!
* These are all functions too:
    - `input()`
    - `max()`
    - `min()`
    - `pow()`
    - `pygame.quit()`
    - `range()`
    - `sys.exit()`

---

* Here's an example of what the `max` function might look like:

```python
def max(a, b):
    if (a > b): return a
    else: return b

print(max(4,7))
```

* What does this function do?

```python
def lcd(a, b):
    for i in range(2, min(a,b)+1):
        if (a % i == 0 and b % i == 0):
            return i
    return -1

print(lcd(5, 10))
```

* Evaluate the following:
    - `print(lcd(4, 12))`
    - `print(lcd(14, 21))`
    - `print(lcd(50, 100))`
    - `print(lcd(7, 9))`
---

## Functions calling functions
* Functions can call other functions.
* Consider the following example:

```python
def weekday():
    print("Work work...")

def weekend():
    print("Yehaw!")

def day(name):
    if (name == 'Saturday' or name == 'Sunday'):
        weekend()
    else:
        weekday()

day('Monday')
day('Friday')
day('Saturday')
day('sunday')
```

---

## Function scope
* Variables defined outside a function are called *global variables*.
* Global variables can be accessed inside a function, but their value cannot be changed unless the `global` keyword is used.
* Variables defined inside a function are not accessible outside a function.
* Variables defined inside one function are not available inside another function!
* Consider the following examples:

```python
def func1():
    b = 5

func1()
print(b)
```

```python
def func1():
    b = 5

def func2():
    func1()
    print(b)

func2()
```
---

* Evaluate the following example:

```python
a = 1

def func1():
    print('func1: ' + str(a))

def func2():
    a = 5
    print('func2: ' + str(a))

def func3():
    global a
    a = 10
    print('func3: ' + str(a))

func1()
func2()
func1()
func3()
func1()
```
---

## Challenge: `game_functions.py`
Modify our game from last week so that each section of code is inside a function. Here is some starter code:
```python
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
```
---

```python
    drawing()

```
---

## That's all, folks!
* You've finished the sixth workshop!