class h_PiecePosition():
    def __init__(self, turn_nr, move_nr, square):
        self.turn_nr = turn_nr
        self.move_nr = move_nr
        self.square = square

class h_SquarePiece():
    def __init__(self, turn_nr, move_nr, piece):
        self.turn_nr = turn_nr
        self.move_nr = move_nr
        self.piece = piece

class h_Move():
    def __init__(self, turn_nr, move_nr, square1, square2, isCheck):
        self.turn_nr = turn_nr
        self.move_nr = move_nr
        self.square1 = square1
        self.square2 = square2
        self.isCheck = isCheck
        self.checkmate = 0
    def get_string(self):
        if not self.checkmate:
            if not self.isCheck:
                return "abcdefgh"[self.square1.x] + "12345678"[self.square1.y] + " - " + "abcdefgh"[self.square2.x] + "12345678"[self.square2.y]
            else:
                return "abcdefgh"[self.square1.x] + "12345678"[self.square1.y] + " - " + "abcdefgh"[self.square2.x] + "12345678"[self.square2.y] + " Check"
        else:
            return "abcdefgh"[self.square1.x] + "12345678"[self.square1.y] + " - " + "abcdefgh"[self.square2.x] + "12345678"[self.square2.y] + " Mate"
    def setCheckmate(self, checkmate):
        self.checkmate = checkmate

class H_PiecePosition():
    def __init__(self):
        self.piecePositions = []
    def add(self, turn_nr, move_nr, square):
        self.piecePositions.append(h_PiecePosition(turn_nr, move_nr, square))

class H_SquarePiece():
    def __init__(self):
        self.squarePieces = []
    def add(self, turn_nr, move_nr, piece):
        self.squarePieces.append(h_SquarePiece(turn_nr, move_nr, piece))
class H_Move():
    def __init__(self):
        self.moves = []
    def add(self, turn_nr, move_nr, square1, square2, isCheck):
        self.moves.append(h_Move(turn_nr, move_nr, square1, square2, isCheck))
    def resetTo(self, move_nr):
        self.moves = [m for m in self.moves if m.move_nr <= move_nr]
