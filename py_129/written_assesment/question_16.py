
"""

Employee Management Application

Employee
    - Regular_Employee
    - Part_Time_Employee
    - Managers
        - Executives

Employee
    - has a name
    - has a serial number
    - has a full or part time
    - should print
            Name: Dave
            Type: Manager
            Serial number: 123456789
            Vacation days: 14
            Desk: private office
    

Part_Time_Employee:
    - no vacation
    - work in workspace with no reserved desk

Regular Employee
    - full time employee
    - has take_a_vacation method
    - desk in cubical farm

Executive(Type of manager)
    -Full time employee
    -Can higher and fire employess
    - 20 days of vacation
    - Work in a corner office
    - Can delegate work (delegate method)

Managers
    -Full time employee
    -14 days of vacation
    -work in a regular private office
    - Can delegate work (delegate method)
"""


class Employee:

    def __init__(self, name, serial_number, type, desk, vacation):
        self._name = name
        self._type = type
        self._serial_number = serial_number
        self._desk = desk
        self._vacation = vacation
    
    @property
    def name(self):
        return self._name

    @property
    def type(self):
        return self._type
    
    @property
    def serial_number(self):
        return self._serial_number
    
    @property
    def desk(self):
        return self._desk
    
    @property
    def vacation(self):
        return self._vacation
    
    def __str__(self):

        return f'Name: {self.name}\nType: {self.type}'

class FullTimeMixin:

    def take_a_vacation(self):
        pass

class ManagerMxin:

    def delegate(self):
        pass

class FullTimeEmployee(FullTimeMixin, Employee):
    def __init__(self, name, serial_number):
        super().__init__(name, serial_number, 'Fill Time Employee', 'cubical farm', 10)

class PartTimeEmployee(Employee):

    def __init__(self, name, serial_number):
        super().__init__(name, serial_number, 'Part Time Employee', 'reserved desk', 0)

class Executives(FullTimeMixin, ManagerMxin, Employee):
    def __init__(self, name, serial_number):
        super().__init__(name, serial_number, 'Executive', 'corner office', 20)
    
    def hire_or_fire(self):
        pass

class Managers(FullTimeMixin, ManagerMxin, Employee):
    def __init__(self, name, serial_number):
        super().__init__(name, serial_number, 'Part Time Employee', 'private office', 14)

emp1 = Executives('Jack', '9988')

print(emp1.type)
print(emp1)