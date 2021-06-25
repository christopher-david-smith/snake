import pygame
import time

class Snake:

    def __init__(self, game, x, y, length=3, direction="right"):
        self.game = game
        self.body = []
        self.direction = direction
        self.refresh_time = 0.2 
        self.next_update_time = time.time()
        self.can_move_this_frame = True
        self.eaten_food_this_frame = False

        # Create the body of our snake, ensuring that each section of the
        # snake is to the right, left, above, or below the x,y coordinates
        # provided, depending on the given direction.
        _x, _y = x, y
        for i in [_ for _ in range(length)][::-1]:
            if direction == "right":
                _x = (int(x/40) * 40) - (40 * i)

            if direction == "left":
                _x = (int(x/40) * 40) + (40 * i)

            if direction == "down":
                _y = (int(y/40) * 40) - (40 * i)

            if direction == "up":
                _y = (int(y/40) * 40) + (40 * i)
        
            self.body.append((_x, _y))

    @property
    def position(self):
        return self.body[-1]

    def update(self):
        
        if time.time() < self.next_update_time:
            return

        self.next_update_time = time.time() + self.refresh_time
    
        x, y = self.body[-1]
        x += 40 if self.direction == "right" else 0
        x -= 40 if self.direction == "left" else 0
        y += 40 if self.direction == "down" else 0
        y -= 40 if self.direction == "up" else 0

        self.can_move_this_frame = True
        self.body.append((x, y))
        if not self.eaten_food_this_frame:
            del self.body[0]

        self.eaten_food_this_frame = False

    def draw(self):
        for section in self.body[:-1]:
            pygame.draw.rect(
                self.game.display,
                (0, 255, 0),
                (section[0], section[1], 39, 39))

        pygame.draw.rect(
            self.game.display,
            (255, 255, 0),
            (self.body[-1][0], self.body[-1][1], 39, 39))
