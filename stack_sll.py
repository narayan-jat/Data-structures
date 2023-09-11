'''
This module is specially designed to contain stack data structure
and supports all operations which are supported by a stack.  
This data structure has been implemented based on the singly
linked list concept.

Author: Narayan Jat
Date: 7 September, 2023
'''

from Error import Empty     # Importing error class.

class LinkedStack(object):
    '''This is a stack based on the singly linked list data structure.'''

    def __init__(self):
        '''This initializes the LinkedStack class'''
        self._head = None
        self._size = 0

    # -------------------Node Class -------------------------
    class _Node(object):
        '''This is lightweight non-public node class.'''
        __slots__ = '_element', "_next"         # strealine memory usage.
        
        def __init__(self, element, next):
            '''This initializes the node class'''
            self._element = element
            self._next = next

    # ------------------Node class ended------------

    def is_empty(self):
        '''Returns True if stack is empty otherwise False.'''
        return self._size == 0
    
    def __len__(self):
        '''This is the length of the stack.'''
        return self._size
    
    def top(self):
        '''Returns the top element of the stack.'''
        if self.is_empty():
            raise Empty('Stack is empty.')
        return self._head._element
    
    def push(self, element):
        '''This add the element to the stack at the end.'''
        new_node = self._Node(element, self._head)      # creating new node
        self._head = new_node       # assigning new node as a head.
        self._size += 1

    def pop(self):
        '''Returns and remove the element from the stack at the end of stack.'''
        if self.is_empty():
            raise Empty('Stack is empty.')
        popped_element = self._head._element
        self._head = self._head._next
        self._size -= 1
        return popped_element
    
    
#-------Testing----------------
if __name__ == '__main__':
    stack = LinkedStack()
    print(len(stack))       # length testing
    for i in range(5):
        stack.push(i)       # checking push operation
    print(len(stack))
    for i in range(4):
        print(stack.pop())
    print(stack.top())
    print(stack.is_empty())