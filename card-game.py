import random
import time
import sys


class Card:
        # These are the relevant aspects of a card
        def __init__(self, value, suit, face_card = False):
            self.value = value
            self.face_card = face_card
            self.suit = suit
            self.color = ""

            # Sets the card color based on suit
            if self.suit in ["\u2665", "\u2666"]: # Hearts or Diamonds
                self.color = "\033[91m"
            elif self.suit in ["\u2660", "\u2663"]: # Spade or Clubs
                self.color = "\033[90m"
            else:
                self.color = "\033[0m"
        
        # This formats how the card is shown. Resets the color so text goes back to white
        def show_card(self):
            reset_color = "\033[0m"
            return "{}{}{}{}".format(self.color, self.value, self.suit, reset_color)

        # Defines the value of face cards
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



class Player:
        # Some of the params aren't used for highest card but can be used for other games once I add them
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
        
        # Appends to the hand list
        def draw_card(self, deck):
            self.hand.append(deck.draw_from_deck())
            return self

        # Returns a list of values and suits, which is exactly what a hand would be
        def show_hand(self):
            hand_value = [card.show_card() for card in self.hand]
            return hand_value

        # If the list has an item, it can be discarded when this function is called
        def discard_card(self, index):
            # equal to 0 means there is a card in the hand
            if 0 <= index < len(self.hand):
                return self.hand.pop(index)
            else:
                print("There are no cards to discard")



class Deck:
        # Some of these params aren't used in highest card but can be used in more games when added
        def __init__(self, number_of_decks=1, trump = False):
            self.trump = trump # A lot of my favorite games rely on a trump card
            self.cards = []
            self.discard_pile = []
            self.number_of_decks = number_of_decks
            self.build()
            self.shuffle()  # Double shuffle for good measure
            self.shuffle()

        # This builds the deck in a list. 
        def build(self):
            for i in range(self.number_of_decks):
                # Loops through a group of 13 cards and gives them a suit
                for suit in ["\u2660", "\u2663", "\u2665", "\u2666"]:
                    # Value here is overridden by the get_value function. 
                    # I am using the value as it's sequential order here for ease of conception
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
                        # Creates the actual card object with all the specifics    
                        self.cards.append(Card(value, suit, face_card))

        def shuffle(self):
            random.shuffle(self.cards)  

        def draw_from_deck(self):
            #Pop acts as the top of the deck because it removes from the last item (-1) as default
            return self.cards.pop()
        
        def show_top_card(self):
            if self.cards:
                # -1 goes to the very end of the list. This is the top card because its the last card facing away from you
                self.cards[-1].show_card()
                self.determine_trump()
            else:
                print("The deck is empty. Reshuffle the discard")
        
        def determine_trump(self):
                # Checks to see the value of the top cards suit
                self.trump = self.cards[-1].suit

        def add_to_discard(self, card):
            self.discard_pile.append(card)

