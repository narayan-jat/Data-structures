'''
This module contains the implemention of Deque, Doubly linked list 
as a undelying data structure. This supports all the operations which are 
supported by the Deque.

Author: Narayan Jat
Date: 14 September, 2023
'''

from Error import Empty     # importing user defined error module.

class DoublyLinkedDeque(object):
    '''
    This is deque whose underlying implementation is a doubly linked list.
    '''
    __slots__ = '_header', '_trailer' , '_size'    # to streamline the memory usage.

    def __init__(self):
        '''
        This initializes this Deque.
        '''
        self._header = self._Node(None, None, None)     # header and trailer are the sentinels.
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0


    class _Node(object):
        '''
        This is non-public light-weight node class.
        '''
        __slot__ = '_element', '_prev', '_next'

        def __init__(self, element, previous, next):
            '''This initilizes the Node class'''
            self._element = element
            self._prev = previous
            self._next = next

    def is_empty(self):
        '''Returns true if the deque is empty otherwise false'''
        return self._size == 0
    
    def __len__(self):
        '''Returns the length of the  deque.'''
        return self._size
    
    def add_first(self, element):
        '''Adds element to the front of the deque.'''
        self._insert_element(element, self._header, self._header._next)

    def add_last(self, element):
        '''Adds the element to the last of the list.'''
        self._insert_element(element, self._trailer._prev, self._trailer)

    def delete_first(self):
        '''Returns and remove the first element of the deque.'''
        if self.is_empty():
            raise Empty('Deque is empty.')
        return self._delete_node(self._header._next)

    def delete_last(self):
        '''Returns and remove the last element of the deque.'''
        if self.is_empty():
            raise Empty('Deque is empty.')     
        return self._delete_node(self._trailer._prev)
    
    def _delete_node(self, node):
        '''This is helper method to delete node.'''
        removed_element = node._element
        node._prev._next = node._next
        node._next._prev = node._prev
        self._size -= 1
        return removed_element
    
    def _insert_element(self, element, predessor, successor):
        '''Helper to insert element.'''
        new_node = self._Node(element, predessor, successor)
        predessor._next = new_node
        successor._prev = new_node
        self._size += 1

    def first(self):
        '''Returns the first element of the deque.'''
        if self.is_empty():
            raise Empty('Deque is empty.')
        return self._header._next._element
    
    def last(self):
        '''Returns the last element of th deque.'''
        if self.is_empty():
            raise Empty('Deque is empty.')
        return self._trailer._prev._element


#-----------------------------TESTING-------------------------
if __name__ == '__main__':
    deque = DoublyLinkedDeque()
    print("Id when it's blank", id(deque))
    #raising error when they should be raised.
    # deque.first()
    # deque.last()       
    # deque.delete_last()
    # deque.delete_first()
    # comment above for statements to see output of the following.
    print(deque.is_empty())

    # adding element to deque.
    for i in range(20):
        if i > 10:
            deque.add_first(i)
        else:
            deque.add_last(i)

    print("Id when it's filled", id(deque))
    # checking the is_empty and size of the deque.
    print(deque.is_empty())
    print(len(deque))

    # deleting the elements from the deque.

    for i in range(8):
        if i % 2 == 0:
            print(deque.delete_first())
        else:
            print(deque.delete_last())

    # checking the first and last functions.
    print(deque.first())
    print(deque.last())

    print(deque.is_empty())
    print(len(deque))

    # output for above test case should be matched with the elements in list.
    # [Exception, Exception, Exception, Exception True, False, 20, 19, 10, 18, 
    # 9, 17, 8, 16, 7, 15, 6, False, 12]