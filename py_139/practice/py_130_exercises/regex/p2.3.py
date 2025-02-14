import re
string = """
0xDEADBEEF
1234.5678
Jamaica
plow ahead
"""

print(re.findall(r'[0-9A-J]', string, flags=re.IGNORECASE))