import PySimpleGUI as sg             
import time

from cv2 import DrawMatchesFlags_DRAW_RICH_KEYPOINTS         
from automine import autoPressG,autoMine,autoLog,autoFish

layout = [[sg.Button('Auto Press G',size=(12,2))],
          [sg.Button('Auto Mine', size=(12,2))],
          [sg.Button('Auto Logging', size=(12,2))],
          [sg.Button('Auto Fishing', size=(12,2))],
          [sg.Button('Stop', size=(12,2))]]

window = sg.Window('Lost Ark Script', layout,size=(600, 400)) 

while True:
    event, values = window.read()             
    if event:
        time.sleep(2)
        if event == sg.WIN_CLOSED:
            break
        if event == 'Auto Press G':
            autoPressG()
        elif event == 'Auto Mine':
            autoMine()
        elif event == 'Auto Logging':
            autoLog()
        elif event == 'Auto Fishing':
            autoFish()