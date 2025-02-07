import re

string = """
Hello 4567 bye CDEF - cdef
0x1234 0x5678 0xABCD
1F8A done
"""

print(re.findall(r'\s\h\h\h\h\s', string))