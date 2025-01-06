class Person:
    count = 0

    def __init__(self):
        Person.count += 1

    @classmethod
    def total_people(cls):
        return cls.count

bob = Person()
alice = Person()
print(Person.total_people())     # this should print 2