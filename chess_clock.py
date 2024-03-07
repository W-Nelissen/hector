from colors import *
import pygame as pg
import time as t
from event_handler import Button

class PlayerClock(Button):
    def __init__(self,parent) -> None:
        Button.__init__(self,parent,0,0,0,0,"",0)
        self.paused = True
        self.period = 0
        self.t0 = t.time()

    def resetClock(self):
        self.t0 = t.time()
        pass

    def time_string():
        return "05:00:00"                

    def update_data():
        pass                

    def draw(self,win):
        pg.draw.rect(win,BLACK,self.rect,0)

class ChessClock(Button):
    def __init__(self, parent) -> None:
        Button.__init__(self,parent,0,0,0,0,"",0)
        self.margin_x = 5
        self.margin_y = 5
        self.player_clock1 = PlayerClock(self)
        self.player_clock2 = PlayerClock(self)
        self.resize(pg.Rect(self.parent.rect))
        
    def resize(self,r):
        self.rect = pg.Rect(r.left + self.margin_x, r.top + self.margin_y, r.width - 2 * self.margin_x, 100)
        self.player_clock1.rect = pg.Rect(self.rect.x + 12, self.rect.y + 12, self.rect.width // 2 - 21, self.rect.height - 24)
        self.player_clock2.rect = pg.Rect(self.rect.x + self.rect.width // 2 + 9, self.rect.y + 12, self.rect.width // 2 - 21, self.rect.height - 24)

    def setMode(self):
        pass

    def resetClock(self, clockNr):
        pass

    def draw(self,win):
        pg.draw.rect(win,B_burlywood,self.rect,0)
        pg.draw.rect(win,B_chocolate,self.rect,6)
        mid_x = self.rect.x + self.rect.width //2
        pg.draw.line(win,B_chocolate,(mid_x,self.rect.top),(mid_x,self.rect.bottom - 3),6)
        self.player_clock1.draw(win)
        self.player_clock2.draw(win)

