# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 14:16:23 2021

@author: User
"""
import os
import csv

csvfile = open('test.csv','w+')
try:
    writer = csv.writer(csvfile)
    writer.writerow(('number','number plus 2', 'number times 2'))
    for i in range(10):
        writer.writerow((i, i+2, i*2))

finally:
    csvfile.close()
                        
