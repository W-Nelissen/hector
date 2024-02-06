from game_area import GameArea
import pygame as pg

class GameAreaControls(GameArea):
    def __init__(self, game, r):
        GameArea.__init__(self, game, r)

    def draw(self):
        GameArea.draw(self)
        # Teken hier de controls
        # Save, Open, Quit, ...

