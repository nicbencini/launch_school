"""
Write a class such that the following code prints the results indicated by the comments:
"""

class Transform:

    def __init__(self, data):
        self.data = data

    def uppercase(self):
        return self.data.upper()
    
    @staticmethod
    def lowercase(input_data):
        return input_data.lower()
        



my_data = Transform('abc')
print(my_data.uppercase())              # ABC
print(Transform.lowercase('XYZ'))       # xyz