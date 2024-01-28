from game_area import GameArea
from evt_obj import *

class ChessSquare(EvtBtn):
    def __init__(self, x, y, w, h):
        EvtBtn.__init__(self, x, y, w, h, "", 0, False, False)

    def draw(self, win):
        if self.isWithin:
            pg.draw.rect(win, B_burlywood, self.rect, 0)
        else:
            pg.draw.rect(win, B_rosybrown, self.rect, 0)
class Horse(EvtBtn):
    def __init__(self, parent, x, y):
        EvtBtn.__init__(self, x, y, 44, 44, "", 0,  False, True)
        self.horse_image = pg.image.load("assets/pieces/W_Knight.png")
        self.horse_image_opacity = pg.image.load("assets/pieces/W_Knight.png").convert_alpha()
        opacity = 100  # Opaciteitswaarde tussen 0 (transparant) en 255 (ondoorzichtig)
        self.horse_image_opacity.set_alpha(opacity)
        self.parent = parent
    def getOffsetRect(self, dx, dy):
        return pg.Rect(self.rect.left + dx, self.rect.top + dy, self.rect.width, self.rect.height)

    def MOUSEBUTTONUP(self, mouse_x, mouse_y):
        if self.isPressed:
            self.parent.checkMove(self)
        EvtBtn.MOUSEBUTTONUP(self, mouse_x, mouse_y)

    def draw(self, win):
        bg_color = BLUE
        fg_color = RED
        txt_color = RED
        if self.isPressed:
            win.blit(self.horse_image_opacity, self.getOffsetRect(self.x2 - self.x1, self.y2 - self.y1))
        else:
            win.blit(self.horse_image, self.rect)

class GameAreaSANDBOX(GameArea):
    def __init__(self, game, r):
        GameArea.__init__(self, game, r)
        self.test_button = EvtBtn(self._x(10), self._y(10), self.rect.width - 20, 40, "Klik mij", 1)
        self.evtObjects.append(self.test_button)

        self.testSquare1 = ChessSquare(self._x(10), self._y(200), 44,44)
        self.evtObjects.append(self.testSquare1)

        self.testSquare2 = ChessSquare(self._x(80), self._y(200),44,44)
        self.evtObjects.append(self.testSquare2)

        self.horse = Horse(self, self._x(10), self._y(200))
        self.evtObjects.append(self.horse)

    def checkMove(self, chessPiece):
        if self.testSquare1.isWithin:
            chessPiece.rect.x = self.testSquare1.rect.x
        elif self.testSquare2.isWithin:
            chessPiece.rect.x = self.testSquare2.rect.x

    def draw(self):
        GameArea.draw(self)
        for obj in self.evtObjects:
            obj.draw(self.game.win)
