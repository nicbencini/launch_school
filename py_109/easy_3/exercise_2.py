def crunch(input_sting):
    
    output_string = ''

    if len(input_sting) == 0:
        return output_string
    else:
        output_string = input_sting[0]
        for char in input_sting:
            if char != output_string[-1]:
                output_string += char
    
    return output_string


# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')