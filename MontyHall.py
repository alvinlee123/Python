# -*- coding: utf-8 -*-
"""
Created on Fri Jul 18 03:08:59 2014

@author: alvin
"""

import random
import numpy as np
def simulate_prizedoor(nsim):
    #compute here
    x=0
    answer=[]
    for i in range(nsim):
        x=random.randrange(3)
        answer.append(x)
    return answer
 
def simulate_guess(nsim):
    x = np.random.randint(3, size=nsim )
    z=[]
    for i in x:
        z.append(i)
    return z
 
def goat_door(prizedoor,guesses):
    doorswitch=[]
    for i in range(len(prizedoor)):
        if prizedoor[i] in [0,1] and guesses[i] in[0,1]:
            doorswitch.append(2)
        elif prizedoor[i] in [0,2] and guesses[i] in[0,2]:
            doorswitch.append(1)
        elif prizedoor[i] in [1,2] and guesses[i] in[1,2]:
            doorswitch.append(0)
        elif prizedoor[i] ==guesses[i]:
            if prizedoor[i]==0:
                doorswitch.append(1)
            elif prizedoor[i]==1:
                doorswitch.append(0)
            elif prizedoor[i]==2:
                doorswitch.append(1)
    return doorswitch
 
def switch_guess(guesses,goatdoors):
    switch_guess=[]
    for i in range(len(guesses)):
        if guesses[i] in [0,1] and goatdoors[i] in[0,1]:
            switch_guess.append(2)
        elif guesses[i] in [0,2] and goatdoors[i] in[0,2]:
            switch_guess.append(1)
        elif guesses[i] in [1,2] and goatdoors[i] in[1,2]:
            switch_guess.append(0)
    return switch_guess
 
def win_percentage(guesses,prizedoors):
    wins=0
    for i in range(len(guesses)):
        if guesses[i]==prizedoors[i]:
            wins+=1
    percent=wins/float(len(guesses))
    return percent*100
 
def main(numdoors,timesrun):
    for i in range(timesrun):
        prizedoor=simulate_prizedoor(numdoors)
        #print "This is the prize door: \t ",prizedoor
        guess=simulate_guess(numdoors)
        #print "This is the guess for each door: ",guess
        goatdoor=goat_door(prizedoor,guess)
        #print "This is the door a goat is in:   ",goatdoor
        switchedguess=switch_guess(guess,goatdoor)
        #print "This is when you switch guess:\t ",switchedguess
        noswitch_win=win_percentage(guess,prizedoor)
    print "Percent of wins without switching",noswitch_win
    switch_win=win_percentage(switchedguess,prizedoor)
    print "Percent of wins with switching",switch_win
main(10000,100)