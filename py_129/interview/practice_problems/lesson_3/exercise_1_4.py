class Silly:
    def __init__(self, value):
        if isinstance(value, int):
            self.value = value
        else:
            self.value = str(value)

    def __str__(self):
        return f'Silly({repr(self.value)})'
    
    def __add__(self, other):

        value_1 = str(self.value)
        value_2 = str(other)

        if (value_1.isnumeric() and value_2.isnumeric()):
            value_1 = int(value_1)
            value_2 = int(value_2)
    
        return value_1 + value_2

print(Silly('abc') + 'def')        # Silly('abcdef')
print(Silly('abc') + 123)          # Silly('abc123')
print(Silly(123) + 'xyz')          # Silly('123xyz')
print(Silly('333') + 123)          # Silly(456)
print(Silly(123) + '222')          # Silly(345)
print(Silly(123) + 456)            # Silly(579)
print(Silly('123') + '456')        # Silly(579)