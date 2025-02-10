"""
Create a custom set type.

Sometimes it is necessary to define a custom data structure of some type. 
In some languages, including Python, there is a built-in Set type. For this problem, you're expected to implement your own custom set type. 
How it works internally doesn't matter, as long as it behaves like a set of unique elements that can be manipulated in several well defined ways. 
Once you've reached a solution, feel free to play around with using the built-in implementation of Set.

For simplicity, you may assume that all elements of a set must be numbers.

problem:
    -create a custom set type

rules:
    -

data structure:
    CustomSet(list of values):
        -is_empty -> checks if set is empty
        -contains -> checks if set contains a value
        -is_sub_set -> checks whether all items of subset are in set
        -is_disjoint -> ?
        -is_same -> checks if sets are the same set
        -add -> adds item to the set
        -intersection -> checks intersection between both sets
        -difference -> checks difference between two sets
        -union -> joins two sets


"""

class CustomSet:
    
    def __init__(self, input_list = []):
        
        self._internal_list = []

        for item in input_list:
            self.add(item)
    
    def is_empty(self):
        if len(self._internal_list) == 0:
            return True
        
        return False
    
    def contains(self, item):
        if item in self._internal_list:
            return True
        
        return False
    
    def is_subset(self, other_set):


        for item in self._internal_list:
            if item not in other_set._internal_list:
                return False
        
        return True
    
    def is_disjoint(self, other_set):

        for item in self._internal_list:
            if item in other_set._internal_list:
                return False
        
        return True
    
    def __eq__(self, other_set):

        if not isinstance(other_set, CustomSet):
            raise TypeError
        
        if sorted(self._internal_list) == sorted(other_set._internal_list):
            return True
        return False
    
    def is_same(self, other_set):

        if self == other_set:
            return True
        
        return False
    
    def add(self, new_item):
        if new_item not in self._internal_list:
                self._internal_list.append(new_item)
    
    def intersection(self, other_set):

        intersection_list = []

        for item in self._internal_list:
            if item in other_set._internal_list:
                intersection_list.append(item)
        
        return CustomSet(intersection_list)
    
    def difference(self, other_set):

        difference_list = []

        for item in self._internal_list:
            if item not in other_set._internal_list:
                difference_list.append(item)
        
        return CustomSet(difference_list)
    
    def union(self, other_set):

        unified_list = self._internal_list + other_set._internal_list

        return CustomSet(unified_list)


    

        
