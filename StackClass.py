# -*- coding: utf-8 -*-
"""
Created on Tue Jul 22 02:15:49 2014

@author: alvin
"""

#stackerino


class Stack():
    def __init__(self):
        self.stack=[]
    def __str__(self):
        return str(self.stack)
        
    def push(self,val):
        self.stack.append(val)
        
    def pop(self):
        return self.stack.pop()
        
    def isEmpty(self):
        return self.stack==[]
        
    def peek(self):
        return self.stack[-1]
    def size(self):
        return len(self.stack)
        
        
    
a=Stack()
a.push('v')
a.push(3)
print a
a.pop()
print a
a.push(5)

print a

print a.peek()

print a.isEmpty()

print a.size()

def revstring(mystr):
    stackerjoe=Stack()
    x=''
    for i in mystr:
        stackerjoe.push(i)
    for i in range(len(mystr)):
        x+=str(stackerjoe.pop())
    return x
    
revstring("snackerjoe")