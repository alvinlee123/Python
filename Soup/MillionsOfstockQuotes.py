# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 22:29:31 2014

@author: alvin
"""

infile=open("companylist.csv")

from bs4 import BeautifulSoup as bs
import requests
import time


for i in infile:
    symbol=i.split('\r\n')[0].lower()
    time.sleep(3)
    supa='http://finance.yahoo.com/q?s='+symbol

    url=requests.get(supa).text
    
    time.sleep(3)
    soup=bs(url,features='html')
    classy='yfs_l84_'+symbol
    price=soup.find('span',{'id':classy}).text
    

    print "%s is %s today"%(symbol, price)
