from game_area import GameArea
from listbox import *
import pygame as pg
from chess_game import *

class GameAreaHistory(GameArea):
    def __init__(self, game, r):
        GameArea.__init__(self, game, r)
        rect = pg.Rect(self._x(10), self._y(10), self.rect.width - 20, self.rect.height - 20)
        self.historylistbox = ListBox_MoveHistory(self, rect, self.game.chess_board.h)

    def draw(self):
        GameArea.draw(self)
        
        self.historylistbox.draw(self.game.win)