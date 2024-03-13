from event_handler import EventHandler
from colors import *
from game_constants import *
import chess_pieces as cp
import pygame as pg



# Een schaakbord heeft donkere en lichte vakjes
DARKSQUARE = 1
LIGHTSQUARE = 2


class BoardSquare(EventHandler):
    def __init__(self, parent, x, y): #x en y gaan van 1 tot 8
        EventHandler.__init__(self, parent)
        self.x = x
        self.y = y
        self.isValidMove = False
        if (self.x + self.y) % 2 == 0:
            self.type = LIGHTSQUARE
        else:
            self.type = DARKSQUARE
        self.piece = None

    def draw(self, win):
        if self.type == DARKSQUARE:
            c = B_chocolate
        elif self.type == LIGHTSQUARE:
            c = B_burlywood
        pg.draw.rect(win, c, self.rect)
        if self.isValidMove:
            #pg.draw.rect(win, GREEN, self.rect)
            s = pg.Surface((self.rect.width,self.rect.height), pg.SRCALPHA)
            s.fill((0,255,0,80))
            win.blit(s, (self.rect.x,self.rect.y))
 
    def drawPiece(self, win):
        if self.piece:
            self.piece.draw(win, self.rect)

    def setPiece(self, piece):
        self.piece = piece
        piece.setSquare(self)
    def MOUSEBUTTONDOWN(self, mouse_x, mouse_y):
        if self.piece:
            self.piece.MOUSEBUTTONDOWN(mouse_x, mouse_y)
    def MOUSEBUTTONUP(self, mouse_x, mouse_y):
        if self.piece:
            self.piece.MOUSEBUTTONUP(mouse_x, mouse_y)
    def MOUSEBUTTONMOVE(self, mouse_x, mouse_y):
        if self.piece:
            self.piece.MOUSEBUTTONMOVE(mouse_x, mouse_y)


