# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 21:15:04 2014

@author: alvin
"""

from bs4 import BeautifulSoup as bs
import requests
import time
import datetime
symbols=['aapl','goog','fb','gpro']

for symbol in symbols:
    time.sleep(3)
    supa='http://finance.yahoo.com/q?s='+symbol
    url=requests.get(supa).text
    time.sleep(3)
    soup=bs(url,features='html')
    
    price=soup.find('span',{'id':'yfs_l84_'+symbol}).text
    

    print "%s is %s today"%(symbol, price)
    
