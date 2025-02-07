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

query = r'(A|The) [a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z] (cat|dog)'

print(re.findall(query, string, re.MULTILINE))