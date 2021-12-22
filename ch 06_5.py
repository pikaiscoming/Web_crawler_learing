# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 10:20:55 2021

@author: User
"""

import pymysql
conn = pymysql.connect(host='127.0.0.1',
                       user='root', passwd='Lf2mnhmymjmnmyh', db='mysql')

cur = conn.cursor()
cur.execute('USE scraping')
cur.execute('SELECT * FROM pages WHERE id=1')
print(cur.fetchone())   #呼叫游標
cur.close()
conn.close()
