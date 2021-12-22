# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 12:40:21 2021

@author: User
"""

'''
By searching website to crawler web
'''
class Content:
    """
    article or website basic class.
    """
    def __init__(self, topic, url, title, body):
        self.topic = topic
        self.title = title
        self.body = body
        self.url = url
    
    def print(self):
        """
        use to print information.
    
        """       
        print("New article found for topic: {}".format(self.topic))
        print('title: {}'.format(self.title))
        print('body: {}'.format(self.body))
        print('url: {}'.format(self.url))
        
class Website:
    """
    to get the information from website
    """
    def __init__(self, name, url, searchUrl, resultListing, resultUrl, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.searchUrl = searchUrl
        self.resultListing = resultListing
        self.resultUrl = resultUrl
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag
        
import requests
from bs4 import BeautifulSoup as BS

class Crawler:
    
    def getpage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BS(req.text, 'html.parser')
    
    def safeget(self, pageObj, selector):
        childObj = pageObj.select(selector)
        if childObj is not None and len(childObj)>0:
            return childObj[0].get_text()   #different with .text 感覺這個是一種呼叫的方法，用get可以獲得更多的控制
        return ''
    
    def search(self, topic, site):
        """
        all websites will be collected to avoid finding the same website.

        """
        bs = self.getpage(site.searchUrl+topic) #很多網站的搜尋都長這樣:網頁加上搜尋看你想在這個網站查什麼topic
        searchResults = bs.select(site.resultListing)
        for result in searchResults:
            url = result.select(site.resultUrl)[0].attrs["href"]
            #檢查是否為絕對或相對url
            if(site.absoluteUrl):
                bs = self.getpage(url)
            else:
                bs = self.getpage(site.url+url)
            if bs is None:
                print('Something was wrong with that page or Url. skipping!')
                return
            title = self.safeget(bs, site.titleTag)
            body = self.safeget(bs, site.bodyTag)
            if title != '' and body != '':
                content = Content(topic, url, title, body)
                content.print()

crawler = Crawler()

sitedata = [
    ['O\'Reilly Media', 'http://oreilly.com', 
     'https://ssearch.oreilly.com/?q=','article.product-result',
     'p.title a', True, 'h1', 'section#product-description'],
    ['Brookings', 'http://www.brookings.edu',
    'https://www.brookings.edu/search/?s=',
    'div.list-content article', 'h4.title a', True, 'h1',
    'div.post-body']
    ]
sites = []
for row in sitedata:
    sites.append(Website(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]))
    
topics = ['python']
for topic in topics:
    print('GETTING INFO ABOUT: ' + topic)
    for targetSite in sites:
        crawler.search(topic, targetSite)
    
