import re

string = """
The red d0g chases the b1ack cat.
a_b c_d
"""

print(re.findall(r'[a-z][a-z][a-z]', string,flags=re.IGNORECASE))