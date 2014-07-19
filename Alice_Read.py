# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 23:04:56 2014

@author: alvin
"""

infile=open('/home/alvin/Desktop/alice.txt', 'r')
text=infile.read()

infile.close()
print "Word\tCount"
hah=text.split()

wordcount={}
for i in hah:
    if i in wordcount:
        wordcount[i]+=1
    else:
        wordcount[i]=1
keysort=wordcount.value()

keysort.sort()

for i in keysort:
    print i, wordcount[i]