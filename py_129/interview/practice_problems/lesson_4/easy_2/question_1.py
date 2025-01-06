class Game:
    count = 0

    def __init__(self):
        Game.count += 1

    def play(self):
        return f'Start the {self.__class__.__name__} game!'

class Bingo(Game):

    def __init__(self, game, player):
        super().__init__()
        self._game = game
        self._player = player

    @property
    def player_name(self):
        return self._player

class Scrabble(Game):

    def __init__(self, game, player_1, player_2):
        super().__init__()
        self._game = game
        self._player_1 = player_1
        self._player_2 = player_2

    @property
    def player_name1(self):
        return self._player_1
    
    @property
    def player_name2(self):
        return self._player_2

bingo = Bingo('Bingo', 'Bill')
print(Game.count)                       # 1
print(bingo.play())                     # Start the Bingo game!
print(bingo.player_name)                # Bill

scrabble = Scrabble('Scrabble', 'Jill', 'Sill')
print(Game.count)                       # 2
print(scrabble.play())                  # Start the Scrabble game!
print(scrabble.player_name1)            # Jill
print(scrabble.player_name2)            # Sill
print(scrabble.player_name)
# AttributeError: 'Scrabble' object has no attribute 'player_name'