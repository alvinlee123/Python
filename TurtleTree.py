# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 15:10:54 2014

@author: alvin
"""

import turtle

joe=turtle.Turtle()
wn=turtle.Screen()

def drawtree(turtle,distance):
    if distance>5:
        turtle.forward(distance)
        turtle.right(20)
        drawtree(turtle,distance-15)
        turtle.left(40)
        drawtree(turtle,distance-10)
        turtle.right(20)
        turtle.backward(distance)

def main():
    joe.left(90)
    joe.backward(100)
    drawtree(joe,90)
    wn.exitonclick()
    
main()