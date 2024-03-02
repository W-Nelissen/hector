#from pynput import keyboard
import pygame as pg
""""
 keyboardhandler handles only keyboard events.
    This causes less lag than pygame
    Repeats of keys are disposed of faster
    Creates a global object KBH = KeyboardHandler() that can be linked in any object that needs keyboard input
    One object can override settings of another: have a plan before you start.
        
    ...

"""

class Key:
    def __init__(self, key, action):
        self.down = False
        self.key = key
        self.action = action

KEY_IN_USE = -1
KEY_SET = 1
class KeyboardHandler:
    def __init__(self):
        self.keys = []

    def add_key(self, key, action):
        self.keys.append(Key(key, action))


    # Set key replaces the key for an action, because the other way around would be silly
    def set_key(self, key, action):
        found = False
        # Check whether key was already assigned to other action
        for k in self.keys:
            if k.key == key:
                if k.action != action:
                    return KEY_IN_USE
        # Check if there is already a key assigned to the action and replace if needed
        for k in self.keys:
            if k.action == action:
                found = True
                k.key = key
                return KEY_SET
        # If no key was found for the action, add key/action
        if not found:
            self.add_key(key, action)
        return KEY_SET

    # only used with listener, not needed if pygame is used
    def on_key_press(self, key):
        #  print(f'Key {key} pressed')
        for k in self.keys:
            if str(k.key) == str(key):
                k.down = True

    # only used with listener, not needed if pygame is used
    def on_key_release(self, key):
        # print(f'Key {key} released')
        for k in self.keys:
            if str(k.key) == str(key):
                k.down = False

    # only used with pygame, not needed if listener is used
    def is_active(self, action):
        keys = pg.key.get_pressed()
        for k in self.keys:
            if k.action == action:
                return keys[int(k.key)]
        return False

 #   def active(self, action):
 #       for k in self.keys:
 #           if k.action == action:
 #               return k.down
 #       return False


# KBH = KeyboardHandler()

