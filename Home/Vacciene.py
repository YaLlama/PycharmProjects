##continue (547, 785)
##try again (943, 535)
from pynput.mouse import Button, Controller as Mctr
import keyboard
import time
from PIL import ImageGrab
mouse = Mctr()

def toggleRun():
    global boolean
    if boolean:
        boolean = False
    else:
        boolean = True

boolean = False

def toggleQuit():
    global quit
    if quit:
        quit = False
    else:
        quit = True

quit = False

keyboard.add_hotkey('ctrl', toggleRun, args=())
keyboard.add_hotkey('esc', exit, args=())

def testPage():
    ##first click box
    mouse.position = (547, 785)
    mouse.click(Button.left, 1)
    ##time waiting for popup
    ##time.sleep(.2)


    ##insert screen read
    mouse.position = (1005, 348)
    screen = ImageGrab.grab()
    screen.convert("RGB")
    color = screen.getpixel((1005, 348))
    if((125, 125, 125) != color):
        count = 0
        while(count < 50):
            time.sleep(.2)
            mouse.position = (1005, 348)
            screen = ImageGrab.grab()
            screen.convert("RGB")
            color = screen.getpixel((1005, 348))
            if((124, 124, 124) != color):
                count += 1
                if(count == 40):
                    exit("AutoStop")
            else:
                break
    ##seccond click box
    mouse.position = (943, 535)
    mouse.click(Button.left, 1)
    ##time beofre switching tabs
    time.sleep(.3)

def click(x, y):
    mouse.position = (x, y)
    mouse.click(Button.left, 1)

##page1 = (116, 11)
##page2 = (354, 20)
##page3 = (603, 18)
##xCHeck = (1005, 348)

reloadPage = .3

while(not quit):
    while(boolean):
        ##page1
        ##click(116,11)
        ##wait for page to relaod
        ##time.sleep(reloadPage)
        ##test page for apointment
        testPage()
        ##click(354, 20)
        ##time.sleep(reloadPage)
        ##testPage()



