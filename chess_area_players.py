from game_area import GameArea
import pygame as pg
pg.init()
win = pg.display.set_mode((1200, 600))


BROWN= ( 132, 94, 66)
rect1 = pg.Rect((40, 80, 200, 75))  # (left,top,width,height)
pg.draw.rect(win, BROWN , rect1, 4)
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
        # Teken hier de Player informatie
        # Player 1: naam, tijd, ...
        # Player 2: naam, tijd, ...

