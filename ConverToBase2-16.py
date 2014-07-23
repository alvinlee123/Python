# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 17:08:39 2014

@author: alvin
"""

def converttobinary(n,base):
    key='0123456789abcdef'
    if n<base:
        return n
    else:        
        return str(converttobinary(n//base,base))+ key[n%base]
        


print converttobinary(4,2)