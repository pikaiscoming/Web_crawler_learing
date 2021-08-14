# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 15:38:35 2021

@author: User
"""

#用來擷取wiki的表格資料

import csv
from urllib.request import urlopen 
from bs4 import BeautifulSoup as BS

html = urlopen('http://en.wikipedia.org/wiki/Comparison_of_text_editors')
bs = BS(html, 'html.parser')

table = bs.find_all('table', {'class':'wikitable'})[0]
rows = table.find_all('tr')

csvfile = open('editors.csv', 'w+') #https://stackoverflow.com/questions/23051062/open-files-in-rt-and-wt-modes
writer = csv.writer(csvfile)

try:
    for row in rows:
        csvRow=[]
        for cell in row.find_all(['td', 'th']):  #this waty can select all id are 'th' and 'td'
            csvRow.append(cell.get_text())
            writer.writerow(csvRow)
finally:
    csvfile.close()


