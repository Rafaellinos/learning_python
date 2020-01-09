
def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    inner()
    print("outer:", x)


outer() 
# when we use nonlocal, we are calling the parent variable
# and overwriting

