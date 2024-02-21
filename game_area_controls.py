from game_area import GameArea
import pygame as pg
from colors import *

from evt_obj import EvtBtn as Button

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
        
        # tip 1: self.rect bevat de coördinaten van de linkerbovenhoek. Die kan je opslaan in een variabelen om er verder mee te rekenen
        # vb/ 
        # left = self.rect[0]
        # top = self.rect[1]
        # pg.draw.rect(self.game.win,BLACK,(self.rect[0],self.rect[1],10,10))


        # tip 2: gebruik de EvtBtn klasse in evt_obj.py (zie ook import hierboven)
        # ga eens op zoek naar de definitie van die klasse 
        # button = Button(self,500,500,100,100,"test","test")
        # button.draw(self.game.win)
        



