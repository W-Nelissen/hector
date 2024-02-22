from game_constants import *
from event_handler import EventHandler
import time as t
import pygame as pg
from keyboardhandler import KeyboardHandler
class Game(EventHandler):
    """
    Implementeert basisfunctionaliteiten voor een generiek game
    Heeft niets te maken met specifieke functionaliteiten zoals die van een schaakspel
    """
    def __init__(self, window, clock):
        EventHandler.__init__(self, None)
        self.win = window
        self.clock = clock
        self.keep_running = True
        self.last_cycle = t.time()
        self.key_handler = KeyboardHandler()
    def handle_events(self):
        """
        Zet pygame events om naar onze eigen handige routines
        Je kan dan bijvoorbeeld de functie self.MOUSEBUTTONDOWN(x, y) oproepen,
        zonder te weten hoe de pygame eventhandler dit opslaat.
        """

        # Keyboard Events are handled separately
        self.handle_keyboard_events()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.keep_running = False
            if event.type == pg.MOUSEWHEEL:
                self.MOUSEWHEEL(event.y)
            if event.type == pg.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pg.mouse.get_pos()
                self.MOUSEBUTTONDOWN(mouse_x, mouse_y)
            if event.type == pg.MOUSEBUTTONUP:
                mouse_x, mouse_y = pg.mouse.get_pos()
                self.MOUSEBUTTONUP(mouse_x, mouse_y)
            if event.type == pg.MOUSEMOTION:
                mouse_x, mouse_y = pg.mouse.get_pos()
                self.MOUSEMOTION(mouse_x, mouse_y)

    def update_data(self):
        # whatever needs to changed (used for animation or special effects)
        pass

    def draw(self):
        # whatever needs to drawn happens here
        pass

    # execute_cycle is typically called from the main loop
    # execute_cycle can be called from 'background' routine like an AI-learning cycle
    #   - we can then play the game while the AI learns in the background
    def execute_cycle(self):
        self.last_cycle = t.time()
        self.handle_events()
        self.update_data()
        self.draw()
        return self.keep_running

    def execute(self):
        while self.execute_cycle():
            pg.display.update()
            self.clock.tick(FRAME_RATE)

    # execute_from_background must be called from 'background' routine like an AI-learning cycle
    # if not called, the background routine locks the user out.
    # call frequency must be higher than FRAME_RATE to avoid lagging.
    def execute_from_background(self):
        elapsed_time = t.time() - self.last_cycle
        if elapsed_time * FRAME_RATE > 1:
            self.execute_cycle()

