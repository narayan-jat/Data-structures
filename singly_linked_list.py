from Error import Empty     # Importing error class.
class SinglyList(object):
    '''This is Queue based on the circular linked list data structure.'''      

    #-------------------------- Node Class ----------------------------
    class _Node(object):
        '''This is lightweight non-public node class.'''
        __slots__ = '_element', "_next"         # strealine memory usage.
        
        def __init__(self, element, next):
            '''This initializes the node class'''
            self._element = element
            self._next = next

    #-------------------------- Node Class Ended ----------------------

    def __init__(self):
        '''This initializes the LinkedQueue.'''
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        '''Returns True if the Queue is empty otherwise False.'''
        return self._size == 0
    
    def __len__(self):
        '''Returns the length of the LinkedQueue.'''
        return self._size
    
    def first(self):
        '''Returns the first element of the sll.'''
        if self.is_empty():
            raise Empty('list is empty.')
        return self._head._element
    
    def __iter__(self):
        '''Gives one by one value from list.'''
        node = self._head
        i = 0
        while self._size != i:
            yield node._element
            node = node._next
            i += 1
    
    def add_first(self, element):
        '''This method add element at the end of the queue.'''
        new_node = self._Node(element, None)        # creating node with None reference value.
        if self.is_empty():     
            self._head = new_node       # adding new node itself as node if it's first node.
            self._tail = new_node
        else:
            self._tail._next = new_node
            self._tail = new_node
        self._size += 1

    def node(self, element):
        '''Return the node holding given value.'''
        i = 0
        current = self._head
        while i < len(self):
            i += 1
            if element == current._element:
                return current
            current = current._next
    
    def remove(self):
        '''Removes the first element.'''
        if self.is_empty():
            raise Empty('list is empty.')
        self._head = self._head._next
        self._size -= 1

#-----------------------Testing-----------------------------
if __name__ == '__main__':
    lst = SinglyList()
    for i in range(4):
        lst.add_first(i)
    for i in lst:
        print(i)