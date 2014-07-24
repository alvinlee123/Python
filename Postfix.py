# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 19:04:56 2014

@author: alvin
"""

from StackClass import Stack


def postfix(infix):
    
    #op stack is where we store left parentheses, it will count
    #how much we need to pop when we hit a right parenthesis
    opstack=Stack()
    #output will be the return of all our values
    output=[]
    #splits up the infix notation equation
    input1=list(infix)
    #declare a dict
    prec={}
    #determine the level of precedence for operators
    prec['*']=3
    prec['/']=3
    prec['+']=2
    prec['-']=2
    prec['(']=1
    
    for i in input1:
        #append non operators/ parenthesises into output
        if i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1023456789':
            output.append(i)
        #if is a left parenthesis, append it to the stack
        elif i =='(':
            opstack.push(i)
        #if it is a right parenthesis,
        #pop a left parenthesis out of the stack
        elif i==')':
            topToken=opstack.pop()
        #while the top of the stack is NOT a left parenthesis and
        #is an operator, keep on popping that shit into the output
            while topToken !="(":
                output.append(topToken)
                topToken=opstack.pop()
        #else if it is an operator
        else:
            #while the opstack is NOT empty and and the operator's precident in the stack
            #is GREATER than the operator currently being iterated on
            #pop that operator into the stack
            while (not opstack.isEmpty()) and (prec[opstack.peek()]) >=prec[i]:
                output.append(opstack.pop())
            #otherwise, just push the current operator into the stack
            opstack.push(i)
    #and this last while loop is to get out the remaining operators at the end
    while not opstack.isEmpty():
        output.append(opstack.pop())
    return " ".join(output)
           
            
            
        
            
    
print postfix("(5+3)+6*7")