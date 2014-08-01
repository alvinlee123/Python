# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 22:29:31 2014

@author: alvin
"""

infile=open("companylist.csv")

from bs4 import BeautifulSoup as bs
import requests
import time
import re

for i in infile:
    symbol=i.split('\r\n')[0].lower()

    time.sleep(3)
    supa='https://www.google.com/finance?q='+symbol

    url=requests.get(supa).text
    
    time.sleep(3)
    soup=bs(url)
    

    price= soup.find('span',{'class':'pr'})
    
    print "%s price today is %s"%(symbol,price.text)