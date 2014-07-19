# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 20:17:41 2014

@author: alvin
"""

def gcd(m,n):
    while m%n!=0:    
        oldm=m
        oldn=n
        
        m=oldn
        n=oldm%oldn
    return n
    
class fraction():
    
    def __init__(self,num,dem):
        self.num=num
        self.dem=dem
        
    def __str__(self):
        return str(self.num)+"/"+str(self.dem)
        
    def reduce(self):
        common=gcd(self.num,self.dem)
        self.num=self.num//common
        self.dem=self.dem//common
    def __add__(self,otherfraction):
        top=(self.num*otherfraction.dem+self.dem*otherfraction.num)
        bot=self.dem*otherfraction.dem
        common=gcd(top,bot)
        return fraction(top//common,bot//common)

a=fraction(9,24)
b=fraction(33,24)

print a+b

print 9+33

print gcd(42,24)