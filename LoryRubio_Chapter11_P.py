# Lory Rubio Programming Assignment 11
# This game program uses the Deck object. It deals a Poker hand of five cards.
# Then prompts the user to enter a series of numbers that selects cards to be replaced during a draw phrase.
# Then it will print the result of drawing the new cards.

import random
from zipfile import sizeEndCentDir


# Create the Deck class that will have an auto-shuffling deck of 5-card size
class Deck():
    def __init__(self,size):
        self.card_list = [i for i in range(52)]
        random.shuffle(self.card_list)
        self.current_card = 0
        self.size = size

    def deal(self):
        if self.size - self.current_card <1:
            random.shuffle (self.card_list)
            self.current_card = 0
            print ('reshuffling ...!!!')
        self.current_card += 1
        return self.card_list [self.current_card -1]

# Now create the suits and the combination of cards
ranks =['2','3','4','5','6','7','8','9','10','J','Q','K','A']
suits = ['clubs','diamonds','hearts','spades']

# Now the functions that will assign the corresponding values to the rank and suit
def assign_cards(card_number):
    rank = ranks[card_number % 13]
    suit = suits[card_number // 13]
    return f"{rank} of {suit}"

# Function to deal the 5 handed card
def deal_hand(deck, hand_size=5):
        hand = [deck.deal() for _ in range(hand_size)]
        return hand

# Function to replace selected cards
def replace_cards(deck, hand, indexes):
    for index in indexes:
        if 0 <= index < len(hand):
            hand[index] = deck.deal()
    return hand

# Creating the game function
my_deck = Deck(52)
hand = deal_hand(my_deck)

# Show the user his hand
print ('Your hand is:')
for i, card in enumerate(hand):
    print(f'{i + 1}: {assign_cards(card)}')

# Ask user to input the number for the crd they want to replace
to_replace = input('Enter the cards from 1-5 you want to replace:' ).strip()

# If the statement to replace the hand
if to_replace:
    indexes = [int(i) - 1 for i in to_replace.split() if i.isdigit()]
    hand = replace_cards(my_deck, hand, indexes)

# Show new hand
print('Your new hand is:')
for card in hand:
    print(assign_cards(card))



