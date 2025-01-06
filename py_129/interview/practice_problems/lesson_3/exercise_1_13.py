class Student:

    school_name = 'Oxford'

    def __init__(self, name):
        self._name = name
    
    @classmethod
    def get_school_name(cls):
        print(cls.school_name)

new_student = Student('chap')
print(new_student.__class__.school_name)
new_student.__class__.get_school_name()