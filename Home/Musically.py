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

boolean = True

keyboard.add_hotkey('q', toggle, args=())




while True:
    while boolean:
        printscreen_pil = ImageGrab.grab()
        





##mouse.position = (1342, 38)
##mouse.click(Button.left, 1)
