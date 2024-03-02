from game_area import GameArea
import pygame as pg
pg.init()
win = pg.display.set_mode((1200, 600))

# tip: zet alles wat je wil tekenen in de draw functie
# wat doet dit hier?
BROWN= ( 132, 94, 66)
rect1 = pg.Rect((40, 80, 200, 75))  # (left,top,width,height)
pg.draw.rect(win, BROWN , rect1, 4)



class GameAreaPlayers(GameArea):
    """
   Dit is de game area waar alle spelerinformatie wordt getoond 
   player1: name, type, timer, ...
   player2: name, type, timer, ...
   """
    def __init__(self, game, r):
        GameArea.__init__(self, game, r)

    def draw(self):
        GameArea.draw(self)


        JULIET = (188,143,143 )
        ROMEO= (177,102,102)
        # tip: definieer je kleuren in de file colors.py en gebruik die kleuren
        # op die manier zorg je ervoor dat iedereen dezelfde kleuren gebruikt -> leesbare code

        rect1 = pg.Rect((5, 200, 200, 75))  # (left,top,width,height) 
        pg.draw.rect(self.game.win, JULIET , rect1, 100)
        
        rect2 = pg.Rect((5, 200, 200, 50))  # (left,top,width,height) 
        pg.draw.rect(self.game.win, ROMEO , rect2, 100)

        # tip 2: self.rect bevat de coördinaten van de linkerbovenhoek.
        # Je kan relatieve coordinaten gebruiken t.o.v die bovenhoek via self._x() en self._y()
        # vb/ 
        # x = self._x(20)
        # y = self._y(10)
        # pg.draw.rect(self.game.win,BLACK,(x,y,200,50))

        