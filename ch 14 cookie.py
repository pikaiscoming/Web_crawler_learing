# -*- coding: utf-8 -*-
"""
Created on Mon Nov 15 10:24:08 2021

@author: pikachu
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options() # 啟動無頭模式
chrome_options.add_argument('--headless')  #規避google bug
chrome_options.add_argument('--disable-gpu')
'''
PhantomJS is replaced by this.
'''
driver = webdriver.Chrome(options=chrome_options)

driver.get('http://pythonscraping.com')
driver.implicitly_wait(1)
savedcookie = driver.get_cookies()
print(savedcookie)

#driver.quit()
#change the cookie in different web

driver2 = webdriver.Chrome(options=chrome_options)
driver2.get('http://pythonscraping.com')
driver2.delete_all_cookies()
for cookie in savedcookie:
    driver2.add_cookie(cookie)
    
