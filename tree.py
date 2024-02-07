"""
This script implements the tree data structure classes there are abstract classes
for tree, binary tree and implmented classes too for the same.

Author: Narayan Jat
Date: 5 October, 2023
"""

#Importing other data structure.
from queue_sll import SingliLinkedQueue as queue

#Exception class
class NotImplementedError(Exception):
    '''This is exception class to generate specific error messages.'''
    pass


# Tree ADT
class Tree(object):
    '''Abstract base class representing a Tree.'''

    # Defining position class
    class Position:
        '''This is the position class which holds the position of element.'''

        def element(self):
            '''return the element of the position.'''
            raise NotImplementedError('Must be implemented by subclass.')
        
        def __eq__(self, other):
            '''Returns true if other is a position representing the same position.'''
            raise NotImplementedError('Must be implemented by subclass.')
        
        def __ne__(self, __value: object) -> bool:
            '''Return True if self is not equal to other.'''
            raise not self == __value

    #Abstract functions must be implemented by subclasses.
    def root(self):
        '''Return the position representing root of tree(None if empty.)'''
        raise NotImplementedError('Must be implemented by subclass.')
    
    def parent(self, p):
        '''Return p's parent None if p is root.'''
        raise NotImplementedError('Must be implemented by subclass.')
    
    def num_children(self, p):
        '''Return the number of children p has.'''
        raise NotImplementedError('Must be implemented by subclass.')
    
    def children(self, p):
        '''Generate iteration of positions representing children of p.'''
        raise NotImplementedError('Must be implemented by subclass.')
    
    def __len__(self):
        '''Returns the total number of elements in a tree.'''
        raise NotImplementedError('Must be implemented by subclass.')
    
    def position(self):
        '''Generates positions for all elements of the tree.'''
        raise NotImplemented('This must be implemented by subclass.')

    def __iter__(self):
        '''Generate iteration all positions stored in tje tree.'''
        raise NotImplemented('This must be implemented by subclasses.')
    
    def height(self):
        '''Returns the height of tree.'''
        return self._height1()
    
    #Implemented functions which uses above unimplemented functions.
    def is_root(self, p):
        '''Return True if position p represent root of the tree.'''
        raise self.root() == p
    
    def is_leaf(self, p):
        '''Returns True if p is leaf node of tree.'''
        raise self.num_children(p) == 0
    
    def is_empty(self):
        '''Returns True if the tree is empty.'''
        return len(self) == 0

    def _height1(self):
        '''Return the height of the tree.'''
        for position in self.position():
            pass
            

#Binary tree ADT
class BinaryTree(Tree):
    '''Abstract base class representing Binary tree structure.'''

    #Abstract functions.
    def left(self, p):
        '''Return the position representing p's left child.
        None if p does not have any left child.'''
        raise NotImplementedError('Must be implemented by subclass.')
    
    def right(self, p):
        '''Return the position representing p's right child
        None if p does not have any right child'''
        raise NotImplementedError('Must be implemented by subclass.')
    
    #Implemented functions.
    def sibling(self, p):
        '''Return position representing p's sibling None if no sibling.
        '''
        parent = self.parent(p)
        if parent is None:  # p must be root
            return None # No sibling
        else:
            if p == self.left(parent):
                return self.right(parent)   #Possibly None
            else:
                return self.left(parent)    # Possibly None
            
    def children(self, p):
        '''Generate an iteration of positions of children of p. None if no children.'''
        if self.left(p) is not None:    #If left child exist.
            yield self.left(p)
        if self.right(p) is not None:   #If right child exist.
            yield self.right(p)


