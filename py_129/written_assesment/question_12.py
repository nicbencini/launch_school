class Student:
    def __init__(self, name, grade):
        self._name = name
        self._grade = grade

bob1 = Student('Bob', 12)
bob2 = Student('Bob', 12)
print(bob1 == bob2)             # False