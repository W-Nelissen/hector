from ai_default_tables import *


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

    def calc(self, cb):
        pass

class ai_rule:
    def __init__(self, rule, weight):
        self.rule = rule
        self.weight = weight
class ai:
    def __init__(self):
        self.rules = []
        self.rules.append(ai_rule(cr_piece_value(), 1))
    def calc_board(self, cb, BW):
        value = 0
        for ai_rule in self.rules:
            value += ai_rule.rule.calc(cb, BW) * ai_rule.weight
        return value