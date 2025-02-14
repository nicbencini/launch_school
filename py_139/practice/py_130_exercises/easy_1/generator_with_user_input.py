"""
Create a generator function that yields user input strings until the word "stop" is entered.
"""

def user_input_generator():

    while True:
        user_input = input('Please input a word:')

        if user_input.lower() == 'stop':
            break
        yield user_input

print(list(user_input_generator()))