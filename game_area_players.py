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


        JULIET = (188,143,143 )
        ROMEO= (177,102,102)

        rect1 = pg.Rect((5, 200, 200, 75))  # (left,top,width,height) 
        pg.draw.rect(self.game.win, JULIET , rect1, 100)
        
        rect2 = pg.Rect((5, 200, 200, 50))  # (left,top,width,height) 
        pg.draw.rect(self.game.win, ROMEO , rect2, 100)

        