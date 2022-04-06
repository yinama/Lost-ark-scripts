import time
import pyautogui
import os

#Time.sleep(2)
Orecolor = (109, 191, 1)
Treecolor = (116, 203, 1)

options = ['1-auto press g','2-auto mine', '3-auto log', '4-auto fish']

#walks to a random location
#def randomWalk():
    

#just press g
def autoPressG():
    while True:
        pyautogui.press('g')
        time.sleep(0.5)

#new method with locateOnScreen
def autoMine():
    while True:
        pos = pyautogui.locateOnScreen('copper_ore.png',confidence=0.5)
        if pos:
            pyautogui.moveTo(pos[0]+40, pos[1]+50)
            time.sleep(0.5)
            pyautogui.leftClick()
            time.sleep(5)
            pyautogui.press('g')
            time.sleep(4)
        else:
            time.sleep(0.5)

def autoLog():
    pos = pyautogui.locateOnScreen('giant_mushroom.png',confidence=0.5)
    print(pos)
    
    if pos:
        pyautogui.moveTo(pos[0]+40, pos[1]+50)
        time.sleep(0.5)
        pyautogui.leftClick()
        time.sleep(1)
        pyautogui.press('g')
        while True:
            time.sleep(2)
            pos = pyautogui.locateOnScreen('gathering.png',confidence=0.99)
            if pos:
                print(pos)
                print('logging')
            else:
                print('done logging')
                return
    else:
        return
        
def autoFish():
    pyautogui.press('e')
    while True:
        pos = pyautogui.locateOnScreen('fish_mark.png',confidence=0.80)
        if pos:
            pyautogui.press('e')
            time.sleep(6)
            pyautogui.press('e')
        else:
            time.sleep(0.2)
            
    
def getPosition():
    im = pyautogui.screenshot()
    
    while True:
        position = pyautogui.position()
        print(im.getpixel(position))
        time.sleep(0.1)
        
def testdo():
    pyautogui.moveTo(90, 110)
    pyautogui.mouseDown()
    time.sleep(3)
    pyautogui.mouseUp()
    time.sleep(1)
    pyautogui.press('g')
    return

#(90, 110, 53) (58, 56, 28)
# getPosition()
print(options)
choice = input()
time.sleep(2)
match (choice):
    case '1' :
        autoPressG()
    case '2' :
        autoMine()
    case '3' :
        autoLog()
    case '4':
        autoFish()
    case '5':
        getPosition()
    case '6':
        testdo()