from game_area import GameArea
from event_handler import *
from game_constants import *
from keyboardhandler import KeyboardHandler

def write_string( win, strText, text_color, x, y, size):
    font = pg.font.Font("freesansbold.ttf", size)
    text_surface = font.render(strText, True, text_color)
    win.blit(text_surface, (x, y))

class ChessSquare(Button):
    def __init__(self, parent, x, y, w, h):
        Button.__init__(self, parent,x, y, w, h, "", 0, False, False)

    def draw(self, win):
        if self.isWithin:
            pg.draw.rect(win, B_burlywood, self.rect, 0)
        else:
            pg.draw.rect(win, B_rosybrown, self.rect, 0)


class Horse(Button):
    def __init__(self, parent, x, y):
        Button.__init__(self, parent, x, y, 44, 44, "", 0,  False, True)
        self.horse_image = pg.image.load("assets/pieces/W_Knight.png")
        self.horse_image_opacity = pg.image.load("assets/pieces/W_Knight.png").convert_alpha()
        opacity = 100  # Opaciteitswaarde tussen 0 (transparant) en 255 (ondoorzichtig)
        self.horse_image_opacity.set_alpha(opacity)
        self.parent = parent
    def getOffsetRect(self, dx, dy):
        return pg.Rect(self.rect.left + dx, self.rect.top + dy, self.rect.width, self.rect.height)

    def action_dragged(self):
        self.parent.checkMove(self)
    
    def draw(self, win):
        bg_color = BLUE
        fg_color = RED
        txt_color = RED
        if self.isPressed:
            win.blit(self.horse_image_opacity, self.getOffsetRect(self.x2 - self.x1, self.y2 - self.y1))
        else:
            win.blit(self.horse_image, self.rect)

class Textje(Button):
    def __init__(self, parent, x, y, w, h, name):
        Button.__init__(self,parent, x,y,w,h,name,0)

    def draw(self, win):
        write_string(win, self.name, BLACK, self.rect.left + 4, self.rect.top + 4, 20)

class NamedRect(Button):
    def __init__(self, parent, x, y, w, h, name):
        Button.__init__(self,parent,x,y,w,h,name,0)
        self.cNormal = GREEN

    def draw(self, win):
        pg.draw.rect(win, self.cNormal, self.rect, 0)
        write_string(win, self.name, GREY, self.rect.left + 4, self.rect.top + 4, 20)


class GameAreaSANDBOX(GameArea):
    def __init__(self, game, r):
        GameArea.__init__(self, game, r)

        # code om button te testen
        self.test_button = Button(self, self._x(10), self._y(10), self.rect.width - 20, BUTTON_HEIGHT, "Klik mij", "DEMO_CLICK")
        #self.evtObjects.append(self.test_button)
        self.nr_of_clicks_text = Textje(self, self._x(40), self._y(50), 150, 36, '0')
        self.nr_of_clicks = 0

        # code om paardje te slepen
        self.drag_instruction = Textje(self, self._x(10), self._y(100), 160, 36, "Sleep het paardje")
        self.chessSquares = []
        for i in range(3):
            for j in range(3):
                new_square = ChessSquare(self, self._x(20 + j * 60), self._y(140 + i * 60 + j * 10), 44,44)
                self.chessSquares.append(new_square)
                self.addEvtObj(new_square)
        self.horse = Horse(self, self._x(20), self._y(140))
        self.addEvtObj(self.horse)

        # code om keyboard te lezen
        self.keyboard_instruction = Textje(self, self._x(10), self._y(320), 150, 36, "Tik 'a' of 'b'")
        self.game.key_handler.set_key(pg.K_a, "HILITE_A")
        self.game.key_handler.set_key(pg.K_b, "HILITE_B")
        self.A_pressed = NamedRect(self, self._x(10), self._y(360), 160, 32, "'a' is pressed")
        self.B_pressed = NamedRect(self, self._x(10), self._y(400), 160, 32, "'b' is pressed")

    def checkMove(self, chessPiece):
        for chess_square in self.chessSquares:
            if chess_square.isWithin:
                chessPiece.rect.x = chess_square.rect.x
                chessPiece.rect.y = chess_square.rect.y

    def execute_action(self, action):
        if action == "DEMO_CLICK":
            self.nr_of_clicks += 1
            self.nr_of_clicks_text.name = str(self.nr_of_clicks)

    def handle_keyboard_events(self):
        if self.game.key_handler.is_active("HILITE_A"):
            self.A_pressed.cNormal = GREEN
        else:
            self.A_pressed.cNormal = GREY
        if self.game.key_handler.is_active("HILITE_B"):
            self.B_pressed.cNormal = GREEN
        else:
            self.B_pressed.cNormal = GREY

    def draw(self):
        GameArea.draw(self)
        # save current clip rect before changing it
        clip_rect = self.game.win.get_clip()
        self.game.win.set_clip(self.rect)

        for obj in self.evtObjects:
            obj.draw(self.game.win)
        self.nr_of_clicks_text.draw(self.game.win)
        self.drag_instruction.draw(self.game.win)
        self.keyboard_instruction.draw(self.game.win)
        self.A_pressed.draw(self.game.win)
        self.B_pressed.draw(self.game.win)

        # revert to old clip rect
        self.game.win.set_clip(clip_rect)

