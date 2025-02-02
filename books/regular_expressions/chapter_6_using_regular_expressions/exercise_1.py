import re

def is_url(input_string):
    return re.match(r'^https?://\S+$', input_string) is not None




print(is_url('https://launchschool.com'))   # -> true
print(is_url('http://example.com'))          # -> true
print(is_url('https://example.com hello'))   # -> false
print(is_url('   https://example.com'))      # -> false