number_1 = input('Please input number 1: ')
number_2 = input('Please input number 2: ')

try:
    answer = float(number_1)/float(number_2)
except (ValueError, ZeroDivisionError) as e:
    print(e)
else:
    print(answer)
finally:
    print('End')