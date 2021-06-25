import pygame
from .basescene import BaseScene

class GameOverScene(BaseScene):
   
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.font = pygame.font.Font(pygame.font.get_default_font(), 100)

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            self.game.current_scene = "game"
            self.game.score = 0
            self.game.scenes[self.game.current_scene].reset()

    def update(self):
        pass

    def draw(self):
        text = self.font.render("Game over!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.game.board_width/2, self.game.board_height/2 - 250))
        self.game.display.blit(text, text_rect)

        text = self.font.render("You scored: " + str(self.game.score), True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.game.board_width/2, self.game.board_height/2 - 50))
        self.game.display.blit(text, text_rect)
        
        text = self.font.render("Press enter", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.game.board_width/2, self.game.board_height/2 + 150))
        self.game.display.blit(text, text_rect)
        
        text = self.font.render("to play again", True, (255, 0, 0))
        text_rect = text.get_rect(center=(self.game.board_width/2, self.game.board_height/2 + 250))
        self.game.display.blit(text, text_rect)
