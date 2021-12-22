# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 21:17:04 2021

@author: User
"""

import requests
from bs4 import BeautifulSoup as BS

class Content:
    
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body
        
def getpage(url):
    req = requests.get(url) #download html
    return BS(req.text, 'html.parser')  #req.text is a url 
    
def scrapeNYTimes(url):
    bs = getpage(url)
    title = bs.find("h1").text
    lines = bs.find_all("p", {'class':'story-content'})
    body = '\n'.join([line.text for line in lines]) #for every line in lines and line get text something join every space between list elements
    return Content(url, title, body)
    
def scrapeBrookings(url):
    bs = getpage(url)
    title = bs.find("h1").text
    body = bs.find('div', {'class':'post-body'}).text
    return Content(url, title, body)

url = 'http://www.brookings.edu/blog/future-development/2018/01/26/delivering-inclusive-urban-access-3-uncomfortable-truths/'

content = scrapeBrookings(url)
print('Title: {}'.format(content.title))
print('URL: {}'.format(content.url))
print(content.body)


url ='http://www.nytimes.com/2018/01/25/opinion/sunday//silicon-valley-immortality.html'

content = scrapeNYTimes(url)
print('Title: {}'.format(content.title))
print('URL: {}\n'.format(content.url))
print(content.body)


