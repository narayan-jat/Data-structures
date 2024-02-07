'''
This module is to learn how one can know the things present in module.
'''
import inspect
import datetime

# Querying the modules.
classes_in_datetime = inspect.getmembers(datetime, inspect)
print(classes_in_datetime)


# this method is very efficient dir can be used to get all the things.
constants_and_functions = [name for name in dir(datetime) if not name.startswith('__') and not isinstance(getattr(datetime, name), type)]
print(constants_and_functions)

# Querying classes.

class MyClass:
    def __init__(self):
        self.attribute = 42

    def method_one(self):
        pass

    def method_two(self):
        pass

obj = MyClass()

# using inspect
# Get members of MyClass (functions, methods, and variables)
members = inspect.getmembers(MyClass)
print(members)

# Get members of an instance of MyClass (functions, methods, and variables)
obj_members = inspect.getmembers(obj)
print(obj_members)

# # using dir
# Get members of MyClass (functions, methods, and variables)
members = dir(MyClass)
print(MyClass.__getattribute__)

# Get members of an instance of MyClass (functions, methods, and variables)
print()
obj_members = dir(obj)
print(obj_members)

# using vars()
# Get members of MyClass (functions, methods, and variables)
members = vars(MyClass)
print(members)

# Get members of an instance of MyClass (functions, methods, and variables)
obj_members = vars(obj)
print('objest ')
print(obj_members)