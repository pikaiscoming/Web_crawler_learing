# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 21:45:06 2021

@author: User
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
from urllib.error import HTTPError

html = urlopen('http://pythonscraping.com/pages/page1.html')
b = BS(html.read(), 'html.parser')
print(b.h1)


try:
    html = urlopen('http://www.pythonscraping.com/pages/page1.html')
except HTTPError as e:
    print(e)
else:
    print('success')
    
def gettitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None 
    try:
        b = BS(html.read(), 'html.parser')
        title = b.body.h1
    except AttributeError as e:
        return None
    return title 

title = gettitle('https://www.youtube.com/watch?v=EaA6NlH80wg')
if title==None:
    print('Title cannot be found')
else:
    print(title)