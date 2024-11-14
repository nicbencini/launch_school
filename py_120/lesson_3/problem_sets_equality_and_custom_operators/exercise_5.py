


class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f'Silly({repr(self.value)})'
    
    def __add__(self, other):

        if isinstance(self.value, int) and isinstance(other, int):
            return self.value + other
        
        elif isinstance(self.value, int) and other.isdigit():
            return self.value + int(other)
        
        elif isinstance(other, int) and self.value.isdigit():
            return other + int(self.value)
        
        elif isinstance(self.value,str) and self.value.isdigit() and other.isdigit():
            return int(self.value) + int(other)
        
        return str(self.value) + str(other)


print(Silly('abc') + 'def')        # Silly('abcdef')
print(Silly('abc') + 123)          # Silly('abc123')
print(Silly(123) + 'xyz')          # Silly('123xyz')
print(Silly('333') + 123)          # Silly(456)
print(Silly(123) + '222')          # Silly(345)
print(Silly(123) + 456)            # Silly(579)
print(Silly('123') + '456')        # Silly(579)