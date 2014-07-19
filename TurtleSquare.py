# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 15:07:26 2014

@author: alvin
"""

import turtle

joe=turtle.Turtle()
wn=turtle.Screen()

def turtlesquare(turtle,num):
    if num>0:
        turtle.forward(num)
        turtle.right(90)
        turtlesquare(turtle,num-5)
        
turtlesquare(joe,300)

wn.exitonclick()