#Implementing Linked Binary Tree
class LinkedBinaryTree(BinaryTree):
    '''Linked representation of Binary tree.'''

    # Creating non-public node class.
    class _Node():
        '''Non-public node class.'''
        __slots__ = '_element', '_left', '_right', '_parent'

        def __init__(self, element, parent=None, left=None, right=None):
            '''Initializes the node class.'''
            self._element = element
            self._left = left
            self._right = right
            self._parent = parent

    #Creating public position class for tree.
    class Position(BinaryTree.Position):
        '''This class represents the position of a single node.'''
        def __init__(self, container, node):
            '''Initializes the position class.'''
            self._container = container
            self._node = node
        
        def element(self):
            '''Return the element at given position.'''
            return self._node._element
        
        def __eq__(self, other):
            '''Returns True if other is representing same location of the object.'''
            return type(other) is type(self) and other._node is self._node
        
    def __init__(self):
        '''Initializes the class Binary Tree.'''
        self._root = None
        self._size = 0

    # #Utilities
    def _validate(self, p):
        '''Return the node of position if p is a valid positions.'''
        if not isinstance(p, self.Position):
            raise TypeError('p is not a valid Position.')
        if p._container is not self:
            raise ValueError('p does not belong to this container.')
        if p._node._parent is p._node:  #Convention for deprecated node.
            raise ValueError('p is no longer valid node of this container.')
        return p._node
    
    def _make_position(self, container, node):
        '''Return the position of node provided.'''
        return self.Position(container, node) if node is not None else None
    
    #public accessors
    def root(self):
        '''Return the position representing root of tree(None if empty.)'''
        return self._make_position(self, self._root)
    
    def __len__(self):
        '''Return the total number of elements in a tree.'''
        return self._size
    
    def parent(self, p):
        '''Return the position of parent of the node p. None if p is a root node.'''
        node = self._validate(p)
        return self._make_position(self, node._parent)
    
    def num_children(self, p):
        '''Return the total number of childrens for a position p.'''
        node = self._validate(p)
        count = 0
        if not node._left:  #if left None no left child.
            count += 1
        if not node._right: #if right None no right child.
            count += 1
        return count
    
    def left(self, p):
        '''Return the position of p's left child. None is no left child.'''
        node = self._validate(p)
        return self._make_position(self, node._left)

    def right(self, p):
        '''Return the position of p's right child. None is no right child.'''
        node = self._validate(p)
        return self._make_position(self, node._right)
    
    def position(self):
        '''Generates all positions of elementes in tree.'''
        return self.preorder()
    
    def __iter__(self):
        '''Generates the elements of tree.'''
        for position in self.preorder():
            yield position._node._element

    #Tree traversal methods.
    def preorder(self):
        '''Generates the iterations of all positions of tree.'''
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def postorder(self):
        '''Generates the iterations of all position of tree.'''
        if not self.is_empty():
            for c in self._subtree_postorder(self.root()):
                yield c
    
    def breadth_first(self):
        '''Generates the iteration of positions in the tree.'''
        if not self.is_empty():
            q = queue()
            q.enqueue(self.root())
            while not q.is_empty():
                p = q.dequeue()
                yield p
                for c in self.children(p):
                    q.enqueue(c)

    def inorder(self):
        '''Generates iterations of the positions in the tree.'''
        if not self.is_empty():
            for c in self._subtree_inorder(self.root()):
                yield c

    #Utility methods.
    def _subtree_preorder(self, p):
        '''Generates iteration of all positions rooted at p.'''
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other
                
    def _subtree_postorder(self, p):
        '''Generates iterations of all positions rooted at p.'''
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other    
        yield p

    def _subtree_inorder(self, p):
        '''Generates iterations of the positions of tree.'''
        if self.left(p):
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p):
            for other in self._subtree_inorder(self.right(p)):
                yield other

    #-------------update methods-----------------
    def add_root(self, e):
        '''
        Creates a root for the tree storing e as element and returns it's position.
        Raise an error if tree is non-empty.
        '''
        if self._root:
            raise ValueError('Root exists.')
        node = self._Node(e)
        self._root = node
        self._size += 1
        return self._make_position(self, node)
    
    def add_left(self, p, e):
        '''Creates the node for left children storing element e
        of p and returns it's position.'''
        parent = self._validate(p)
        if self.left(p):
            raise ValueError('left node already exists.')
        node = self._Node(e, parent)
        parent._left = node
        self._size += 1
        return self._make_position(self, node)
    
    def add_right(self, p, e):
        '''Creates the node for right children storing element e
        of p and returns it's position.'''
        parent = self._validate(p)
        if self.right(p):
            raise ValueError('right node already exists.')
        node = self._Node(e, parent)
        parent._right = node
        self._size += 1
        return self._make_position(self, node)
    
    def replace(self, p, e):
        '''Replace the element with e at position p.
        Returns the priviously stored element at position p.'''
        node = self._validate(p)
        previous_element = node._element
        node._element = e
        return previous_element
    
    def delete(self, p):
        '''
        Remove the node at position p, replacing it with its child,
        if any, and return the element that had been stored at p;
        an error occurs if p has two children
        '''
        node = self._validate(p)
        element = node._element
        if self.left(p) and self.right(p):
            raise ValueError('Both children exist can not delete parent.')
        child = self.left(p) if not self.left(p) else self.right(p)
        if child is not None:
            child._parent =  node._parent
        if self.is_root(p):
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node #deprecation convention of a node.
        return element
    
    def attach(self, p, tree1, tree2):
        '''Attach the tree1 and tree2 as child to the leaf node p left and right respectively.
        Error if p is not a leaf node. Making tree1 and tree2 empty.'''
        if not self.is_leaf(p):
            raise ValueError('p is not a leaf node.')
        node = self._validate(p)
        if not type(self) is type(tree1) is type(tree2):
            raise TypeError('Tree types must match.')
        self._size += len(tree1) + len(tree2)
        if not tree1.is_empty():
            node._left = tree1._root
            tree1._root._parent = node
            tree1._root = None #tree deprecated convention.
            tree1._size = 0
        if not tree2.is_empty():
            node._right = tree1._root
            tree2._root._parent = node
            tree2._root = None #tree deprecated convention.
            tree2._size = 0


#-------------------------Testing Tree--------------------------
if __name__ == '__main__':
    tree = LinkedBinaryTree()
    tree.add_root(1)
    left = tree.add_left(tree.root(), 2)
    right = tree.add_right(tree.root(), 3)
    tree.add_left(left, 4)
    tree.add_right(left, 5)
    tree.add_left(right, 6)
    tree.add_right(right, 7)
    for i in tree.position():       # position of all the nodes.
        print(i)
    for elem in tree:       # tree as iterator
        print(elem)