# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 12:15:37 2021

@author: User
"""

from urllib.request import urlopen
from io import StringIO
import csv



textPage = urlopen('http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt')

print(str(textPage.read(),'utf-8'))

data = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('ascii', 'ignore')

datafile = StringIO(data)   #包裝在裡面來節省ram
csvReader = csv.reader(datafile)

for row in csvReader:
    print(row)
