import random
import pygame

class Food:
    def __init__(self, game):
        self.game = game

        # Generate random position on the map to display food
        possible_coordinates = []
        for a in range(25):
            for b in range(20):
                _a = a * 40
                _b = b * 40
                if (_a, _b) not in self.game.scenes[self.game.current_scene].snake.body:
                    possible_coordinates.append((_a, _b))

        coordinates = random.choice(possible_coordinates)
        self.x = coordinates[0]
        self.y = coordinates[1]

    def draw(self):
        pygame.draw.rect(
            self.game.display,
            (255, 0, 0),
            (self.x, self.y, 39, 39))
