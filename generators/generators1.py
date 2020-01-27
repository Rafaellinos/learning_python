"""
check the performace of range vs list
"""
from time import time

def performance(func):
    def wrap_func(*args, **kw):
        t1 = time()
        result = func(*args, **kw)
        t2 = time()
        print(f"took {t2-t1}s")
        return result
    return wrap_func

@performance
def long_time():
    print('1')
    for i in range(1000000):
        i*5

@performance
def long_time2():
    print('2')
    for i in list(range(1000000)):
        i*5

long_time()
long_time2()
"""
1
took 0.06453680992126465s
2
took 0.10934734344482422s

The diference is because the range() generator do not hold
things in memory, when the goes to the next, it just replace in memory
list() in the other hands hold all numbers on list in memory
"""