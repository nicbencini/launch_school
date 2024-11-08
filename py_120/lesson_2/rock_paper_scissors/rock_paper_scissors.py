import random

class Player:

    CHOICES = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.move = None

class Computer(Player):
    def __init__(self):
        super().__init__()
    
    def choose(self):
        self.move = random.choice(Player.CHOICES)

class Human(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        while True:
            choice = input('Please input \'rock\', \'paper\' or \'scissors\'')
            if choice in Player.CHOICES:
                self.move = choice
                break
            print('Choice not valid!')


class Move:
    def __init__(self):
        # This seems like we need something to keep track
        # of the choice... a move object can be "paper", "rock" or "scissors"
        pass

class Rule:
    def __init__(self):
        pass

    # not sure where "compare" goes yet
    def compare(self, move1, move2):
        pass

class RPSGame:
    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors')

    def _display_goodbye_message(self):
        print('Thanks for playing Rock Paper Scissors. Goodbye!')

    def _display_winner(self):

        print(f'You choose {self._human.move}')
        print(f'The computer choses {self._computer.move}')

        if self._human.move == self._computer.move:
            print('It is a draw!')

        elif ((self._human.move == 'scissors' and self._computer.move == 'paper') 
            or (self._human.move == 'rock' and self._computer.move == 'scissors') 
            or (self._human.move == 'paper' and self._computer.move == 'rock')):

            print('Player has won!')
        else:
            print('Computer has won!')

    def _play_again(self):

        user_input = input('Do you want to play again? (y/n)')

        if user_input.startswith('y'):
            return True
        
        return False

    def play(self):

        self._display_welcome_message()

        while True:
            
            self._human.choose()
            self._computer.choose()
            self._display_winner()
            if not self._play_again():
                break
            
        self._display_goodbye_message()


game = RPSGame()
game.play()