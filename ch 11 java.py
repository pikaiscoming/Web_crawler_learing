# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 11:49:05 2021

@author: pikachu
"""
import requests
from selenium import webdriver
import time

driver = webdriver.PhantomJS() #Seem we don't need to write down the path.
driver.get('http://pythonscraping.com/pages/javascript/ajaxDemo.html')
time.sleep(3) #because html will change after 2 sec.
print(driver.find_element_by_id('content').text)
driver.close()

