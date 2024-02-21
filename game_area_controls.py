from game_area import GameArea
import pygame as pg
import colors
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


