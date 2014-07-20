# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 20:12:54 2014

@author: alvin
"""

class Fraction():
    
    def __init__(self,num,dem):
        if type(num)!=int or type(dem)!=int:
            raise RuntimeError("Make your Numerator/Denominator ints plz")
        else:
            self.numerator=num
            self.denominator=dem
    
    def __str__(self):
        return str(self.numerator)+"/"+str(self.denominator)
    
    def simpilify(self):
        m=abs(self.numerator)
        n=abs(self.denominator)
        while (m)%(n)!=0:
            oldm=(m)
            oldn=(n)
            
            m=oldn
            n=oldm%oldn
        self.numerator=self.numerator/n
        self.denominator=self.denominator/n
        if self.numerator<0 and self.denominator<0:
            self.numerator*=-1
            self.denominator*=-1
        if self.numerator>self.denominator:
            print self.numerator//self.denominator,self.numerator%self.denominator,"/",self.denominator
    
    def __add__(self, otherfraction):
        top=self.numerator*otherfraction.denominator+otherfraction.numerator*self.denominator
        bot=self.denominator*otherfraction.denominator
        return Fraction(top,bot)
        
    def __sub__(self,otherfraction):
        top=self.numerator-otherfraction.numerator
        bot=self.denominator-otherfraction.denominator
        return Fraction(top,bot)
    
    def __mul__(self,otherfraction):
        top=self.numerator*otherfraction.numerator
        bot=self.denominator*otherfraction.denominator
        return Fraction(top,bot)
    
    def __div__(self,otherfraction):
        top=self.numerator*otherfraction.denominator
        bot=self.denominator*otherfraction.numerator
        return (Fraction(top,bot).simpilify())
    
    def __radd__(self,otherfraction):
        top=self.numerator*otherfraction.denominator+otherfraction.numerator*self.denominator
        bot=self.denominator*otherfraction.denominator
        return Fraction(top,bot)
        


Joe= Fraction(1,5)
Angus=Fraction(5,9)


(Joe+5).simpilify()

