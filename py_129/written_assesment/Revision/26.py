
import random

class GuessingGame():

    NUMBER_OF_GUESSES = 7

    def __init__(self):
        self._guesses = None
        self._hidden_number = None

    def _get_number(self):
        while True:
            number = int(input('Enter a number between 1 and 100: '))

            if number <= 100 and number >= 1:
                return number
            
            print('Invalid guess.')


    def play(self):

        self._guesses = self.NUMBER_OF_GUESSES
        self._hidden_number = random.randint(1,100)

        while True:

            if self._guesses == 0:
                print('You have no more guesses. You lost!')
                break
            else:
                print(f'You have {self._guesses} remaining')

            number = self._get_number()

            if number < self._hidden_number:
                print('Your guess is too low.')
            
            elif number > self._hidden_number:
                print('Your guess is too high.')
            
            else:
                print('Thats the number.\n\nYou Won!')
                break

            self._guesses -= 1
        

game = GuessingGame()
game.play()
            
                


