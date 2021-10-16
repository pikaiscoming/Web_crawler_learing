# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 14:56:21 2021

@author: pikachu
"""

import json
from urllib.request import urlopen

def getcountry(ipaddress):
    response = urlopen('http://freegeoip.net/json/' + str(ipaddress)).read().decode(encoding='utf-8')
    responsejson = json.loads(response)
    return responsejson.get('country_code')

print(getcountry('192.168.1.1'))
    