# -*- coding: utf-8 -*-
"""
Created on Mon Jul 12 19:15:56 2021

@author: User
"""

'''
get the url and title from another web
'''

import requests 
from bs4 import BeautifulSoup as BS

class Content:
    
    def __init__(self, url, title, body):
        self.url = url
        self.title = title
        self.body = body
        
    def print(self):
        print('Title: {}'.format(self.title))
        print('URL: {}'.format(self.url))
        print(self.body)
        
        
class Website:  #網站架構資訊

    def __init__(self, name, url, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.titleTag = titleTag
        self.bodyTag = bodyTag
    
class Crawler:
    
    def getpage(self, url):
        try :
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BS(req.text, 'html.parser')
        
    def safeget(url, pageobj, selector):
        selectedElems = pageobj.select(selector)
        if selectedElems is not None and len(selectedElems)>0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''
    
    def parse(self, site, url): #指定要擷取的內容
        bs = self.getpage(url)  #用self去代替某個名子，看我們怎麼命名這個class
        if bs is not None:
            title = self.safeget(bs, site.titleTag)  #ㄍwe use select to find 'tag' especially
            body = self.safeget(bs, site.bodyTag)
            if title != '' and body != '':
                content=Content(url, title, body)
                content.print()
                
        
crawler = Crawler()

siteData = [    #save the method to get titles in different websites. here are 4 website.  
    ['O\'Reilly Media', 'http://oreilly.com', 'h1', 'section#product-description'], 
    ['Reuters', 'http://reuters.com', 'h1', 'div.StandardArticleBody_body_1gnLA'],
    ['Brookings', 'http://www.brookings.edu', 'h1', 'div.post-body'],
    ['New York Times', 'http://nytimes.com', 'h1', 'p.story-content']
    ]

websites=[]
for row in siteData:
    websites.append(Website(row[0], row[1], row[2], row[3]))
    
crawler.parse(websites[0], 'http://shop.oreilly.com/product/'\
              '0636920028154.do') #可以下一航繼續輸入且不會被分開
crawler.parse(websites[1], 'http://www.reuters.com/article/'\
              'us-usa-epa-pruitt-idUSKBN19W2D0')
#crawler.parse(websites[2], 'http://brookings.edu/blog/'\
              #'techtank/2016/03/01/idea-to-retire-old-methods-of-policy-education/')
crawler.parse(websites[3], 'http://www.nytimes.com/2018/01/'\
              '28/business/energy-environment/oil-boom.html')
    
