# -*- coding: utf-8 -*-
"""
Created on Wed Jul 16 03:00:53 2014

@author: alvin
"""

#recursion factorial


def factorial(n):
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)


def summer(n):
    if n==0:
        return 0
    else:
        return n+summer(n-1)


def toStr(num,base):
    convert="0123456789ABCDEF"
    if num<base:
        return convert[num]
    else:
        return toStr(num//base,base)+convert[num%base]
        
s="apple saucd343e"

def reverse(s):
    if len(s)==0:
        return s
    else:
        return reverse(s[1:])+s[0]
        
def removeWhite(s):
    lowercase=s.lower()
    key='abcdefghijklmnopqrstuvwxyz'
    stringer=''
    for i in lowercase:
        if i in key:
            stringer+=i
    return stringer

def recursivepalindrome(s):
    if len(s)<2:
        return True
    elif s[0]==s[-1]:
        return recursivepalindrome(s[1:-1])
    else:
        return False
        

def snacker(s):
    if s>10:
        print "hello"
    elif s>5:
        print "hello again"
        
snacker(130)