from game_area import GameArea
import pygame as pg
from game_constants import *
from colors import *

from event_handler import Button



class GameAreaControls(GameArea):
    def __init__(self, game, r):
        GameArea.__init__(self, game, r)
        self.startbutton = Button(self, self._x(10), self._y(10), BUTTON_WIDTH, BUTTON_HEIGHT, "start", "launch_start" )
        self.loadbutton = Button(self, self._x(20 + BUTTON_WIDTH), self._y(10), BUTTON_WIDTH, BUTTON_HEIGHT, "load", "load_game" )
        self.loadbutton.enabled = False
        self.savebutton = Button(self, self._x(30 + 2 * BUTTON_WIDTH), self._y(10), BUTTON_WIDTH, BUTTON_HEIGHT, "save", "save_game" )
        self.savebutton.enabled = False

    def draw(self):
        GameArea.draw(self)
        # Teken hier de controls
        # Save, Open, Quit, ...
        # rect = pg.Rect((645, 45, 150, 70))
        # pg.draw.rect(self.game.win, LTRED, rect, 0)
        # pg.draw.rect(self.game.win, DRED, rect,4)
        # pg.draw.line(self.game.win,DRED, (rect.left, rect.top), (rect.right, rect.bottom), 4)
        # pg.draw.line(self.game.win,DRED, (rect.right, rect.top), (rect.left, rect.bottom), 4)

        
        self.startbutton.draw(self.game.win)
        self.loadbutton.draw(self.game.win)
        self.savebutton.draw(self.game.win)

    def execute_action(self, action):
        pg.draw.line(self.game.win,B_brown, (500,200), (1000,300), 4)
        # in iets anders dan self.draw mag je niets tekenen, omdat het de volgende frame overtekend wordt
        pg.display.update




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
        



