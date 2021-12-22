# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 11:22:32 2021

@author: pikachu
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
import re
import string
from collections import Counter



def cleansentence(sentence):
    sentence = sentence.split(' ')
    sentence = [word.strip(string.punctuation+string.whitespace)
                for word in sentence]
    sentence = [word for word in sentence if len(word)>1
                or (word.lower() == 'a' or word.lower() == 'i')]
    
    return sentence

def cleaninput(content):
    content = re.sub('\n|[[\d+\]]', ' ', content)
    content = bytes(content, 'UTF-8')
    content = content.decode('ascii', 'ignore') #可以殺掉所有的跳脫字元
    sentences = content.split('. ')

    return [cleansentence(sentence) for sentence in sentences]

def getngramsfromsentence(content, n):
    output = []
    
    for i in range(len(content)+1):
        output.append(content[i:i+1])
        
    return output

def getngrams(content, n):
    content = cleaninput(content)
    ngrams = []
    for sentence in content:
        ngrams.extend(getngramsfromsentence(sentence, n))
    return ngrams


html = urlopen('http://en.wikipedia.org/wiki/Python_(programming_language)')
bs = BS(html, 'html.parser')
content = bs.find('div', {'id':'mw-content-text'}).get_text()
ngrams = getngrams(content, 2)
print(ngrams)
print('2-gram count is: '+str(len(ngrams)))
