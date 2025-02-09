"""
Write a simple linked list implementation. The linked list is a fundamental data structure in computer science, often used in the implementation of other data structures.

The simplest kind of linked list is a singly linked list. Each element in the list contains data and a "next" field pointing to the next element in the list of elements. 
This variant of linked lists is often used to represent sequences or push-down stacks (also called a LIFO stack; Last In, First Out).

Let's create a singly linked list whose elements may contain a range of data such as the numbers 1-10. Provide methods to reverse the linked list and convert a 
linked list to and from a list.

problem:
to create a singly linked list where each element in the list contains data and a next field pointing to the next element in the list

rules:
    -elements can accept numbers from 1-10

data structures:
    -Element(class):
        -datum (property) -> data in element
        -next_element (optional property) -> next item in list
    
    - SimpleLinkedList(class):
        -size (property) -> gets size of list
        -push (method) inputs:value -> pushes an item to the list
        -is_empty (method) -> checks that list is empty
        -peek (method) -> ?? returns first item in list
        -head (property) -> returns the leading item as an Element
        -is_tail(method) -> checks whether item is the last item
        -pop(method) -> removes item from list
        -from_list (method) -> creates a linked list from a list
        -to_list (method) -> converts linked list to a list
        -reverse(method) -> reverses the order of the linked list

"""

class Element:

    def __init__(self, datum, next=None):
        self._datum = datum
        self._next = next
    
    @property
    def datum(self):
        return self._datum
    
    @property
    def next(self):
        return self._next
    
    def is_tail(self):

        if self._next is None:
            return True
        
        return False

class SimpleLinkedList:
    
    def __init__(self):
        self._current_element = None
    
    @property
    def size(self):

        count = 0

        element = self._current_element

        while True:
            if element == None:
                break

            count += 1
            
            if element.next == None:
                break
            
            element = element.next
            
        
        return count
        
    
    @property
    def head(self):

        if self.is_empty():
            return None
        
        return self._current_element

    def is_empty(self):
        
        if self.size == 0:
            return True
        
        return False
    
    def push(self, element):

        if self.is_empty():
            new_element = Element(element)
        else:
            new_element = Element(element, self._current_element)

        self._current_element = new_element
    
    def peek(self):

        if self.is_empty():
            return None
        
        return self._current_element.datum
    
    def pop(self):

        old = self._current_element

        self._current_element = old.next

        return old.datum
    
    def to_list(self):
        output = []

        element = self._current_element

        while True:
            if element == None:
                break

            output.append(element.datum)
            
            if element.next == None:
                break
            
            element = element.next
        
        return output
        
    
    def reverse(self):

        elements = self.to_list()[::-1]
        return self.from_list(elements)
        
    
    @classmethod
    def from_list(cls, input_list):

        if input_list == None:
            input_list = []

        lst = SimpleLinkedList()
        for item in input_list[::-1]:
            lst.push(item)
        
        return lst

    
    