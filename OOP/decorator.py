"""
like @classmethod and @staticmethod

decorator super charge a function by adding a new functionality
"""

def hello():
    print("hellllloooooo")

greet = hello
del hello
"""
Even if you delet the name hello, greet still poiting (in memory) to function hello
and the greet will work normally
"""
print(greet())

"""
Hight order function HOC ia a function that accepts a func as param or return a func
ex: map, filter, reduce
"""
def nice(func):
    def func():
        return 2
    return func

#####################



def my_decorator(func):
    def wrap_func():
        print("******")
        func()
        print("******")
    return wrap_func

@my_decorator
def hello():
    print('hello')
@my_decorator
def bye():
    print('see ye')

hello()
bye()
# same thing as:
my_decorator(hello)()
