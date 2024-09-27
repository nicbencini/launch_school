"""
Given a dictionary where both keys and values are unique, invert this dictionary so that its keys become values and its values become keys.
"""

"""
def invert_dict(input_dictionary):

    output_dictionary = {}

    for key,value in input_dictionary.items():
        output_dictionary[value] = key
    
    return output_dictionary

"""

def invert_dict(input_dictionary):
    return {value:key for key,value in input_dictionary.items()}


print(invert_dict({
          'apple': 'fruit',
          'broccoli': 'vegetable',
          'salmon': 'fish',
      }) == {
          'fruit': 'apple',
          'vegetable': 'broccoli',
          'fish': 'salmon',
      })  # True
