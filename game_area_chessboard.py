from colors import *
from game_area import GameArea
import pygame as pg
from evt_obj import EvtBtn as Button

class GameAreaChessBoard(GameArea):
    def __init__(self, game, r):
        GameArea.__init__(self, game, r)

    def draw(self):
        # Hier moet het bord met de stukken getekend worden.
        # We laten het chessboard object dit zelf doen
        # We geven het window en de rechthoek waarin getekend moet worden mee door
        GameArea.draw(self)
        self.game.chess_board.draw(self.game.win, self.rect)
        
        # tip: self.rect bevat de coördinaten van de linkerbovenhoek. Die kan je opslaan in een variabelen om er verder mee te rekenen
        # vb/ 
        # left = self.rect[0]
        # top = self.rect[1]
        # pg.draw.rect(self.game.win,BLACK,(self.rect[0],self.rect[1],10,10))