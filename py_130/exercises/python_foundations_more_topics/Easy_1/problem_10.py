"""
Create a generator function that yields user input strings until the word "stop" is entered.
"""

def write_string():

    print('started')

    while True:
        input_string = input('Enter string...')
        if input_string == 'stop':
            break
        yield('==>' + input_string)


for user_input in write_string():
    print(user_input)

