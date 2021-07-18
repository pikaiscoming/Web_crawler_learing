# -*- coding: utf-8 -*-
"""
Created on Wed Jul  7 11:45:00 2021

@author: User
"""

from urllib.request import urlopen 
from bs4 import BeautifulSoup as BS
import re 


pages = set()    #set can let all of elements in it are different

def getlink(url):
    global pages   #全域變數
    html = urlopen('http://en.wikipedia.org{}'.format(url))
    bs = BS(html,  'html.parser')
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        
        if 'herf' in link.attrs:
            
            if link.attrs['href'] not in pages:
                
                #We have encourageed a new page 
                newpage = link.attrs['href']
                print(newpage)
                pages.add(newpage)
                getlink(newpage)
                

getlink('')
                
    

#design a new web crawler. add the condition if we face the error 

def getlink1(url):
    global pages
    html = urlopen('http://em.wikipedia.org{}'.format(url))
    bs = BS(html, 'html.parser')
    try:
        print(bs.h1.get_txet())
        print(bs.find({'id':'mw-content-text'}).find_all('p')[0]) #the first term of 標籤
        print(bs.find({'id':'ca-edit'}).find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something! Continuing.')
        
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #we have to get another one
                newpage = link.attrs['href']
                print('-'*20)
                print(newpage)
                pages.add(newpage)
                getlink(newpage)
getlink1('Apple')
                
        
    
    
