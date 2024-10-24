

my_list = [6, 3, 0, 11, 20, 4, 17]

count = 0

while(count < len(my_list)):
    
    number = my_list[count]

    if (number % 2 == 0):
        print(my_list[count])
    count += 1

print('\n')

for i in range(len(my_list)):

    number = my_list[i]
    if (number % 2 != 0):
        print(my_list[i])

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

print('\n')

for sub_list in my_list:
    for value in sub_list:
        if value % 2 == 0:
            print(value)

print('\n')

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

new_list = []

for value in my_list:
    if value % 2 == 0:
        new_list.append('even')
    else:
        new_list.append('odd')

print(new_list)

print('\n')


def find_integers(tuple):

    int_list = []

    for value in tuple:
        if (type(value) is int):
            int_list.append(value)

    return int_list




my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)
integers = find_integers(my_tuple)
print(integers)                    # [1, 3, -4]

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

result = { name: len(name)
           for name in my_set
           if len(name) % 2 != 0 }
print(result)
# {'Cheddar': 7, 'Pudding': 7, 'Cocoa': 5}


print('\n')

def factorial(value):

    count = 1
    for i in range(value):
        count *= i+1

    return count

print(factorial(1))   # 1
print(factorial(2))   # 2
print(factorial(3))   # 6
print(factorial(4))   # 24
print(factorial(5))   # 120
print(factorial(6))   # 720
print(factorial(7))   # 5040
print(factorial(8))   # 40320
print(factorial(25))  # 15511210043330985984000000

print('\n')

import random

highest = 10

while True:
    number = random.randrange(highest + 1)
    print(number)

    if number == highest:
        break


my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]




def internal_function(sub_list):

    even_number_sublist = []
    counter2 = 0

    while (counter2 < len(sub_list)):

        value = sub_list[counter2]

        if (value % 2 == 0):
            even_number_sublist.append(value)

        counter2 += 1
    
    return even_number_sublist



even_number_list = []

counter1 = 0

while (counter1 < len(my_list)):
        
    sub_list = my_list[counter1]

    even_number_list.extend(internal_function(sub_list))

    counter1 += 1



print(even_number_list)