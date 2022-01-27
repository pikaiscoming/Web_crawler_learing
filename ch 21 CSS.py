# -*- coding: utf-8 -*-
"""
Created on Thu Jan 27 12:39:54 2022

@author: pikachu
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

chrome_options = Options() # 啟動無頭模式
chrome_options.add_argument('--headless')  #規避google bug
chrome_options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://histock.tw/stock/3711')

elem = driver.find_element(By.CSS_SELECTOR,'#jsJquery') #id
elem2 = driver.find_element(By.CSS_SELECTOR, ".topnav2") #class
elem3 = driver.find_element(By.CSS_SELECTOR, "div") #tag
#elem4 = driver.find_element(By.CSS_SELECTOR, "[type='submit']") #attribute
elem5 = driver.find_element(By.CSS_SELECTOR, 'div>input') #div 下的所有input
print(elem)

driver.quit()

