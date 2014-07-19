# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 13:16:05 2014

@author: alvin
"""

def anagram(s1,s2):
    list1=list(s1)
    list2=list(s2)
    
    list1.sort()
    list2.sort()
    
    position=0
    matches=True
    
    while position<len(s1) and matches:
        if list1[position]==list2[position]:
            position+=1
        else:
            matches=False
        
    return matches
    
print(anagram('abcde','edcba'))