def clean_up(input_string):
    
    output = ''
    
    for char in input_string:
        if not str(char).isalpha():
            if not output.endswith(' '):
                output += ' '
        else:
            output += char
    
    return output

print(clean_up("---what's my +*& line?") == " what s my line ")
# True

string = "count_me"

for i,char in enumerate(string):
    print(i)
    print(char)