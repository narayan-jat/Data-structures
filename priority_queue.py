"""
This module contains the priority queue adt and ite's implementation.

Author: Narayan Jat
Date: 20 Oct, 2023
"""
#Importing required modules.
from positionalList import PositionalList
from Error import Empty

# creating an customized error class.
class NotImplementedError(Exception):
    '''This is customized error class.'''
    pass


# Implementing Priority queue ADT.
class PriorityQueue(object):
    '''This is the abstract class for priority queue data structure.'''

    class _Item:
        '''Non-public light weight helper class.'''

        def __init__(self, key, value):
            '''Initializes the class.'''
            self._key = key
            self._value = value

        def __lt__(self, other):
            '''Returns true if self lesser than the other.'''
            return self._key <= other._key 
            
    def add(self, key, value):
        '''This add key, value pair to the priority queue.'''
        raise NotImplementedError('This class must be implemented by subclass')

    def min(self):
        '''Returns the element which is at the highest priority.'''
        raise NotImplementedError('This class must be implemented by subclass')
    
    def remove_min(self):
        '''Returns and removes the element at priority first.'''
        raise NotImplementedError('This class must be implemented by subclass')
    
    def is_empty(self):
        '''Returns true if queue is empty otherwise False.'''
        return len(self) == 0
    
    def len(self):
        '''Returns the length of the queue.'''
        raise NotImplementedError('This class must be implemented by subclass')


#Implementing Priority Queue with unsorted list.
class UnsortedPriorityQueue(PriorityQueue):
    '''Unsorted priority queue.'''
        
    def __init__(self):
        '''Initializes the main class.'''
        self._queue = PositionalList()

    def len(self):
        '''Returns the length of the queue.'''
        return len(self._queue)
    
    def add(self, key, value):
        '''This add key, value pair to the priority queue.'''
        self._queue.add_last(self._Item(key, value))

    def min(self):
        '''Returns the element which is at the highest priority.'''
        position = self._find_min()
        item = position.element()
        return (item._key, item._value)
            
    def remove_min(self):
        '''Returns and removes the element at priority first.'''
        position = self._find_min()
        item = self._queue.delete(position)
        return (item._key, item._value)

    def _find_min(self):
        '''Returns the position of the highest priority item.'''
        if self.is_empty:
            raise Empty('Queue is empty.')
        small = self._queue.first()
        walk = self._queue.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk.element()
            walk = self._queue.after(walk)
        return small

#Implementing Priority queue with Sorted list.
class SortedPriorityQueue(UnsortedPriorityQueue):
    '''This Sorted priority queue class.'''        

    def add(self, key, value):
        '''Adds given item to the prirority queue.'''
        item = self._Item(key, value)
        self._add_item(item)

    def min(self):
        '''Return the tuple of key and value pair for which key is minimum.'''
        if self.is_empty():
            raise Empty('queue is empty.')
        position = self._queue.first()
        item = position.element()
        return (item._key, item._value)
    
    def remove_min(self):
        '''Remove and return the key value pair.'''
        if self.is_empty():
            raise Empty('queue is empty.')
        position = self._queue.first()
        item = self._queue.delete(position)
        return (item._key, item._value)
    
    #Non-public methods.
    def _add_item(self, item):
        '''Helper for add method.'''
        walk = self._queue.last()
        while walk:
            if walk.element() < item:
                target_node = walk
                break
            walk = self._queue.before(walk)
        if walk is None:
            self._queue.add_first(item)
        else:
            self._queue.add_after(target_node, item)


#Implementing Priority queue with Heap.
class MinHeapPriorityQueue(PriorityQueue):
    '''This class implements Priority queue with underlying min heap data structure.'''

    #Public behaviours
    def __init__(self, contents = ()):
        self._queue = [self._Item(k, v) for k, v in contents]
        if len(self._queue) > 1:
            self._heapify(self._queue // 2 - 1)

    def __len__(self):
        '''Returns the length of the queue.'''
        return len(self._queue)
    
    def is_empty(self):
        '''Return True if queue is empty otherwise False.'''
        return len(self) == 0
    
    def add(self, key, value):
        '''Adds the key value pair to priority queue.'''
        self._queue.append(self._Item(key, value))
        self._upheap(len(self._queue) - 1)

    def min(self):
        '''Remove and return the key value pair.'''
        if self.is_empty():
            raise Empty('queue is empty.')
        item = self._queue[0]
        return (item._key, item._value)
        
    def remove_min(self):
        '''Remove and return the key value pair.'''
        if self.is_empty():
            raise Empty('queue is empty.')
        self._swap(0, len(self._queue) - 1)
        item = self._queue.pop()
        self._downheap(0)
        return (item._key, item._value)
           
    #---------------------Private methods.-------------
    def _parent(self, child):
        '''Return the position for parent of child.'''
        return (child - 1) // 2
    
    def _left(self, parent):
        '''Return the position for the left child of parent.'''
        return 2 * parent + 1
    
    def _right(self, parent):
        '''Return the position for the right child of parent.'''
        return 2 * parent + 2
    
    def _hasleft(self, parent):
        '''Return True if parent has left child.'''
        return self._left(parent) <= len(self._queue) - 1

    def _rightleft(self, parent):
        '''Return True if parent has right child.'''
        return self._right(parent) <= len(self._queue) - 1
    
    def _swap(self, position1, position2):
        '''Swaps the items at position1 with position2.'''
        temp_value = self._queue[position1]
        self._queue[position1] = self._queue[position2]
        self._queue[position2] = temp_value

    def _upheap(self, position):
        '''Helper to do upheap operation.'''
        walk = self._parent(position)
        if self._queue[walk] >= self._queue[position] and position > 0:
            self._swap(position, walk)
            self._upheap(walk)

    def _downheap(self, position):
        '''Helper to peform downheap.'''
        if self._hasleft(position):
            left = self._left(position)
            small_child = left
            if self._hasright(position):
                right = self._right(position)
                if right < left:
                    small_child = left
            if self._queue[position] > self._queue[small_child]:
                self._swap(position, small_child)
                self._downheap(small_child)

    def _heapify(self, position):
        '''Creates min heap from the list of items given.'''
        self._downheap(position)
        if position >= 1:
            self._heapify(position - 1)


#Implementing Priority Queue with max heap notion.
class MaxHeapPriorityQueue(MinHeapPriorityQueue):
    '''This is max heap based implementation of priority queue.'''

    #------------------private methods---------------------
    def _upheap(self, position):
        '''Helper to do upheap operation.'''
        walk = self._parent(position)
        if self._queue[walk] <= self._queue[position] and position > 0:
            self._swap(position, walk)
            self._upheap(walk)

    def _downheap(self, position):
        '''Helper to peform downheap.'''
        if self._hasleft(position):
            left = self.left(position)
            small_child = left
            if self._hasright(position):
                right = self.right(position)
                if right < left:
                    small_child = left
            if self._queue[position] < min:
                self.swap(position, small_child)
                self._downheap(small_child)

    #-------------------public methods-----------------
    def max(self):
        '''Returns the key value pair which is at lowest priority.'''
        super().min()

    def remove_max(self):
        '''Return and Remove the key value pair which are at lowest priority.'''
        super().remove_min()


#------------------------Testing--------------------------
if __name__ == '__main__':
    pass