import pygame as pg

def play_mp3(file_path):
        pg.mixer.init()
        pg.mixer.music.load(file_path)
        pg.mixer.music.play()

class GameSound:
    """
    For now only mp3 files
    """
    def __init__(self, file_path):
        self.file_path = file_path
    
    def play(self):
        self.play_mp3()

    def play_mp3(self):
        pg.mixer.init() # Maybe move this to Main or __init__ ?
        pg.mixer.music.load(self.file_path)
        pg.mixer.music.play()
    