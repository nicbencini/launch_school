"""


- (N) Game
    -(V) Play
    -(V) Select Winner
- (N) Board
    - (V) Evaulate 
    - (N) Square
        - (N) Mark
- (N) Player
    - (V) Mark
    - (V) Play
    -Human
    -Computer



"""

import random

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
    
    def mark_square_at(self, key, marker):
        self.squares[key].marker = marker
    
    def unused_squares(self):
        return [key
                for key, square in self.squares.items()
                if square.is_unused()]

class Row:
    def __init__(self):
        # STUB
        # We need some way to identify a row of 3 squares
        pass

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
    def __init__(self):
        self.board = Board()
        self.human = Human()
        self.computer = Computer()

    def play(self):
        # SPIKE
        self.display_welcome_message()

        while True:
            self.board.display()

            self.human_moves()
            if self.is_game_over():
                break

            self.computer_moves()
            if self.is_game_over():
                break

        
        self.board.display()
        self.display_results()
        self.display_goodbye_message()
    
    def display_welcome_message(self):
        print("Welcome to Tic Tac Toe!")

    def display_goodbye_message(self):
        print("Thanks for playing Tic Tac Toe! Goodbye!")

    def display_results(self):
        # STUB
        # Show the results of this game (win, lose, tie).
        pass

    def human_moves(self):
        choice = None
        while True:
            valid_choices = self.board.unused_squares()
            choices_list = [str(choice) for choice in valid_choices]
            choices_str = ", ".join(choices_list)
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
        choice = random.choice(valid_choices)
        self.board.mark_square_at(choice, self.computer.marker)

    def is_game_over(self):
        # STUB
        # We'll start by assuming the game never ends.
        return False

game = TTTGame()
game.play()