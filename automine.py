from imutils.object_detection import non_max_suppression
import numpy as np
import time
import cv2
import pyautogui
import os

image = pyautogui.screenshot()
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
orig = image.copy()
#myScreenshot.save(r'C:\Users\18044\Desktop\test.png')
net = cv2.dnn.readNet("frozen_east_text_detection.pb")

imgWidth=1920
imgHeight=1920

(H, W) = image.shape[:2]
(newW, newH) = (imgWidth, imgHeight)

rW = W / float(newW)
rH = H / float(newW)
image = cv2.resize(image, (newW, newH))

(H, W) = image.shape[:2]

blob = cv2.dnn.blobFromImage(image, 1.0, (W, H), (123.68, 116.78, 103.94), True, False)

outputLayers = []
outputLayers.append("feature_fusion/Conv_7/Sigmoid")
outputLayers.append("feature_fusion/concat_3")

net.setInput(blob)
output = net.forward(outputLayers)
scores = output[0]
geometry = output[1]

(numRows, numCols) = scores.shape[2:4]
rects = []
confidences = []

for y in range (0, numRows):
    scoresData = scores[0, 0, y]
    xData0 = geometry[0, 0, y]
    xData1 = geometry[0, 1, y]
    xData2 = geometry[0, 2, y]
    xData3 = geometry[0, 3, y]
    anglesData = geometry[0, 4, y]
    
    for x in range(0, numCols):
        if scoresData[x] < 0.5:
            continue
        
        (offsetX, offsetY) = (x * 4.0, y * 4.0)
        
        angle = anglesData[x]
        cos = np.cos(angle)
        sin = np.sin(angle)
        
        h = xData0[x] + xData2[x]
        w = xData1[x] + xData3[x]
        
        endX = int(offsetX + (cos * xData1[x]) + (sin * xData2[x]))
        endY = int(offsetY - (sin * xData1[x]) + (cos * xData2[x]))
        startX = int(endX - w)
        startY = int(endY - h)
        
        rects.append((startX, startY, endX, endY))
        confidences.append(scoresData[x])
        
boxes = non_max_suppression(np.array(rects), probs=confidences)

for (startX, startY, endX, endY) in boxes:
    startX = int(startX * rW)
    startY = int(startY * rH)
    endX = int(endX * rW)
    endY = int(endY * rH)
    
    cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 255, 0), 2)
    
directory = r'C:\Users\18044\Desktop'
os.chdir(directory)
cv2.imwrite('test.png', orig)