from game_area import GameArea
import pygame as pg
pg.init()
win = pg.display.set_mode((1200, 600))

"""
   Dit is de game area waar alle spelerinformatie wordt getoond 
   player1: name, type, timer, ...
   player2: name, type, timer, ...
"""
class GameAreaPlayers(GameArea):
    def __init__(self, game, r):
        GameArea.__init__(self, game, r)

    def draw(self):
        GameArea.draw(self)

        self.game.chess_clock.draw(self.game.win)
