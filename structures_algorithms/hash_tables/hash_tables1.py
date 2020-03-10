"""
Exercise: Create our own hash function

In python, dic
"""
from random import randint


class Hashtable:

    def __init__(self, size: int):
        self.mydict = ['None'] * size
        self.addr_list = []

    def __str__(self):
        # return each obj with key as variable name and value as the
        # value of the variable
        return str(self.__dict__)

    def _hash(self):
        while True:
            # pick a number between 0 and 49, if address not found,
            # still o while loop, only return value that aren't on addr_list
            x = randint(0, 49)
            if x not in self.addr_list:
                return x

    def set(self, key, value):
        address = self._hash() # return the unique address
        self.mydict[address] = [key, value]
        # insert the address as index and key/value the the value
        self.addr_list.append(address)
        # add the address on the list of addresses

    def get(self, key):

        for i in self.addr_list:
            if self.mydict[i][0] == key:
                return self.mydict[i][1]

    def keys(self):
        key_arr = []
        for i in self.addr_list:
            key_arr.append(self.mydict[i][0])
        return key_arr


h = Hashtable(50)
h.set('grapes', 1000)
h.set('apples', 10)
h.set('oranges', 300)
h.set('bananas', 200)
x = h.get('grapes')
key_arr = h.keys()
print(h)
print(x)
print(key_arr)

