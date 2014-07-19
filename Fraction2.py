# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 20:12:54 2014

@author: alvin
"""

class Fraction():
    
    def __init__(self,num,dem):
        self.numerator=num
        self.denominator=dem
    
    def __str__(self):
        return str(self.numerator)+"/"+str(self.denominator)
    
    def simpilify(self):
        m=self.numerator
        n=self.denominator
        while abs(m)%abs(n)!=0:
            oldm=abs(m)
            oldn=abs(n)
            
            m=oldn
            n=oldm%oldn
        self.numerator=self.numerator/n
        self.denominator=self.denominator/n
    
    def __add__(self, otherfraction):
        top=self.numerator+otherfraction.numerator
        bot=self.denominator+otherfraction.denominator
        return Fraction(top,bot)
        
    def __sub__(self,otherfraction):
        top=self.numerator-otherfraction.numerator
        bot=self.denominator-otherfraction.denominator
        return Fraction(top,bot)
        


Joe= Fraction(2,4)
Angus=Fraction(5,9)

Liz=Joe-Angus

