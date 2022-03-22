from imutils.object_detection import non_max_suppression
import numpy as np
import time
import cv2
import pyautogui
import os
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

imgWidth=1920
imgHeight=1920

def text_detector():
    
    image = pyautogui.screenshot()
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    orig = image.copy()
    #myScreenshot.save(r'C:\Users\18044\Desktop\test.png')
    net = cv2.dnn.readNet("frozen_east_text_detection.pb")

    

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
        boundary = 2
        
        cv2.rectangle(orig, (startX, startY), (endX, endY), (0, 255, 0), 2)
        
        text = orig[startY-boundary:endY+boundary, startX - boundary:endX + boundary]
        text = cv2.cvtColor(text.astype(np.uint8), cv2.COLOR_BGR2GRAY)
        textRecongized = pytesseract.image_to_string(text)
        orig = cv2.putText(orig, textRecongized, (endX,endY+5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2, cv2.LINE_AA) 
        
    directory = r'C:\Users\18044\Desktop'
    os.chdir(directory)
    cv2.imwrite('test.png', orig)
    
    return orig
    

def text_interreptor(img):
    for i in range(0,2):
        img = cv2.resize(img, (imgWidth,imgHeight), interpolation = cv2.INTER_AREA)
        orig = cv2.resize(img, (imgWidth,imgHeight), interpolation = cv2.INTER_AREA)
        textDetected = text_detector(orig)
        cv2.imshow("Orig Image",orig)
        cv2.imshow("Text Detection", textDetected)
        time.sleep(2)
        k = cv2.waitKey(30)
        if k == 27:
            break

def main():
    print("main")
    text_detector()
    #text_interreptor(img)
    
if __name__ == "__main__":
    main()