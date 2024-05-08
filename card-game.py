'''
Deck Class;
    Trump = some suit
    Shuffle = 
    Deal = deck minus the cards dealt
    Discard pile = There usually is a discard pile


Player Class:
    Dealer = Boolean
    Number = number
    Name = input value
    Score = {
        "win":
        "loss":
        "draw":
    }

    Draw
    Show
    turn = boolean

Card Class:
    color = red or black
    value/number = value of card
    face_card = boolean
    suit = heart, spades, diamonds, clubs

        
Calculate Hand
Check for winner

deck = []
playerHand = []
dealerHand = []

Thinking through the highest card game:
The player and the dealer must each be dealt a card. 
    Create a deal function
The players need to know the value of their hand
    Create a total function
The round ends and they show their hands
    Create a show function. Maybe add a command, ready to show?
The totals need to be compared and a winner needs to be checked for

import Random
'''
class Player:
    def __init__(self, dealer, number, name, score):
        self.dealer = dealer
        self.number = number
        self.name = name
        self.score = score
        
class Deck:
    def __init__(self):

        
class Card:
    def __init__(self, color, value, face_card, suit):
        self.color = color
        self.value = value
        self.face_card = face_card
        self.suit = suit
    
    def show(self):
        print "{} of {}".format(self.value, self.suit)


print("\u2665")
print("\u2660")
print("\u2663")
print("\u2666")