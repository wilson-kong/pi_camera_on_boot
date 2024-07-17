import time
import picamera
import numpy as np
from PIL import Image, ImageDraw,ImageFont
import pygame, sys
from pygame.locals import *
import os

# set camera resolution
width = 1600
height = 1020

# button size
button = 100

# initialise pygame screen
pygame.init()
windowSurfaceObj = pygame.display.set_mode((width,height),pygame.FULLSCREEN)

def on_press(key):
    global end, overlay
    # exit
    if key == 27: # ESC key
        camera.remove_overlay(overlay)
        camera.close()
        pygame.display.quit()
        end = 1
        exit()
               
# setup overlay
image_array = np.zeros((height, width, 4), dtype=np.uint8)
image = Image.fromarray(image_array)
draw = ImageDraw.Draw(image)

# setup camera
camera = picamera.PiCamera()
camera.resolution = (width, height)
camera.framerate = 24
camera_array = np.asarray(image)
overlay = camera.add_overlay(bytes(memoryview(camera_array)),format='rgba',layer=3) 
camera.start_preview()
end = 0

# check for key press
while end == 0:
    time.sleep(0.01)
    for event in pygame.event.get():
       if event.type == KEYDOWN:
           key = event.key
           on_press(key)
       elif event.type == MOUSEBUTTONUP:
           mousex, mousey = event.pos
           # exit if screen button pressed
           if mousex > width - button and mousey < button:
               pygame.display.quit()
               pygame.quit()
               camera.remove_overlay(overlay)
               camera.close()
               end = 1
os.system("sudo shutdown -h now")
