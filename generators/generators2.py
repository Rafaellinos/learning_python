"""

"""
# how for loops works
def special_for(itarable):
    iterator = iter(itarable) # makes a list an iterator obj
    while True:
        try:
            print(iterator)
            print(next(iterator)) # goes one by one obj
        except StopIteration:
            break # if exception of no more itarables, breaks the loop

special_for([1,2,3])

# create our own range
class MyGen(object):
    current = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last
    def __iter__(self):
        return self
    def __next__(self):
        if MyGen.current < self.last: 
            # it keeps returning num until it reaches the self.last
            num = MyGen.current
            MyGen.current += 1
            return num
        # when is current is higher or equal to self.last,
        # return stop iteration and breaks the for loop
        raise StopIteration

gen = MyGen(0, 100)
for i in gen:
    print(i)    

        