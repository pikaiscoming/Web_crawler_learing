# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 10:34:49 2021

@author: pikachu
"""
import pytesseract
import cv2
from pytesseract import Output
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def cleanfile(filePath, threshold):
    img = cv2.imread(filePath)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img = cv2.threshold(img, threshold, 255, cv2.THRESH_TOZERO)  #0 is black
    return img

def getconfidence(img):
    data = pytesseract.image_to_data(img, output_type=Output.DICT) #box boundaries, confidences, and other information.
    text = data['text']
    confidences = []
    numCharts = []
    
    for i in range(len(text)):
        #a = data['conf'][i]
        if  float(data['conf'][i]) > -1:
            confidences.append(float(data['conf'][i]))
            numCharts.append(len(text[i]))
            
    return np.average(confidences, weights=numCharts), sum(numCharts)

filePath = 'D:\web crawler\S__410435590.jpg'

for threshold in range(40, 200, 10):
    img = cleanfile(filePath, threshold)
    scores = getconfidence(img)
    print('threshold: '+ str(threshold) + ', confidence: '
          + str(scores[0]) + 'numChars ' +str(scores[1]))