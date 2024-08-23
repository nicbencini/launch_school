def xor(value_1, value_2):
    if(value_1 and not value_2) or (value_2 and not value_1) :
        return True
    else:
        return False
    
print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)