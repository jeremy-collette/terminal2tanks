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
* It can take in arguments, and can return a value.
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

## Return values
* If a function uses the `return` statement, the value after the `return` keyword is _returned_ and the function ends.
* When functions `return` a value, we can use it in our code.
* For example, we can `print` it, store it in a variable, or use it in an `if` statement. 
* Consider the `max` function, which we can use to find the bigger of two numbers. For example, `max(1,2)` would return `2`. Below we see how we can use the return value from this function.

```python
def max(a, b):
    if (a > b): return a
    return b

print(max(1,2))  # prints '2'
m = max(5,10)  # stores '10' in m

if (max(100, 2) == 100):  # returns '100', which we use in our if statement
    print('Max is 100!')

```

* Note: the `max` function is already defined by Python, so we don't need to define it ourselves. However, this helps us understand how to write functions.

---

## Functions calling functions
* Functions can call other functions.
* Consider the following example:

```python
def weekday():
    print("Work work...")

def weekend():
    print("Yeehaw!")

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
...

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
```
---

```python

    # drawing
    drawing()

```
---

## That's all, folks!
* You've finished the sixth workshop!