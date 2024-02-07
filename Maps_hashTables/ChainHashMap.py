from HashMapBase import HashMapBase
from UnsortedMap import UnsortedMap

class ChainHashMap(HashMapBase):
    '''This is a hash map based on the separate chaining.'''
    # change here.

    def _bucket_setitem(self, hashcode, key, value):
        if self._table[hashcode] is None:
            self._table[hashcode] = UnsortedMap()
        old_size = len(self._table[hashcode])
        self._table[hashcode][key] = value
        if len(self._table[hashcode]) > old_size:
            self._n += 1
    
    def _bucket_getitem(self, hashcode, key):
        bucket = self._table[hashcode]
        if bucket:
            return bucket[key]
        raise KeyError("key doesn't exist.")
    
    def _bucket_delitem(self, hashcode, key):
        bucket = self._table[hashcode]
        if bucket is None:
            raise KeyError("key doesn't exist.")
        del bucket[key]

    def __iter__(self):
        for bucket in self._table:
            if bucket:
                for key in bucket:
                    yield key
 