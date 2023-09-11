'''
This module is specially designed to contain Queue data structure
and supports all operations which are supported by a Queue.
 This data structure has been implemented based on the array.

Author: Narayan Jat
Date: 7 September, 2023
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
    
    def dequeue(self):
        '''Return and remove the first element of the queue.'''
        if self.is_empty():
            raise Empty('queue is already empty: ')
        first_element = self._data[self._front]
        if len(self._data) == self._front + 1:
            self._front = 0
        else:
            self._front += 1
        self._size -= 1
        return first_element
        
    def enqueue(self, element):
        '''This add the elements in the queue at the end of queue.'''
        if self._size == self._capacity:
            self._resize(2 * self._capacity)
            self._front = 0
            self._data[self._size] = element
            self._size += 1
            self._rear = self._size
        else:
            self._data[self._rear] = element
            self._size += 1
            self._rear = (self._rear + 1) % self._capacity

    def _resize(self, size):
        '''This is helper function to resize the array used to create queue.'''
        array = self._make_array(size)
        for i in range(self._size):
            array[i] = self._data[self._front]
            self._front = (self._front + 1) % self._capacity
        self._data = array
        self._capacity = size

    def _make_array(self, c):
        '''returns an array of capacity c'''
        return (c * ctypes.py_object)() 


# Testing 
if __name__ == '__main__':
    # creating the objects of queue.
    queue = Queue()
    queue.dequeue()     # testing error for dequeue on empty queue
    queue.enqueue(24)
    queue.enqueue(465)      # testing addition of element to queue.
    queue.enqueue(234)
    queue.enqueue(4659)
    queue.enqueue(45623279)
    queue.enqueue(45623279)
    queue.enqueue(45623279)
    queue.enqueue(45623279)
    print(len(queue))       # testing length of the queue.
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
    print(len(queue))
    # print(queue._capacity)
    print(queue.is_empty())        # testing is_empty function.
    # ensuring that the implemetation is circular.
    queue.enqueue(546)
    queue.enqueue(54986)
    queue.enqueue(45623279)
    queue.enqueue(45623279)
    queue.enqueue(45623279)
    print(len(queue))
    # print(queue._capacity)
    print(queue.first())      # testing first method for queue.