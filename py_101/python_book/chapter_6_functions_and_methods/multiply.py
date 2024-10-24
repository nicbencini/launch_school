def multiply(number1 , number2):
    return number1*number2


def remainder_3(numbers):
    return [number % 3 for number in numbers]


numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []


print(any(remainder_3(numbers_1)))
print(any(remainder_3(numbers_2)))
print(any(remainder_3(numbers_3)))
print(any(remainder_3(numbers_4)))

def remainder5(numbers):
    return [number % 5 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_2 = [1, 2, 3, 4, 6, 7, 8, 9]
numbers_3 = [0, 5, 10]
numbers_4 = []

print(all(remainder5(numbers_2)))