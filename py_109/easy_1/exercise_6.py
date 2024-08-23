number = int(input('Please enter an integer greater than 0: '))
action = input('Enter "s" to compute the sum, or "p" to compute the product. ')


if action == 's':
    print(f'The sum of the integers between 1 and {str(number)} is {sum(range(1,number + 1))}')
elif action == 'p':

    product_result = 1
    for value in range(1,number):
        product_result *= value

    print(f'The product of the integers between 1 and {str(number)} is {product_result}')
else:
    print('Input not valid.')