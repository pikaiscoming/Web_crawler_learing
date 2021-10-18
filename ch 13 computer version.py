# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 17:08:13 2021

@author: pikachu
"""

import cv2
from matplotlib import pyplot as plt
import pytesseract
from pytesseract import Output


image = cv2.imread('D:\web crawler\S__410435590.jpg')
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret, img = cv2.threshold(img, 100, 255, cv2.THRESH_TOZERO)  #0 is black

result = pytesseract.image_to_string(img, lang='eng')

arr = result.split('\n')[0:-1]
result = '\n'.join(arr)


print(result)



cv2.imshow('frame', img)
cv2.waitKey(0)

cv2.destroyAllWindows()
