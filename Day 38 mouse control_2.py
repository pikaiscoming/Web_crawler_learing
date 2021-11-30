# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 21:37:59 2021

@author: 皮皮卡卡
"""
import pyautogui as gui
import cv2
import numpy as np
print(gui.position())
gui.moveTo(1225, 800, duration=0.5)
gui.scroll(-200) #postive up and nagative go down

#we can surf the url: https://mouseinfo.readthedocs.io/

img = gui.screenshot() #region = (0, 0, 400, 800)
open_cv_image = np.array(img) 
# Convert RGB to BGR 其他的PIL 也適用RGB 只有opencv適用BGR
fig = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)
cv2.imshow('frame', fig)
cv2.waitKey(0)
cv2.destroyAllWindows()