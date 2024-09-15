
statement = "The Flintstones Rock"

output_dictionary = {}

for character in statement:
    if character not in output_dictionary:
        output_dictionary[character] = 0
    
    output_dictionary[character] += 1

print(output_dictionary)