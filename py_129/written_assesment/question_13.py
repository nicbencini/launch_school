
class Student:
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade
    
    def __eq__(self, other):
        if isinstance(other, Student):
            return self._name == other._name and self._grade == other._grade
        
        return NotImplemented

bob1 = Student('Bob', 12)
bob2 = Student('Bob', 12)


print(bob1 == bob2)             # False