from colors import *
from game_constants import *
import chess_pieces as cp
import pygame as pg

DARKSQUARE = 1
LIGHTSQUARE = 2

class BoardSquare:
    def __init__(self, x, y): #x en y gaan van 1 tot 8
        self.x = x
        self.y = y
        self.rect = pg.Rect(0, 0, 0, 0)
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

    def drawPiece(self, win):
        if self.piece:
            self.piece.draw(win, self.rect)

    def setPiece(self, piece):
        self.piece = piece
        piece.square = self


class ChessBoard:
    """
    Het chessboard bevat schaakstukken. We beginnen met een lege array.
    Om snel te starten resetten we het bord bij initialisatie zodat er stukken opstaan
    """
    def __init__(self):
        self.margin_x = 20
        self.margin_y = 20
        self.size = 0
        self.rect = None

        # Een 8x8 matrix waar elk element overeen komt met een vierkantje op het bord
        self.squares = [[None for _ in range(8)] for _ in range(8)]  # Lege 8x8-matrix
        for x in range(8):
            for y in range(8):
                self.squares[x][y] = BoardSquare(x + 1, y + 1)
        self.resize(pg.Rect(GAME_RECT))
        # Een array van de stukken die op het bord staan
        #self.pieces = []

        self.resetBoard()

    def resize(self, r):
        if r.height - 2 * self.margin_y >= r.width - 2 * self.margin_x:
            self.size = r.width - 2 * self.margin_x
        else:
            self.size = r.height - 2 * self.margin_y
        self.rect = pg.Rect(r.left + self.margin_x, r.top + self.margin_y, self.size, self.size)
        for x in range(8):
            for y in range(8):
                size = self.size // 8
                self.squares[x][y].rect.left = self.rect.left + x * size
                self.squares[x][y].rect.top = self.rect.top + y * size
                self.squares[x][y].rect.height, self.squares[x][y].rect.width = size, size

    def ClearBoard(self):
        # Een 8x8 matrix maken waar elk vakje leeg is (None bevat)
        #self.squares = [[None for _ in range(8)] for _ in range(8)]
        pass

    def GetSquare(self, x, y):
        return self.squares[x - 1][y - 1]
    def AddPiece(self, x, y, piece):

        square = self.GetSquare(x, y)
        square.setPiece(piece)

    def removePiece(self, piece):
        pass

    def resetBoard(self):
        # We vegen alle stukken van het bord
        self.ClearBoard()

        # We plaatsen alle zwarte stukken bovenaan
        self.AddPiece( 1, 8, cp.ChessPieceTower(cp.CP_BLACK))
        self.AddPiece( 2, 8, cp.ChessPieceKnight(cp.CP_BLACK))
        self.AddPiece( 3, 8, cp.ChessPieceBishop(cp.CP_BLACK))
        self.AddPiece( 4, 8, cp.ChessPieceQueen(cp.CP_BLACK))
        self.AddPiece(5, 8, cp.ChessPieceKing(cp.CP_BLACK))
        self.AddPiece( 6, 8, cp.ChessPieceBishop(cp.CP_BLACK))
        self.AddPiece( 7, 8, cp.ChessPieceKnight(cp.CP_BLACK))
        self.AddPiece( 8, 8, cp.ChessPieceTower(cp.CP_BLACK))
        # Ook een rij pionnen
        for i in range(1, 9):
            self.AddPiece(i, 7, cp.ChessPiecePawn(cp.CP_BLACK))

        # We plaatsen alle witte stukken onderaan
        self.AddPiece(1, 1, cp.ChessPieceTower(cp.CP_WHITE))
        self.AddPiece(2, 1, cp.ChessPieceKnight(cp.CP_WHITE))
        self.AddPiece(3, 1, cp.ChessPieceBishop(cp.CP_WHITE))
        self.AddPiece(4, 1, cp.ChessPieceQueen(cp.CP_WHITE))
        self.AddPiece(5, 1, cp.ChessPieceKing(cp.CP_WHITE))
        self.AddPiece(6, 1, cp.ChessPieceBishop(cp.CP_WHITE))
        self.AddPiece(7, 1, cp.ChessPieceKnight(cp.CP_WHITE))
        self.AddPiece(8, 1, cp.ChessPieceTower(cp.CP_WHITE))
        # Ook een rij witte pionnen
        for i in range(1, 9):
            self.AddPiece(i, 2, cp.ChessPiecePawn(cp.CP_WHITE))


    def draw(self,win,r):
        self.resize(r)
        pg.draw.rect(win, RED, self.rect)

        for x in range(8):
            for y in range(8):
                self.squares[x][y].draw(win)
        for x in range(8):
            for y in range(8):
                if self.squares[x][y].piece:
                    self.squares[x][y].piece.draw(win)
