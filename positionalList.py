'''
This module contains the implementation of the Positional List 
Abstract Data Type(ADT) which is based Doubly linked list.

Author:Narayan Jat
Date:17 September, 2023
'''

class _DoublyLinkedList(object):
    '''This is a base class for position list class.'''

    #------------------Node Class----------------------
    class _Node(object):
        '''This a light weight non-public supporting class for doubly linked list.'''

        def __init__(self, element, previous, next) -> None:
            '''Initialising the Node class.'''
            self._element = element
            self._prev = previous
            self._next = next

    #---------------Doubly Linked list-----------------
    def __init__(self) -> None:
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def is_empty(self):
        '''Returns True if the list is empty.'''
        return self._size == 0
    
    def __len__(self):
        '''Returns the length of the list.'''
        return self._size
    
    def _insert_between(self, e, predecessor, successor):
        '''Inserts the node between predessor and successor.'''
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        '''Deletes the and node and return the element.'''
        popped_element = node._element
        node._prev._next = node._next
        node._next._prev = node._prev
        self._size -= 1
        return popped_element

# Positional list class

class PositionalList(_DoublyLinkedList):
    '''This is a positional list.'''

    #----------------------Position class----------------------
    class _Position(object):
        '''This is the position which holds the position of a node in the list.'''

        def __init__(self, container, node) -> None:
            self._container = container     # track type of node
            self._node = node
            
        def element(self):
            '''return the element of the position.'''
            return self._node._element
        
        def __eq__(self, other):
            '''Returns true if other is a position representing the same position.'''
            return type(self) is type(other) and self._node is other._node
        
        def __ne__(self, __value: object) -> bool:
            '''Return True if self is not equal to other.'''
            return not(self == __value)
            
    #-------------------Positional List utilities-------------------------
    def _validate(self, position):
        '''Returns position's node and validate the position.'''
        if not isinstance(position, self._Position):
            raise TypeError('position is not of type Position.')
        if position._container is not self:
            raise ValueError('position does not belong to this container.')
        if position._node._next is None:
            raise ValueError('position no longer exist.')
        return position._node
    
    def _make_position(self, node):
        '''Returns the position instance or return None if list is empty.'''
        if node is self._header or node is self._trailer:
            return None
        else:
            return self._Position(self, node)
        
    #-----------------Accessors-------------------------
    def first(self):
        '''Returns the position of the first element of list. None if is list empty.'''
        return self._make_position(self._header._next)
    
    def last(self):
        '''Returns the position of the last element of list. None if is list empty.'''
        return self._make_position(self._trailer._prev)

    def before(self, p):
        '''Returns the position just before the p. None if is list empty.'''
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self, p):
        '''Returns the position just after the p. None if is list empty.'''
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        '''generates the elements one by one from list.'''
        cursor = self.first()
        while not (cursor is None):
            yield cursor.element()
            cursor = self.after(cursor)
    
    #---------------------Mutators---------------------------
    def _insert_between(self, e, predecessor, successor):
        '''Returnd the position and insert the element between two given nodes.'''
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)
    
    def add_first(self, e):
        '''Adds the element at the first of list.'''
        return self._insert_between(e, self._header, self._header._next)
 
    def add_last(self, e):
        '''Adds the element at the last of list.'''
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        '''Adds the element before p.'''
        original = self._validate(p)
        return self._make_position(e, original._prev, original)

    def add_after(self, p, e):
        '''Adds the element before p.'''
        original = self._validate(p)
        return self._make_position(e, original, original._next)

    def delete(self, p):
        '''Returns and remove the element at position p.'''        
        original = self._validate(p)
        return self._delete_node(original)
    
    def replace(self, p, e):
        '''Replace the element with value at position p
        
        Returns the formerly value at position p.'''
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value
    

#---------------------Testing----------------------
if __name__ == '__main__':
    lst = PositionalList()
    print(lst.is_empty())
    for i in range(10):
        if i % 2 == 0:
            lst.add_last(i * 44)        # adding at last
        else:
            lst.add_first(i * 62)       # adding at  first
    print(lst.first())      # Return hexadecimal refrence value.
    print(lst.last())
    print(len(lst))
    print(lst.is_empty())
    for i in range(15):
        print(lst.delete(lst.first()))  # will delete element and raise exception if list is empty.