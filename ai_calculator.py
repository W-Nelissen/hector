from ai_default_tables import *
import chess_pieces as cp
import numpy as n
import time as t

class calc_rule:
    def __init__(self):
        self.calc_level = False

    def calc(self, cb):
        pass

    def calc_diff(self, cb, move):
        return 0

class cr_piece_value(calc_rule):
    def __init__(self):
        super().__init__()
        self.values = DEFAULT_PIECE_VALUES
        self.calc_level = 99
    def calc(self, cb, BW):
        """
        Calculates the total piece value of 1 colour
        """
        value = 0
        for square in cb.allsquares:
            if square.piece and BW == square.piece.BW: 
                ID = square.piece.ID
                value += self.values[ID]
        return value

    def calc_diff(self, cb, maximizing_player, move):
        startsquare, endsquare = move
        taken_piece = endsquare.piece
        if taken_piece:
            print(taken_piece,endsquare.x,endsquare.y,startsquare.piece)
            ID = taken_piece.ID
            if maximizing_player: 
                return self.values[ID]
            else:
                return -self.values[ID]
        return 0
    
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
        self.calc_level = 99
    
    def calc(self, cb, BW):
        value = 0
        for square in cb.allsquares:
            if square.piece and BW == square.piece.BW:
                ID = square.piece.ID
                if BW == cp.CP_BLACK:
                    value += self.values[ID][square.y][square.x]
                else:
                    value += self.values[ID][7 - square.y][square.x]
        return value
    
    def calc_diff(self, cb, maximizing_player, move):
        value = 0
        startsquare, endsquare = move
        moved_piece = startsquare.piece
        ID = moved_piece.ID
        if moved_piece.BW == cp.CP_BLACK:
            value = self.values[ID][endsquare.y][endsquare.x]-self.values[ID][startsquare.y][startsquare.x]
        else:
            value = self.values[ID][7-endsquare.y][endsquare.x]-self.values[ID][7-startsquare.y][startsquare.x]
        taken_piece = endsquare.piece
        if taken_piece:
            print(taken_piece,endsquare.x,endsquare.y,startsquare.piece)
            ID = taken_piece.ID
            if taken_piece.BW == cp.CP_BLACK:
                value += self.values[ID][endsquare.y][endsquare.x]
            else:
                value += self.values[ID][7-endsquare.y][7-endsquare.x]
        if maximizing_player:
            return value
        else:
            return -value
    
class ai_rule:
    def __init__(self, rule, weight):
        self.rule = rule
        self.weight = weight
