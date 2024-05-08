import random
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
    def __init__(self, name, dealer = False, number = 1, score = 0):
        self.dealer = dealer
        self.number = number
        self.name = name
        self.score = score
        self.hand = []

    def draw_card(self, deck):
        self.hand.append(deck.draw_from_deck())
        return self

    def show_hand(self):
        for card in self.hand:
           card.show_card()

    def discard_card(self):
        return self.hand.pop()
        

class Deck:
    def __init__(self, trump = False):
        self.trump = trump
        self.cards = []
        self.discard_pile = []
        self.build()

    def build(self):
        for suit in ["\u2660", "\u2663", "\u2665", "\u2666"]:
            for value in range(1, 14):
                self.cards.append(Card(value, suit))

    def shuffle(self):
        # First -1 means last card, 0 means decrementing towards 0 index, last -1 means 
        for i in range(len(self.cards)-1, 0, -1):
            random_card = random.randint(0, i)
            self.cards[i], self.cards[random_card] = self.cards[random_card], self.cards[i]

    def draw_from_deck(self):
        #Pop acts as the top of the deck because it removes from the last item
        return self.cards.pop()
    
    def determine_trump(self):
        suits = ["\u2660", "\u2663", "\u2665", "\u2666"]
        self.trump = random.choice(suits)
    
    def show_top_card(self):
        for card in self.cards:
            card.show_card()
        self.determine_trump()               
        
class Card:
    def __init__(self, value, suit, color = "red", face_card = False):
        self.color = color
        self.value = value
        self.face_card = face_card
        self.suit = suit
    
    def show_card(self):
        print("{}{}".format(self.value, self.suit))



# Spade "\u2660"
# Clubs "\u2663"
# Heart "\u2665"
# Diamonds "\u2666"

# python card-game.py

# card = Card(6, "\u2666")
# card.show()

deck = Deck()
deck.shuffle()
# deck.show()

player = Player("Jeanine")
player.draw_card(deck).draw_card(deck).draw_card(deck).draw_card(deck).draw_card(deck)
player.show_hand()

# card = deck.draw()
# card.show()