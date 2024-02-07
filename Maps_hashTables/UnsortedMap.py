from MapBase import *

class UnsortedMap(MapBase):

    def __init__(self):
        self._table = []

    def __setitem__(self, key, value):
        for item in self._table:
            if item._key == key:
                item._value = value
                return
        self._table.append(self._Item(key, value))
        
    def __getitem__(self, key):
        for item in self._table:
            if item._key == key:
                return item._value
        raise KeyError("Key doesn't exist.")

    def __delitem__(self, key):
        for item in self._table:
            if item._key == key:
                self._table.remove(item)
                return
        raise KeyError("Key doesn't exist.")
    
    def __len__(self):
        return len(self._table)
    
    def __iter__(self):
        for item in self._table:
            yield item._key

