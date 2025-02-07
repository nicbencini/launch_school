"""
You have a function that should check whether a key exists in a dictionary and returns its value. However, it's raising an error. Why is that? How would you fix this code?

"""


def get_key_value(my_dict, key):
    if key in my_dict:
        return my_dict[key]
    else:
        return None

print(get_key_value({"a": 1}, "b"))

# The error is occuring because the code on line 8 is used for returning the value from a dictionary using a key. If the key does not exist, the code will return a key error. 
