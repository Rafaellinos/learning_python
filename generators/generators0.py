"""
range() is a generator.
Generator procuces a sequence of values of any type

interable = __iter__ to iterator

generator are iterators objects. Everything that is a generator
is a itarable object. But not every itarable is a generator

ex:
range() -> is a generator and iterable
list() -> is iterable but not generator
"""


def make_list(num):
    return [i * 2 for i in range(num)]  # same as list(range(100))


my_list = make_list(100)
print(my_list)


def generator_func(num):
    for i in range(num):
        yield i  # pauses the func
        # when the function has yield, is that number that the generator will return


for i in generator_func(1000):
    print(i)  # out 0,1,2..999
    # got throug the iterable that generator_func 
    # produces and prints each number at the time

g = generator_func(100)
print(g)  # out generator obj
# next goes to the next itarable
print(next(g))  # out 0
print(next(g))  # out 1
print(next(g) + 10)  # out 12
# the item still in memory
