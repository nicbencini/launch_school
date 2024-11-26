
"""
- (N) Dealer
- (N) Player
- (N) Hand
- (N) Deck
    -(N) Card
    -(V) Shuffle
    -(V) Deal
- (N) Game
    -(V) Evaluate
    -(V) Display


"""

import random
import os

class Card_Player:
    def __init__(self):
        self.hand = Hand()

    def take_card(self, card):
        self.hand += card

class Player(Card_Player):
    
    def display_cards(self):
        print(f'Player cards: {str(self.hand)}')
    
    def display_score(self):
        print(f'Player score: {self.hand.score}')
    
    def __str__(self):
        return 'Player'


class Dealer(Card_Player):   

    def display_cards(self):
        print(f'Dealer cards: [------------]  {self.hand.cards[0]}')
    
    def reveal_cards(self):
        print(f'Dealer cards: {str(self.hand)}')
    
    def __str__(self):
        return 'Dealer'
    

class Hand:
    
    def __init__(self):
        self.cards = []
    
    def __iadd__(self, other):

        if not isinstance(other, Card):
            return NotImplemented('Only cards can be added to hands')
        
        self.cards.append(other)
        return self
    
    @property
    def score(self):
        return sum([card.score for card in self.cards])
    
    def __str__(self):
        return '  '.join([str(card) for card in self.cards])

class Deck:

    VALUES = ['2',
              '3',
              '4',
              '5',
              '6',
              '7',
              '8',
              '9',
              '10',
              'Jack',
              'Queen',
              'King',
              'Ace'              
              ]
    
    SUITS = ['Hearts',
             'Spades',
             'Diamonds',
             'Clubs'
             ]

    def __init__(self):
        self.cards = [Card(suit, value) for value in self.VALUES for suit in self.SUITS]

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, player, number_of_cards):
        
        for _ in range(number_of_cards):
            player.hand += self.cards.pop(0)
    
    def reset(self):
        self.cards = [Card(suit, value) for value in self.VALUES for suit in self.SUITS]

        

    
class Card:

    CARD_RANK = { '2': 2,
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
    
    def __init__(self, suit, value):
        self.value = value
        self.suit = suit
    
    def __str__(self):
        return f'[{self.value} of {self.suit}]'
    
    @property
    def score(self):
        return self.CARD_RANK[self.value]


class TO_Game:
    """
    Algorithm 
    - Shuffle Deck
    - Deal hand for player and for dealer
    - Display cards
    - Ask player to hit or stay
        if hit deal another card. If stay break
    - Dealer plays
    - Check for winner
    """
    LIMIT = 21
    
    def __init__(self):
        self.deck = Deck()
        self.dealer = Dealer()
        self.player = Player()
    
    def play(self):

        self.deck.shuffle()
        self.deck.deal(self.dealer, 2)
        self.deck.deal(self.player, 2)

        self.player_plays()
        self.dealer_plays()
        
        self.display_result()

        self.display_goodbye_message()

    
    def display_welcome_message(self):
        print('Welcome to Twenty One!\n')
    
    def display_goodbye_message(self):
        print('\nThanks for playing! Goodbye!')
    
    def player_plays(self):

        while True:

            os.system('clear')

            self.display_welcome_message()

            self.player.display_cards()
            self.dealer.display_cards()

            print('\n')
            self.player.display_score()

            if self.hit_or_stay():
                self.deck.deal(self.player,1)
            else:
                break


    def display_winner(self, player):
        print(f'\n{player} wins!!!!')

    def dealer_plays(self):
        pass
    
    def display_result(self):
        
        if self.player.hand.score > 21:
            self.display_winner(self.dealer)
        elif self.dealer.hand.score > 21:
            self.display_winner(self.player)

    def hit_or_stay(self):

        while True:

            if self.player.hand.score > 21:
                return False

            player_input = input('Hit or stay? (h/s)')

            if player_input == 'h':
                return True
            elif player_input == 's':
                return False
            else:
                print('Input not valid!')   

twenty_one = TO_Game()
twenty_one.play()