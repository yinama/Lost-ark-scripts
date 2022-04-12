import PySimpleGUI as sg                      
from automine import autoPressG,autoMine,autoLog,autoFish

layout = [[sg.Button('Auto Press G',size=(12,2))],
          [sg.Button('Auto Mine', size=(12,2))],
          [sg.Button('Auto Logging', size=(12,2))],
          [sg.Button('Auto Fishing', size=(12,2))]]

window = sg.Window('Lost Ark Script', layout,size=(600, 400)) 

event, values = window.read()             

if event == 'Auto Press G':
    autoPressG()
elif event == 'Auto Mine':
    autoMine()
elif event == 'Auto Mine':
    autoLog()
elif event == 'Auto Mine':
    autoFish()        