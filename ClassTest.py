# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 16:32:10 2014

@author: alvin
"""

class human:
    def __init__(self,name="noname",age=0,weight=0,height=0):
        self.name=name
        self.age=age
        self.weight=weight
        self.height=height
    def get_age(self):
        return self.age
    def get_weight(self):
        return self.weight
    def get_bmi(self):
        return (float(self.weight)/(self.height**2))*703.0704
    def __str__(self):
        return "Name is %s\nAge is %i\nWeight is %i\nHeight is %i\n"%(self.name,self.age,self.weight,self.height)
    def makebaby(self,person):
        name=self.name+person.name +"jr"
        return human(name)
        
def whosfatter(human1,human2):
    if human1.weight>human2.weight:
        print "%s is fatter than %s"%(human1.name,human2.name)
    else:
        print"%s is fatter than %s"%(human2.name,human1.name)
        
jim=human()        





joe=human("joe",26,175,67)
'''
print joe.get_age()
print joe.get_weight()
print joe.get_bmi()
print joe

whosfatter(jim,joe)
'''
newbaby=joe.makebaby(jim)
print newbaby