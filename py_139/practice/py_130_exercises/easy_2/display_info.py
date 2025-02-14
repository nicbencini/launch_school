

def display_info(data ,/ , *, reverse=False, uppercase=False):
    output = data
    
    if reverse:
        output = output[::-1]
    
    if uppercase:
        output = output.upper()
    
    return output



print(display_info("Launch", reverse=True)) # hcnuaL
print(display_info("School", uppercase=True)) # SCHOOL
print(display_info("cat", uppercase=True, reverse=True)) # TAC