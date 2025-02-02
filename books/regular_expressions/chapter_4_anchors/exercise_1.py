import re

string = """
The lazy cat sleeps.
The number 623 is not a word.
Then, we went to the movies.
Ah. The bus has arrived.
"""

print(len(re.findall(r'^The\b', string,flags=re.MULTILINE)))