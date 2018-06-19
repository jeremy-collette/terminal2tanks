class: center, middle

# Week 09 - Game workshop II
---

## Last Week's Challenge
### `game_extensions.py`

* Last week's challenge was to make some modification to the game that you think would be fun.
* Here is an example, which makes the tank driver faster if the player is holding the SHIFT key.
* We can achieve this by modifying the `Tank` class `handle_input()` function. 

```python
...

    def handle_input(self):
        keys = pygame.key.get_pressed()
        shift_speed = self.speed * (1 + keys[K_LSHIFT])
        x_vel = keys[K_LEFT] * -shift_speed + keys[K_RIGHT] * shift_speed
        y_vel = keys[K_UP] * -shift_speed + keys[K_DOWN] * shift_speed
        self.pos = (self.pos[0] + x_vel, self.pos[1] + y_vel)

        if (x_vel != 0 or y_vel != 0):
            new_orientation = math.atan2(x_vel, -y_vel) * (180 / math.pi)
            angle_diff = self.initial_orientation - new_orientation
            self.rotated_image = pygame.transform.rotate(self.image, angle_diff)
...
```
---
## Adding bullets!
* We want our tank to shoot bullets. 
* We can create a `Bullet` class to represent bullets.
* Our `Tank` should shoot bullets when the user presses spacebar.

---

## Challenge: game extensions
* Make some modification to the game that you think would be fun!
* For example, make an enemy tank that is controlled by the computer.
---

## That's all, folks!
* You've finished the ninth workshop!