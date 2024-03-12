from colors import *
from game_area import GameArea
import pygame as pg

class GameAreaChessBoard(GameArea):
    def __init__(self, game, r):
        GameArea.__init__(self, game, r)

    def draw(self):
        GameArea.draw(self)
        self.game.chess_board.draw(self.game.win)
        
        