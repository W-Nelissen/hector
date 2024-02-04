from colors import *
import pygame as pg


CP_WHITE = 1
CP_BLACK = 2
class ChessPiece:
    def __init__(self,pos, black_or_white):
        # positie van het schaakstuk (1-8,1-8)
        self.pos = pos
        # een generiek stuk heeft nog geen moves, elk schaakstuk moet dat zelf invullen
        self.possible_moves = []
        self.extra_moves = []
        self.capture_moves = []
        self.extra_capture_moves = []
        self.repeat_moves = False
        self.BW = black_or_white

    def draw(self,win,square_width,x,y):
        # Teken stuk, square_width = de afmeting van het vakje en de positie
        # De positie is in pixels en moet worden doorgegeven
        # Je kan images gebruiken uit assets/pieces/
        # Of je laadt zelf images op in assets/pieces/
        pass

class ChessPieceKing(ChessPiece):
    def __init__(self,pos, black_or_white):
        ChessPiece.__init__(self, pos, black_or_white)
        # Koning mag maar 1 stapje zetten, dus repeat_moves = False
        self.repeat_moves = False
        # Alle mogelijke moves, zonder rekening te houden met het bord
        self.possible_moves=[(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,-1),(0,-1),(1,-1)]

class ChessPieceQueen(ChessPiece):
    def __init__(self, pos, black_or_white):
        ChessPiece.__init__(self, pos, black_or_white)
        # Koningin mag maar meerde stapjes zetten, dus repeat_moves = True
        self.repeat_moves = True
        # Alle mogelijke moves, zonder rekening te houden met het bord
        # Dus hetzelfde als bij de Koning
        self.possible_moves = [(1, 0), (1, 1), (0, 1), (-1, -1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

class ChessPieceKnight(ChessPiece):
    def __init__(self, pos, black_or_white):
        ChessPiece.__init__(self, pos, black_or_white)
        self.repeat_moves = False
        # 8 mogelijke zetten van het paard
        self.possible_moves=[(2, 1),(1,2),(-1, 2),(1,-2),(-2,-1),(-1,-2),(1,-2),(2,-1)]

class ChessPieceBishop(ChessPiece):
    def __init__(self, pos, black_or_white):
        ChessPiece.__init__(self, pos, black_or_white)
        self.repeat_moves = True
        # Enkel schuin bewegen
        self.possible_moves = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

class ChessPieceTower(ChessPiece):
    def __init__(self, pos, black_or_white):
        ChessPiece.__init__(self, pos, black_or_white)
        self.repeat_moves = True
        # Enkel recht bewegen
        self.possible_moves=[(0,-1),(1,0),(0,1),(-1,0)]

class ChessPiecePawn(ChessPiece):
    def __init__(self, pos, black_or_white):
        ChessPiece.__init__(self, pos, black_or_white)
        self.repeat_moves = True
        # Standaard 1 stapje voorruit
        self.possible_moves = [(1, 0)]
        # 2 stapjes voorruit indien nog niet bewogen
        self.extra_moves = [(2, 0)]
        # Schuin slaan
        self.capture_moves = [(1, 1),(1, -1)]
        # En passant slaan
        self.extra_capture_moves = [(1, 1),(1, -1)]
