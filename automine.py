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
    duration = [2.0, 2.1]
    
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
                    walkToNextTree(direction[counter%2], duration[counter%2])
                    counter = counter + 1
                    break
        else:
            walkToNextTree(direction[counter%2], duration[counter%2])
            counter = counter + 1
            time.sleep(0.5)
            
def walkToNextTree(direction, duration):
    time.sleep(2)
    pyautogui.moveTo(direction[0], direction[1])
    pyautogui.mouseDown()
    print(duration)
    time.sleep(duration)
    pyautogui.mouseUp()
    time.sleep(1)
    return
        
def autoFish():
    timer = 0
    pyautogui.press('e')
    while True:
        pos = pyautogui.locateOnScreen('images/fish_mark.png',confidence=0.75)
        if pos:
            print('found fish mark')
            pyautogui.press('e')
            print('pull fishing rod')
            time.sleep(8)
            print('fishing again')
            pyautogui.press('e')
        elif timer > 200:   
            pyautogui.press('e')
            timer = 0
        else:
            time.sleep(0.2)
            
def autoPlaySheetMusic():
    while True:
        pos = pyautogui.locateOnScreen('images/play.png',confidence=0.80)
        pyautogui.moveTo(pos)
        pyautogui.leftClick()
        time.sleep(20)
        
def autoRepairTradeTool():
    pyautogui.moveTo(pyautogui.locateOnScreen('images/guide.png',confidence=0.50))
    pyautogui.leftClick()
    time.sleep(0.5)
    pyautogui.moveTo(pyautogui.locateOnScreen('images/pets.png',confidence=0.80))
    pyautogui.leftClick()
    time.sleep(0.5)
    pyautogui.moveTo(pyautogui.locateOnScreen('images/remote_repair.png',confidence=0.90))
    pyautogui.leftClick()
    time.sleep(0.5)
    pyautogui.moveTo(pyautogui.locateOnScreen('images/repair_all.png',confidence=0.90))
    pyautogui.leftClick()
    time.sleep(0.5)
    pyautogui.moveTo(pyautogui.locateOnScreen('images/ok.png',confidence=0.90))
    pyautogui.leftClick()
    time.sleep(3)
    pyautogui.press('esc')
    pyautogui.press('esc')
    time.sleep(0.5)
    
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
# time.sleep(2)
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