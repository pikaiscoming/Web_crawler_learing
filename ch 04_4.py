# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 14:03:47 2021

@author: User
"""

class Website:
    """
    to get the information from website
    """
    def __init__(self, name, url, targetPattern, absoluteUrl, titleTag, bodyTag):
        self.name = name
        self.url = url
        self.targetPattern = targetPattern
        self.absoluteUrl = absoluteUrl
        self.titleTag = titleTag
        self.bodyTag = bodyTag
        
class Content:
    """
    article or website basic class.
    """
    def __init__(self, url, title, body):
        self.title = title
        self.body = body
        self.url = url
    
    def print(self):
        """
        use to print information.
    
        """       
        print('title: {}'.format(self.title),end='\n\n')
        print('body: {}'.format(self.body),end='\n\n')
        print('url: {}'.format(self.url))
        
import re 
import requests
from bs4 import BeautifulSoup as BS

class Crawler():
    """
    從首頁開始，找出內部的每個連結
    """
    def __init__(self, site):
        self.site = site
        self.visited = []
    
    def getpage(self, url):
        try:
            req = requests.get(url)
        except requests.exceptions.RequestException:
            return None
        return BS(req.text, 'html.parser')
    
    def safeget(self, pageobj, selector):
        selectedElems = pageobj.select(selector)
        if selectedElems is not None and len(selectedElems)>0:
            return '\n'.join([elem.get_text() for elem in selectedElems])
        return ''
    
    def parse(self, site, url): #指定要擷取的內容
        bs = self.getpage(url)  #用self去代替某個名子，看我們怎麼命名這個class
        if bs is not None:
            title = self.safeget(bs, self.site.titleTag)  #we use select to find 'tag' especially
            body = self.safeget(bs, self.site.bodyTag)
            if title != '' and body != '':
                content=Content(url, title, body)
                content.print()
    
    def crawl(self):
        """
        從首頁去抓網頁
        """
        bs = self.getpage(self.site.url)
        targetpages = bs.findAll("a", href=re.compile(self.site.targetPattern))
        for targetpage in targetpages:
            targetpage = targetpage.attrs['href']
            if targetpage not in self.visited:
                self.visited.append(targetpage)
                if not self.site.absoluteUrl:
                    targetpage = '{}{}'.format(self.site.url, targetpage)
                self.parse(targetpage)
selector1 = {'class':'Text__text___3eVx1j Text__dark-grey___AS2I_p Text__regular___Bh17t- Text__large___1i0u1F Body__base___25kqPt Body__large_body___3g04wK ArticleBody__element___3UrnE'}            
reuters = Website('Reuters', 'https://www.reuters.com', '^(/article/)', False, 'h1', selector1)
crawler = Crawler(reuters)
crawler.crawl()


        
