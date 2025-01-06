
list = [1,2,3,4,10,21,23,45]

def key_sort(value):

    value_string = str(value)

    if value_string[0] == '2':

        return 0
    else:
        return 1

def soret_it(input_list):

    return sorted(input_list, key=key_sort)

print(soret_it(list))