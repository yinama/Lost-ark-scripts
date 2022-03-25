import time
import pyautogui
import os

time.sleep(2)
Orecolor = (109, 191, 1)
Treecolor = (116, 203, 1)
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

while True:
    print('looping')
    time.sleep(2)   
    getTreeLocation()
