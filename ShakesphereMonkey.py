# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 02:03:19 2014

@author: alvin
"""


def check_equal(string1):
    count=0
    key='methinks it is like a weasel'
    
    for i in range(len(key)):
        if string1[i]==key[i]:
            count+=1
    return float(count)/28
    

def generate_string():
    import random    
    key='abcdefghijklmnopqrstuvwxyz '
    wez='methinks it is like a weasel'
    newstring=''
    for i in range(len(wez)):
        newstring+=key[random.randrange(0,len(key))]
    return newstring
'''    
print generate_string()
print 'methinks it is like a weasel'
    

snack=generate_string()
'''
def main():
    maxi=0
    bestvalue=""
    for i in range(5000000):
        jim=generate_string()
        joe=check_equal(jim)
        if joe>maxi:
            maxi=joe
            bestvalue=jim
    return maxi,bestvalue
    
print main()

