


number = float(input('Please input a number: '))

if number < 0:
    raise ValueError('Negative numbers are not allowed!')

print(f'You entered {number}')