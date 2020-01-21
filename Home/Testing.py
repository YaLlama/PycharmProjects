from pynput.mouse import Button, Controller as Mctr
import keyboard

def toggle():
    global boolean
    if boolean:
        boolean = False
    else:
        boolean = True

boolean = False

keyboard.add_hotkey('p', toggle, args=())

mouse = Mctr()

previousPos = (-1, -1)

while True:
    if(boolean):
        if(previousPos != mouse.position):
            print('The current pointer position is {0}'.format(mouse.position))
            previousPos = mouse.position