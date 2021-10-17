# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 10:33:15 2021

@author: pikachu
"""
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = Image.open(r'D:\web crawler\test1.png')

result = pytesseract.image_to_string(img, lang='eng')

''' 
後面兩行解決無法顯示的問題 
'''
arr = result.split('\n')[0:-1]
result = '\n'.join(arr)


print(result)
#print(pytesseract.__version__)