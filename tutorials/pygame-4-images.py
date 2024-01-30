"""
Om te kunnen tekenen op een window hebben we een externe library of package nodig.
Wij kiezen voor PYGAME (je zal pygame eerst moeten installeren voor je deze tutorial doet)
PYGAME zorgt voor:
    -Het openen van een window met bepaalde grootte en titel(caption)
    -Tekenen van lijnen en figuren (al dan niet opgevuld)
    -Opladen, herschalen en tekenen van images (bmp,png,jpeg,...)
    -Opvangen van user-events zoals mousedown, mousemove,...

Tutorial-pygame-deel-4: werken met images
"""

import pygame as pg
pg.init()
win = pg.display.set_mode((800, 600))
pg.display.set_caption("Hector Chess - Sint-Pieterscollege, Jette")

# Voordat we beginnen met tekenen bepalen we de kleuren die we gaan gebruiken
# Constanten altijd in hoofdletters
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 0, 255)
CYAN = (0, 255, 255)
BURLYWOOD = (222, 184, 135)
CHOCOLATE = (210, 105, 30)

# Om een image te tekenen moeten we het bestand eerst opladen
# Hiervoor gebruiken het pygame object :image:
# Dit object heeft een functie pg.image.load
# Omdat de tutorial in de folfer tutorials staat, begint het pad met "../"
queen_image = pg.image.load("./assets/pieces/W_Queen.png")

# Eerst kleuren we een vierkantje (alsof het een vakje is van een schaakbord)
rect1 = pg.Rect((100, 240, 42, 42))  # (left,top,width,height)
pg.draw.rect(win,CHOCOLATE , rect1, 0)  # Eerst de achtergrond
# Herinner dat :win: een object is met eigen functies
# We gebruiken de :win.blit(image,rect) functie om de pixels van het image te copieren naar een recthoek
win.blit(queen_image, rect1)

# We kunnen dit herhalen met een kleiner vakje, maar dan is de image te groot.
# pygame heeft een object :pg.transform: dat images kan transformeren.
# De belangrijkste functie van :pg.transform: is :pg.transform.scale(image,(width, height)):
# We maken een kleine rechthoek met (width=32,height=32) en tekenen die
rect1 = pg.Rect((180, 260, 32, 32))  # (left,top,width,height)
pg.draw.rect(win, CHOCOLATE, rect1,0)  # Eerst de achtergrond
# We scalen onze image naar (width=32,height=32)
scaled_queen_image = pg.transform.scale(queen_image,(32, 32))
# Nu tekenen we de rechthoek, en blitten we ons nieuw aangemaakte kleinere image naar die rechthoek
win.blit(scaled_queen_image, rect1)

pg.display.update()


keep_running = True
while keep_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            keep_running = False

# Als het game klaar is roep je best pg.quit() op zodat alle geheugen wordt vrijgegeven
pg.quit()
