
class Foo:
    def __init__(self, bar, qux):
        self._bar = bar
        self._qux = qux
    
    @property
    def bar(self):
        return self._bar
    
    @property
    def qux(self):
        self._qux = self.bar
        return self._qux
        

    @bar.setter
    def bar(self, new_value):
        self._bar = new_value
    


foo = Foo(1, 2)



print(foo.bar)      # 1
foo.bar = 2
print(foo.bar)      # 2
print(foo.qux)      # 2

try:
    foo.qux = 4
except AttributeError as e:
    print(f"Error: {e}")      # prints an error message