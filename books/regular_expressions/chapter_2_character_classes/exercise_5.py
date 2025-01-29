import re

string = """
0x1234abcd
1,000,000,000s and 1,000,000,000s.
THE quick BROWN fox JUMPS over THE lazy DOG!
"""

print(len(re.findall(r'[^a-z \n\r]', string, flags=re.I)))