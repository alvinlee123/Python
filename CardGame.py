# -*- coding: utf-8 -*-
"""
Created on Sat Jul 19 14:09:51 2014

@author: alvin
"""

class Deck():
    def __init__(self):
        a=['2','3','4','5','6','7','8','9',"10","Jack","Queen","King","Ace"]
        suit=['Diamonds','Clubs','Hearts','Spades']        
        numcards=[i+" of " +j for i in a for j in suit]
        dicty={numcards[i]:i for i in range(len(numcards))}
        self.numcards=numcards
        self.dicty=dicty
    
    def __str__(self):
        return str(self.numcards)
    
    def shuffle(self,numshuffle):
        import random
        for i in range(numshuffle):
            x=random.randrange(0,52)
            y=random.randrange(0,52)
            new=self.numcards.pop(x)
            self.numcards.insert(y,new)
        return self.numcards
    
    def deal(self):
        if len(self.numcards)==0:
           return "No cards left to deal"
        else:
            x=self.numcards.pop()
            return x
    def cardsleft(self):
        print "There are %i cards left in the deck"%(len(self.numcards))
        return (len(self.numcards))
        

class Hand():
    def __init__(self):
        self.hand=[]
    
    def getcard(self,card):
         self.hand.append(card)
    
    def __str__(self):
        return str(self.hand)
        
    def removecard(self):
        print "Which card do you want to remove?"
        for i in range(len(self.hand)):
            print i, self.hand[i]
        x=input("Which card?Type  -1 to remove none")
        if x==-1:
            return self.hand
        else:
            self.hand.pop(x)
            print str(self.hand)
            

def game(n):
    newdeck=Deck()
    newdeck.shuffle(529)
    scorekeeper=0
    x=newdeck.numcards.pop()
    temp=newdeck.numcards.pop()
    print temp +" is the current card"
    for i in range(n):
        inputt=raw_input("Will the next card be higher or lower? Type H or L\n")
        print inputt
        if inputt=='H' and newdeck.dicty.get(temp)>newdeck.dicty.get(x):
            
            print "Wrongo! the next card is "+x
        elif inputt=='H' and newdeck.dicty.get(temp)<newdeck.dicty.get(x):
            
            scorekeeper+=1
            print "Correct! the next card is "+x
            
            
        
        if inputt=='L' and newdeck.dicty.get(temp)<newdeck.dicty.get(x):

            print "Wrongo! the next card is "+x
            
        elif inputt=='L' and newdeck.dicty.get(temp)>newdeck.dicty.get(x):
            scorekeeper+=1
            print "Correct! the next card is "+x
            
        temp=x
        x=newdeck.numcards.pop()
    
    print "You got %i/%i correct"%(scorekeeper,n)
            


def main():
    print "Guessing game, will the next card be higher or lower?"
    print "This game has no skill and is pure RNG"
    print "Type H if you think the next card will be higher"
    print "Type L if you think the next card will be lower"
    print "\n\n\n\n "
    try:
        numgames=int(input("How many turns do you want? Type a number between 1-52\n"))
        if not (1<=numgames<53):
            raise ValueError()
    except ValueError():
        print "Need to be integer betwen 1-52"
    else:
        print "Your choice is", numgames
    game(numgames)
    
        
    
        

        
main()
'''

import operator
sorted_x = sorted(newdict.iteritems(), key=operator.itemgetter(1))

for i in sorted_x:
    print i
'''


'''
for i,j in newdict.iteritems():
    print i,'\t',j
'''    

'''
newdeck.shuffle(500)


handy=Hand()

for i in range(25):
    handy.getcard(newdeck.deal())
    

print handy
handy.removecard()


'''