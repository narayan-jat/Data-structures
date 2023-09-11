'''
This module solves the problems given in the book.

Author: Narayan Jat,
Date: 7 September, 2023
'''
# Importing data structures.
from stack import *

# Problem 6.4
# recursive function to make a stack empty.
stack = Dynamic_Stack()
def make_empty(stack):
    '''Makes empty a stack.'''
    if len(stack) == 1:
        print(stack.pop())
    else:
        print(stack.pop())
        make_empty(stack)


# Problem C 6.15
# write a pseudocode to find greatest amaong three numbers.
stack1 = Dynamic_Stack().push(239)
x = stack1.pop()
# compare this with next popped value.
# this will ensure that value in x in greatest with probability 2/3.




# testing
if __name__ == '__main__':
    for i in range(45):
        stack.push(i)
    make_empty(stack)