class ChessBoard(EventHandler):
    """
    Het chessboard bevat vakjes (BoardSquare). 
    Een BoardSquare kan 1 schaakstuk bevatten (ChessPiece).
    """
    def __init__(self,parent):
        EventHandler.__init__(self, parent)
        self.margin_x = 20
        self.margin_y = 20
        self.size = 0
        self.rect = None

        # Een 8x8 matrix waar elk element overeen komt met een vierkantje op het bord
        self.squares = [[None for _ in range(8)] for _ in range(8)]  # Lege 8x8-matrix
        for x in range(8):
            for y in range(8):
                self.squares[x][y] = BoardSquare(self, x + 1, y + 1)

        # Wanneer de game area met het schaakbord wordt vergroot of verkleind moet de afmetingen van het schaakbord worden herrekend
        # We roepen die functie ook op bij de aanmaak van het schaakbord
        self.resize(pg.Rect(self.parent.rect))
        # Om snel te starten resetten we het bord bij initialisatie zodat er stukken opstaan
        self.resetBoard()

    def resize(self, r):
        """
        r: Rect waarbinnen het schaakbord moet worden getekend
        """
        if r.height - 2 * self.margin_y >= r.width - 2 * self.margin_x:
            self.size = r.width - 2 * self.margin_x
        else:
            self.size = r.height - 2 * self.margin_y
        self.size = 8 * (self.size // 8)
        self.rect = pg.Rect(r.left + (r.width-self.size)//2, r.top + self.margin_y, self.size, self.size)
        for x in range(8):
            for y in range(8):
                size = self.size // 8
                self.squares[x][y].rect.left = self.rect.left + x * size
                self.squares[x][y].rect.top = self.rect.bottom - (y+1) * size
                self.squares[x][y].rect.height, self.squares[x][y].rect.width = size, size

    def ClearBoard(self):
        pass

    def GetSquare(self, x, y):
        # We nummeren onze vierkantjes van 1-8,1-8
        # Maar arrays beginnen te tellen van 0
        # Returnt het BoardSquare (zie lijn 12) dat op die plaats op het bord ligt
        return self.squares[x - 1][y - 1]
    
    def isOnBoard(self, x, y):
        return 0 < x < 9 and 0 < y < 9
 
    def isValidMove(self, x1, y1, x2, y2):
        startsquare = self.GetSquare(x1, y1)
        endsquare = self.GetSquare(x2, y2)
        chesspiece = startsquare.piece
        if chesspiece is None:
            return False
        for move in chesspiece.possible_moves:
            repeat = True
            new_x = x1
            new_y = y1
            while repeat:
                repeat = chesspiece.repeat_moves
                if chesspiece.BW == cp.CP_WHITE:
                    new_x = new_x + move[0]
                    new_y = new_y + move[1]
                else:
                    new_x = new_x - move[0]
                    new_y = new_y - move[1]
                if self.isOnBoard(new_x, new_y):
                    square = self.GetSquare(new_x, new_y)
                    piece = square.piece
                    if square is endsquare:
                        if piece is None:
                            return True
                        elif not chesspiece.BW == piece.BW:
                            return True
                        else:
                            return False
                    elif piece:
                        repeat = False
                else:
                    repeat = False

    def showValidMoves(self, x0, y0):
        for x in range(8):
            for y in range(8):
                square=self.GetSquare(x,y)
                square.isValidMove = self.isValidMove(x0, y0, x, y)                    

    def AddPiece(self, x, y, piece):
        square = self.GetSquare(x, y)
        square.setPiece(piece)

    def removePiece(self, piece):
        pass

    def resetBoard(self):
        # We vegen alle stukken van het bord
        self.ClearBoard()

        # We plaatsen alle zwarte stukken bovenaan
        self.AddPiece( 1, 8, cp.ChessPieceTower(self,cp.CP_BLACK))
        self.AddPiece( 2, 8, cp.ChessPieceKnight(self,cp.CP_BLACK))
        self.AddPiece( 3, 8, cp.ChessPieceBishop(self,cp.CP_BLACK))
        self.AddPiece( 4, 8, cp.ChessPieceQueen(self,cp.CP_BLACK))
        self.AddPiece(5, 8, cp.ChessPieceKing(self,cp.CP_BLACK))
        self.AddPiece( 6, 8, cp.ChessPieceBishop(self,cp.CP_BLACK))
        self.AddPiece( 7, 8, cp.ChessPieceKnight(self,cp.CP_BLACK))
        self.AddPiece( 8, 8, cp.ChessPieceTower(self,cp.CP_BLACK))
        # Ook een rij pionnen
        for i in range(1, 9):
            self.AddPiece(i, 7, cp.ChessPiecePawn(self,cp.CP_BLACK))

        # We plaatsen alle witte stukken onderaan
        self.AddPiece(1, 1, cp.ChessPieceTower(self,cp.CP_WHITE))
        self.AddPiece(2, 1, cp.ChessPieceKnight(self,cp.CP_WHITE))
        self.AddPiece(3, 1, cp.ChessPieceBishop(self,cp.CP_WHITE))
        self.AddPiece(4, 1, cp.ChessPieceQueen(self,cp.CP_WHITE))
        self.AddPiece(5, 1, cp.ChessPieceKing(self,cp.CP_WHITE))
        self.AddPiece(6, 1, cp.ChessPieceBishop(self,cp.CP_WHITE))
        self.AddPiece(7, 1, cp.ChessPieceKnight(self,cp.CP_WHITE))
        self.AddPiece(8, 1, cp.ChessPieceTower(self,cp.CP_WHITE))
        # Ook een rij witte pionnen
        for i in range(1, 9):
            if i==4:
                self.AddPiece(i, 4, cp.ChessPiecePawn(self,cp.CP_WHITE))
            else:
                self.AddPiece(i, 2, cp.ChessPiecePawn(self,cp.CP_WHITE))


    def draw(self,win):
        #voorlopige rechthoek waar het schaakbord zal komen
        pg.draw.rect(win, RED, self.rect)
        pg.draw.rect(win,GREEN,(400,300,2,2))

        # Je moet nu de vakjes tekenen.
        # Je kan daartoe een dubbele for-loop gebruiken.
        # for x in range(8):
        #    for y in range(8):
        # Gebruik steeds de GetSquare(x,y) functie om een vakje te krijgen                 
        #       square=GetSquare(x,y)
        #       square.draw(win)             
        # Vervolgens moet je de schaakstukken tekenen.
        # Overloop de vakjes en teken het schaakstuk dat erop staat.

        for x in range(8):
            for y in range(8):
                square=self.GetSquare(x,y) # jullie waren hier vergeten om het keyword "self" toe te voegen
                square.draw(win)
                if square.piece:
                    square.piece.draw(win)
        for x in range(8):
            for y in range(8):
                square=self.GetSquare(x,y)
                if square.piece:
                    square.piece.draw_dragged(win)
        # probeer ook te begrijpen hoe het komt dat de squares juist getekend worden!

        
