# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 13:03:59 2021

@author: User
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
import re

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
b = BS(html.read(), 'html.parser')
'''
findAll(tag, attributes, text, limit, keyword)
find(tag, attributes, recursive, text, keyword)
'''
nameList = b.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

#for name in nameList:
    #print(name.get_text())
    
'''
b.find_all(id='text')
b.find_all('',{'id':'text'})
'''

html1 = urlopen('http://www.pythonscraping.com/pages/page3.html')
b1 = BS(html1, 'html.parser')

#for child in b1.find('table',{'id':'giftList'}).children:
    #print(child)
   
print(b1.find('img',
              {'src':'../img/gifts/img1.jpg'}).parent.previous_sibling.get_text())

for silbling in b1.find('table', {'id':'giftList'}).tr.next_siblings: #不包括本身，沒有物件item, descripution等等東西
    print(silbling)
    
images = b1.find_all('img',
                     {'src':re.compile('\.\.\/img\/gifts/img.*\.jpg')}) #常規表示法可以避免找到不需要的圖片

for image in images:
    print(image['src'])
    #print(type(image))
    
#lambda can be used in BeautifulSoup to sort which texts should be print

b1.find_all(lambda tag: len(tag.attrs)==2)
