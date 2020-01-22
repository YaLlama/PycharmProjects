from pynput.mouse import Button, Controller as Mctr
import keyboard
import time

code = '764389'
openBrowser = 3
pageLoad = 2 + 2
reload = .1 + 2
naemReload = 1 + 2

accNum = 0

def stop():
    mouse.position = (574, 852)
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
    mouse.position = (761, 426)
    mouse.click(Button.left, 1)
    keyboard.wait('ctrl')

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

def inject():
    mouse.position = (1402, 47)
    mouse.click(Button.left, 1)
    keyboard.wait('ctrl')
    mouse.position = (1373, 276)
    mouse.click(Button.left, 1)
    keyboard.wait('ctrl')
    mouse.position = (1289, 256)
    mouse.click(Button.left, 1)
    keyboard.press_and_release('enter')
    keyboard.wait('ctrl')
    mouse.position = (171, 177)
    mouse.click(Button.left, 1)
    keyboard.wait('ctrl')
    keyboard.press_and_release('ctrl+v')
    time.sleep(.2)
    mouse.position = (335, 78)
    mouse.click(Button.left, 1)
    keyboard.wait('ctrl')
    keyboard.press_and_release('v')
    time.sleep(.1)
    keyboard.press_and_release('c')
    keyboard.wait('ctrl')



def injectGetCode():
    mouse.position = (1402, 47)
    mouse.click(Button.left, 1)
    keyboard.wait('ctrl')
    mouse.position = (1373, 276)
    mouse.click(Button.left, 1)
    keyboard.wait('ctrl')
    mouse.position = (1289, 256)
    mouse.click(Button.left, 1)
    keyboard.press_and_release('enter')
    keyboard.wait('ctrl')
    mouse.position = (120, 150)
    mouse.click(Button.left, 1)
    keyboard.wait('ctrl')
    keyboard.write(code[0])
    keyboard.wait('ctrl')
    keyboard.write(code[1])
    keyboard.wait('ctrl')
    keyboard.write(code[2])
    keyboard.wait('ctrl')
    keyboard.write(code[3])
    keyboard.wait('ctrl')
    keyboard.write(code[4])
    keyboard.wait('ctrl')
    keyboard.write(code[5])
    keyboard.wait('ctrl')
    mouse.position = (146, 117)
    mouse.click(Button.left, 1)
    keyboard.wait('ctrl')
    mouse.position = (146, 117)
    mouse.click(Button.left, 3)
    keyboard.wait('ctrl')
    keyboard.press_and_release('ctrl+a')
    keyboard.wait('ctrl')
    keyboard.press_and_release('ctrl+c')
    mouse.position = (493, 14)
    mouse.click(Button.left, 1)
    keyboard.wait('ctrl')
    mouse.position = (171, 177)
    mouse.click(Button.left, 1)
    keyboard.press_and_release('ctrl+v')
    time.sleep(.2)
    mouse.position = (335, 78)
    mouse.click(Button.left, 1)
    keyboard.wait('ctrl')
    keyboard.press_and_release('v')
    time.sleep(.1)
    keyboard.press_and_release('c')
    keyboard.wait('ctrl')




keyboard.add_hotkey('alt', stop, args=())

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
keyboard.wait('shift')
mouse.position = (704, 666)
mouse.click(Button.left, 1)

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
joinGame('part')

nextAccount()
newTab()
joinGame('brannndon')

##injection

injectGetCode()
accNum -= 1
newTab()
inject()
accNum -= 1
newTab()
inject()
accNum -= 1
newTab()
inject()
accNum -= 1
newTab()
inject()

stop()