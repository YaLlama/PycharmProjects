from pynput.mouse import Button, Controller as Mctr
import keyboard
import time

code = '532474'
openBrowser = 3
pageLoad = 2 + 2
reload = .1 + 2
naemReload = 1 + 2

accNum = 0

def stop():
    mouse.position = (856, 847)
    mouse.click(Button.left, 1)
    time.sleep(.2)
    mouse.position = (108, 594)
    mouse.click(Button.left, 1)


def joinGame(name):
    mouse.position = (188, 50)
    mouse.click(Button.left, 3)
    keyboard.write('https://quizlet.com/live')
    keyboard.press_and_release('enter')
    keyboard.wait('ctrl')
    keyboard.write(code)
    mouse.position = (767, 458)
    mouse.click(Button.left, 1)
    keyboard.wait('ctrl')
    keyboard.write(name)
    keyboard.wait('ctrl')
    mouse.position = (761, 426)
    mouse.click(Button.left, 1)

def nextAccount():
    global accNum
    accNum += 1
    if(accNum > 7):
        stop()
    mouse.position = (88, 15)
    mouse.click(Button.left, 1)
    keyboard.wait('ctrl')
    mouse.position = (1326, 108)
    mouse.click(Button.left, 1)
    keyboard.wait('ctrl')
    mouse.position = (1270, 244)
    mouse.click(Button.left, 1)
    keyboard.wait('ctrl')
    mouse.position = (1267, 107)
    mouse.click(Button.left, 1)
    keyboard.wait('ctrl')
    mouse.position = (630, 459)
    mouse.click(Button.left, 1)
    keyboard.wait('ctrl')
    if (accNum == 1):
        mouse.position = (581, 83)
    elif (accNum == 2):
        mouse.position = (601, 149)
    elif (accNum == 3):
        mouse.position = (586, 199)
    elif (accNum == 4):
        mouse.position = (594, 254)
    elif (accNum == 5):
        mouse.position = (597, 316)
    elif (accNum == 6):
        mouse.position = (623, 374)
    mouse.click(Button.left, 1)
    mouse.position = (704, 666)
    mouse.click(Button.left, 1)

def newTab():
    global accNum
    mouse.position = (270 + 240 * accNum, 16)
    mouse.click(Button.left, 1)
    keyboard.wait('ctrl')


keyboard.add_hotkey('p', stop, args=())

mouse = Mctr()

previousPos = (-1, -1)

##open school tab
mouse.position = (574, 852)
mouse.click(Button.left, 1)
keyboard.wait('ctrl')
##click the search bar
##go to quizlet live
joinGame('Kaden')

##open bot browserpp
mouse.position = (516, 839)
mouse.click(Button.left, 1)
keyboard.wait('ctrl')

##open quizlet
mouse.position = (188, 50)
mouse.click(Button.left, 3)
keyboard.write('https://quizlet.com/logout')
keyboard.press_and_release('enter')
keyboard.wait('ctrl')

##Cycle
##open new tab
newTab()
joinGame('charlse')
##Next account as said
nextAccount()

newTab()
joinGame('uma')
##cycle
nextAccount()
newTab()
joinGame('brian')

nextAccount()
newTab()
joinGame('will')

nextAccount()
newTab()
joinGame('ethan')