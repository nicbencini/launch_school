import re

string = """
0xDEADBEEF
1234.5678
Jamaica
plow ahead
"""

print(len(re.findall(r'[0-9A-Ja-j]', string)))