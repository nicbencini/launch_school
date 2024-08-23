def short_long_short(string_1, string_2):
    if (len(string_1) < len(string_2)):
        return string_1 + string_2 + string_1
    else:
        return string_2 + string_1 + string_2
    
print(short_long_short('abc','defgh'))
print(short_long_short('abcxxx','defgh'))