# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 22:06:39 2014

@author: alvin
"""

#get a list of a bunhc of stocks

from bs4 import BeautifulSoup as bs

import re
import requests


url='http://eoddata.com/stocklist/NYSE/A.htm'
page=requests.get(url).text

soup=bs(page,features='html')

quotes=soup.find_all('tr',{"class":'ro'})

print quotes