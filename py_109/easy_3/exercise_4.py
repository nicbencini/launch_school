def stringy(input_int):
    return ''.join([str((i+1)%2) for i in range(input_int)])

print(stringy(6))
print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True