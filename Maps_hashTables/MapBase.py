'''
This module is basic of maps in python.
'''
#Importing built-in class for maps
from collections.abc import MutableMapping

class MapBase(MutableMapping):
    '''This is base class for map data structure.'''

    #----------------Item class----------------------
    class _Item():
        '''This is non-public class for Item.'''

        def __init__(self, key, value):
            self._key = key
            self._value = value

        def __eq__(self, other):
            return self._key == other._key
        
        def __lt__(self, other):
            return self._key < other._key
        
        def __ne__(self, other):
            return not self == other