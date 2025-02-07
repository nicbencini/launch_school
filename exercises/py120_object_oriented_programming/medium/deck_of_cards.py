import random

class Card:

    CARD_RANKING = [2,3,4,5,6,7,8,9,10,'Jack','Queen','King','Ace']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    @property
    def value(self):
        return self.CARD_RANKING.index(self.rank)
    
    def __lt__(self, other):

        if not isinstance(other,Card):
            return NotImplemented
        
        return self.value < other.value
    
    def __gt__(self, other):

        if not isinstance(other,Card):
            return NotImplemented
        
        return self.value > other.value
    
    def __ge__(self, other):

        if not isinstance(other,Card):
            return NotImplemented
        
        return self.value >= other.value
    
    def __le__(self, other):

        if not isinstance(other,Card):
            return NotImplemented
        
        return self.value <= other.value
    
    def __eq__(self, other):

        if not isinstance(other,Card):
            return NotImplemented
        
        return self.value == other.value


    def __str__(self):
        return f'{self.rank} of {self.suit}'


class Deck:
    RANKS = list(range(2, 11)) + ['Jack', 'Queen', 'King', 'Ace']
    SUITS = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

    def __init__(self):

        self._cards = []
        self._regenerate_deck()
    
    def draw(self):
        if len(self._cards) == 0:
            self._regenerate_deck()
        
        return self._cards.pop(0)


    def _regenerate_deck(self):

        self._cards = [Card(rank,suit) for rank in self.RANKS for suit in self.SUITS]
        random.shuffle(self._cards)



deck = Deck()
drawn = []
for _ in range(52):
    drawn.append(deck.draw())

count_rank_5 = sum([1 for card in drawn if card.rank == 5])
count_hearts = sum([1 for card in drawn if card.suit == 'Hearts'])

print(count_rank_5 == 4)      # True
print(count_hearts == 13)     # True

drawn2 = []
for _ in range(52):
    drawn2.append(deck.draw())

print(drawn != drawn2)        # True (Almost always).

print([str(card) for card in drawn])
print([str(card) for card in drawn2])