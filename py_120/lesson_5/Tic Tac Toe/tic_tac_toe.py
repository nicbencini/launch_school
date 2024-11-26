"""


- (N) Game
    -(V) Play
    -(V) Select Winner
- (N) Board
    - (V) Evaulate 
    - (N) Square
        - (N) Mark
    - (N) Row
        - 3_in_a_row
        - 2_in_a_row

- (N) Player
    - (V) Mark
    - (V) Play
    -Human
    -Computer



"""

import random
import os

def clear_screen():
    os.system('clear')

class Square:
    INITIAL_MARKER = " "
    HUMAN_MARKER = "X"
    COMPUTER_MARKER = "O"

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, marker):
        self._marker = marker

    def __init__(self, marker=INITIAL_MARKER):
        self.marker = marker
    
    def __str__(self):
        return self.marker
    
    def is_unused(self):
        return self.marker == Square.INITIAL_MARKER

class Board:

    def __init__(self):
        self.squares = {count:Square() for count in range(1,10)}

    def display(self):
        print()
        print("     |     |")
        print(f"  {self.squares[1]}  |"
              f"  {self.squares[2]}  |"
              f"  {self.squares[3]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[4]}  |"
              f"  {self.squares[5]}  |"
              f"  {self.squares[6]}")
        print("     |     |")
        print("-----+-----+-----")
        print("     |     |")
        print(f"  {self.squares[7]}  |"
              f"  {self.squares[8]}  |"
              f"  {self.squares[9]}")
        print("     |     |")
        print()
    
    def display_with_clear(self):
        clear_screen()
        print("\n")
        self.display()

    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker
    
    def unused_squares(self):
        return [key
                for key, square in self.squares.items()
                if square.is_unused()]
    
    def is_full(self):
        return len(self.unused_squares()) == 0
    
    def count_markers_for(self, player, keys):
        markers = [self.squares[key].marker for key in keys]
        return markers.count(player.marker)
    
    def reset(self):
        self.squares = {count:Square() for count in range(1,10)}

    def unused_row_squares(self, keys):
        return [key for key in keys if self.squares[key].is_unused()]




class Marker:
    def __init__(self):
        # STUB
        # A marker is something that represents a board
        #   square that belongs to a particular player. That
        #   is, it's a square that was chosen by the player.
        pass

class Player:
    def __init__(self, marker):
        self.marker = marker

    @property
    def marker(self):
        return self._marker

    @marker.setter
    def marker(self, value):
        self._marker = value

    # Delete `Player.mark` method; `Board` provides
    # `mark_square_at` instead.


    def mark(self):
        # STUB
        # We need a way to mark the board with this player's
        #   marker. How do we access the board?
        pass

class Human(Player):
    def __init__(self):
        super().__init__(Square.HUMAN_MARKER)

class Computer(Player):
    def __init__(self):
        super().__init__(Square.COMPUTER_MARKER)

class TTTGame:

    POSSIBLE_WINNING_ROWS = (
        (1, 2, 3),  # top row of board
        (4, 5, 6),  # center row of board
        (7, 8, 9),  # bottom row of board
        (1, 4, 7),  # left column of board
        (2, 5, 8),  # middle column of board
        (3, 6, 9),  # right column of board
        (1, 5, 9),  # diagonal: top-left to bottom-right
        (3, 5, 7),  # diagonal: top-right to bottom-left
    )

    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()

    def play(self):
        self.display_welcome_message()
        self.board.display()
        while True:
            while True:

                self.human_moves()
                if self.is_game_over():
                    break

                self.computer_moves()
                if self.is_game_over():
                    break

                self.board.display_with_clear()
            
            self.board.display_with_clear()
            self.display_results()
            if not self.display_play_again():
                break

            self.board.reset()
            self.board.display_with_clear()

        self.display_goodbye_message()
    
    def display_welcome_message(self):
        clear_screen()
        print("Welcome to Tic Tac Toe!")
        print()

    def display_goodbye_message(self):
        print("Thanks for playing Tic Tac Toe! Goodbye!")

    def display_play_again(self):
        result = input('Would you like to play again? (y/n)')

        if result.lower().startswith('y'):
            return True
        
        return False

    def display_results(self):
        if self.is_winner(self.human):
            print("You won! Congratulations!")
        elif self.is_winner(self.computer):
            print("I won! I won! Take that, human!")
        else:
            print("A tie game. How boring.")

    def is_winner(self, player):
        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.three_in_a_row(player, row):
                return True

        return False

    def is_game_over(self):
        return self.board.is_full() or self.someone_won()
    
    def three_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 3
    
    def two_in_a_row(self, player, row):
        return self.board.count_markers_for(player, row) == 2

    def someone_won(self):
        return (self.is_winner(self.human) or
                self.is_winner(self.computer))

    def human_moves(self):
        choice = None
        while True:
            valid_choices = self.board.unused_squares()
            choices_list = [str(choice) for choice in valid_choices]
            choices_str = TTTGame.join_or(choices_list)
            prompt = f"Choose a square ({choices_str}): "
            choice = input(prompt)

            try:
                choice = int(choice)
                if choice in valid_choices:
                    break
            except ValueError:
                pass

            print("Sorry, that's not a valid choice.")
            print()

        self.board.mark_square_at(choice, self.human.marker)

    def computer_moves(self):
        valid_choices = self.board.unused_squares()

        choice = self.find_winning_square(self.computer)

        if choice == None:
            choice = self.find_winning_square(self.human)
        
        if choice == None:

            if 5 in valid_choices:
                choice = 5
            else:
                choice = random.choice(valid_choices)
            

        self.board.mark_square_at(choice, self.computer.marker)
    
    def find_winning_square(self, player):

        for row in TTTGame.POSSIBLE_WINNING_ROWS:
            if self.board.count_markers_for(player, row) == 2 and len(self.board.unused_row_squares(row)) == 1:
                return self.board.unused_row_squares(row)[0]

        return None

    @staticmethod
    def join_or(numbers_list, seperator=',', conjunctor='and'):

        if len(numbers_list) > 1:
            return f'{seperator} '.join(numbers_list[:-1]) + f' {conjunctor} ' + numbers_list[-1]
        
        return numbers_list[0]


game = TTTGame()
game.play()