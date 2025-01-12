
strings = ['four', 'score', 'and', 'seven', 'years', 'ago']

def capitalize(string_list):
    for string in string_list:
        if len(string) < 5:
            yield string.capitalize()

print(list(capitalize(strings)))