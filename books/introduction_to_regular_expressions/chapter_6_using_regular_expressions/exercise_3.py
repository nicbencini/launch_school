import re

def mystery_math(input_string):

    return re.sub(r'[\+\-\*\/]', '?', input_string, count=1)


print(mystery_math('4 + 3 - 5 = 2'))
# '4 ? 3 - 5 = 2'

print(mystery_math('(4 * 3 + 2) / 7 - 1 = 1'))
# '(4 ? 3 + 2) / 7 - 1 = 1'