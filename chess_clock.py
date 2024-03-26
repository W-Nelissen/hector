from colors import *
import pygame as pg
import time as t
from event_handler import Button
from chess_board import NOPLAYER, PLAYER1, PLAYER2

class PlayerClock(Button):
    def __init__(self,parent) -> None:
        Button.__init__(self,parent,0,0,0,0,"",0, game_style= "CLOCK")
        self.time_limit = 0
        self.countdown = False
        self.isticking = False
        self.clocktime = self.time_limit
        self.lastresume = t.time()

    def resumeClock(self):
        self.isticking = True
        self.lastresume = t.time()

    def getClockTime(self):
        if not self.isticking:
            return self.clocktime
        dt = t.time() - self.lastresume
        if self.countdown:
            return self.clocktime - dt
        else:
            return self.clocktime + dt

    def pauseClock(self):
        self.clocktime = self.getClockTime()
        self.isticking = False

    def resetClock(self):
        self.clocktime = self.time_limit      
        self.isticking = False

    def time_string(self):
        clocktime = int(self.getClockTime())
        h = clocktime // 3600
        m = (clocktime % 3600) // 60
        s = int(clocktime % 60)
        
        return f"{h:02d}:{m:02d}:{s:02d}"                

    def update_data(self):
        pass                

    def draw(self,win):
        pg.draw.rect(win,BLACK,self.rect,0)
        self.write_string(win, self.time_string(), WHITE, self.rect.centerx, self.rect.centery, "CENTER")

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

    def switchClock(self, player):
        if player == PLAYER1:
            self.player_clock1.resumeClock()
            self.player_clock2.pauseClock()
        else:
            self.player_clock2.resumeClock()
            self.player_clock1.pauseClock()

    def setMode(self):
        pass

    def resetClock(self):
        self.player_clock1.resetClock()
        self.player_clock2.resetClock()

    def draw(self,win):
        pg.draw.rect(win,B_burlywood,self.rect,0)
        pg.draw.rect(win,B_chocolate,self.rect,6)
        mid_x = self.rect.x + self.rect.width //2
        pg.draw.line(win,B_chocolate,(mid_x,self.rect.top),(mid_x,self.rect.bottom - 3),6)
        self.player_clock1.draw(win)
        self.player_clock2.draw(win)

