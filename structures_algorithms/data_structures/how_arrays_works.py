"""
How to build array by using class
"""

class MyArray():

    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        lastitem = self.data[self.length-1]
        # -1 because length of the index. index of 1 is equals to the second
        # item in the list ex: list[1]. So, if we want to take the last item
        # we need to take the length -1. If we dont do that, we will get key
        # error.
        del self.data[self.length-1]
        self.length -= 1
        return lastitem

    def delete(self, index):
        item = self.data[index]
        self.shiftitem(index)
        return item

    def shiftitem(self, index): # O(n)
        i = index
        # for each item, starting at the index that we want to delete
        while (i < self.length-1):
            self.data[i] = self.data[i+1]
            # get the next item and assign to the actual item
            i += 1
        # with this, the last item will be duplicate
        # example:
        # {0: 'ha',1:'hu',2:'ho',3:'!'} then -> shift the index of 1
        # {0: 'ha',1:'ho',2:'!',3:'!'}
        del self.data[self.length-1]
        self.length -= 1

    def see_all(self):
        return self.data

newArray = MyArray()
newArray.push('hi')
newArray.push('hu')
newArray.push('ho')
newArray.push('ha')
newArray.push('!')
# print(newArray.pop())
print(newArray.see_all())
print(newArray.length)
print(newArray.delete(1))
print(newArray.see_all())
print(newArray.length)