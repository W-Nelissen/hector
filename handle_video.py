import cv2
import pygame
import numpy as np
import time as t

class Video():
    def __init__(self,file_path):
        self.t0=0
        self.cap = cv2.VideoCapture(file_path)
        if not self.cap.isOpened():
            print("Error: Failed to open video file.")
       
    def startVideo(self):
        self.t0 = t.time()
        
    def closeVideo(self):
        self.cap.release()
    
    def getFrame(self):
        frame_time=t.time()-self.t0
        frame_number = int(frame_time * self.cap.get(cv2.CAP_PROP_FPS))
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
        ret, frame = self.cap.read()
        if ret:
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            surface = pygame.image.frombuffer(frame_rgb.tobytes(), frame_rgb.shape[1::-1], "RGB")
            return surface
        return None


pygame.init()
screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Video Frame")

file_path = "assets\\videos\chess_funny.mp4"
myVideo = Video(file_path)
myVideo.startVideo()

running = True
while running:
    frame_surface = myVideo.getFrame()
    if frame_surface:
        screen.blit(frame_surface, (0, 0))
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
    
pygame.quit()