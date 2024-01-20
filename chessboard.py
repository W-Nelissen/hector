import pygame
import chess

class ChessBoard(object):
    def __init__(self,left,top,width):
        self.left=left
        self.top=top
        self.width=width
        self.height=width
        self.rect = (left,top,width,width)

    def draw_background(self,window):
        """Draws the background of the chess board"""
        # This shows how to draw a rectangle on the screen
        color="grey"
        rectangle = pygame.Rect(self.left,self.top,self.width,self.heigth)
        pygame.draw.rect(window,color,rectangle)
        # verander deze code zodat je in plaats van 1 rect in 1 kleur, 64 rects in de juiste kleuren tekent


        
    def draw_pieces(self,window,position):
        """Draws the pieces on the board"""
        # Hier tonen we hoe je een foto van een schaakstuk op het scherm zet
        piece = pygame.image.load("./assets/K-black.png")
        window.blit(piece,(self.left,self.top))
        # verander deze code zodat je in plaats van 1 schaakstuk, alle juiste schaakstukken op het scherm zet
        # probeer dit eerst met eender welke positie van het bord
        # zorg daarna dat je rekening houdt met de positie die meegegeven is in het argument "position"