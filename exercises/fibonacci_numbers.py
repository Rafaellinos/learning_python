from time import time

def performance(func):
    def wrap_func(*args, **kw):
        t1 = time()
        result = func(*args, **kw)
        t2 = time()
        print(f'took {t2-t1} s')
        return result

    return wrap_func

# not a generator, just prints the number
@performance
def fib(n):
    a = 1
    b = 0

    for x in range(n+1): 
        if x < 2:
            print(x)
        else:
            tmp = a
            a = a+b 
            print(a)
            b = tmp 
                    
### generator using yield, return a for each next()
@performance
def fib2(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        #when the function has yield, is that number that the generator will return
        tmp = a
        a = b
        b = tmp + b


# not a generator, just return a list
@performance
def fib3(n):
    fibs = [0,1]
    for i in range(n):
        fibs.append(fibs[-2] + fibs[-1])
    return fibs


fib(2000)
for x in fib2(2000):
    x = x
fib3(2000)
"""
the advantage of the generator without list is that the numbers isn't store in memory, 
for each next() the previous number is replaced for the new one.

If you give a huge amount of number to fib genator, the performance will be better.
Or not??
output:
took 0.11019325256347656 s
took 3.337860107421875e-06 s
took 0.0008633136749267578 s
"""
