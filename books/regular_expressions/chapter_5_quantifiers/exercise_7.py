import re

string = """
Mississippi
ziti 0minimize7
inviting illegal iridium
"""

print(re.findall(r'\b[a-z]*i[a-z]*i[a-z]*i[a-z]*\b', string,flags=re.MULTILINE | re.IGNORECASE))