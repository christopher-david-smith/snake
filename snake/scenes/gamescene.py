from .basescene import BaseScene
from snake import Snake
from food import Food
import pygame

class GameScene(BaseScene):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.snake = Snake(self.game, 0, 0)
        self.food = Food(self.game)
        self.font = pygame.font.Font(pygame.font.get_default_font(), 100)

    def reset(self):
        self.snake = Snake(self.game, 0, 0)

    def handle_event(self, event):

        if event.type == pygame.KEYDOWN:

            if not self.snake.can_move_this_frame:
                return

            if event.key == pygame.K_DOWN and self.snake.direction != "up":
                self.snake.direction = "down"

            if event.key == pygame.K_UP and self.snake.direction != "down":
                self.snake.direction = "up"

            if event.key == pygame.K_LEFT and self.snake.direction != "right":
                self.snake.direction = "left"

            if event.key == pygame.K_RIGHT and self.snake.direction != "left":
                self.snake.direction = "right"
            
            if event.key in [pygame.K_DOWN, pygame.K_UP, pygame.K_LEFT, pygame.K_RIGHT]:
                self.snake.can_move_this_frame = False

    def update(self):

        # Food 
        x, y = self.snake.body[-1]
        if x == self.food.x and y == self.food.y:
            self.snake.eaten_food_this_frame = True
            self.food = Food(self.game)
            self.game.score += 1

            if self.game.score % 5 == 0:
                self.snake.refresh_time -= 0.01

        self.snake.update()

        # Collision detection
        x, y = self.snake.body[-1]
        if x < 0 or x > self.game.board_width - 40:
            self.game.current_scene = 'gameover'

        if y < 0 or y > self.game.board_height - 140:
            self.game.current_scene = 'gameover'

        for body_x, body_y in self.snake.body[:-1]:
            if x == body_x and y == body_y:
                self.game.current_scene = 'gameover'

    def draw(self):

        self.food.draw()
        self.snake.draw()

        pygame.draw.rect(
            self.game.display,
            (100, 100, 100),
            (0, self.game.board_height - 100, self.game.board_width, 200))

        text = self.font.render("Score: " + str(self.game.score), True, (0, 0, 0))
        self.game.display.blit(text, dest=(20, self.game.board_height - 80))
