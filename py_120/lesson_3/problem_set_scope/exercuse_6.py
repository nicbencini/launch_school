class Student:

    school_name = 'Oxford'

    def __init__(self, name):
        self.name = name


student_1 = Student('Jack')
student_2 = Student('Jill')
print(f'{student_1.name} goes to {student_1.__class__.school_name}')
print(f'{student_2.name} goes to {student_2.__class__.school_name}')