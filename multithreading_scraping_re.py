# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 09:50:37 2021

@author: pikachu
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup as BS
import re
import random
import os
from multiprocessing import Process, Queue
import time, threading

'''this method can let two threads work together.'''

def task_delegator(taskQueue, urlsQueue):
    visited = ['/wiki/Kevin_Bacon', '/wiki/Monty_Python'] #ready to arriver url
    taskQueue.put('/wiki/Kevin_bacon')
    taskQueue.put('/wiki/Monty_python')
    while 1:
        if not urlsQueue.empty(): #是不是空的
            links = [link for link in urlsQueue.get() if link not in visited]
            for link in links:
                taskQueue.put(link)
                
            
    

def get_links(bs):
    links = bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))
    
    return [link.attrs['href'] for link in links]


def scrape_article(taskQueue, urlsQueue):
    while 1:
        
        while taskQueue.empty():
            time.sleep(0.1)
        path = taskQueue.get()    
        html = urlopen('http://en.wikipedia.org{}'.format(path))
        time.sleep(3)
        bs = BS(html, 'html.parser')
        title = bs.find('h1').get_text()
        #newname = path[6:]
        print('Scraping {} in thread {}'.format(title,os.getpid()))
        links = get_links(bs)
        urlsQueue.put(links)
        '''
        if len(links) > 0 and int(error)<15:
        
            newArticle = links[random.randint(0, len(links)-1)].attrs['href'] #scraping the web which is one of all links we get
            print(newArticle)
            scrape_article(thread_name, newArticle)

        '''
processes = []
taskQueue = Queue()
urlsQueue = Queue()
processes.append(Process(target=task_delegator, args=(taskQueue, urlsQueue)))
processes.append(Process(target=scrape_article, args=(taskQueue, urlsQueue)))
processes.append(Process(target=scrape_article, args=(taskQueue, urlsQueue)))

for p in processes:
    p.start()
    