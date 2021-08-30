# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 21:47:37 2021

@author: User
"""

import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

dwonloaddir = 'downloaded'
baseurl = 'http://pythonscraping.com'

def getabsoluteurl(baseurl, source):
    if source.startswith('http://www.'):
        url = 'http://{}'.format(source[11:])
    
    elif source.startswith('http://'):
        url = source
        
    elif source.startswith('www.'):
        url = source[4:]
        url = 'http://{}'.format(source)
    
    else:
        url = '{}/{}'.format(baseurl, source)
        
    if baseurl not in url:
        return None
    
    return url

def getdownloadpath(baseurl, absoluteurl, downloaddir):
    path = absoluteurl.replace('www.', '')
    path = path.replace(baseurl, '')
    path = downloaddir+path
    directory = os.path.dirname(path)
    
    
    if not os.path.exists(directory):
        os.makedirs(directory)
        
html = urlopen('http://www.pythonscraping.com')
bs = BS(html, 'html.parser')
downloadList = bs.find_all(src=True)

for download in downloadList:
    fileurl = getabsoluteurl(baseurl, download['src'])
    if fileurl is not None:
        print(fileurl)
        
urlretieve(fileurl, getdownloadpath(baseurl, absoluteurl, downloaddir))

'''
下載東西一樣要注意風險
'''
