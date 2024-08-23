def multiply(first_number, second_number):
    return first_number * second_number

def square(number):
    return multiply(number,number)

print(multiply(5, 3) == 15)  # True
print(square(5) == 25)   # True
print(square(-8) == 64)  # True