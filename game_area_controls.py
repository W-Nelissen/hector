from game_area import GameArea
import pygame as pg
from colors import *

from event_handler import Button

LTRED = (252, 50, 50)
DRED = (191, 17, 17)
# feedback: definieer alle kleuren mee in de file colors.py en gebruik dan die kleuren
# op die manier zorg je ervoor dat iedereen dezelfde kleuren gebruikt -> leesbaardere code

class GameAreaControls(GameArea):
    def __init__(self, game, r):
        GameArea.__init__(self, game, r)

    def draw(self):
        GameArea.draw(self)
        # Teken hier de controls
        # Save, Open, Quit, ...
        rect = pg.Rect((645, 45, 150, 70))
        pg.draw.rect(self.game.win, LTRED, rect, 0)
        pg.draw.rect(self.game.win, DRED, rect,4)
        pg.draw.line(self.game.win,DRED, (rect.left, rect.top), (rect.right, rect.bottom), 4)
        
        # tip 1: self.rect bevat de coördinaten van de linkerbovenhoek.
        # Je kan relatieve coordinaten gebruiken t.o.v die bovenhoek via self._x() en self._y()
        # vb/ 
        # x = self._x(20)
        # y = self._y(10)
        # pg.draw.rect(self.game.win,BLACK,(x,y,200,50))

        # tip 2: gebruik de Button klasse in event_handler.py (zie ook import hierboven)
        # ga eens op zoek naar de definitie van die klasse 
        # button = Button(self,500,500,100,100,"test","test") (steek dit in de __init__)
        # button.draw(self.game.win)
        



