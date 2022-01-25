# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 12:41:58 2022

@author: pikachu
"""

'''
<!doctype html>
<html dir="ltr" lang="zh">
  <head>
    <meta charset="utf-8">
    <title>新分頁</title>
    <style>
      body {
        background: #CBDCF7;
        margin: 0;
      }

      #backgroundImage {
        border: none;
        height: 100%;
        pointer-events: none;
        position: fixed;
        top: 0;
        visibility: hidden;
        width: 100%;
      }

      [show-background-image] #backgroundImage {
        visibility: visible;
      }
    </style>
  </head>
  <body>
    <iframe id="backgroundImage" src="chrome-untrusted://new-tab-page/custom_background_image?url=https%3A%2F%2Flh5.googleusercontent.com%2Fproxy%2FE60bugMrz3Jw0Ty3vD1HqfrrabnAQGlHzIJjRadV1kDS_XSE0AtWuMnjW9VPvq1YeyPJK13gZw63TQYvh2RlaZq_aQm5xskpsgWW1l67gg3mkYaZr07BQqMV47onKA%3Dw3840-h2160-p-k-no-nd-mv"></iframe>
    <ntp-app></ntp-app>
    <script type="module" src="new_tab_page.js"></script>
    <link rel="stylesheet" href="chrome://resources/css/text_defaults_md.css">
    <link rel="stylesheet" href="shared_vars.css">
  </body>
</html>
'''
import os
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By # new one
from selenium.webdriver.chrome.service import Service #new one

#find_element_by_xxx('')
#find_element(By.xxx, '')



# PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
# DRIVER_BIN = os.path.join(PROJECT_ROOT, "chromedriver")

# s = Service(DRIVER_BIN)
# browser = webdriver.Chrome(service=s) #to solve the commands are deprecated.
browser = webdriver.Chrome()

browser.get('https://2048game.com/')
browser.maximize_window()
#linkElem = browser.find_element_by_link_text('Automate the Boring Stuff with Python')
#linkElem.click()
htmlElem = browser.find_element(By.TAG_NAME,'html')     #按鍵都傳給他 改成用Ｂy
#htmlElem.send_keys(Keys.PAGE_DOWN)

for i in range(100):

    htmlElem.send_keys(Keys.DOWN)
    htmlElem.send_keys(Keys.RIGHT)
    htmlElem.send_keys(Keys.LEFT)
    htmlElem.send_keys(Keys.UP)































