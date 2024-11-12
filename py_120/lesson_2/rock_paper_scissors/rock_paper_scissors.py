
import os
import random

#-----MIXINS-----#
class DisplayMixin:

    # Dispaly mixin for handling all display related methods

    def update_display(self):

        os.system('clear')
        self.disaply_welcome_message()
        self.display_score()

    def display_choices(self):
        print(f'You choose {self._human.move}. The computer choses {self._computer.move}')

    def display_score(self):
        print(f'Player Score: {self._human.score} | Computer Score: {self._computer.score}\n')

    @staticmethod
    def display_player_choice_input():
        choice = input('Please input \'rock\', \'paper\' or'
                       ' \'scissors\' or \'lizard\' or \'spock\'')
        return choice

    @staticmethod
    def display_round_winner(player):
        print(f'{player} has won the round!')

    @staticmethod
    def display_game_winner(player):
        print(f'\n*****{str(player).upper()} HAS WON THE GAME!*****')

    @staticmethod
    def display_tie():
        print('It is a tie!')

    @staticmethod
    def display_continue_message():
        input('\nPress enter to continue...')

    @staticmethod
    def disaply_welcome_message():
        print('Welcome to Rock Paper Scissors Lizard Spock')

    @staticmethod
    def display_goodbye_message():
        print('\nThanks for playing. Goodbye!')

    @staticmethod
    def display_play_again():
        user_input = input('Do you want to play again? (y/n)')

        if user_input.startswith('y'):
            return True
        return False

    @staticmethod
    def display_not_valid_choice_message():
        print('Choice not valid!')

    @staticmethod
    def display_move_history():
        user_input = input('Do you want to display move history? (y/n)')

        if user_input.startswith('y'):
            return True
        return False

#-----PLAYERS-----#
class Player:

    def __init__(self):
        self.move = Move()
        self._score = 0

    @property
    def score(self):
        return self._score

    def increase_score(self):
        self._score += 1

    def reset_score(self):
        self._score = 0

class Computer(Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move.computer_choice()

    def __str__(self):
        return 'Computer'

class Human(DisplayMixin, Player):
    def __init__(self):
        super().__init__()

    def choose(self):
        self.move.human_choice()

    def __str__(self):
        return 'Player'

#-----MOVES-----#
class Rock():

    def __init__(self):
        pass

    def __gt__(self, other):

        if isinstance(other, (Lizard, Scissors)):
            return True
        return False

    def __eq__(self,other):

        if isinstance(other,Rock):
            return True
        return False

    def __str__(self):
        return 'rock'

class Paper():

    def __init__(self):
        pass

    def __gt__(self, other):

        if isinstance(other, (Rock, Spock)):
            return True
        return False

    def __eq__(self,other):

        if isinstance(other,Paper):
            return True
        return False

    def __str__(self):
        return 'paper'

class Scissors():

    def __init__(self):
        pass

    def __gt__(self, other):

        if isinstance(other, (Paper, Lizard)):
            return True
        return False

    def __eq__(self,other):

        if isinstance(other,Scissors):
            return True
        return False

    def __str__(self):
        return 'scissors'

class Lizard():

    def __init__(self):
        pass

    def __gt__(self, other):

        if isinstance(other, (Paper, Spock)):
            return True
        return False

    def __eq__(self,other):

        if isinstance(other,Lizard):
            return True
        return False

    def __str__(self):
        return 'lizard'

class Spock():

    def __init__(self):
        pass

    def __gt__(self, other):

        if isinstance(other, (Scissors, Rock)):
            return True
        return False

    def __eq__(self,other):

        if isinstance(other,Spock):
            return True
        return False

    def __str__(self):
        return 'spock'

class Move(DisplayMixin):

    CHOICES = {'rock':Rock(),
            'paper':Paper(),
            'scissors':Scissors(),
            'lizard':Lizard(),
            'spock':Spock()
    }

    move_history = []

    def __init__(self):

        self._player_choice = None

    def computer_choice(self):
        self._player_choice = random.choice(list(self.CHOICES.values()))
        Move.move_history.append(f'- Computer has played {self._player_choice}')

    def human_choice(self):
        while True:
            choice = self.display_player_choice_input()
            if choice in self.CHOICES.keys():
                self._player_choice = self.CHOICES[choice]
                Move.move_history.append(f'- Human has played {self._player_choice}')
                break
            self.display_not_valid_choice_message()

    def __gt__(self, other):

        if not isinstance(other, Move):
            return NotImplemented

        return self._player_choice > other._player_choice

    def __eq__(self, other):

        if not isinstance(other, Move):
            return NotImplemented

        return self._player_choice == other._player_choice

    def __str__(self):
        return str(self._player_choice)

    @staticmethod
    def print_move_history():

        os.system('clear')

        print('----Move History----')
        for log in Move.move_history:
            print(log)

#-----GAME-----#
class RPSGame(DisplayMixin):
    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _get_winner(self):

        self.display_choices()

        if self._human.move == self._computer.move:
            self.display_tie()

        elif self._human.move > self._computer.move:
            self._human.increase_score()
            self.display_round_winner(self._human)

        else:
            self._computer.increase_score()
            self.display_round_winner(self._computer)


    def play(self):

        while True:

            while True:

                self.update_display()
                self._human.choose()
                self._computer.choose()
                self._get_winner()

                if self._human.score == 5:
                    self.display_game_winner(self._human)
                    break
                if self._computer.score == 5:
                    self.display_game_winner(self._computer)
                    break

                self.display_continue_message()

            if not self.display_play_again():
                break

            self._human.reset_score()
            self._computer.reset_score()

        self.display_goodbye_message()
        if self.display_move_history():
            Move.print_move_history()

game = RPSGame()
game.play()
