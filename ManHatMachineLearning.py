# -*- coding: utf-8 -*-
"""
Created on Sat Jul 26 04:43:20 2014

@author: alvin
"""

from math import sqrt

users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
        }

def manhat(user1,allusers):
    storage={}
    users=allusers
    for people in users:
        storage[people]=0
        if people!=user1:        
            for i,k in users[people].iteritems():
                if i in users[user1]:
                    storage[people]+=abs(k-users[user1][i])





    mindistance=99999
    closest="" 
    for i,k in storage.iteritems():
        if k <mindistance and i!=user1:
            mindistance=k
            closest=i
        
                        
    RecList=[]


    for i,k in users[closest].iteritems():
        if i not in users[user1]:
            RecList.append((i,k))
           

    return "The Recommendation for %s is the following " %(user1), RecList
    
print manhat("Hailey",users)
    