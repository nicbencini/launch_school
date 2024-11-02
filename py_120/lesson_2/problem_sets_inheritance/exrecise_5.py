"""

What is the method resolution order and why is it important?
"""

"""
The method resolution order (MRO) is the order in which classes superclasses are searched for methods. Python will move through the heirachy of supeclasses until the method is found. 
If the method is not found, an error will be returned. 

The MRO for the bulldog class is:

Bulldog, Dog, Pet, Object.
"""