import time
import pyautogui
import os

time.sleep(2)
color = (109, 191, 1)
# ore_pos = pyautogui.locateOnScreen("test.png")
# posXY = pyautogui.position() 
# print(posXY, pyautogui.pixel(posXY[0], posXY[1]) )

def findGather ():
    s = pyautogui.screenshot()
    for x in range(s.width):
        for y in range(s.height):
            if s.getpixel((x, y)) == color:
                print('found it')
                print(x)
                print(y)
                pyautogui.moveTo(x+40, y+50)  # do something here
                time.sleep(0.5)
                pyautogui.leftClick()
                time.sleep(5)
                pyautogui.press('g')
                time.sleep(4)
                return

while True:
    findGather()