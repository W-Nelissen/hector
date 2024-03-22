from event_handler import Button
import pygame as pg
from colors import *
from chess_history import *

class ListBox(Button):
    def __init__(self, parent, rect, has_select=False, has_dragging=False, game_style="STDLIST"):
        super().__init__(parent, 0, 0, 0, 0, "", "", has_select, has_dragging, game_style)
        self.listobjects = None
        #self.r0 = 0
        self.rowheight = 20
        self.maxrows = rect.height // self.rowheight
        self.rect = rect
        self._rowrect = None
    
    def drawRow(self, win, i):
        self._rowrect = pg.Rect(self.rect.x, self.rect.y + i * self.rowheight, self.rect.width, self.rowheight)
        if i % 2 == 0:
            c = B_chocolate
        else:
            c = B_burlywood
        pg.draw.rect(win, c, self._rowrect)

    def draw(self, win):
        for i in range(self.maxrows):
            self.drawRow(win, i)

class ListBox_MoveHistory(ListBox):
    def __init__(self, parent, rect, h):
        super().__init__(parent, rect)
        self.h = h

    def drawRow(self, win, i):
        ListBox.drawRow(self, win, i)
        moves = self.h.moves
        if moves:
            if len(moves) > i*2:
                self.write_string(win, moves[i*2].get_string(), WHITE, self._rowrect.x + 6, self._rowrect.centery, "LEFT")
            if len(moves) > i*2 + 1:
                self.write_string(win, moves[i*2 + 1].get_string(), DKGREY, self._rowrect.right - 6, self._rowrect.centery, "RIGHT")
