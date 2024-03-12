from event_handler import Button
from colors import *
import pygame as pg

CP_WHITE = 1
CP_BLACK = 2
class ChessPiece(Button):
    def __init__(self, parent, black_or_white, B_name, W_name):
        Button.__init__(self, parent, 0, 0, 0, 0, "", 0) 
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
        opacity = 150  # Opaciteitswaarde tussen 0 (transparant) en 255 (ondoorzichtig)
        self.image_opacity.set_alpha(opacity)
    
    def action_pressed(self):
        chessboard = self.parent
        chessboard.showValidMoves(self.square.x, self.square.y)
    
    def setSquare(self, square):
        self.square = square
        self.rect = square.rect
        
    def draw(self,win):
        if not self.isPressed:
            if self.image:
                r = self.rect
                x = r.x + (r.width - self.image.get_width()) // 2
                y = r.y + (r.height - self.image.get_height()) // 2
                win.blit(self.image, (x, y))
        
    def draw_dragged(self,win):
        if self.isPressed:
            if self.image_opacity:
                r = self.getOffsetRect(self.x2-self.x1,self.y2-self.y1)
                x = r.x + (r.width - self.image.get_width()) // 2
                y = r.y + (r.height - self.image.get_height()) // 2
                win.blit(self.image_opacity, (x, y))

class ChessPieceKing(ChessPiece):
    def __init__(self, parent, black_or_white):
        ChessPiece.__init__(self, parent, black_or_white, "assets/pieces/B_King.png", "assets/pieces/W_King.png")


        # Koning mag maar 1 stapje zetten, dus repeat_moves = False
        self.repeat_moves = False
        # Alle mogelijke moves, zonder rekening te houden met het bord
        self.possible_moves=[(1,0),(1,1),(0,1),(-1, 1),(-1,0),(-1,-1),(0,-1),(1,-1)]

class ChessPieceQueen(ChessPiece):
    def __init__(self, parent, black_or_white):
        ChessPiece.__init__(self, parent, black_or_white, "assets/pieces/B_Queen.png", "assets/pieces/W_Queen.png")
        # Koningin mag maar meerde stapjes zetten, dus repeat_moves = True
        self.repeat_moves = True
        # Alle mogelijke moves, zonder rekening te houden met het bord
        # Dus hetzelfde als bij de Koning
        self.possible_moves = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

class ChessPieceKnight(ChessPiece):
    def __init__(self, parent, black_or_white):
        ChessPiece.__init__(self, parent, black_or_white, "assets/pieces/B_Knight.png", "assets/pieces/W_Knight.png")
        self.repeat_moves = False
        # 8 mogelijke zetten van het paard
        self.possible_moves=[(2, 1),(1,2),(-1, 2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]

class ChessPieceBishop(ChessPiece):
    def __init__(self, parent, black_or_white):
        ChessPiece.__init__(self, parent, black_or_white, "assets/pieces/B_Bishop.png", "assets/pieces/W_Bishop.png")
        self.repeat_moves = True
        # Enkel schuin bewegen
        self.possible_moves = [(1, 1), (-1, 1), (-1, -1), (1, -1)]

class ChessPieceTower(ChessPiece):
    def __init__(self, parent, black_or_white):
        ChessPiece.__init__(self, parent, black_or_white, "assets/pieces/B_Tower.png", "assets/pieces/W_Tower.png")
        self.repeat_moves = True
        # Enkel recht bewegen
        self.possible_moves=[(0,-1),(1,0),(0,1),(-1,0)]

class ChessPiecePawn(ChessPiece):
    def __init__(self, parent, black_or_white):
        ChessPiece.__init__(self, parent, black_or_white, "assets/pieces/B_Pawn.png", "assets/pieces/W_Pawn.png")
        self.repeat_moves = False
        # Standaard 1 stapje voorruit
        self.possible_moves = [(0, 1)]
        # 2 stapjes vooruit indien nog niet bewogen
        self.extra_moves = [(0, 2)]
        # Schuin slaan
        self.capture_moves = [(1, 1),(-1, 1)]
        # En passant slaan
        self.extra_capture_moves = [(1, 1),(-1, 1)]
