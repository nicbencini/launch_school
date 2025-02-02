import re

string  = """
123,456,789,123,345
123,456,,789,123
23,56,7
13,45,78,23,45,34
13,45,78,23,45,34,56
"""

print(re.findall(r'^(\d+,){2}|\d+$(\d+,){5,}\d+$', string, flags= re.MULTILINE|re.IGNORECASE))