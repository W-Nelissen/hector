from game_area import GameArea
from evt_obj import *





class GameAreaSANDBOX(GameArea):
    def __init__(self, game, r):
        GameArea.__init__(self, game, r)
        self.test_button = EvtBtn(self.rect.left + 10, self.rect.top + 10, self.rect.width - 20, 40, "Klik mij", 1)
        self.evtObjects.append(self.test_button)
    def draw(self):
        GameArea.draw(self)
        for obj in self.evtObjects:
            obj.draw(self.game.win)



