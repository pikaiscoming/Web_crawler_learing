# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 14:59:16 2021

@author: pikachu
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

def getngrams(content, n):
    content = content.split(' ')
    output = []
    
    for i in range(len(content)+1):
        output.append(content[i:i+1])
        
    return output

def getngrams1(content, n):
    content = content.split(' ')
    output = []
    
    for i in range(len(content)+1):
        output.append(content[i:i+1])
        
    return output

html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bs = BS(html, 'html.parser')
content = bs.find('div', {'id':'mw-content-text'}).get_text()
ngrams = getngrams(content, 2)
print(ngrams)
print('2-gram count is: '+str(len(ngrams)))