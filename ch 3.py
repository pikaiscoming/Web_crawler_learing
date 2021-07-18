# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 09:57:31 2021

@author: User
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
import re
import datetime
import random


html = urlopen('http://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/')
bs = BS(html, 'html.parser')

'''
for link in bs.find_all('a'):   #'a'超連結的標籤，用href取得
    if 'href' in link.attrs:
        print(link.attrs['href'])
        
for link1 in bs.find('div', {'id':'bodyContent'}).find_all(
    'a', href=re.compile('^(/wiki/)((?!:).)*$')):
    if 'href' in link1.attrs:
        print(link.attrs['href'])
'''        
#print(bs.find('img',
              #{'src':'//upload.wikimedia.org/wikipedia/commons/thumb/9/98/Kevin_Bacon_Cannes_2004.jpg/170px-Kevin_Bacon_Cannes_2004.jpg'}))

for child in bs.find("title").children:
    print(child)


random.seed(datetime.datetime.now())    #today 的數字變成一個亂碼

'''
def getlink(aurl):
    html = urlopen('http://en.wikipedia.org{}'.format(aurl))
    bs = BS(html, 'html.parser')
    return bs.find('div', {'class':'vector-body'}).find_all('a',href=re.compile('^(/wiki/)((?!:).)*$'))

links = getlink('/wiki/Kevin_Bacon')
while len(links) > 0:
    newarticle = links[random.randint(0, len(links)-1)].attrs['href']
    print(newarticle)
    links=getlink(newarticle)
'''