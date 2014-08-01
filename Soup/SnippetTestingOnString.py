# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 02:26:31 2014

@author: alvin
"""
from bs4 import BeautifulSoup as bs
text='<span class="pr"><span id="ref_663137_l">172.87</span></span>'

soup=bs(text)


price= soup.find('span',{'class':'pr'})

print price.text