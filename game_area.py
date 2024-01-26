from game_constants import *
from colors import *
from evt_obj import EvtObj
import pygame as pg

class GameArea(EvtObj):
    """
    Generieke klasse die een deel van het scherm afbakend
    Alle schermgebieden worden hiervan afgeleid
    GameArea is afgeleid van EvtObj zodat het user-events kan ontvangen
    """
    def __init__(self, game, r):
        # :param game: wordt mee doorgegeven zodat we toegang hebben tot alle spelparameters en structuren
        # :param r: geeft de rechthoek aan waarbinnen we tekenen (clippen indien nodig)
        EvtObj.__init__(self)
        self.game = game
        self.rect = pg.Rect(r)

    def frame_area(self):
        # Tekent een kader rond de game area
        pg.draw.rect(self.game.win, BLUE, self.rect,4)

    def _x(self, x):
        return self.rect.left + x

    def _y(self, y):
        return self.rect.top + y

    def draw(self):
        # Indien de afgeleide klasse nog geen draw(self) methode heeft wordt een frame getekend
        self.frame_area()
