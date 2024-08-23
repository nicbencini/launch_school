import json
import os


project_directory = os.path.dirname(os.path.abspath(__file__))
file_path = project_directory + '/message_data.json'


message_egn_dictionary = {'welcome': 'Welcome to calculator',
                      'intro_1': 'What\'s the first number?',
                      'error_1': 'Hmm... that doesnt look like a valid number.',
                      'select': 'What operation would you like to perform?' + '\n' + '1) Add 2) Subtract 3) Multiply 4) Divide',
                      'error_2': 'You must choose 1, 2, 3, 4',
                      'proceed': 'Would you like to perform another calculation? (y/n)',
                      'error_3': 'Input not valid. Please re-enter.',
                      'intro_2': 'What\'s the second number?',
                      'result' : 'The result is:'
                      }


message_spn_dictionary = {'welcome': 'Bienvenido a la calculadora',
                      'intro_1': '¿cual es el primer numero?',
                      'error_1': 'Hmm... eso no parece un número válido.',
                      'select': '¿Qué operación le gustaría realizar?' + '\n' + '1) Sumar 2) Restar 3) Multiplicar 4) Dividir',
                      'error_2': 'Debes elegir 1, 2, 3, 4',
                      'proceed': '¿Le gustaría realizar otro cálculo? (y/n)',
                      'error_3': 'Entrada no válida. Por favor vuelva a ingresar.',
                      'intro_2': '¿Cuál es el segundo número?',
                      'result' : 'El resultado es:'
                      }


message_dictionary = {'eng': message_egn_dictionary,
                      'spn': message_spn_dictionary
                      }


with open(file_path, 'w') as f:
    json.dump(message_dictionary, f)

print('File built successfully')