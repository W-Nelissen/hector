"""
Om te kunnen tekenen op een window hebben we een externe library of package nodig.
Wij kiezen voor PYGAME (je zal pygame eerst moeten installeren voor je deze tutorial doet)
PYGAME zorgt voor:
    Het openen van een window met bepaalde grootte en titel(caption)
    Tekenen van lijnen en figuren (al dan niet opgevuld)
    Opladen, herschalen en tekenen van images (bmp,png,jpeg,...)
    Opvangen van user-events zoals mousedown, mousemove,...

Tutorial-pygame-deel-2: Tekenen van lijnen en figuren
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

# Om dingen te tekenen spreken we het object :draw: van pygame aan.
# Het object :draw: werd aangemaakt tijdens pg.init()
# Het object :draw: heeft tekenroutines

# Tekenroutine 1: teken een rechthoek met de functie pg.draw.rect
#    pg.draw.rect(surface, color, rect, width=0)
#        :surface: Het oppervlak waarop je wilt tekenen, dus :win:
#        :color: de kleur waarin je wil tekenen, bvb RED
#        :rect: de coordinaten van de rechthoek, (left,top,width,height)
#     Rechthoeken: We gebruiken geen standaard rechthoeken, maar pygame recthoeken
#         rect = (left,top,width,height) is een standaard rechthoek, maar heeft weinig mogelijkheden
#         rect = pg.Rect(left,top,width,height) zet die standaard rechthoek om naar een OBJECT
#            Nu kan je rect.top, rect.left, rect.width, rect.height, rect.bottom, rect. right gebruiken
# Teken een rode rechthoek met lijndikte 4
rect1 = pg.Rect((40, 80, 200, 75))  # (left,top,width,height)
pg.draw.rect(win, RED, rect1, 4)

# Tekenroutine 2: teken een lijn met de functie pg.draw.line



pg.draw.line(win, GREEN, (rect1.left, rect1.top), (rect1.right, rect1.bottom))
# We tekenen een cirkel met straal 45, rond de rechteronderhoek van de rectangle, met dikte 3
pg.draw.circle(win, BLUE, (rect1.right, rect1.bottom), 45, 3)

# Alles wordt getekend op een onzichtbaar venster
# pg.display.update() kopieert alles naar het zichtbare scherm in 1 stap
pg.display.update()

keep_running = True
while keep_running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            keep_running = False

# Als het game klaar is roep je best pg.quit() op zodat alle geheugen wordt vrijgegeven
pg.quit()