
def get_inverse(number_list):

    output_list = []

    for number in number_list:
        try:
            inverse = 1/number
        except ValueError:
            print('Incorrect Value input')
        except ZeroDivisionError:
            print('Attempted to divide by zero.')
        else:
            output_list.append(inverse)

    return output_list

list = [2,3,4,0,5,8,9,0]

print(get_inverse(list))
