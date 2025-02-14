import re

string = """
Mississippi
ziti 0minimize7
inviting illegal iridium
"""

print(re.findall(r'\b([a-hj-z]*i){3,}[a-hj-z]*\b', string, flags=re.IGNORECASE|re.MULTILINE))