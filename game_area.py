from game_constants import *
from colors import *
from event_handler import EventHandler
import pygame as pg

class GameArea(EventHandler):
    """
    Generieke klasse die een deel van het scherm afbakent
    -  Alle schermgebieden (game areas) worden hiervan afgeleid
    -  Afgeleid van EvtentHandler zodat het user-events worden doorgegeven aan de areas
    """
    def __init__(self, game, r):
        # :param game: wordt mee doorgegeven zodat we toegang hebben tot alle spelparameters en structuren
        # :param r: geeft de rechthoek aan waarbinnen we tekenen (clippen indien nodig)
        EventHandler.__init__(self, game)
        self.game = game
        self.rect = pg.Rect(r)


    def frame_area(self):
        # Hier kan je alles tekenen dat gemeenschappelijk is voor een game area
        # - Kader
        # - Achtergrond patroon

        # Teken een kader rond de game area
        pg.draw.rect(self.game.win, B_chocolate, self.rect,4)

    def draw(self):
        # Indien de afgeleide klasse nog geen draw(self) methode heeft wordt een frame getekend
        # Indien de afgeleide klasse wel een draw(self) methode heeft 
        #    kan je daar GameArea.draw(self) oproepen voor je extra dingen tekent
        self.frame_area()
