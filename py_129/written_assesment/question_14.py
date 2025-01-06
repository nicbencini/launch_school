class Counter:

    def __init__(self):
        self._value = 0

    def __add__(self, other):

        if isinstance(other, Counter):
            new_counter = Counter()
            new_counter.increment(self._value + other._value)
            return new_counter
        
        return NotImplemented
    
    def __str__(self):
        return str(self._value)

    def increment(self, value):
        self._value += value

    def decrement(self, value):
        self._value -= value


c1 = Counter()
c2 = Counter()
c1.increment(3)
c2.increment(5)
c1.decrement(1)

result = c1 + c2
print(result)                 # 7

try:
    c1.value += 1
except AttributeError as e:
    print(f"Error: {e}")      # Prints error message

try:
    c1 = c1 + 1
except TypeError as e:
    print(f"Error: {e}")      # Prints error message