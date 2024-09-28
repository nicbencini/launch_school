"""
Problem:

Examples:

Data structure:
Dictionary with the key being the card and the value being the amount of points

Algorithm:
1. Initialize deck
    - Create dictionary
    - Create algorithm for combinig suit with card value as string
        -Cycle through suits and cycle through cards and combine to create deck
2. Deal cards to player and dealer
    - Create dealing algorithm that select 2 cards to the player and 2 cards to the dealer
3. Player turn: hit or stay
   - repeat until bust or stay
4. If player bust, dealer wins.
5. Dealer turn: hit or stay
   - repeat until total >= 17
6. If dealer busts, player wins.
7. Compare cards and declare winner.
"""

import random
import os

# Constants
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
VALUES = { '2': 2,
           '3': 3,
           '4': 4,
           '5': 5,
           '6': 6,
           '7': 7,
           '8': 8,
           '9': 9,
           '10': 10,
           'Jack': 10,
           'Queen':10,
           'King': 10,
           'Ace': 1}

SCORE_LIMIT = 42
DEALER_LIMIT =  SCORE_LIMIT - 4

# Functions
def initialize_deck():

    return [f'{value[0]} of {suit}' for suit in SUITS
                                    for value in VALUES.items()
            ]

def shuffle_deck(deck_):

    random.shuffle(deck_)

def deal(deck_, number_of_cards):
    cards = []

    for _ in range(number_of_cards):
        cards.append(deck_.pop(0))

    return cards


def display_cards(player_cards_, dealer_cards_):

    os.system('clear')

    print(f'Player win count: {player_win_count:02d} | Dealer win count: {dealer_win_count:02d}')
    print(f'Player score: {get_score(player_cards_):02d}     |'
          f' Dealer score: {get_score(dealer_cards_):02d}')
    print(f'Game score limit is {SCORE_LIMIT}')

    print('\nPlayer Cards:')
    for card in player_cards_:

        print (f'[ {card} ]')


    print('\nDealer Cards:')
    for card in dealer_cards_:

        print (f'[ {card} ]')

    if len(dealer_cards_) == 1:
        print('[--------------]')


def get_score(cards_):
    """
    Algorithm:
    # create count for aces
    # cycle through cards and count aces, if card is not ace then add score to total score
    # if card is ace
        # check if adding 11 is within limit
        # if not add 11, otherwise add 1 to score
    """
    aces_count = 0
    score = 0

    for card in cards_:
        if 'Ace' in card:
            aces_count += 1
        else:
            score += VALUES[card.split(' ')[0]]

    for i in range(aces_count):
        if score + 11 > SCORE_LIMIT:
            score += 1
        else:
            score += 11

    return score

def evaluate_result(player_cards_, dealer_cards_):

    player_score = get_score(player_cards_)
    dealer_score = get_score(dealer_cards_)

    if player_score > dealer_score:
        return True
    elif dealer_score > player_score:
        return False
    else:
        return None

def prompt(message):
    print(f'==> {message}')

def input_handler(message, proceed_key, return_key):

    while True:
        prompt(f'{message} ({proceed_key}/{return_key})')
        user_input = input()

        if user_input == proceed_key:
            return True
        elif user_input == return_key:
            return False
        else:
            prompt('Input not recognised.')



def play_twenty_one():

    deck = initialize_deck()
    shuffle_deck(deck)

    player_cards = deal(deck, 2)
    dealer_cards = deal(deck, 2)

    display_cards(player_cards, [dealer_cards[0]])

    while True:

        print('\n')
        deal_again = input_handler('Choose whether to Hit or Stay', 'h', 's')

        if not deal_again:
            break

        player_cards += deal(deck, 1)
        display_cards(player_cards, [dealer_cards[0]])

        if get_score(player_cards) > SCORE_LIMIT:
            print('\n\nPlayer busts! The dealer has won!')
            return False

    while True:
        dealer_cards += deal(deck, 1)

        display_cards(player_cards, dealer_cards)

        if get_score(dealer_cards) > SCORE_LIMIT:
            print('\n\nDealer busts! The player has won!')
            return True

        if get_score(dealer_cards) > DEALER_LIMIT:
            break

    result = evaluate_result(player_cards, dealer_cards)

    if result is True:
        print('\n\nPlayer wins!')
    elif result is False:
        print('\n\nDealer wins!')
    else:
        print('\n\nIt is a draw!')

    return result

# Global Variables
player_win_count = 0
dealer_win_count = 0

#Game Loop
while True:

    game_result = play_twenty_one()

    if game_result is True:
        player_win_count += 1
    elif game_result is False:
        dealer_win_count += 1

    if player_win_count == 3:
        print ('Player has won the match - best out of five!')
        player_win_count = 0
        dealer_win_count = 0
    elif dealer_win_count == 3:
        print ('Dealer has won the match- best out of five!')
        player_win_count = 0
        dealer_win_count = 0

    print('\n')
    play_again = input_handler('Would you like to play again?', 'y', 'n')

    if not play_again:
        break
