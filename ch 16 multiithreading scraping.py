# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 18:31:23 2021

@author: pikachu
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
import re
import random

import time, threading

start = time.time()

def get_links(thread_name, bs):
    print('Getting links in {}'.format(thread_name))
    return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

def scrape_article(thread_name, path):
    html = urlopen('http://en.wikipedia.org{}'.format(path))
    time.sleep(3)
    bs = BS(html, 'html.parser')
    title = bs.find('h1').get_text()
    #newname = path[6:]
    print('Scraping {} in thread {}'.format(title,thread_name))
    links = get_links(thread_name, bs)
    error = time.time()-start
    if len(links) > 0 and int(error)<15:
        
        newArticle = links[random.randint(0, len(links)-1)].attrs['href'] #scraping the web which is one of all links we get
        print(newArticle)
        scrape_article(thread_name, newArticle)


try:

    thread_1 = threading.Thread(target=scrape_article, args = ('thread1', '/wiki/Kevin_Bacon'))
    thread_2 = threading.Thread(target=scrape_article, args = ('thread2', '/wiki/Monty_Python'))
    thread_1.start()
    thread_2.start()

except:
    print('Error: unalbe to start threads')
    