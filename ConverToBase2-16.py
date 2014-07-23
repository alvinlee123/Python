# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 17:08:39 2014

@author: alvin
"""
from StackClass import Stack

def converttobinary(n,base):
    key='0123456789abcdef'
    if n<base:
        return n
    else:        
        return str(converttobinary(n//base,base))+ key[n%base]
        



def convertbase2(n):
    
    a=Stack()
    binstring=""
    while n>0:
        a.push(n%2)
        n=n//2
    while not a.isEmpty():
        binstring+=str(a.pop())
    return binstring
    
print convertbase2(10)