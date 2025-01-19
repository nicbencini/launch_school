
def reverse_string(input_string):

    for char in input_string[::-1]:
        yield char
    

print(list(reverse_string('something')))