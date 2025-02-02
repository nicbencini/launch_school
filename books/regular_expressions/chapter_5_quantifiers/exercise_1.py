import re

string = """
To be or not to be
Be a busy bee
I brake for animals.
"""

print(re.findall(r'\bb[a-z]*e\b', string))