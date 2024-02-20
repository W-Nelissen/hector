from game_area import GameArea
import pygame as pg
pg.init()
import colors






class GameAreaControls(GameArea):
    def __init__(self, game, r):
        GameArea.__init__(self, game, r)

    def draw(self):
        GameArea.draw(self)
        rect2 = pg.Rect((40,80,70,67))
        pg.draw.rect(self.game.win, colors.RED, rect2 , 5)
        # Teken hier de controls
        # Save, Open, Quit, ...



