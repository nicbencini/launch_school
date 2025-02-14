import re

string = """
The regex /[^a-z]/i matches any character that is
not a letter. Similarly, /[^0-9]/ matches any
non-digit while /[^A-Z]/ matches any character
that is not an uppercase letter. Beware: /[^+-<]/
is at best obscure, and may even be wrong.
"""

print(re.findall(r'\[\^[0-9a-z]\-[0-9a-z]\]', string, flags=re.IGNORECASE))