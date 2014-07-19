# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 23:10:48 2014

@author: alvin
"""

infile=open('/home/alvin/Desktop/alice.txt', 'r')
text=infile.read()
infile.close()
xa=text.lower()
print "Word\tCount"
hah=xa.split()

wordcount={}
for i in hah:
    if i in wordcount:
        wordcount[i]+=1
    else:
        wordcount[i]=1
    

sortedwordcount=wordcount.keys()

sortedwordcount.sort()
for i in sortedwordcount:
    print i, wordcount[i]

temp=0
for i in wordcount:
    if wordcount[i]>temp:
        temp=wordcount[i]
        word=i
#print word,temp

tempting=0    
for i in sortedwordcount:
        if len(i)>tempting:
            tempting=len(i)
            wilt=i
#print wilt,tempting
            