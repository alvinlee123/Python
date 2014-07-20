# -*- coding: utf-8 -*-
"""
Created on Sat Jul 19 14:09:51 2014

@author: alvin
"""

class Deck():
    def __init__(self):

        a=["Ace",'2','3','4','5','6','7','8','9',"10","Jack","Queen","King"]
        suit=['Clubs','Diamonds','Hearts','Spades']   
        numcards=[i+" of " +j for i in a for j in suit]
        self.numcards=numcards
    
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
            
        


newdeck=Deck()
newdeck.shuffle(500)


handy=Hand()

for i in range(25):
    handy.getcard(newdeck.deal())
    

print handy
handy.removecard()


