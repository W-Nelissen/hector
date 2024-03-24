from ai_default_tables import *
import chess_pieces as cp

class calc_rule:
    def __init__(self):
        pass

    def calc(self, cb):
        pass

class cr_piece_value(calc_rule):
    def __init__(self):
        super().__init__()
        self.values = DEFAULT_PIECE_VALUES
    def calc(self, cb, BW):
        """
        Calculates the total piece value of 1 colour
        """
        value = 0
        for x in range(8):
            for y in range(8):
                square=cb.Square(x,y)
                if square.piece:
                    if BW == square.piece.BW: 
                        ID = square.piece.ID
                        value += self.values[ID]
        return value


class cr_piece_position_value(calc_rule):
    def __init__(self):
        super().__init__()
        self.values = []
        self.values.append(PAWN_TABLE)
        self.values.append(KNIGHT_TABLE)
        self.values.append(BISHOP_TABLE)
        self.values.append(ROOK_TABLE)
        self.values.append(QUEEN_TABLE)
        self.values.append(KING_TABLE)
    def calc(self, cb, BW):
        value = 0
        for x in range(8):
            for y in range(8):
                square=cb.Square(x,y)
                if square.piece:
                    if BW == square.piece.BW:
                        ID = square.piece.ID
                        if BW == cp.CP_BLACK:
                            value += self.values[ID][y][x]
                        else:
                            value += self.values[ID][7 - y][x]
        return value

class ai_rule:
    def __init__(self, rule, weight):
        self.rule = rule
        self.weight = weight
class ai:
    def __init__(self):
        self.rules = []
        self.rules.append(ai_rule(cr_piece_value(), 1))
        self.rules.append(ai_rule(cr_piece_position_value(), 1))
    def calc_board(self, cb, BW):
        value = 0
        for ai_rule in self.rules:
            value += ai_rule.rule.calc(cb, BW) * ai_rule.weight
        return value