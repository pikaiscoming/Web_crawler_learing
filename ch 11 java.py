# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 11:49:05 2021

@author: pikachu
"""
import requests
from selenium import webdriver
import time

driver = webdriver.PhantomJS(executable_path=r'D:\code\Lib\site-packages\selenium\webdriver\phantomjs\webdriver.py')
driver.get('http://pythonscraping.com/pages/javescript/ajaxDemo.html')
time.sleep(3) #because html will change after 2 sec.
print(driver.find_element_by_id('content').text)
driver.close()

