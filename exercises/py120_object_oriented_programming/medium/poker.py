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

class PokerHand:
    def __init__(self, deck):

        self._hand = [deck.draw() for _ in range(5)]
        self._ranks = [card.rank for card in self._hand]
        self._suits = [card.suit for card in self._hand]
        self._values = [card.value for card in self._hand]
        self._unique_suits = set(self._suits)
        self._unique_values = set(self._values)

    def names(self):
        return [str(card) for card in self._hand]

    def print(self):
       for card in self._hand:
           print(card)

    def evaluate(self):
        if self._is_royal_flush():
            return "Royal flush"
        elif self._is_straight_flush():
            return "Straight flush"
        elif self._is_four_of_a_kind():
            return "Four of a kind"
        elif self._is_full_house():
            return "Full house"
        elif self._is_flush():
            return "Flush"
        elif self._is_straight():
            return "Straight"
        elif self._is_three_of_a_kind():
            return "Three of a kind"
        elif self._is_two_pair():
            return "Two pair"
        elif self._is_pair():
            return "Pair"
        else:
          return "High card"
        
    def _is_same_suit(self):
        return len(self._unique_suits) == 1

    def _are_in_sequence(self):

        sorted_values = sorted(self._values)

        for idx,value in enumerate(sorted_values):
            if idx < len(sorted_values) - 1 and sorted_values[idx + 1] - value != 1:
                return False
        
        return True
    
    def _count_values(self):

        value_count = []

        for value in self._unique_values:

            value_count.append(self._values.count(value))
        
        value_count.sort()

        return value_count

    def _is_royal_flush(self):

        royal_flush = ['Ace', 'Queen', 'King', 'Jack', 10]

        return self._is_same_suit() and all([rank in self._ranks for rank in royal_flush])

    def _is_straight_flush(self):

        return self._is_same_suit() and self._are_in_sequence()

    def _is_four_of_a_kind(self):

        value_count = self._count_values()

        return value_count == [1,4]
        
    def _is_full_house(self):

        value_count = self._count_values()

        return value_count == [2,3]

    def _is_flush(self):

        return self._is_same_suit()

    def _is_straight(self):

        return self._are_in_sequence() and len(self._unique_suits) > 1

    def _is_three_of_a_kind(self):

        value_count = self._count_values()

        return value_count == [1,1,3]

    def _is_two_pair(self):

        value_count = self._count_values()

        return value_count == [1,2,2]

    def _is_pair(self):

        value_count = self._count_values()

        return value_count == [1,1,1,2]

hand = PokerHand(Deck())
hand.print()
print(hand.evaluate())
print()

# Adding TestDeck class for testing purposes

class TestDeck(Deck):
    def __init__(self, cards):
        self._cards = cards

# All of these tests should return True

hand = PokerHand(
    TestDeck(
        [
            Card("Ace", "Hearts"),
            Card("Queen", "Hearts"),
            Card("King", "Hearts"),
            Card("Jack", "Hearts"),
            Card(10, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Royal flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Clubs"),
            Card("Queen", "Clubs"),
            Card(10, "Clubs"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight flush")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Four of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Full house")

hand = PokerHand(
    TestDeck(
        [
            Card(10, "Hearts"),
            Card("Ace", "Hearts"),
            Card(2, "Hearts"),
            Card("King", "Hearts"),
            Card(3, "Hearts"),
        ]
    )
)

print(hand.evaluate() == "Flush")

hand = PokerHand(
    TestDeck(
        [
            Card(8, "Clubs"),
            Card(9, "Diamonds"),
            Card(10, "Clubs"),
            Card(7, "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card("Queen", "Clubs"),
            Card("King", "Diamonds"),
            Card(10, "Clubs"),
            Card("Ace", "Hearts"),
            Card("Jack", "Clubs"),
        ]
    )
)
print(hand.evaluate() == "Straight")

hand = PokerHand(
    TestDeck(
        [
            Card(3, "Hearts"),
            Card(3, "Clubs"),
            Card(5, "Diamonds"),
            Card(3, "Spades"),
            Card(6, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Three of a kind")

hand = PokerHand(
    TestDeck(
        [
            Card(9, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(8, "Spades"),
            Card(5, "Hearts"),
        ]
    )
)
print(hand.evaluate() == "Two pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card(9, "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "Pair")

hand = PokerHand(
    TestDeck(
        [
            Card(2, "Hearts"),
            Card("King", "Clubs"),
            Card(5, "Diamonds"),
            Card(9, "Spades"),
            Card(3, "Diamonds"),
        ]
    )
)
print(hand.evaluate() == "High card")