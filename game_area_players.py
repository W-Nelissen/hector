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

        JULIET = (188,143,143 )
        ROMEO= (177,102,102)

        rect1 = pg.Rect(( 9 , 200, 190, 75))  # (left,top,width,height) 
        pg.draw.rect(self.game.win, JULIET , rect1, 100)
        
        rect2 = pg.Rect((9, 190, 190, 10))  # (left,top,width,height) 
        pg.draw.rect(self.game.win, ROMEO , rect2, 100)
        
        rect3 = pg.Rect((9, 270, 190, 10))  # (left,top,width,height) 
        pg.draw.rect(self.game.win, ROMEO , rect3, 100)
        
        rect4 = pg.Rect((100, 200, 9,80))  # (left,top,width,height) 
        pg.draw.rect(self.game.win, ROMEO , rect4, 100)
        
        rect5 = pg.Rect((9, 200, 9,80))  # (left,top,width,height) 
        pg.draw.rect(self.game.win, ROMEO , rect5, 100)
        
        rect6 = pg.Rect((190, 200, 9,80))  # (left,top,width,height) 
        pg.draw.rect(self.game.win, ROMEO , rect6, 100)    