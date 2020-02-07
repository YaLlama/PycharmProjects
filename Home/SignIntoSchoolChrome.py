from pynput.mouse import Button, Controller as Mctr
import keyboard
import time
password = 'cpos262COLD'
mouse = Mctr()


mouse.position = (565, 842)
mouse.click(Button.left, 1)
keyboard.wait('ctrl')
mouse.position = (1442, 52)
mouse.click(Button.left, 1)
time.sleep(.1)
mouse.position = (1338, 357)
mouse.click(Button.left, 1)
keyboard.wait('ctrl')
mouse.position = (904, 651)
time.sleep(.2)
mouse.click(Button.left, 1)
keyboard.wait('ctrl')
keyboard.write(password)
mouse.position = (897, 525)
time.sleep(.2)
mouse.click(Button.left, 1)