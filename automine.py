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
        pos = pyautogui.locateOnScreen('images/copper_ore.png',confidence=0.5)
        if pos:
            pyautogui.moveTo(pos[0]+40, pos[1]+50)
            time.sleep(0.5)
            pyautogui.leftClick()
            time.sleep(5)
            pyautogui.press('g')
            time.sleep(4)
        else: time.sleep(0.5)

def autoLog():
    counter = 0
    direction = [[1275,412],[666,631]]
    
    
    while True:
        pos = pyautogui.locateOnScreen('images/giant_mushroom.png',confidence=0.5)
        print(pos)
        if pos:
            pyautogui.moveTo(pos[0]+40, pos[1]+50)
            time.sleep(0.5)
            pyautogui.leftClick()
            time.sleep(1)
            pyautogui.press('g')
            time.sleep(2)
            while True:
                time.sleep(5)
                pos = pyautogui.locateOnScreen('images/gathering.png',confidence=0.99)
                if pos:
                    print('logging')
                else:
                    print('done logging')
                    walkToNextTree(direction[counter%2])
                    counter = counter + 1
                    break
        else:
            walkToNextTree(direction[counter%2])
            counter = counter + 1
            time.sleep(0.5)
            
def walkToNextTree(direction):
    pyautogui.moveTo(direction[0], direction[1])
    pyautogui.mouseDown()
    time.sleep(2.3)
    pyautogui.mouseUp()
    time.sleep(1)
    return
        
def autoFish():
    pyautogui.press('e')
    while True:
        pos = pyautogui.locateOnScreen('images/fish_mark.png',confidence=0.80)
        if pos:
            pyautogui.press('e')
            time.sleep(6)
            pyautogui.press('e')
        else:
            time.sleep(0.2)
            
    
def getPosition():
    im = pyautogui.screenshot()
    
    while True:
        print(pyautogui.position())
        time.sleep(0.1)
        
def testdo():
    pyautogui.moveTo(1275, 412)
    pyautogui.mouseDown()
    time.sleep(2.3)
    pyautogui.mouseUp()
    time.sleep(1)
    pyautogui.press('g')
    return

#Point(x=666, y=631)
#Point(x=1275, y=412)
# getPosition()
# print(options)
# choice = input()
time.sleep(2)
# match (choice):
#     case '1' :
#         autoPressG()
#     case '2' :
#         autoMine()
#     case '3' :
#         autoLog()
#     case '4':
#         autoFish()
#     case '5':
#         getPosition()
#     case '6':
#         testdo()