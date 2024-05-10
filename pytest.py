import pytest
from card-game.py import Player, Deck, Card, determine_winner

# Your test functions go here...


# Test case for determining the winner
def test_determine_winner():
    # Create players
    dealer = Player("Dealer", 1)
    player = Player("Player", 2)

    # Create cards
    dealer_card = Card("A", "\u2660")
    player_card = Card("2", "\u2663")

    # Assign cards to players
    dealer.hand.append(dealer_card)
    player.hand.append(player_card)

    # Determine winner
    winner = determine_winner(dealer, player)

    # Check if the correct winner is determined
    assert winner == "Player"

# Test case for drawing card from the deck
def test_draw_from_deck():
    # Create a deck with known cards
    deck = Deck(number_of_decks=1)
    deck.cards = [Card("A", "\u2660"), Card("2", "\u2663")]

    # Draw a card from the deck
    drawn_card = deck.draw_from_deck()

    # Check if the drawn card matches the top card of the deck
    assert drawn_card.value == "2"
    assert drawn_card.suit == "\u2663"