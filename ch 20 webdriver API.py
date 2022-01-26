# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 12:18:58 2022

@author: pikachu
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By # new one

chrome_options = Options() # 啟動無頭模式
chrome_options.add_argument('--headless')  #規避google bug
chrome_options.add_argument('--disable-gpu')
'''
PhantomJS is replaced by this.
'''
driver = webdriver.Chrome(options=chrome_options)

driver.get('https://histock.tw/stock/3711')

elem = driver.find_element(By.XPATH, '/html/head/title') #xpath 絕對路徑 /html/body/...
#elem2 = driver.find_element(By.XPATH, "//meta[@id='keywords']") #@ is select attribute
#elem 3 = driver.find_element(By.XPATH, ")
print(elem.read())

driver.quit()



