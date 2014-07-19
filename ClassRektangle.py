# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 21:07:25 2014

@author: alvin
"""
import ClassPoint


class Rectangle():
    
    def __init__(self,point,width,height):
        
        self.point=point
        self.width=width
        self.height=height
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
        
    def __str__(self):
        return str(self.point)+" "+str(self.width) +" "+ str(self.height)
    
    def area(self):
        return self.width*self.height
        
    def perimeter(self):
        return 2*self.width+2*self.height
    
    def transpose(self):
        oldwidth=self.width
        oldheight=self.height
        
        self.width=oldheight
        self.height=oldwidth
    
    def contains(self,testpoint):
        upperboundx=self.width+self.point.x
        upperboundy=self.height+self.point.y
        
        if self.point.x<testpoint.x and upperboundx>testpoint.x:
            if self.point.y<testpoint.y and upperboundy>testpoint.y:
                return True
            else:
                return False
        else:
            return False
    
a=Point(3,3)

joe=Rectangle(a,3,9)

print joe

joe.transpose()


print joe.contains(Point(4,6))
