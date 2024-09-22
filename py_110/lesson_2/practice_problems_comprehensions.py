# Problem 1

munsters = {
    'Herman':  {'age': 32,  'gender': 'male'},
    'Lily':    {'age': 30,  'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie':   {'age': 10,  'gender': 'male'},
    'Marilyn': {'age': 23,  'gender': 'female'},
}

age_count = 0

for item in munsters.items():
    if item[1]['gender'] == 'male':
        age_count += (item[1]['age'])



age_count_2 = sum([item[1]['age'] for item in munsters.items() 
                                  if item[1]['gender'] == 'male']
                                  )

print(age_count)
print(age_count_2)

# Problem 2

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

print([sorted(sub_lst) for sub_lst in lst])

# Problem 3

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]


print([sorted(sub_lst, key=str) for sub_lst in lst])

# Problem 4

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

print({sub_lst[0]:sub_lst[1] for sub_lst in lst})

# Problem 5

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def return_sum_of_odds(input_lst):
    return sum([number for number in input_lst if number % 2 != 0])

print(sorted(lst, key=return_sum_of_odds))

# Problem 6

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

print([{item[0]:item[1] + 1 for item in dictionary.items()} for dictionary in lst])

# Problem 7

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

print(
    [number for sublist in lst 
            for number in sublist 
            if number % 3 == 0]
)

def get_multiples_of_3(input_list):
    return [number for number in input_list if number % 3 == 0]

print([get_multiples_of_3(sublist) for sublist in lst])

new_list = [[num for num in sublist if num % 3 == 0] for sublist in lst]
print(new_list)

# Problem 8

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

print( [dictionary['colors'] for dictionary in dict1.values()])

# Problem 9

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

def check_if_even(in_lst):
    return all([number % 2 == 0 for number in in_lst])

def check_dictionary(input_dictionary):
    return all([check_if_even(item[1]) for item in input_dictionary.items()])

print([disctionary for disctionary in lst if check_dictionary(disctionary)])

# Problem 10

print(ord('a')) # 97
print(ord('f')) # 122

import random

def random_number():
    return str(random.randint(0,9))

def random_letter():
    return chr(random.randint(97,102))

def random_generator(length):
    
    block = ''

    for generation in range(length):
        option = random.randint(0,1)

        if option:
            block += random_letter()
        else:
            block += random_number()
    
    return block

def random_hex():
    option = random.randint(0,1)

    if option:
        return random_letter()
    else:
        return random_number()

print(random_generator(8)
      + '-'
      + random_generator(4)
      + '-'
      + random_generator(4)
      + '-'
      + random_generator(4)
      + '-'
      + random_generator(12)
      )

print(''.join([random_hex() if i not in [8,13,17,21] else '-' for i in range (36)]))

# Problem 11

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# Your code goes here

for value in dict1.values():
    for word in value:
        for character in word:
            if character in 'AEIOUaeiou':
                print(character)


print([character for value1 in dict1.values()
                 for word in value1
                 for character in word
                 if character in 'AEIOUaeiou'])

print('new')
print([print(character) for character in 'wewerdfsd' if character in 'aeiou'])

# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
