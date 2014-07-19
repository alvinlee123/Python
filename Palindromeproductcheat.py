# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 03:58:38 2014

@author: alvin
"""



#998001

def is_pali(n):
    tr=str(n)
    return tr==tr[::-1]
    
def check():
    li=[]
    for i in range(998001,100000,-1):
        if is_pali(i):
            li.append(i)
    return li



newlist=check()


def findit(listy):
    found={}
    for i in listy:
        for j in range(100,999):
            if i%j==0:
                found[j]=i
    return found
    
joe=findit(newlist)
                
                
maxpower=0
for key,pali in joe.iteritems():
    if pali/key>99 and pali/key<999:
        if pali>maxpower:
            maxpower=pali


print maxpower
        
    