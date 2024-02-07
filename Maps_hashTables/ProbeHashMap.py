from HashMapBase import HashMapBase

class ProbeHashMap(HashMapBase):

    _AVAIL = object()       # marker for depricated node.

    def _is_available(self, index):
        return self._table[index] is None or self._table[index] is ProbeHashMap._AVAIL
    
    def _find_slot(self, index, key):
        first_avail = None
        while True:
            if self._is_available(index):
                if first_avail is None:
                    first_avail = index
                if self._table[index] is None:
                    return(False, index)
            elif key == self._table[index]._key:
                return (True, index)
            index = (index + 1) % len(self._table)

    def _bucket_setitem(self, hashcode, key, value):
        found, s = self._find_slot(hashcode, key)
        if not found:
            self._table[s] = self._Item(key, value)
            self._size += 1
        else:
            self._table[s]._value = value

    def _bucket_getitem(self, hashcode, key):
        found, s = self._find_slot(hashcode, key)
        if not found:
            raise KeyError("key doesn't exist.")
        return self._table[s]._value
    
    def _bucket_delitem(self, hashcode, key):
        found, s = self._find_slot(hashcode, key)
        if not found:
            raise KeyError("key doesn't exist.")
        self._table[s] = ProbeHashMap._AVAIL

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key
