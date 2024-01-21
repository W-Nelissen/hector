from colors import *
from game_area import GameArea
import pygame as pg

class GameAreaChessBoard(GameArea):
    def __init__(self, game, r):
        GameArea.__init__(self, game, r)

    def draw(self):
        # Hier moet het bord met de stukken getekend worden.
        # We laten het chessboard object dit zelf doen
        # We geven het window en de rechthoek waarin getekend moet worden mee door
        GameArea.draw(self)
        self.game.chess_board.draw(self.game.win, self.rect)
