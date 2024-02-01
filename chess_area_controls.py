from game_area import GameArea
import pygame as pg
pg.init()
pg.font.init()
pg.font.get_fonts()
pg.font.SysFont(None,30, bold=False, italic=False)
pg.font.Font.render()
win = pg.display.set_mode((800,500))
myrectangle = pg.Rect((40,80,200,75))
white = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 0, 255)
CYAN = (0, 255, 255)
BURLYWOOD = (222, 184, 135)
CHOCOLATE = (210, 105, 30)
pg.draw.rect( win , white, myrectangle, 4)

pg.draw.circle(win,CYAN, (myrectangle.bottomleft), 20, 6 )
pg.draw.circle(win, RED,(myrectangle.topright), 50, 0 )
pg.draw.circle(win,CYAN, (myrectangle.topright), 50, 6 )

pg.display.update()
class GameAreaControls(GameArea):
    def __init__(self, game, r):
        GameArea.__init__(self, game, r)

    def draw(self):
        GameArea.draw(self)
         # Teken hier de controls
        # Save, Open, Quit, ...
#moet ik de window opnieuw definiëren ook al is het in main.py al gebeurd?        


keep_running = True
while keep_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            keep_running = False

pg.quit()