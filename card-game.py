import random
import time
import sys



class Player:
        
        def __init__(self, name, number, turn = False, dealer = False):
            self.dealer = dealer
            self.number = number
            self.name = name
            self.turn = turn
            self.score = {
                "wins" : 0,
                "losses" : 0,
                "draws" : 0,
                "purse" : 0,
            }
            self.hand = []

        def draw_card(self, deck):
            self.hand.append(deck.draw_from_deck())
            return self

        def show_hand(self):
            hand_value = [card.show_card() for card in self.hand]
            return hand_value

        def discard_card(self, index):
            # equal to 0 means there is a card in the hand
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
            for i in range(self.number_of_decks):
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
            random.shuffle(self.cards)  

        def draw_from_deck(self):
            #Pop acts as the top of the deck because it removes from the last item
            return self.cards.pop()
        
        def show_top_card(self):
            if self.cards:
                # -1 is the top card because its the last card facing away from you
                self.cards[-1].show_card()
                self.determine_trump()
            else:
                print("The deck is empty. Reshuffle the discard")
        
        def determine_trump(self):
                self.trump = self.cards[-1].suit

        def add_to_discard(self, card):
            self.discard_pile.append(card)



class Card:
        
        def __init__(self, value, suit, face_card = False):
            self.value = value
            self.face_card = face_card
            self.suit = suit
            self.color = ""

            if self.suit in ["\u2665", "\u2666"]: # Hearts or Diamonds
                self.color = "\033[91m"
            elif self.suit in ["\u2660", "\u2663"]: # Spade or Clubs
                self.color = "\033[90m"
            else:
                self.color = "\033[0m"
        
        def show_card(self):
            reset_color = "\033[0m"
            return "{}{}{}{}".format(self.color, self.value, self.suit, reset_color)

        def get_value(self):
            if self.face_card == False:
                return int(self.value)
            elif self.value == "A":  # For games that have Ace as low, this can be changed with another condition looking at if Ace is low condition
                return 14
            elif self.value == "K":
                return 13
            elif self.value == "Q":
                return 12
            elif self.value == "J":
                return 11
            

# These are functions that can be added to the Game Class most likely.
def slow_type(words):
    words += "\n"
    for char in words:
        time.sleep(random.choice([
          0.01, 0.02, 0.03, 0.04, 0.05,
          0.03, 0.02, 0.01, 0.03, 0.01
        ]))
        sys.stdout.write(char)
        sys.stdout.flush()
    time.sleep(.4)    

def ready():
    slow_type("Are \033[36myou\033[0m ready to see who won? ")
    is_player_ready = input("")
    return is_player_ready.casefold()

def any_affirmative_answer(response):
    affirmative_words = [
    "absolutely", "absotootly", "affirm", "affirmative", "aye", "aye aye", "by all means", "certainly",
    "count me in", "damn straight", "definitely", "defo", "fo sho", "for sure", "heck yea", "heck yes",
    "hell yea", "hell yes", "indeed", "indeedy", "most definitely", "of course", "oh yeah", "okay", "ok",
    "right", "righto", "sure", "sure thing", "sure thing bruh", "totally", "totally bro", "totally dude",
    "totes ma goats", "uh-huh", "uh-huh", "y", "yea", "yea sure", "yeah", "yeah buddy", "yass", "yasss", "yea",
    "yeppers", "yep", "yep", "yep yep", "you bet", "you betcha", "you got it"
]
    case_insensitive_response = response.casefold()
    return case_insensitive_response in affirmative_words

def determine_winner(dealer, player):
    dealer_card_value = dealer.hand[0].get_value()
    player_card_value = player.hand[0].get_value()

    winner = ""
    if dealer_card_value > player_card_value:
        winner = "\033[32mI\033[0m"
        dealer.score["wins"] += 1
        player.score["losses"] += 1
    elif dealer_card_value < player_card_value:
        winner = "you"
        dealer.score["losses"] += 1
        player.score["wins"] += 1
    elif dealer_card_value == player_card_value:
        winner = "neither of us"
        dealer.score["draws"] += 1
        player.score["draws"] += 1
    else: 
        winner = "\033[32mI\033[0m can't figure out who"    
    return winner

