
def reduce(callback, iterable, starting_value):

    accumulator = starting_value
    
    for element in iterable:
        accumulator = callback(element, accumulator)

    return accumulator

numbers = [10, 3, 5]
product = lambda number, accum: accum * number
print(reduce(product, numbers, 2))     # 300

numbers = (1, 2, 4, 8, 16)
total = lambda number, accum: accum + number
print(reduce(total, numbers, 0))        # 31

numbers = [10, 3, 5]
product = lambda number, accum: accum * number
print(reduce(product, numbers, 2))      # 300

colors = ['red', 'orange', 'yellow', 'green',
          'blue', 'indigo', 'violet']
rainbow = lambda color, accum: accum + color[0].upper()
print(reduce(rainbow, colors, ''))      # ROYGBIV

number_list = [1,2,3,4,5]
sum_of_square = lambda number, accum: accum + number**2
print(reduce(sum_of_square, number_list, 0))
print(sum([num**2 for num in number_list]))

