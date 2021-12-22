# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 15:17:06 2021

@author: User
"""

from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

html = urlopen('http://www.pythonscraping.com')
bs = BS(html, 'html.parser')
imageLocation = bs.find('img', {'src':'https://pythonscraping.com/wp-content/uploads/2021/08/logo01.png'})['src']  
#<img class="pagelayer-img pagelayer-wp-title-img" src="https://pythonscraping.com/wp-content/uploads/2021/08/logo01.png"/>得到scr後面那段網址
 

print(imageLocation)

urlretrieve('https://pythonscraping.com/wp-content/uploads/2021/08/logo01.png', 'logo.jpg')