# I wonder if this section can just be part of a start game function in the Game Class?
slow_type("Initializing Program...")
slow_type('Loading')
for i in range(3):
    time.sleep(.4)
    sys.stdout.write('.')
    sys.stdout.flush()
print("\n")

slow_type("Hiya buddy! \033[32mMy\033[0m name is \033[1m\033[32mAce\033[0m and \033[32mI\033[0m will be your dealer!")
time.sleep(.4)
print("\n")

slow_type("What is your name?")
entered_name = input("")
time.sleep(.4)
print("\n")

greetings = ["Yo", "Hey there", "Greetings", "Sup", "Hi", "How it do", "Howdy", "Well \033[32mI'll\033[0m be. Hi"]
welcome = random.choice(greetings)
slow_type(f"{welcome} \033[1m\033[36m{entered_name}\033[0m!")
time.sleep(.4)
print("\n")

slow_type("So glad to meet \033[36myou\033[0m.")
time.sleep(.4) 
print("\n")

# This would be the end of the start game function and wouldnt be part of the While loop.

# This would be part of the Select Game and then Game Intro part
slow_type(f"\033[1m\033[36m{entered_name}\033[0m, we are going to play a simple game called highest card.")
time.sleep(.4)
print("\n")

slow_type("Suit doesn't matter.")
time.sleep(.4)
print("\n")

while True:
    try:
        slow_type("How many decks would \033[36myou\033[0m like to play with? ")        
        deck_qty = int(input(""))
        if deck_qty == 0:
            slow_type("Wrong Choice. \033[36mYou'll\033[0m just get 1 deck")
            deck_qty = 1
        elif deck_qty > 999:
            slow_type("We don't have that many. How about 10? Because that's what \033[36myou're\033[0m going to get")
            deck_qty = 10
        time.sleep(.4)
        print("\n")
        break
    except:
        slow_type("That can't be right. That's not a number.")
        print("\n") 

super_deck = Deck(deck_qty)
player = Player(entered_name, 1)
dealer = Player("Ace", 2)

# This would be part of the While loop that keeps the game going
def highest_card_game_play(dealer, player):
    slow_type("Alright, now \033[32mI\033[0m am going to deal \033[36myou\033[0m a card")
    
    player.draw_card(super_deck)
    dealer.draw_card(super_deck)

    time.sleep(.4)
    print("\n")

    slow_type(f"Ok \033[1m\033[36m{entered_name}\033[0m, go ahead and look at \033[36myour\033[0m card")
    time.sleep(.4)
    player_card = player.show_hand()
    for bologna in player_card:
        print(bologna)
    print("\n")

    # There was a bug where the first response could be almost anything, but all other responses needed to match it.
    user_response = ready()
    while not any_affirmative_answer(user_response):
        responses = ["Hurry up slowpoke", "What's taking so long?", "Need help or something", "Ugh... Hurry!", "What's the hold up?", "Come on already...", "We're aren't getting any younger", "Pick up the pace dude..."]
        slow_type(random.choice(responses))
        print("\n")
        user_response = ready()

    dealer_card = dealer.show_hand()
    for folgers in dealer_card:
            print(folgers) 
    print("\n")    

    end_of_game = determine_winner(dealer, player)
   
    super_deck.add_to_discard(player.hand[0])
    player.discard_card(0)
    
    super_deck.add_to_discard(dealer.hand[0])
    dealer.discard_card(0)
    
    slow_type(f"\033[32mI\033[0m have {dealer_card[0]} and \033[36myou\033[0m have {player_card[0]}. It looks like {end_of_game} won!")
    print("\n")
    slow_type(f" Dealer Wins: \033[92m{dealer.score["wins"]}\033[0m, Losses: \033[31m{dealer.score["losses"]}\033[0m, and Draws: \033[33m{dealer.score["draws"]}\033[0m")
    slow_type(f" {entered_name} Wins: \033[92m{player.score["wins"]}\033[0m, Losses: \033[31m{player.score["losses"]}\033[0m, and Draws: \033[33m{player.score["draws"]}\033[0m")
    print("\n")

    slow_type("Would you like to play again?")
    play_again = input("").casefold()
    return play_again

play_again = "yes"
while play_again == "yes":
    play_again = highest_card_game_play(dealer, player)


# We could have a Would you like to play again?, Go to choose Game Screen, or just quit?
# Each calling their own function 

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
