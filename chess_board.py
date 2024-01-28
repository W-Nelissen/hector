from colors import *
import chess_pieces as cp
import pygame as pg
class ChessBoard:
    """
    Het chessboard bevat schaakstukken. We beginnen met een lege array.
    Om snel te starten resetten we het bord bij initialisatie zodat er stukken opstaan
    """
    def __init__(self):
        # Een 8x8 matrix waar elk element overeen komt met een vierkantje op het bord
        self.squares = [[None for _ in range(8)] for _ in range(8)]
        # Een array van de stukken die op het bord staan
        self.pieces = []

        self.resetBoard()


    """
        omdat we later waarschijnlijk nog andere structuren aanpassen wanneer we een stuk toevoegen,
        verwijderen of verzetten, moeten alle wijzigingen via deze functies verlopen:
            ClearBoard
            AddPiece
            RemovePiece
            MovePiece
        Deze extra structuren zijn nog niet aanwezig en later ook redundant, 
        maar kunnen nodig zijn om de snelheid van de bordevaluatie te verbeteren
        
    """
    def ClearBoard(self):
        # Een 8x8 matrix maken waar elk vakje leeg is (None bevat)
        self.piecesMatrix = [[None for _ in range(8)] for _ in range(8)]

    def AddPiece(self, piece):
        self.pieces.append(piece)
        self.piecesMatrix[piece.pos[0]-1][piece.pos[1]-1] = piece

    def removePiece(self, piece):
        pass

    def resetBoard(self):
        # We vegen alle stukken van het bord
        self.ClearBoard()

        # We plaatsen alle zwarte stukken bovenaan
        self.AddPiece(cp.ChessPieceTower((8, 1), cp.CP_BLACK))
        self.AddPiece(cp.ChessPieceKnight((8, 2), cp.CP_BLACK))
        self.AddPiece(cp.ChessPieceBishop((8, 3), cp.CP_BLACK))
        self.AddPiece(cp.ChessPieceKing((8, 4), cp.CP_BLACK))
        self.AddPiece(cp.ChessPieceQueen((8, 5), cp.CP_BLACK))
        self.AddPiece(cp.ChessPieceBishop((8, 6), cp.CP_BLACK))
        self.AddPiece(cp.ChessPieceKnight((8, 7), cp.CP_BLACK))
        self.AddPiece(cp.ChessPieceTower((8, 8), cp.CP_BLACK))
        # Ook een rij pionnen
        for i in range(1, 8):
            self.AddPiece(cp.ChessPiecePawn((7, i), cp.CP_BLACK))

        # We plaatsen alle witte stukken onderaan
        self.AddPiece(cp.ChessPieceTower((1, 1), cp.CP_WHITE))
        self.AddPiece(cp.ChessPieceKnight((1, 2), cp.CP_WHITE))
        self.AddPiece(cp.ChessPieceBishop((1, 3), cp.CP_WHITE))
        self.AddPiece(cp.ChessPieceKing((1, 4), cp.CP_WHITE))
        self.AddPiece(cp.ChessPieceQueen((1, 5), cp.CP_WHITE))
        self.AddPiece(cp.ChessPieceBishop((1, 6), cp.CP_WHITE))
        self.AddPiece(cp.ChessPieceKnight((1, 7), cp.CP_WHITE))
        self.AddPiece(cp.ChessPieceTower((1, 8), cp.CP_WHITE))
        # Ook een rij witte pionnen
        for i in range(1, 8):
            self.AddPiece(cp.ChessPiecePawn((2, i), cp.CP_WHITE))


    def draw(self,win,r):
        """
        :param win: hierop tekenen we
        :param r: is de rechthoek waarbinnen we tekenen

        Teken bord: 2 opties,
                optie 1: een image die juist geplaatst is (eventueel herschalen)
                          er zit al een image in data/boards/
                optie 2: lijnen zelf tekenen en vierkanten opvullen met pg.draw.rect(win, color, rect
        """
