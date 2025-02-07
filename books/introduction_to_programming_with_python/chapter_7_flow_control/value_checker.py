def value_checker(value):
    value = int(value)

    if (value > 0) and (value <= 50):
        print(f'{value} is between 0 and 50')

    elif (value > 50) and (value <= 100):
        print(f'{value} is between 50 and 100')

    elif (value > 100):
        print(f'{value} is geater than 100')

    else:
        print (f'{value} is less than 0')


value_checker(input())