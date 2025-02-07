import math
import random

# "high" is the highest number in the range
# "low" is the lowest number in the range

class GuessingGame:


    def __init__(self, low, high):
        self.number = 0
        self.low = low
        self.high = high
        self.guess_limit = int(math.log2(high - low + 1)) + 1


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
            guess = input(f'Enter a number between {self.low} and {self.high}: ')

            if guess.isnumeric() and int(guess) <= self.high and int(guess) >= self.low:
                return int(guess)

            print('Invalid guess.')


    def play(self):

        guesses = self.guess_limit
        self.number = random.randint(self.low,self.high)

        while True:

            if guesses == 0:
                print(f'You have no more guesses. You lost!. The number was {self.number}')
                break

            print(f'You have {guesses} guesses remaining')

            guess = self.obtain_guess()

            if self.check_guess(guess):
                break

            guesses -= 1



game = GuessingGame(501, 1500)
game.play()

