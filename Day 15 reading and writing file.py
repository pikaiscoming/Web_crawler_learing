# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 11:09:45 2021

@author: pikachu
"""
from pathlib import Path

import shelve #整個shelve像一個字典，可以去教出不同的檔案
import pprint

shelffile = shelve.open('mydata')
cats = ['a', 'b', 'c']
shelffile['cats'] = cats
shelffile.close()

spam = [{'name':'Zophie', 'desc':'chubby'}, {'name':'pooka', 'desc':'fluuffy'}]
print(pprint.pformat(spam))