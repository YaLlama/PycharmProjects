from pynput.mouse import Button, Controller
import keyboard
import time
import cv2
import numpy as np
from PIL import ImageGrab


def toggle():
    global boolean
    if boolean:
        boolean = False
    else:
        boolean = True


mouse = Controller()

boolean = False

keyboard.add_hotkey('q', toggle, args=())




while True:
    while boolean:
        screen = ImageGrab.grab()
        screen.convert("RGB")
        color = screen.getpixel((1005, 348))
        print(color)




##mouse.position = (1342, 38)
##mouse.click(Button.left, 1)
