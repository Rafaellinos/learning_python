# performace decorator
from time import time

def performance(func):
    def wrap_func(*args, **kw):
        t1 = time()
        result = func(*args, **kw)
        t2 = time()
        print(f'took {t2-t1} s')
        return result

    return wrap_func


@performance
def long_time():
    for i in range(100000000):
        print(i)
        i = i**5
        print(i)
        

long_time() #took 33.680824279785156 s