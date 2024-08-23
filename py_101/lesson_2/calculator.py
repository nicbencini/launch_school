# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for the operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.

import json
import os

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True

    return False

project_directory = os.path.dirname(os.path.abspath(__file__))
file_path = project_directory + '/message_data.json'

with open(file_path, 'r') as f:
    message_dictionary = json.load(f)

prompt('Select language:' + '\n' + '1) English' + '\n' + '2) Spanish')
language_select = input()

while language_select not in ['1', '2']:
    prompt('Value must be 1 or 2')
    language_select = input()

if language_select == '1':
    message_dictionary = message_dictionary['eng']
elif language_select == '2':
    message_dictionary = message_dictionary['spn']

prompt(message_dictionary['welcome'])

progression_flag = True

while progression_flag:


    prompt(message_dictionary['intro_1'])
    number1 = input()

    while invalid_number(number1):
        prompt(message_dictionary['error_1'])
        number1 = input()

    prompt(message_dictionary['intro_2'])
    number2 = input()

    while invalid_number(number2):
        prompt(message_dictionary['error_1'])
        number2 = input()

    prompt(message_dictionary['select'])

    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt(message_dictionary['error_2'])
        operation = input()

    match operation:
        case '1':
            output = float(number1) + float(number2)
        case '2':
            output = float(number1) - float(number2)
        case '3':
            output = float(number1) * float(number2)
        case '4':
            output = float(number1) * float(number2)



    prompt(message_dictionary['result'] + ' ' + str(output))

    prompt(message_dictionary['proceed'])
    continue_bool = input()

    while continue_bool not in ['y' , 'n']:
        prompt(message_dictionary['error_3'])
        continue_bool = input()

    if continue_bool == 'y':
        progression_flag = True
    elif continue_bool == 'n':
        progression_flag = False

        


