# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 14:03:54 2021

@author: User
"""

import csv 
from urllib.request import urlopen
from bs4 import BeautifulSoup as BS

html = urlopen('https://www.taiwanlottery.com.tw/lotto/superlotto638/history.aspx')
bs = BS(html, 'html.parser')

table = bs.find('table', {'id':'SuperLotto638Control_history1_dlQuery'})
#rows = table.find('table', {'class':"table_org td_hm"})

rows_bs4 = table.find_all('tr')
del rows_bs4[1]
del rows_bs4[2]
del rows_bs4[3]

print(rows_bs4)

csvfile = open('lotterytest.csv', 'wt+') #https://stackoverflow.com/questions/23051062/open-files-in-rt-and-wt-modes
writer = csv.writer(csvfile)

try:
    for row in rows_bs4:
        csvRow=[]
        for cell in row.find_all(['td', 'th']):  #this waty can select all id are 'th' and 'td'
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
finally:
    csvfile.close()
