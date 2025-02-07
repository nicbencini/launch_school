import random

class GuessingGame:

    GUESS_LIMIT = 7

    def __init__(self):
        self.number = 0


    def check_guess(self, guess):
        if guess == self.number:
            print(f'That\'s the number!\n\nYou have won!')
            return True

        elif guess < self.number:
            print(f'Your guess is too low!')
        
        else:
            print(f'Your guess is too high')

        return False

    def obtain_guess(self):
        while True:
            guess = input('Enter a number between 1 and 100: ')

            if guess.isnumeric() and int(guess) < 100 and int(guess) > 1:
                return int(guess)

            print('Invalid guess.')


    def play(self):

        guesses = self.GUESS_LIMIT
        self.number = random.randint(1,100)

        while True:

            if guesses == 0:
                print(f'You have no more guesses. You lost!. The number was {self.number}')
                break

            print(f'You have {guesses} guesses remaining')

            guess = self.obtain_guess()

            if self.check_guess(guess):
                break

            guesses -= 1


game = GuessingGame()
game.play()

