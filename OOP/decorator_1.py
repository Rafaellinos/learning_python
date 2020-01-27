# Decorator Pattern


def my_decorator(func):
    def wrap_func(*args, **kw): # 
        print("****")
        func(*args, **kw) 
        #in this way, the func can receive any kind of param with decorator patern
        print("****")
    return wrap_func

@my_decorator
def hello(greeting, hi):
    print(greeting, hi)

hello("123","hi")
# same as:
# a = my_decorator(hello)
# a('123)