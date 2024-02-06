from colors import *
import pygame as pg

CP_WHITE = 1
CP_BLACK = 2
class ChessPiece:
    def __init__(self, black_or_white, B_name, W_name):
        # positie van het schaakstuk (1-8,1-8)
        self.square = None
        # een generiek stuk heeft nog geen moves, elk schaakstuk moet dat zelf invullen
        self.possible_moves = []
        self.extra_moves = []
        self.capture_moves = []
        self.extra_capture_moves = []
        self.repeat_moves = False
        self.BW = black_or_white
        if black_or_white == CP_BLACK:
            self.image_name = B_name
        else:
            self.image_name = W_name
        self.image_opacity = self.image_name
        self.image = pg.image.load(self.image_name)
        self.image_opacity = pg.image.load(self.image_name).convert_alpha()
        opacity = 100  # Opaciteitswaarde tussen 0 (transparant) en 255 (ondoorzichtig)
        self.image_opacity.set_alpha(opacity)

    def draw(self,win):
        # Teken stuk, square_width = de afmeting van het vakje en de positie
        # De positie is in pixels en moet worden doorgegeven
        # Je kan images gebruiken uit data/pieces/
        # Of je laadt zelf images op in data/pieces/
        """
        # altijd eerst kijken of er wel een stuk is
        if self.image:
        # je kan een image altijd blitten
            win.blit(self.image, self.square.rect)
        """

class ChessPieceKing(ChessPiece):
    def __init__(self, black_or_white):
        ChessPiece.__init__(self, black_or_white, "assets/pieces/B_King.png", "assets/pieces/W_King.png")


        # Koning mag maar 1 stapje zetten, dus repeat_moves = False
        self.repeat_moves = False
        # Alle mogelijke moves, zonder rekening te houden met het bord
        self.possible_moves=[(1,0),(1,1),(0,1),(-1,-1),(-1,0),(-1,-1),(0,-1),(1,-1)]

class ChessPieceQueen(ChessPiece):
    def __init__(self, black_or_white):
        ChessPiece.__init__(self, black_or_white, "assets/pieces/B_Queen.png", "assets/pieces/W_Queen.png")
        # Koningin mag maar meerde stapjes zetten, dus repeat_moves = True
        self.repeat_moves = True
        # Alle mogelijke moves, zonder rekening te houden met het bord
        # Dus hetzelfde als bij de Koning
        self.possible_moves = [(1, 0), (1, 1), (0, 1), (-1, -1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

class ChessPieceKnight(ChessPiece):
    def __init__(self, black_or_white):
        ChessPiece.__init__(self, black_or_white, "assets/pieces/B_Knight.png", "assets/pieces/W_Knight.png")
        self.repeat_moves = False
        # 8 mogelijke zetten van het paard
        self.possible_moves=[(2, 1),(1,2),(-1, 2),(1,-2),(-2,-1),(-1,-2),(1,-2),(2,-1)]

class ChessPieceBishop(ChessPiece):
    def __init__(self, black_or_white):
        ChessPiece.__init__(self, black_or_white, "assets/pieces/B_Bishop.png", "assets/pieces/W_Bishop.png")
        self.repeat_moves = True
        # Enkel schuin bewegen
        self.possible_moves = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

class ChessPieceTower(ChessPiece):
    def __init__(self, black_or_white):
        ChessPiece.__init__(self, black_or_white, "assets/pieces/B_Tower.png", "assets/pieces/W_Tower.png")
        self.repeat_moves = True
        # Enkel recht bewegen
        self.possible_moves=[(0,-1),(1,0),(0,1),(-1,0)]

class ChessPiecePawn(ChessPiece):
    def __init__(self, black_or_white):
        ChessPiece.__init__(self, black_or_white, "assets/pieces/B_Pawn.png", "assets/pieces/W_Pawn.png")
        self.repeat_moves = True
        # Standaard 1 stapje voorruit
        self.possible_moves = [(1, 0)]
        # 2 stapjes vooruit indien nog niet bewogen
        self.extra_moves = [(2, 0)]
        # Schuin slaan
        self.capture_moves = [(1, 1),(1, -1)]
        # En passant slaan
        self.extra_capture_moves = [(1, 1),(1, -1)]
