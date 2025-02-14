import re

string = """
The lazy cat sleeps
The number 623 is not a cat
The Alaskan drives a snowcat
"""

print(re.findall(r'\bcat$', string, flags=re.MULTILINE))