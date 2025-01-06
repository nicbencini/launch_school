
number_1 = int(input('Please enter a number.'))
number_2 = int(input('Please enter a second number.'))

try:
    answer = number_1/number_2
    
except (ValueError ,ZeroDivisionError) as e:
    print(e.__class__.__name__)
else:
    print(answer)
finally:
    print('End')

