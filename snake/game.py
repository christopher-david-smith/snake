import pygame
from scenes import TitleScene
from scenes import GameScene
from scenes import GameOverScene

class Game:
    def __init__(self):
        pygame.init()
       
        self.grid_width = 40
        self.grid_height = 40

        self.board_width = self.grid_width * 25
        self.board_height = self.grid_height * 20 + 100

        self.display = pygame.display.set_mode((
            self.board_width,
            self.board_height + 100
        ))

        self.scenes = {
            'title':    TitleScene,
            'game':     GameScene,
            'gameover': GameOverScene
        }

        self.current_scene = 'title' 
        self.clock = pygame.time.Clock()
        self.fps = 30
        self.score = 0

        for name, cls in self.scenes.items():
            self.scenes[name] = cls(self)

    def run(self):
        while True:
            events = pygame.event.get()
            for event in events:
                self.scenes[self.current_scene].handle_event(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.display.fill((0, 0, 0))
            self.scenes[self.current_scene].update()
            self.scenes[self.current_scene].draw()
            self.clock.tick(self.fps)
            pygame.display.flip()
