import re

string = """
,123,456,789,123,345,
,123,456,,789,123,
,23,56,7,
,13,45,78,23,45,34,
,13,45,78,23,45,34,56,
"""

print(len(re.findall(r',([0-9]+,){3,6}$',string,flags=re.IGNORECASE|re.MULTILINE)))