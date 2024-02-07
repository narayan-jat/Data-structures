from MapBase import *
import random

class HashMapBase(MapBase):
    '''This map class based on the hash tables where collisions are handled
    using separate chaining.'''
    def __init__(self, capacity = 11, p = 456327983):
        self._table = [None] * capacity
        self._p = p
        self._size = 0
        self._scale = 1 + random.randrange(p-1)
        self._shift = random.randrange(p)

    def __len__(self) -> int:
        return len(self._size)
    
    def _hash_function(self, key):
        return ((hash(key) * self._scale + self._shift) % self._p) % len(self._table)

    def __getitem__(self, key):
        hashcode = self._hash_function(key)
        value = self._bucket_getitem(hashcode, key)
        return value
    
    def __setitem__(self, key, value):
        hashcode = self._hash_function(key)
        self._bucket_setitem(hashcode, key, value)
        if self._size > len(self._table) // 2:
            self._resize(2 * len(self._size) - 1)


    def __delitem__(self, key):
        h = self._hash_function(key)
        self._bucket_delitem(h, key)
        self._size -= 1

    def _resize(self, c):
        old = list(self.items())
        self._table = c * [None]
        self._size = 0
        for k, v in old:
            self[k] = v
       