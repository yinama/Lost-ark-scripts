import time
import pyautogui
import os

#Time.sleep(2)
Orecolor = (109, 191, 1)
Treecolor = (116, 203, 1)

#topleft(753, 434)

# ore_pos = pyautogui.locateOnScreen("test.png")
# posXY = pyautogui.position() 
# print(posXY, pyautogui.pixel(posXY[0], posXY[1]) )

# Doesn't work so well, using getpixel
# def findGather ():
#     s = pyautogui.screenshot()
#     for x in range(s.width):
#         for y in range(s.height):
#             #if s.getpixel((x, y)) == Treecolor:
#             #if pyautogui.pixelMatchesColor(x, y, Treecolor, tolerance=10):
#                 print('found it')
#                 print(x)
#                 print(y)
#                 pyautogui.moveTo(x+40, y+50)  # do something here
#                 time.sleep(0.5)
#                 pyautogui.leftClick()
#                 time.sleep(5)
#                 pyautogui.press('g')
#                 time.sleep(4)
#                 return

options = ['1-auto press g','2-auto mine', '3-auto log']

#just press g
def autoPressG():
    while True:
        pyautogui.press('g')
        time.sleep(0.5)

#new method with locateOnScreen
def getOreLocation():
    pos = pyautogui.locateOnScreen('copper_ore.png',confidence=0.5)
    print(pos)
    pyautogui.moveTo(pos[0]+40, pos[1]+50)
    time.sleep(0.5)
    pyautogui.leftClick()
    time.sleep(5)
    pyautogui.press('g')
    time.sleep(4)
    return

def getTreeLocation():
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
        
    
def getPosition():
    im = pyautogui.screenshot()
    
    while True:
        position = pyautogui.position()
        print(im.getpixel(position))
        time.sleep(0.1)
        
# getPosition()

choice = input(options)
time.sleep(2)
match (choice):
    case 1 :
        autoPressG()
    case 2 :
        getOreLocation()
    case 3 :
        getTreeLocation()
    #getTreeLocation()
    #autoPressG()
    #print(pyautogui.position())