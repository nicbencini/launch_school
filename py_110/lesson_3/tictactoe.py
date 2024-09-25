import random
import os

INITIAL_MARKER = ' '  # near the top of the file
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'
GAMES_TO_WIN = 5
WINNING_LINES = [
                     [1,2,3], [4,5,6], [7,8,9], # rows
                     [1,4,7], [2,5,8], [3,6,9], # cols
                     [1,5,9], [3,5,7]           # diagonals
    ]

def display_board(board, score):

    os.system('clear')

    print(f'You are {HUMAN_MARKER}, computer is {COMPUTER_MARKER}')
    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')
    print(f'Player Score : {score['Player']}\nComputer Score : {score["Computer"]}')

def initialize_board():
    return {square: INITIAL_MARKER for square in range(1, 10)}

def prompt(message):
    print(f'==> {message}')

def empty_squares(board):
    return [key 
            for key, value in board.items() 
            if value == INITIAL_MARKER]

def player_chooses_square(board):

    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f"Choose a square ({join_or(valid_choices)}):")
        square = input().strip()
        if square in valid_choices:

            
            break
            

        prompt("Sorry, that's not a valid choice.")

    board[int(square)] = HUMAN_MARKER

def computer_defend(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line

        if board[sq1] == HUMAN_MARKER and board[sq2] == HUMAN_MARKER and board[sq3] != COMPUTER_MARKER:
            return sq3

        elif board[sq1] == HUMAN_MARKER and board[sq3] == HUMAN_MARKER and board[sq2] != COMPUTER_MARKER:
            return sq2

        elif board[sq3] == HUMAN_MARKER and board[sq2] == HUMAN_MARKER and board[sq1] != COMPUTER_MARKER:
            return sq1
        
    return None

def computer_attack(board):
    for line in WINNING_LINES:
        sq1, sq2, sq3 = line

        if board[sq1] == COMPUTER_MARKER and board[sq2] == COMPUTER_MARKER and board[sq3] != HUMAN_MARKER:
            return sq3

        elif board[sq1] == COMPUTER_MARKER and board[sq3] == COMPUTER_MARKER and board[sq2] != HUMAN_MARKER:
            return sq2

        elif board[sq3] == COMPUTER_MARKER and board[sq2] == COMPUTER_MARKER and board[sq1] != HUMAN_MARKER:
            return sq1
        
    return None
        
def computer_chooses_square(board):
    
    empty_square_values = empty_squares(board)

    if len(empty_square_values) == 0:
        return
    
    square = computer_attack(board)
    if square == None:
        square = computer_defend(board)

    if square == None:

        if 5 in empty_square_values:
            square = 5
        else:
            square = random.choice(empty_square_values)

    
        
    board[square] = COMPUTER_MARKER


def board_full(board):
    return len(empty_squares(board)) == 0

def someone_won(board):
    if detect_winner(board):
        return True
    return False

def detect_winner(board):

    for line in WINNING_LINES:
        sq1, sq2, sq3 = line
        if (board[sq1] == HUMAN_MARKER
                and board[sq2] == HUMAN_MARKER
                and board[sq3] == HUMAN_MARKER):
            return 'Player'
        elif (board[sq1] == COMPUTER_MARKER
                and board[sq2] == COMPUTER_MARKER
                and board[sq3] == COMPUTER_MARKER):
            return 'Computer'
        
    return None

def join_or(input_list, seperator = ', ', word = 'or'):

    output_string = ''

    if len(input_list) == 0:
            pass
    elif len(input_list) == 1:
        output_string = str(input_list[0])
    elif len(input_list) == 2:
        output_string = f'{input_list[0]} {word} {input_list[1]}'
    else:

        for index, number in enumerate(input_list):
            
                if index != len(input_list) - 1:
                    output_string += f'{number}{seperator} '
                else:
                    output_string += f'{word} {number}'
    
    return output_string

def continue_game(message):

    prompt(f'{message} (y or n)')
    answer = input().lower()

    if len(answer[0]) > 0 and answer[0] != 'y':
        return False
    
    return True

def winning_message(winner):
    strs = '*'*17 + '\n'
    print('')
    print (strs * 4)
    print(f'{winner.upper()} WON!!\n')
    print (strs * 4)
    print('')


def play_tic_tac_toe():
    
    score = {'Player':0,
             'Computer':0}
    
    while True:
        board = initialize_board()

        while True:
            display_board(board, score)

            player_chooses_square(board)

            if someone_won(board) or board_full(board):
                break

            computer_chooses_square(board)
            if someone_won(board) or board_full(board):
                break
        
        display_board(board, score)
        print(detect_winner(board))

        if someone_won(board):
            
            winner = detect_winner(board)
            score[winner] += 1

            prompt(f"{winner} won!")

            if score[winner] == 5:
                os.system('clear')
                winning_message(winner)
                prompt(f'{winner} won the match!!!!')
                score['Computer'] = 0
                score['Player'] = 0

        else:
            prompt("It's a tie!")

        prompt("Play again? (y or n)")
        answer = input().lower()[0]

        if answer != 'y':
            break

        prompt('Thanks for playing Tic Tac Toe!')

play_tic_tac_toe()