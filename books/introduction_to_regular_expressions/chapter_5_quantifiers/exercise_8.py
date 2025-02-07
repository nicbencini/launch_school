import re

string = """
What's up, doc?
I tawt I taw a putty tat!
Thufferin' thuccotath!
Oh my darling, Clementine!
Camptown ladies sing this song, doo dah.
"""

print(re.findall(r'\S+$', string,flags=re.MULTILINE | re.IGNORECASE))