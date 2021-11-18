# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 10:30:34 2021

@author: pikachu
"""

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.options import Options

chrome_options = Options() # 啟動無頭模式
chrome_options.add_argument('--headless')  #規避google bug
chrome_options.add_argument('--disable-gpu')
'''
PhantomJS is replaced by this.
'''
driver = webdriver.Chrome(options=chrome_options)
driver.get('http://pythonscraping.com/pages/itsatrap.html')
links = driver.find_elements_by_tag_name('a')

for link in links:
    if not link.is_displayed():
        print('The link {} is a trap'.format(link.get.attribute('href')))
        
fields = driver.find_element_by_tag_name('input')
for field in fields:
    if not field.is_dispalyed():
        print('Do not change value of {}'.format(field.get_attribute('name')))
        