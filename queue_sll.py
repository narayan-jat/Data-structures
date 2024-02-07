'''
This module is specifically designed to contain Queue data structure
and supports all operations which are supported by a Queue.This data 
structure has been implemented based on the singly linked list concept.

Author: Narayan Jat
Date: 7 September, 2023
'''
from singly_linked_list import *
from Error import Empty     # Importing error class.
class SingliLinkedQueue(SinglyList):
    '''This is Queue based on the circular linked list data structure.'''

    def __init__(self):
        '''This initializes the SingliLinkedQueue.'''
        self._tail = None
        self._size = 0

    def is_empty(self):
        '''Returns True if the Queue is empty otherwise False.'''
        return self._size == 0
    
    def __len__(self):
        '''Returns the length of the SingliLinkedQueue.'''
        return self._size
    
    def dequeue(self):
        '''Returns and remove the first element of the Queue.'''
        if self.is_empty():
            raise Empty('Queue is empty.')
        deleted_element = self._tail._next._element      # deleting element next to tail which is head
        self._tail._next = self._tail._next._next     # assigning element just after head to tail.
        self._size -= 1
        return deleted_element
    
    def enqueue(self, element):
        '''This method add element at the end of the queue.'''
        new_node = self._Node(element, None)        # creating node with None reference value.
        if self.is_empty():     
            new_node._next = new_node       # adding new node itself as node if it's first node.
        else:
            new_node._next = self._tail._next
            self._tail._next = new_node
        self._tail = new_node
        self._size += 1

    def first(self):
        '''Returns the first element of the queue.'''
        if self.is_empty():
            raise Empty('Queue is empty.')
        return self._tail._next._element
    

#----------------Testing-------------------
if __name__ == '__main__':
    queue = SingliLinkedQueue()
    print(len(queue))       # length testing
    for i in range(5):
        queue.enqueue(i)       # checking enqueue operation
    print(len(queue))
    print(queue.first())
    for i in range(4):
        print(queue.dequeue())      # testing dequeue
    print(queue.first())
    print(queue.is_empty())     # testing is_empty.