import pygame

from .basescene import BaseScene
from snake import Snake

class TitleScene(BaseScene):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title = [
            "### ### ### # # ###",
            "#   # # # # # # #  ",
            "### # # ### ##  ###",
            "  # # # # # # # #  ",
            "### # # # # # # ###"]

        # Menu options
        self.menu_index = 0
        self.menu = [
            [
                "### #   ### # #",
                "# # #   # # # #",
                "### #   ### ###",
                "#   #   # #   #",
                "#   ### # # ###"
            ],
            [
                "### # # ### ###",
                "#   # #  #   # ",
                "###  #   #   # ",
                "#   # #  #   # ",
                "### # # ###  # "
            ]
        ]

        self.select_left = [
            "#  ",
            " # ",
            "  #",
            " # ",
            "#  "]

        self.select_right = [
            "  #",
            " # ",
            "#  ",
            " # ",
            "  #"]

        self.snake = Snake(self.game, 200, 40, length=5, direction="right")

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_DOWN:
                self.menu_index += 1 
                if self.menu_index >= len(self.menu):
                    self.menu_index = 0

            if event.key == pygame.K_UP:
                self.menu_index -= 1
                if self.menu_index < 0:
                    self.menu_index = len(self.menu) - 1
            
            if event.key == pygame.K_RETURN:
                if self.menu_index == 0:
                    self.game.current_scene = 'game' 

                if self.menu_index == 1:
                    pygame.quit()
                    exit()

    def update(self):
       
        self.snake.update()
        
        position = self.snake.position
        if position == (920, 40):
            self.snake.direction = "down"

        elif position == (920, 360):
            self.snake.direction = "left"

        elif position == (40, 360):
            self.snake.direction = "up"

        elif position == (40, 40):
            self.snake.direction = "right"

    def draw(self):

        # Draw our snake 
        self.snake.draw()

        # Draw the title
        for y, line in enumerate(self.title):
            for x, character in enumerate(self.title[y]):
               
                if character != "#":
                    continue

                pygame.draw.rect(
                    self.game.display,
                    (0, 255, 0),
                    ((x + 3) * 40, (y + 3) * 40, 39, 39))

        # Draw menu
        start_y = 12 
        for index, item in enumerate(self.menu):
            padding = start_y + (6 * index) 
            for y, line in enumerate(item):
                for x, character in enumerate(item[y]):
                    
                    if character != "#":
                        continue
                    
                    colour = (255, 255, 255)
                    if index == self.menu_index:
                        colour = (255, 0, 0)

                    pygame.draw.rect(
                        self.game.display,
                        colour,
                        ((x + 5) * 40, (padding + y) * 40, 39, 39))

            if index == self.menu_index:
                for y, line in enumerate(self.select_left):
                    for x, character in enumerate(self.select_left[y]):
                        
                        if character != "#":
                            continue

                        pygame.draw.rect(
                            self.game.display,
                            (255, 0, 0),
                            ((x + 1) * 40, (padding + y) * 40, 39, 39))
                
                for y, line in enumerate(self.select_right):
                    for x, character in enumerate(self.select_right[y]):
                        
                        if character != "#":
                            continue

                        pygame.draw.rect(
                            self.game.display,
                            (255, 0, 0),
                            ((x + 21) * 40, (padding + y) * 40, 39, 39))
