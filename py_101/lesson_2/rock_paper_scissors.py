import random

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
VALID_CHOICES_SHORT = ['r', 'p', 'sc', 'l', 'sp']

def prompt(message):
    print(f'==> {message}')

def get_match_result(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

    if ((player == "rock" and computer == "scissors") or
        (player == "paper" and computer == "rock") or
        (player == "scissors" and computer == "paper") or
        (player == "rock" and computer == "lizard") or
        (player == "lizard" and computer == "spock") or
        (player == "spock" and computer == "scissors") or
        (player == "scissors" and computer == "lizard") or
        (player == "lizard" and computer == "paper") or
        (player == "paper" and computer == "spock") or
        (player == "spock" and computer == "rock")):
        return(1)
    elif ((computer == "rock" and player == "scissors") or
          (computer == "paper" and player == "rock") or
          (computer == "scissors" and player == "paper") or
          (computer == "rock" and player == "lizard") or
          (computer == "lizard" and player == "spock") or
          (computer == "spock" and player == "scissors") or
          (computer == "scissors" and player == "lizard") or
          (computer == "lizard" and player == "paper") or
          (computer == "paper" and player == "spock") or
          (computer == "spock" and player == "rock")):
        return(2)
    else:
        return(0)

while True:
    
    player_win_count = 0
    computer_win_count = 0

    while True:
        prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
        choice = input()

        while choice not in VALID_CHOICES:
            if choice in VALID_CHOICES_SHORT:
                choice = VALID_CHOICES[VALID_CHOICES_SHORT.index(choice)]
                break
            else:
                prompt("That's not a valid choice")
                choice = input()

        computer_choice = random.choice(VALID_CHOICES)

        result = get_match_result(choice, computer_choice)

        if (result == 1):
            prompt("You win!")
            player_win_count += 1
        elif (result == 2):
            prompt("Computer wins!")
            computer_win_count += 1
        elif (result == 0):
            prompt("It's a tie!")

        if player_win_count >= 3:
            prompt("You have won 3 games first! You are the grand winner!")
            break
        elif computer_win_count >= 3:
            prompt("The computer has won 3 games first! The computer is the grand winner!")
            break
        else:
            prompt(f'You have won {player_win_count} games. The cmputer has won {computer_win_count} games.')

    
    prompt("Do you want to play again (y/n)?")
    answer = input().lower()

    while True:
        if answer.startswith('n') or answer.startswith('y'):
            break

        prompt('Please enter "y" or "n".' )
        answer = input().lower()

    if answer[0] == 'n':
        break