class Game:
        def slow_type(self, words):
            words += "\n"
            for char in words:
                time.sleep(random.choice([
                0.01, 0.02, 0.03, 0.04, 0.05,
                0.03, 0.02, 0.01, 0.03, 0.01
                ]))
                # Used for output of print
                sys.stdout.write(char)
                # Doesnt wait to finish buffering before writing
                sys.stdout.flush()
            time.sleep(.4)    

        def ready(self):
            self.slow_type("Are \033[36myou\033[0m ready to see who won? ")
            is_player_ready = input("")
            return is_player_ready.casefold() # Strongest version of case insensitivity that Python has

        def any_affirmative_answer(self, response):
            affirmative_words = [
            "absolutely", "absotootly", "affirm", "affirmative", "aye", "aye aye", "by all means", "certainly",
            "count me in", "damn straight", "definitely", "defo", "fo sho", "for sure", "heck yea", "heck yes",
            "hell yea", "hell yes", "indeed", "indeedy", "most definitely", "of course", "oh yeah", "okay", "ok",
            "right", "righto", "sure", "sure thing", "sure thing bruh", "totally", "totally bro", "totally dude",
            "totes ma goats", "uh-huh", "uh-huh", "y", "yea", "yes", "yea sure", "yeah", "yeah buddy", "yass", "yasss", "yea",
            "yeppers", "yep", "yep", "yep yep", "you bet", "you betcha", "you got it"
        ]
            case_insensitive_response = response.casefold()
            # Boolean
            return case_insensitive_response in affirmative_words

        def highest_card_game_intro(self):
            self.deck_qty = 1
            while True:
                try:
                    self.slow_type("How many decks would \033[36myou\033[0m like to play with? ")        
                    deck_qty = int(input(""))
                    if deck_qty == 0:
                        self.slow_type("Wrong Choice. \033[36mYou'll\033[0m just get 1 deck")
                        self.deck_qty = 1
                    elif deck_qty > 999:
                        self.slow_type("We don't have that many. How about 10? Because that's what \033[36myou're\033[0m going to get")
                        self.deck_qty = 10
                    time.sleep(.4)
                    print("\n")
                    break
                except:
                    self.slow_type("That can't be right. That's not a number.")
                    print("\n") 
            self.super_deck = Deck(self.deck_qty)
            self.player = Player(self.entered_name, 1)
            self.dealer = Player("Ace", 2)
            self.slow_type(f"\033[1m\033[36m{self.entered_name}\033[0m, we are going to play a simple game called highest card.")
            time.sleep(.4)
            print("\n")

            self.slow_type("Suit doesn't matter.")
            time.sleep(.4)
            print("\n")

            # Handles user input for random text and excessive numbers


            # Creates the players and the deck
        


    # This would be part of the While loop that keeps the game going
        def highest_card_game_play(self):
                    self.slow_type("Alright, now \033[32mI\033[0m am going to deal \033[36myou\033[0m a card")
                    
                    # Players get cards
                    self.player.draw_card(self.super_deck)
                    self.dealer.draw_card(self.super_deck)

                    time.sleep(.4)
                    print("\n")

                    # Player Card is displayed
                    self.slow_type(f"Ok \033[1m\033[36m{self.entered_name}\033[0m, go ahead and look at \033[36myour\033[0m card")
                    time.sleep(.4)
                    player_card = self.player.show_hand()
                    for bologna in player_card: # Named purely for my amusement
                        print(bologna)
                    print("\n")
                    
                    # User response is handled here with the list of acceptable responses
                    # There was a bug where the first response could be almost anything, but all other responses needed to match it.
                    user_response = self.ready()
                    while not self.any_affirmative_answer(user_response):
                        responses = ["Hurry up slowpoke", "What's taking so long?", "Need help or something", 
                                    "Ugh... Hurry!", "What's the hold up?", "Come on already...", 
                                    "We're aren't getting any younger", "Pick up the pace dude..."]
                        self.slow_type(random.choice(responses))
                        print("\n")
                        user_response = self.ready()
                    
                    # Dealer Card is shown
                    dealer_card = self.dealer.show_hand()
                    for folgers in dealer_card: # Named purely for my amusement
                            print(folgers) 
                    print("\n")    

                    end_of_game = self.determine_winner(self.dealer, self.player)

                    # The deck has to receive the card into it's discard before the player discards it from their hand, 
                    # otherwise it causes an error 
                    self.super_deck.add_to_discard(self.player.hand[0])
                    self.player.discard_card(0)
                    self.super_deck.add_to_discard(self.dealer.hand[0])
                    self.dealer.discard_card(0)
                    
                    # Displays the winning message
                    self.slow_type(f"\033[32mI\033[0m have {dealer_card[0]} and \033[36myou\033[0m have {player_card[0]}. It looks like {end_of_game} won!")
                    print("\n")
                    self.slow_type(f" Dealer Wins: \033[92m{self.dealer.score["wins"]}\033[0m, Losses: \033[31m{self.dealer.score["losses"]}\033[0m, and Draws: \033[33m{self.dealer.score["draws"]}\033[0m")
                    self.slow_type(f" {self.entered_name} Wins: \033[92m{self.player.score["wins"]}\033[0m, Losses: \033[31m{self.player.score["losses"]}\033[0m, and Draws: \033[33m{self.player.score["draws"]}\033[0m")
                    print("\n")

                    self.slow_type("Would you like to play again?")
                    play_again = self.any_affirmative_answer(input("").casefold())
                    return play_again
        def determine_winner(self, dealer, player):
            dealer_card_value = dealer.hand[0].get_value()
            player_card_value = player.hand[0].get_value()

            winner = ""
            if dealer_card_value > player_card_value:
                winner = "\033[32mI\033[0m" # Color coded I
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

        # This section can just be part of a start game function in the Game Class. Need to rework the slow type function
        # The function was just expecting on parameter
        def __init__(self):
            self.player = None
            self.dealer = None
            self.slow_type("Initializing Program...")
            self.slow_type('Loading')
            for i in range(3):
                time.sleep(.4)
                sys.stdout.write('.')
                sys.stdout.flush()
            print("\n")

            self.slow_type("Hiya buddy! \033[32mMy\033[0m name is \033[1m\033[32mAce\033[0m and \033[32mI\033[0m will be your dealer!")
            time.sleep(.4)
            print("\n")

            self.slow_type("What is your name?")
            self.entered_name = input("")
            time.sleep(.4)
            print("\n")

            greetings = ["Yo", "Hey there", "Greetings", "Sup", "Hi", "How it do", "Howdy", "Well \033[32mI'll\033[0m be. Hi"]
            welcome = random.choice(greetings)
            self.slow_type(f"{welcome} \033[1m\033[36m{self.entered_name}\033[0m!")
            time.sleep(.4)
            print("\n")

            self.slow_type("So glad to meet \033[36myou\033[0m.")
            time.sleep(.4) 
            print("\n")
            self.highest_card_game_intro()
            play_again = True
            while play_again:
                play_again = self.highest_card_game_play()

            # This will be the end of the start game function and wont be part of the While loop.

            # This would be part of the Select Game and then Game Intro part

Game()


        # We could have a Would you like to play again?, Go to choose Game Screen, or just quit?
        # Each calling their own function 