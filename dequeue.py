'''
This module is specially designed to contain delete_first data structure
and supports all operations which are supported by a Queue. This data 
structure has been implemented based on the array.

Author: Narayan Jat
Date: 9 September, 2023
'''

# importing error module.
from Error import Empty
import ctypes
class Queue(object):
    '''
    This is a Queue.
    '''
    # Attribute _size: this is the actual size of the queue.
    # Attribute _front: This is the pointer to point the first value of the stack.
    # Attribute _rear: This is the pointer to point the blank value in the array.
    # Attribute _capacity: this is the capacity of the array.
    # Attribute _data: this is the actual data.
    
    def __init__(self):
        '''
        This initializes the Queue class.
        '''
        self._size = 0
        self._front = 0   
        self._rear = 0
        self._capacity = 1
        self._data = self._make_array(self._capacity)
        
    def is_empty(self):
        '''Returns True if the queue is empty otherwise False.'''
        return self._size == 0
    
    def __len__(self):
        '''Return the length of the queue.'''
        return self._size
    
    def first(self):
        '''Return the first element of the queue.'''
        if self.is_empty():
            raise Empty('Queue is empty.')
        return self._data[self._front]
    
    def delete_first(self):
        '''Return and remove the first element of the queue.'''
        if self.is_empty():
            raise Empty('queue is already empty: ')
        first_element = self._data[self._front]
        self._front = (self._front + 1) % self._capacity
        self._size -= 1
        return first_element
    
    def delete_last(self):
        '''This removes and returns the element of the queue.'''
        if self.is_empty():
            raise Empty('queue is already empty: ')
        self._rear = (self._rear - 1 + self._capacity) % self._capacity
        element = self._data[self._rear]
        self._size -= 1
        return element
        
    def add_last(self, element):
        '''This add the elements in the queue at the end of queue.'''
        if self._size == self._capacity:
            array = self._make_array(2 * self._capacity)
            self._resize(array, 0)
            self._front = 0
            self._data[self._size] = element
            self._size += 1
            self._rear = self._size
            self._capacity = 2 * self._capacity
        else:
            self._data[self._rear] = element
            self._size += 1
            self._rear = (self._rear + 1) % self._capacity

    def add_first(self, element):
        '''This adds element at the first of the Dequeue.'''
        if self._size == self._capacity:
            array = self._make_array(2 * self._capacity)
            self._resize(array, 1)
            self._data[0] = element
            self._front = 0
            self._size += 1
            self._rear = self._size
            self._capacity = 2 * self._capacity
        else:
            self._front = (self._capacity + self._front - 1) % self._capacity
            self._data[self._front] = element
            self._size += 1

    def _resize(self, array, start):
        '''This is helper function to resize the array used to create queue.'''
        
        for i in range(start, self._size):
            array[i] = self._data[self._front]
            self._front = (self._front + 1) % self._capacity
        self._data = array

    def _make_array(self, c):
        '''returns an array of capacity c'''
        return (c * ctypes.py_object)() 


# Testing 
if __name__ == '__main__':
    # creating the objects of queue.
    queue = Queue()
    # queue.delete_first()     # testing error for delete_first on empty queue
    queue.add_last(24)
    queue.add_last(465)      # testing addition of element to queue.
    queue.add_last(234)
    queue.add_last(4659)
    queue.add_last(45623279)
    queue.add_last(45623279)
    queue.add_last(45623279)
    queue.add_last(45623279)
    print(len(queue))       # testing length of the queue.
    print(queue.delete_first())
    print(queue.delete_first())
    print(queue.delete_first())
    print(queue.delete_first())
    print(queue.delete_first())
    print(queue.delete_first())
    print(queue.delete_first())
    print(queue.delete_first())
    print(len(queue))
    # print(queue._capacity)
    print(queue.is_empty())        # testing is_empty function.
    # ensuring that the implemetation is circular.
    queue.add_last(546)
    queue.add_last(54986)
    queue.add_last(45623279)
    queue.add_last(45623279)
    queue.add_last(45623279)
    queue.add_first(65484)      # testing add_first function.
    for i in range(5):      # testing delete_last function
        queue.delete_last()
    print(len(queue))
    # print(queue._capacity)
    print(queue.first())      # testing first method for queue.