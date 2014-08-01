# -*- coding: utf-8 -*-
"""
Created on Sun Jul 27 21:02:59 2014

@author: alvin
"""
import datetime
import re
import urllib2
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from bs4 import BeautifulSoup as bs
import numpy as np
url="http://charts.realclearpolitics.com/charts/1171.xml"
page=urllib2.urlopen(url)

soup=bs(page,features='xml')

def _strip(s):
    return re.sub(r'[\W_]+', '', s)


g_data=soup.find_all('graph',{'gid':'1'})[0]
g_data2=soup.find_all('graph',{'gid':'1'})[0]
series=soup.find_all('series')[0]

graph1=[i.text for i in g_data]
dates=[dates.text for dates in series]
graph2=[i.text for i in g_data2]

graph1=[float(i) for i in graph1[:-10]]
graph2=[float(i) for i in graph2[:-10]]
dates=[i for i in dates[:-10]]

dates=matplotlib.dates.date2num(dates)
meowdict={'year':dates,'graph1':graph1,'graph2':graph2}    



frame=pd.DataFrame(meowdict)

frame.convert_objects(convert_dates=True,convert_numeric=True)

print frame.describe()
plt.plot(frame.year)

plt.show()
'''
def saveDict(fn,dict_rap):
    f=open(fn, "wb")
    w = csv.writer(f)
    for key, val in dict_rap.items():
        w.writerow([key, val])
    f.close()
    
saveDict("Hi.txt",meowdict)

'''