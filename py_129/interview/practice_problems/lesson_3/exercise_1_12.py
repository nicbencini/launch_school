numbers = [1, 2, 3, 4, 5]

def LBYL(input_list, index):

    if index > (len(input_list) - 1):
        return None
    
    return input_list[index]

def AFNP(input_list, index):

    try:
        return input_list[index]
    except IndexError:
        return None
    

print(LBYL(numbers, 2))
print(AFNP(numbers, 2))