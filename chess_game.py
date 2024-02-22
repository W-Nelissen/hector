from game_constants import *
from colors import *
from game import Game
from game_area_chessboard import GameAreaChessBoard
from game_area_history import GameAreaHistory
from game_area_players import GameAreaPlayers
from game_area_SANDBOX import GameAreaSANDBOX
from game_area_controls import GameAreaControls
from chess_board import ChessBoard


class ChessGame(Game):
    """
    Dit is het game object dat alles van het schaakspel implementeert
    Het is afgeleid van de basis klasse Game die de algemene spelflow controleert
    """
    def __init__(self, window, clock):
        Game.__init__(self, window, clock)
        # We definieren de verschillende delen van het scherm, die elk weten hoe ze zich moeten tekenen.
        # De invulling van die klassen gebeurt in aparte files: chess_area_game.py, ...
        self.chessboard_area = GameAreaChessBoard(self, GAME_RECT)
        self.history_area = GameAreaHistory(self, HIST_RECT)
        self.player_area = GameAreaPlayers(self, PLAYER_RECT)
        self.control_area = GameAreaControls(self, CONTROL_RECT)

        # SANDBOX is een zandbak waarin je mag spelen, maar die in het afgewerkte spel niet wordt getoond
        if SHOW_SANDBOX:
            self.SANDBOX_area = GameAreaSANDBOX(self, SANDBOX_RECT)

        # We definieren de datastructuren van ons spel
        self.chess_board = ChessBoard(self.chessboard_area)

    def update_data(self):
        # whatever needs to change (animation,...)
        pass

    def clear_window(self):
        # Omdat verschillende delen de clip rect kunnen verzetten, resetten we de clip rect tot het volledige venster
        # Zo zijn we niet afhankelijk van slordigheden
        self.win.set_clip((0, 0, WINDOW_WIDTH, WINDOW_HEIGHT))
        self.win.fill(GAME_BG_COLOR)


    def draw(self):
        # Dit object vraagt aan de deelobjecten om zichzelf te tekenen
        self.clear_window()
        self.chessboard_area.draw()
        self.history_area.draw()
        self.player_area.draw()
        self.control_area.draw()
        if SHOW_SANDBOX:
            self.SANDBOX_area.draw()
