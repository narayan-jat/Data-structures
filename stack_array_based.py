'''
This module is specifically designed to contain stack data structure
static and dynamic stack and supports all operations which are supported 
by a stack. This data structure has been implemented based on the array.

Author: Narayan Jat
Date: 7 September, 2023
'''

from Error import Empty     # Importing error class.

# Dynamic stack
class Dynamic_Stack(object):
    '''
    This is a Dynamic stack which grows as data grows and supports many stack operations.
    '''
    # Attribute _data: This the list to store data.
    def __init__(self):
        '''Initializes the stack.'''
        self._data = []

    def __len__(self):
        '''This is the length of the stack.'''
        return len(self._data)
    
    def is_empty(self):
        '''Checks whether a stack is empty or not'''
        return len(self._data) == 0

    def push(self, element):
        '''This method insert the element at the end of the stack'''
        self._data.append(element)

    def top(self):
        '''This is the last element of the stack.'''
        if self.is_empty():
            raise Empty("Stack is empty nothing is there.")
        return self._data[-1]
    
    def pop(self):
        ''' This method removes the last element from the stack.'''
        if self.is_empty():
            raise Empty("Stack is empty nothing is to pop there.")
        return self._data.pop()
    

# Static Stack
class Static_Stack(object):
    '''This is class to create dynamic stack.'''
    
    # Attribute _size: this is the size of the stack 
    # Invariant: It must be a integer value.

    # Attibute _length: This is the length of the stack.
    # Invariant: it is a integer value no more less than zero and not greater than size

    # Attibute _data: This is the data to store stack values.
    # Invariant: This is a list.

    def __init__(self, size = 200):
        '''
        This is a constructor to initialize the Static Stack.

        size: it must be a integer value.
        '''
        assert type(size) == int, str(size) + 'is not a integer.'
        self._size = size
        self._length = 0
        self._data = [None] * size      # by default having entry as None for a fix size list.

    def __len__(self):
        '''This is method returns the length of the stack.'''
        return self._length
    
    def is_empty(self):
        '''Returns True if the stack has no entries otherwise False.'''
        return len(self) == 0
    
    def push(self, element):
        '''This method add the the element at last of the stack.'''
        if self._length == self._size:
            raise Empty('The stack is fulled can not add more element.')
        self._data[self._length] = element       # adding element at current length
        self._length += 1       #incrementing length pointer to track length.

    def top(self):
        '''Returns the last element of the stack.'''
        if self.is_empty():
            raise Empty('No elements are there in stack to show.')
        return self._data[self._length - 1]
    
    def pop(self):
        '''Return and remove the last element of the stack.'''
        if self.is_empty():
            raise Empty('stack is empty nothing to pop.')
        popped_element = self._data[self._length - 1]       # accessing element to pop
        self._length -= 1  # since element from the stack is not removed so decrementing lenth pointer.
        return popped_element

# Main testing code 
if __name__ == "__main__":
    # testing dynamic stack
    dynamic_stack = Dynamic_Stack()
    print(dynamic_stack.pop())       # cheking error on popping for empty stack.
    print(dynamic_stack.is_empty())     # testing empty at starting
    dynamic_stack.push(890)     # testing push method
    print(len(dynamic_stack))      # checking length of the stack.
    print(dynamic_stack.top())      # checking the last element of the stack.
    dynamic_stack.push(2764)
    print(dynamic_stack.pop())    # poping the element from the stack.


    # testing the static stack with default length.
    static_stack = Static_Stack()
    print(static_stack.pop())       # cheking error on popping for empty stack.
    print(len(static_stack))        # checking length before adding any element.
    print(static_stack.is_empty())       # checking is_empty function.
    static_stack.push(2984)     # checking push method.
    static_stack.push(3342)
    print(static_stack.top()) # checking the top method.
    static_stack.push(546597)
    print(static_stack.pop())   # checking the pop method.
    print(len(static_stack))

    # checking error when stack is full.
    for i in range(200):
        static_stack.push(i)

    # checking for static stack for size given by user.
    static_stack = Static_Stack(123.056)    # checking size must be integer.
    static_stack = Static_Stack(150)
    print(static_stack.pop())       # cheking error on popping for empty stack.
    print(len(static_stack))        # checking length before adding any element.
    print(static_stack.is_empty())       # checking is_empty function.
    static_stack.push(2984)     # checking push method.
    static_stack.push(3342)
    print(static_stack.top()) # checking the top method.
    static_stack.push(546597)
    print(static_stack.pop())   # checking the pop method.
    print(len(static_stack))

    # checking error when stack is full.
    for i in range(200):
        static_stack.push(i)