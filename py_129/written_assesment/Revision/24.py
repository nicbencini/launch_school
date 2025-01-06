
class Transform:

    def __init__(self, string):
        self._string = string
    
    def uppercase(self):
        return self._string.upper()
    
    @staticmethod
    def lowercase(input_string):
        return input_string.lower()


my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz