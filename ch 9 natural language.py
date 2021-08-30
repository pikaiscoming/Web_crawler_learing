# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 10:55:08 2021

@author: pikachu
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string
from collections import Counter

def cleanSentence(sentence):    #把sentence中的word 分開 一個個處理
    sentence = sentence.split(' ')
    sentence = [word.strip(string.punctuation+string.whitespace) for word in sentence]      #確保只剩字母，且非字母的符號被消除
    sentence = [word for word in sentence if len(word) > 1 or (word.lower() == 'a' or word.lower() == 'i')]
    return sentence

def cleanInput(content):    #把content的所有字元處理
    content = content.upper()
    content = re.sub('\n', ' ', content)
    content = bytes(content, 'UTF-8')
    content = content.decode('ascii', 'ignore')
    sentences = content.split('. ')     #convert to a list which are made of sentences.
    return [cleanSentence(sentence) for sentence in sentences]      #put every sentence into function

def getNgramsFromSentence(content, n):
    output = []
    for i in range(len(content)-n+1):
        output.append(content[i:i+n])
    return output

def getNgrams(content, n):
    content = cleanInput(content)   #1 第一個接收到資訊的地方
    ngrams = Counter()  #都只剩一個個單字
    ngrams_list = []
    for sentence in content:
        newNgrams = [' '.join(ngram) for ngram in getNgramsFromSentence(sentence, n)] #每組ngram都被加入，從list to string.
        ngrams_list.extend(newNgrams)   #在組成list
        ngrams.update(newNgrams)    #放進dict且幫忙算出現次數
    return(ngrams)


content = str(
      urlopen('http://pythonscraping.com/files/inaugurationSpeech.txt').read(),
              'utf-8')
ngrams = getNgrams(content, 2)
print(ngrams)