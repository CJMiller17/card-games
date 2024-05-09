import random
import time
import sys

class Player:
    def __init__(self, name, number, turn = False, dealer = False, score = 0):
        self.dealer = dealer
        self.number = number
        self.name = name
        self.turn = turn
        self.score = {
            "wins" : 0,
            "losses" : 0,
            "draws" : 0,
        }
        self.hand = []

    def draw_card(self, deck):
        self.hand.append(deck.draw_from_deck())
        return self

    def show_hand(self):
        for card in self.hand:
           card.show_card()

    def discard_card(self, index):
        if 0 <= index < len(self.hand):
            return self.hand.pop(index)
        else:
            print("Try Again")

class Deck:
    def __init__(self, number_of_decks=1, trump = False):
        self.trump = trump
        self.cards = []
        self.discard_pile = []
        self.number_of_decks = number_of_decks
        self.build()
        self.shuffle()
        self.shuffle()

    def build(self):
            for suit in ["\u2660", "\u2663", "\u2665", "\u2666"]:
                for value in range(1, 14):
                    face_card = False 
                    if value == 1:
                        face_card = True
                        value = "A"
                    elif value == 11:
                        face_card = True
                        value = "J"
                    elif value == 12:
                        face_card = True
                        value = "Q"
                    elif value == 13:
                        face_card = True
                        value = "K"
                    self.cards.append(Card(value, suit, face_card))

    def shuffle(self):
        # First -1 means last card, 0 means decrementing towards 0 index, last -1 means 
        for i in range(len(self.cards)-1, 0, -1):
            random_card = random.randint(0, i)
            self.cards[i], self.cards[random_card] = self.cards[random_card], self.cards[i]

    def build_

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

    def add_to_discard(self, card):
        self.discard_pile.append(card)
        
class Card:
    def __init__(self, value, suit, face_card = False):
        self.value = value
        self.face_card = face_card
        self.suit = suit

        if self.suit in ["\u2665", "\u2666"]: # Hearts or Diamonds
            self.color = "red"
        elif self.suit in ["\u2660", "\u2663"]: # Spade or Clubs
            self.color = "black"
        else:
            self.color = "green"
    
    def show_card(self):
        print("{}{}".format(self.value, self.suit))

deck_num_1 = Deck()

player_1 = Player("Kevin", 1, turn=True, dealer=True)
player_2 = Player("Katrina", 2)
player_1.draw_card(deck_num_1)


print('Loading')
for i in range(8):
    time.sleep(.5)
    sys.stdout.write('.')
    sys.stdout.flush()
print("\n")

print("Hiya buddy! My name is Ace and I will be your dealer!")
print("\n")


# for item in deck.cards:
#     print(f'card: {item.value} {item.suit} {item.color} {item.face_card}')
#     print('\n')


'''
# Spade "\u2660"
# Clubs "\u2663"
# Heart "\u2665"
# Diamonds "\u2666"

Calculate Hand
Check for winner

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

# player.draw_card(deck).draw_card(deck).draw_card(deck).draw_card(deck).draw_card(deck)
