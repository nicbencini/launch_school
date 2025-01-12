
string_list = ['toi',
               'shark',
               'test']

captilized_string = (text.capitalize() for text in string_list)

for string in captilized_string:
    print(string)