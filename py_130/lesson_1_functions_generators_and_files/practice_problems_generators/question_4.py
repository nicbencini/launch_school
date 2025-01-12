strings = ['four', 'score', 'and', 'seven', 'years', 'ago']

def captialize(string_list):
    for string in string_list:
        yield string.capitalize()

for string in captialize(strings):
    print(string)