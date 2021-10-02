# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 09:42:28 2021

@author: pikachu
"""

import requests

params = {'username':'pipi', 'password':'password'}
r = requests.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print('Cookie is set to:')
#print(r.cookies.get_dict())
print('Going to profile page...')
r = requests.get('http://pythonscraping.com/pages/cookies/welcome.php/profile.pgh',
                 cookies = r.cookies)   #發送參數給welcome.php檢查



print(r.text)

session = requests.Session()
s = session.post("http://pythonscraping.com/pages/cookies/welcome.php", params)
print('Cookie is set to:')
print(s.cookies.get_dict())
print('Going to profile page...')
s = session.get('http://pythonscraping.com/pages/cookies/profile/php')
print(s.text)


'''
特別的登錄有加密
'''
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('pika', 'password')
r = requests.post(url='http://pythonscraping.com/pages/auth/login.php', auth=auth)

print(r.text)
