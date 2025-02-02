import re

string = """
Doc in a big red box.
Hup! 2 3 4
"""

print(re.findall(r'\s...\s', string))