class ai:
    def __init__(self):
        self.rules = []
        self.rules.append(ai_rule(cr_piece_value(), 1))
        self.rules.append(ai_rule(cr_piece_position_value(), 1))
        self.transpostable = []
        self.transposvalue = []

    def calc_board(self, cb, BW):
        value = 0
        for ai_rule in self.rules:
            value += ai_rule.rule.calc(cb, BW) * ai_rule.weight
        return value

    def get_board_value(self,rule_eval):
        value = 0
        for i in range(len(self.rules)):
            ai_rule = self.rules[i]
            value += rule_eval[i][0] * ai_rule.weight
        return value

    def transposcode(self, cb):
        strcode = ""
        for square in cb.allsquares:
            if square.piece:
                strcode = strcode + square.code + square.piece.code
        return strcode
        
    def alpha_beta_search(self, board, rule_eval, depth, alpha, beta, player, maximizing_player):
        returnVal = 0
        #TODO: is_game_over
        if depth == 0 or board.isCheckmate(player):
            v1 = self.get_board_value(rule_eval)
            if maximizing_player:
                vx = self.calc_board(board, player) - self.calc_board(board, board.opponent(player))
                print(rule_eval,"rule_matrix=",v1,"value=",vx,self.calc_board(board, player) , self.calc_board(board, board.opponent(player)))
                return self.calc_board(board, player) - self.calc_board(board, board.opponent(player))
            else:
                vx = - self.calc_board(board, player) + self.calc_board(board, board.opponent(player))
                print(rule_eval,"rule_matrix=",v1,"value=",vx,self.calc_board(board, player) , self.calc_board(board, board.opponent(player)))
                return self.calc_board(board, board.opponent(player)) - self.calc_board(board, player)
            
        transposcode = self.transposcode(board)
        if transposcode in self.transpostable:
            return self.transposvalue[self.transpostable.index(transposcode)]
        
        if maximizing_player:
            max_eval = float('-inf')
            for move in board.possible_moves(player):
                self.calc_rule_eval(board, rule_eval, player, move, not maximizing_player, depth - 1)
                startsquare, endsquare = move
                p1, p2 = startsquare.piece, endsquare.piece
                endsquare.piece, startsquare.piece = p1, None
                eval = self.alpha_beta_search(board, rule_eval, depth - 1, alpha, beta, board.opponent(player), not maximizing_player)
                startsquare.piece, endsquare.piece = p1, p2
                max_eval = max(max_eval, eval)
                #fail-soft set alpha before break
                alpha = max(alpha, eval)
                break
                if beta <= alpha:
                    break  # Beta cut-off
            returnVal = max_eval
        else:
            min_eval = float('inf')
            for move in board.possible_moves(player):
                self.calc_rule_eval(board, rule_eval, player, move, True, depth - 1)
                startsquare, endsquare = move
                p1, p2 = startsquare.piece, endsquare.piece
                endsquare.piece, startsquare.piece = p1, None
                eval = self.alpha_beta_search(board, rule_eval, depth - 1, alpha, beta, board.opponent(player), not maximizing_player)
                startsquare.piece, endsquare.piece = p1, p2
                min_eval = min(min_eval, eval)
                #fail-soft beta before break
                beta = min(beta, eval)
                break
                if beta <= alpha:
                    break  # Alpha cut-off
            returnVal = min_eval
        self.transpostable.append(transposcode)
        self.transposvalue.append(returnVal)
        return returnVal
    
    def calc_rule_eval(self, cb, rule_eval, player, move, maximizing_player, depth, isTopLevel=False):
        if maximizing_player:
            p1,p2 = player,cb.opponent(player)
        else:
            p2,p1 = player,cb.opponent(player)
        for i in range(len(self.rules)):
            ai_rule = self.rules[i]
            if isTopLevel and ai_rule.rule.calc_level == 99:
                rule_eval[i][depth] = ai_rule.rule.calc(cb, p1) - ai_rule.rule.calc(cb, p2)
            elif ai_rule.rule.calc_level == depth:
                rule_eval[i][depth] = ai_rule.rule.calc(cb, p1) - ai_rule.rule.calc(cb, p2)
            elif ai_rule.rule.calc_level > depth:
                #print("depth=",depth)
                rule_eval[i][depth] = rule_eval[i][depth+1] + ai_rule.rule.calc_diff(cb, maximizing_player, move)
        #print(rule_eval)
        
    def find_best_move(self, board, depth, player):
        t0 = t.time()
        rule_eval = n.zeros((len(self.rules), depth+1))
        print(rule_eval)
        maximizing_player = True
        self.calc_rule_eval(board, rule_eval, player, None, maximizing_player, depth, True)
        self.transpostable = []
        self.transposvalue = []
        best_move = None
        max_eval = float('-inf')
        alpha = float('-inf')
        beta = float('inf')
        for move in board.possible_moves(player):
            self.calc_rule_eval(board, rule_eval, player, move, maximizing_player, depth - 1)
            startsquare, endsquare = move
            p1, p2 = startsquare.piece, endsquare.piece
            endsquare.piece, startsquare.piece = p1, None
            eval = self.alpha_beta_search(board, rule_eval, depth - 1, alpha, beta, board.opponent(player), not maximizing_player)
            startsquare.piece, endsquare.piece = p1, p2
            if eval > max_eval:
                max_eval = eval
                best_move = move
        print("Move in",t.time()-t0,"seconds")
        return best_move
