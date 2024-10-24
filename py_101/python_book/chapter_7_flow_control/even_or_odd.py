

def even_or_odd(number):
    remainder = int(number) % 2

    if remainder:
        print('odd')
    else:
        print('even')


even_or_odd(input('Enter number '))