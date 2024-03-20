from event_handler import EventHandler
from colors import *
from game_constants import *
import chess_pieces as cp
import pygame as pg
import handle_sound as sound
from chess_history import *

# Een schaakbord heeft donkere en lichte vakjes
DARKSQUARE = 1
LIGHTSQUARE = 2


class BoardSquare(EventHandler):
    def __init__(self, parent, x, y): #x en y gaan van 0 tot 7
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
            if self.piece:
                s.fill((255,0,255,80))
            else:
                s.fill((0,255,0,80))
            win.blit(s, (self.rect.x,self.rect.y))
        if self.piece:
            if self.piece.isPressed:
               s = pg.Surface((self.rect.width,self.rect.height), pg.SRCALPHA)
               s.fill((0,0,255,80))
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

PLAYER1 = 1
PLAYER2 = 2
class ChessBoard(EventHandler):
    """
    Het chessboard bevat vakjes (BoardSquare). 
    Een BoardSquare kan 1 schaakstuk bevatten (ChessPiece).
    """
    def __init__(self,parent):
        EventHandler.__init__(self, parent)
        self.flipped = False
        self.flip = False
        self.h = H_Move()
        self.margin_x = 20
        self.margin_y = 20
        self.size = 0
        self.rect = None
        self.silent = False
        # Een 8x8 matrix waar elk element overeen komt met een vierkantje op het bord
        self.squares = [[BoardSquare(self,x,y) for y in range(8)] for x in range(8)]  # Lege 8x8-matrix
        self.player = None
        self.turn_nr = 0
        self.move_nr = 0
        # Wanneer de game area met het schaakbord wordt vergroot of verkleind moet de afmetingen van het schaakbord worden herrekend
        # We roepen die functie ook op bij de aanmaak van het schaakbord
        self.resize()
        # Om snel te starten resetten we het bord bij initialisatie zodat er stukken opstaan
        self.resetBoard()

    def startNextMove(self):
        self.switchPlayer()
        self.move_nr +=1
        if self.player == PLAYER1:
            self.turn_nr +=1

    def switchPlayer(self):
        if self.player == PLAYER1:
            self.player = PLAYER2
        else:
            self.player = PLAYER1
    def ResetMoves(self):
        self.player = PLAYER1
        self.turn_nr = 1
        self.move_nr = 1
    def resize(self):
        rect = pg.Rect(self.parent.rect)
        infomargin = 30
        r = pg.Rect(rect.x, rect.y + infomargin, rect.width, rect.height - infomargin)
        if r.height - 2 * self.margin_y >= r.width - 2 * self.margin_x:
            self.size = r.width - 2 * self.margin_x
        else:
            self.size = r.height - 2 * self.margin_y
        self.size = 8 * (self.size // 8)
        self.rect = pg.Rect(r.left + (r.width-self.size)//2, r.top + self.margin_y, self.size, self.size)
        for x in range(8):
            for y in range(8):
                size = self.size // 8
                if self.flipped:
                    srect=self.Square(7-x,7-y).rect    
                else:
                    srect=self.Square(x,y).rect
                srect.left = self.rect.left + x * size
                srect.top = self.rect.bottom - (y+1) * size
                srect.height, srect.width = size, size
    
    def Square(self,x,y):
        return self.squares[x][y]
    
    def flipBoard(self):
        self.flipped = not self.flipped
        self.resize()

    def ClearBoard(self):
        for x in range(8):
            for y in range(8):
                # Garbage collection ruimt het huidige piece op
                self.Square(x,y).piece = None

    def isOnBoard(self, x, y):
        return -1 < x < 8 and -1 < y < 8
 
    def isValidMove(self, x1, y1, x2, y2):
        validmove = False
        startsquare = self.Square(x1, y1)
        endsquare = self.Square(x2, y2)
        chesspiece = startsquare.piece
        if chesspiece is None:
            return False
        for move in chesspiece.possible_moves:
            new_x = x1
            new_y = y1
            steps = chesspiece.getRepeat()
            while steps > 0:
                steps -= 1
                if chesspiece.BW == cp.CP_WHITE:
                    new_x = new_x + move[0]
                    new_y = new_y + move[1]
                else:
                    new_x = new_x - move[0]
                    new_y = new_y - move[1]
                if self.isOnBoard(new_x, new_y):
                    square = self.Square(new_x, new_y)
                    piece = square.piece
                    if square is endsquare:
                        if piece is None:
                            validmove = True
                        elif not chesspiece.BW == piece.BW:
                            validmove = chesspiece.moveIsCapture
                        else:
                            validmove =  False
                    elif piece:
                        steps = False
                else:
                    steps = False
        if chesspiece.capture_moves:
            for move in chesspiece.capture_moves:
                new_x = x1
                new_y = y1
                if chesspiece.BW == cp.CP_WHITE:
                    new_x = new_x + move[0]
                    new_y = new_y + move[1]
                else:
                    new_x = new_x - move[0]
                    new_y = new_y - move[1]
                if self.isOnBoard(new_x, new_y):
                    square = self.Square(new_x, new_y)
                    piece = square.piece
                    if square is endsquare:
                        if piece is not None:
                            if not chesspiece.BW == piece.BW:
                                validmove = True
        return validmove

    def showValidMoves(self, x0, y0):
        for x in range(8):
            for y in range(8):
                square=self.Square(x,y)
                square.isValidMove = self.isValidMove(x0, y0, x, y)                    

    def clearValidMoves(self):
        for x in range(8):
            for y in range(8):
                square=self.Square(x,y)
                square.isValidMove = False

    def AddPiece(self, strPos, piece):
        x="abcdefgh".find(strPos[0])
        y="12345678".find(strPos[1])
        square = self.Square(x, y)
        square.setPiece(piece)

    def removePiece(self, square):
        # Garbage collection ruimt normaal het piece op
        # Later kunnen we beslissen dat het piece naast het bord blijft bestaan
        # We moeten het dus leeg maken
        square.piece.rect = pg.Rect(0,0,0,0)
        square.piece.square = None
        # square heeft geen piece meer
        square.piece = None

    def movePiece(self, startsquare, endsquare):
        if endsquare.piece:
            self.removePiece(endsquare)
        endsquare.setPiece(startsquare.piece)
        startsquare.piece = None
        if not self.silent:
            sound.play_mp3("assets/sounds/move-self.mp3")
        self.h.add(self.turn_nr, self.move_nr, startsquare, endsquare)
        if self.flip:
            self.flipBoard()
        self.startNextMove()

    def resetBoard(self):
        # We vegen alle stukken van het bord
        self.ClearBoard()
        self.ResetMoves()
        # We plaatsen alle zwarte stukken bovenaan
        self.AddPiece( "a8", cp.ChessPieceTower(self,cp.CP_BLACK))
        self.AddPiece( "b8", cp.ChessPieceKnight(self,cp.CP_BLACK))
        self.AddPiece( "c8", cp.ChessPieceBishop(self,cp.CP_BLACK))
        self.AddPiece( "d8", cp.ChessPieceQueen(self,cp.CP_BLACK))
        self.AddPiece( "e8", cp.ChessPieceKing(self,cp.CP_BLACK))
        self.AddPiece( "f8", cp.ChessPieceBishop(self,cp.CP_BLACK))
        self.AddPiece( "g8", cp.ChessPieceKnight(self,cp.CP_BLACK))
        self.AddPiece( "h8", cp.ChessPieceTower(self,cp.CP_BLACK))
        # Ook een rij pionnen
        for i in range(8):
            self.AddPiece("abcdefgh"[i]+"7", cp.ChessPiecePawn(self,cp.CP_BLACK))

        # We plaatsen alle witte stukken onderaan
        self.AddPiece( "a1", cp.ChessPieceTower(self,cp.CP_WHITE))
        self.AddPiece( "b1", cp.ChessPieceKnight(self,cp.CP_WHITE))
        self.AddPiece( "c1", cp.ChessPieceBishop(self,cp.CP_WHITE))
        self.AddPiece( "d1", cp.ChessPieceQueen(self,cp.CP_WHITE))
        self.AddPiece( "e1", cp.ChessPieceKing(self,cp.CP_WHITE))
        self.AddPiece( "f1", cp.ChessPieceBishop(self,cp.CP_WHITE))
        self.AddPiece( "g1", cp.ChessPieceKnight(self,cp.CP_WHITE))
        self.AddPiece( "h1", cp.ChessPieceTower(self,cp.CP_WHITE))
        # Ook een rij witte pionnen
        for i in range(8):
            self.AddPiece("abcdefgh"[i]+"2", cp.ChessPiecePawn(self,cp.CP_WHITE))
        self.flipped = False
        self.resize()

    def draw(self,win):

        str_aan_zet = "Zwart is aan zet"
        c = BLACK
        if self.player == PLAYER1:
            str_aan_zet = "Wit is aan zet"
            c = WHITE
        self.write_string(win, str_aan_zet, c, self.rect.x, self.rect.top - 20, "LEFT")

        for x in range(8):
            for y in range(8):
                square=self.Square(x,y)
                square.draw(win)
                if square.piece:
                    square.piece.draw(win)
        for x in range(8):
            for y in range(8):
                square=self.Square(x,y)
                if square.piece:
                    square.piece.draw_dragged(win)
        
