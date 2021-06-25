import abc

class BaseScene(abc.ABC):
    def __init__(self, game):
        self.game = game

    @abc.abstractmethod
    def handle_event(self, event):
        pass

    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def draw(self):
        pass
