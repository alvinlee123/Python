# -*- coding: utf-8 -*-
"""
Created on Mon Jul 28 23:07:39 2014

@author: alvin
"""

from bs4 import BeautifulSoup as bs
import requests
import re
url='http://charts.realclearpolitics.com/charts/1171.xml'
page=requests.get(url).text

soup=bs(page)
soup.prettify()
#print soup
#print soup.contents


#for tag in soup.find_all(re.compile("^p")):
    #print tag.contents
    
#for tag in soup.find_all(True):
#    print tag

#print(soup.find_all('a','b'))


for tag in soup.find_all('graph',{'title':'Obama'}):
    print tag.text
    print '\n'