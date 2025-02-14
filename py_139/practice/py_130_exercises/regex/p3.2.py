import re

string = """
Hello 4567 bye CDEF - cdef
0x1234 0x5678 0xABCD
1F8A done
"""

print(re.findall(r'\s[0-9A-F][0-9A-F][0-9A-F][0-9A-F]\s', string, flags=re.IGNORECASE))