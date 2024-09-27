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

    print(f'Score limit is {SCORE_LIMIT}')
    print(f'Player score: {get_score(player_cards_)} | Dealer score: {get_score(dealer_cards_)}')

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
    # create count for aces
    # cycle through cards and count aces, if card is not ace then add score to total score
    # if total score + (count of aces -1 + 11) < 21 then first ace is 11
    # all following aces are 1
    # if not all aces are 1
    """
    aces_count = 0
    score = 0

    for card in cards_:
        if 'Ace' in card:
            aces_count += 1
        else:
            score += VALUES[card.split(' ')[0]]

    if aces_count > 0 and (score + aces_count -1 + 11) <= SCORE_LIMIT:
        score += 11 + aces_count - 1
    else:
        score += aces_count

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

def play_twenty_one():

    deck = initialize_deck()
    shuffle_deck(deck)

    player_cards = deal(deck, 2)
    dealer_cards = deal(deck, 2)

    display_cards(player_cards, [dealer_cards[0]])

    while True:

        print('Choose whether to Hit or Stay (h/s)')
        player_choice = input()

        if player_choice == 's':
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

    if result == True:
        print('\n\nPlayer wins!')
    elif result == False:
        print('\n\nDealer wins!')
    else:
        print('\n\nIt is a draw!')

    return result

player_win_count = 0
dealer_win_count = 0

while True:
    
    play_twenty_one()

    game_result = True

    if game_result == True:
        player_win_count += 1
    elif game_result == False:
        dealer_win_count += 1

    print(f'Player win count = {player_win_count} | Dealer win count = {dealer_win_count}')

    print('Would you like to play again? (y/n)')

    play_again = input()

    if play_again != 'y':
        break

