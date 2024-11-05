import random

class GuessingGame:

    def __init__(self):
        self.guesses = 0
        self.number = 0

    def play(self):

        self.guesses = 7
        self.number = random.randint(1,100)

        while True:

            if self.guesses == 0:
                print('You have no more guesses. You lost!')
                break

            print(f'You have {self.guesses} guesses remaining')

            while True:
                guess = input('Enter a number between 1 and 100: ')

                if guess.isnumeric() and int(guess) < 100 and int(guess) > 1:
                    guess = int(guess)
                    break
                print('Invalid guess.')

            if guess == self.number:
                print(f'That\'s the number!\n\nYou have won!')
                break

            elif guess < self.number:
                print(f'Your guess is too low!')
            
            elif guess > self.number:
                print(f'Your guess is too high')
            
            else:
                pass

            self.guesses -= 1


game = GuessingGame()
game.play()

