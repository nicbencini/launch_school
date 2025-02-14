import re

string = """
A grey cat
A blue caterpillar
The lazy dog
The white cat
A loud dog
--A loud dog
Go away dog
The ugly rat
The lazy, loud dog
"""

print(re.findall(r'^(A|The) [a-z][a-z][a-z][a-z] (dog|cat)$', string, flags=re.MULTILINE))