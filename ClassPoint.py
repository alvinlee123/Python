# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 17:19:42 2014

@author: alvin
"""

class Point:
    """ Point class for representing and manipulating x,y coordinates. """

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
    
    def reflect_x(self):
        reflect=int(self.y)*(-1)
        return Point(self.x,reflect)
    
    def __str__(self):
        return "%s,%s"%(self.x,self.y)
    
    def distanceFromPoint(self,otherpoint):
        diffy=(self.y-otherpoint.y)**2
        diffx=(self.x-otherpoint.x)**2
        return (diffy+diffx)**0.5
    
    def slopeFromOrigin(self):
        return float(self.y)/self.x
    
    def returnMx(self,otherpoint):
        diffy=self.y-otherpoint.y
        diffx=self.x-otherpoint.x
        slope=float(diffy)/diffx
        bvalue=slope*self.x-self.y
        return Point(slope,bvalue)
    def perpGradiant(self,otherpoint):
        diffy=self.y-otherpoint.y
        diffx=self.x-otherpoint.x
        slope=float(diffx)*-1/diffy
        return slope
        
    
    def move(self,dx=0,dy=0):
        self.x+=dx
        self.y+=dy
    def getmidpoint(self,otherpoint):
        difx=self.x-otherpoint.x/2
        dify=self.y-otherpoint.y/2
        return Point(difx,dify)
    
def getcircle(a,b,c):
    #get midpoint of y from A and B
    midpointABY=float(a.y-b.y)/2
    #get midpoint of BC\
    midpointBC=b.getmidpoint(c)
    #get perp gradiant of CB
    perpgrad=c.perpGradiant(b)
    x=float(midpointABY-midpointBC.y)/perpgrad+midpointBC.x
    return x,midpointABY
        
    
'''    
a=Point(0,0)
b=Point(3,3)
c=Point(-3,-3)

print getcircle(a,b,c)    
    
'''
'''
p = Point(7,6)
q= Point(3,4)

print p.distanceFromOrigin()
reflect=p.reflect_x()
print reflect



print p
p.move(1,1)
print p
'''