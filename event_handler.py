from colors import *
import pygame as pg

class EventHandler:
    """
    A class that handles all events, such as clicking and dragging
    Parameters:
    parent: use 'self' here when defining the object
    has_select: ??
    has_dragging: ??
    """
    def __init__(self, parent, has_select=False, has_dragging=False):
        #all features are turned off by default, but adding them is just adding parameters
        self.parent = parent
        self.has_select = has_select
        self.has_dragging = has_dragging

        # Keep track of mouse activity, object dragging, button mechanics
        self.isWithin = False
        self.isPressed = False
        self.isDragged = False

        # Default colors for highlighting objects
        self.cPressed = (0, 255, 255)
        self.cNormal = (255, 255, 0)
        self.cDragged = LTGREY

        #TODO: implement modifiers (_left/_right may be ditched later)
        self.mod_shift = False
        self.mod_shift_left = False
        self.mod_shift_right = False
        self.mod_ctrl = False
        self.mod_ctrl_left = False
        self.mod_ctrl_right = False
        self.mod_alt = False

        self.rect = pg.Rect(0, 0, 0, 0)

        self.evtObjects = []
        if self.parent:
            self.parent.addEvtObj(self)

    def addEvtObj(self, evtObj):
        self.evtObjects.append(evtObj)

    def isMouseWithin(self, mouse_x, mouse_y):
        """
        Checks if the click was within an object. Needs override.
        What do you mean with override?
        """
        if self.rect is not None:
            return self.rect.left < mouse_x < self.rect.right and self.rect.top < mouse_y < self.rect.bottom
        else:
            return False
        
    def _x(self, x):
        """
        What does this function do? How should the user use it?
        """
        if self.rect:
            return self.rect.left + x
        else:
            return x

    def _y(self, y):
        """
        What does this function do? How should the user use it?
        """
        if self.rect:
            return self.rect.top + y
        else:
            return y

    def MOUSEWHEEL(self, _wheel):
        for obj in self.evtObjects:
            obj.MOUSEWHEEL(_wheel)
    def MOUSEBUTTONDOWN(self, mouse_x, mouse_y):
        for obj in self.evtObjects:
            obj.MOUSEBUTTONDOWN(mouse_x, mouse_y)
    def MOUSEBUTTONUP(self, mouse_x, mouse_y):
        for obj in self.evtObjects:
            obj.MOUSEBUTTONUP(mouse_x, mouse_y)
    def MOUSEMOTION(self, mouse_x, mouse_y):
        for obj in self.evtObjects:
            obj.MOUSEMOTION(mouse_x, mouse_y)

    def handle_keyboard_events(self):
        for obj in self.evtObjects:
            obj.handle_keyboard_events()

    def action_hovering(self):
        pass
    def action_dragging(self):
        pass
    def action_dropped(self):
        pass
    def action_clicked(self):
        pass

class Button(EventHandler):
    """
    Class for buttons.
    Parameters:
    parent: use 'self' here when defining the object
    x, y: coördinates of top-left
    w: width
    h: height
    name: text on the button
    action: unique string to identify your action e.g.:"move_chess_piece"
    """
    def __init__(self, parent, x, y, w, h, name, action, has_select=False, has_dragging=False):
        EventHandler.__init__(self, parent, has_select, has_dragging)
        self.parent = parent
        self.rect = pg.Rect((x, y, w, h))
        self.name = name
        self.action = action
        self.x1 = 0
        self.y1 = 0
        self.x2 = 0
        self.y2 = 0

    def MOUSEBUTTONDOWN(self, mouse_x, mouse_y):
        self.isWithin = self.isMouseWithin(mouse_x, mouse_y)
        if self.isWithin:
            self.isPressed = True
            self.x1 = mouse_x
            self.y1 = mouse_y
            self.x2 = mouse_x
            self.y2 = mouse_y

    def MOUSEBUTTONUP(self, mouse_x, mouse_y):
        self.isWithin = self.isMouseWithin(mouse_x, mouse_y)
        if self.has_dragging:
            if self.isPressed:
                self.action_dragged()
        elif self.isWithin and self.isPressed:
            self.action_clicked()
        self.isPressed = False

    def MOUSEMOTION(self, mouse_x, mouse_y):
        self.isWithin = self.isMouseWithin(mouse_x, mouse_y)
        self.x2 = mouse_x
        self.y2 = mouse_y

    def action_dragged(self):
        pass
    
    def action_clicked(self):
        if self.parent:
            self.parent.execute_action(self.action)
        else:
            self.execute()

    def execute_action(self, action):
        pass

    def execute(self):
        pass

    def write_string(self, win, strText, text_color, x, y):
        self.font = pg.font.Font("freesansbold.ttf", 24)
        text_surface = self.font.render(strText, True, text_color)
        win.blit(text_surface, (x, y))

    def draw(self, win):
        bg_color = BLUE
        fg_color = RED
        txt_color = RED
        if self.isPressed and self.isWithin:
            fg_color = BLUE
            bg_color = RED
            txt_color = BLUE
        pg.draw.rect(win, bg_color, self.rect, 0)
        pg.draw.rect(win, fg_color, self.rect, 4)
        self.write_string(win, self.name, txt_color, self.rect.left + 4, self.rect.top + 4)
