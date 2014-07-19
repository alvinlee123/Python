# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 03:57:32 2014

@author: alvin
"""

def primero(x):
    list=[]
    storage=0
    count=2
    voyager=1
    while(x):
        if x % count == 0:
            list.append(count)
            print (list)
            voyager*=count
            x=x/count
            print (voyager)
        else:
           # print ("hello2")
            count+=1
    return list
    
primero(6008514751)