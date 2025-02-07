# Question 1

numbers = [1, 2, 3, 4, 5]

numbers_reversed_1 = list(reversed(numbers))
numbers_reversed_2 = numbers[::-1]

print(numbers_reversed_1)
print(numbers_reversed_2)
print(numbers)

# Question 2

numbers = [1, 2, 3, 4, 5, 15, 16, 17, 95, 96, 99]

number1 = 8  # False (not in numbers)
number2 = 95 # True (in numbers)

print(number1 in numbers)
print(number2 in numbers)

# Question 3

print(42 >= 10 and 42 <= 100)
print(100 >= 10 and 100 <= 100)
print(101 >= 10 and 101 <= 100)

# Question 4

List = [1, 2, 3, 4, 5]
List.pop(2)
print(List)

# Question 5

numbers = [1, 2, 3, 4]
table = {'field1': 1, 'field2': 2, 'field3': 3, 'field4': 4}

print( type(numbers) is list)
print( type(table) is list)

# Question 6

title = "Flintstone Family Members"
centred_title = title.center(40)
print (centred_title)

# Question 7

statement1 = "The Flintstones Rock!"
statement2 = "Easy come, easy go."

print(statement1.count('t'))
print(statement2.count('t'))

# Question 8

ages = {'Herman': 32, 'Lily': 30, 'Grandpa': 402, 'Eddie': 10}

print ('Spot' in ages.keys())

# Question 9

additional_ages = {'Marilyn': 22, 'Spot': 237}

ages.update(additional_ages)