#DRY don't repeat yourself

def blabla(num=0): # num=0 default parameter
    print(f"HAHAHAHAHAH{num}")

for _ in range(0,100):
    blabla(_) # positional arguments
    blabla(num=_) # keyword arguments
blabla() # call default arguments

def sum(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(sum(10, sum(4,5,2,1,2,3,4,5,6,10,1111)))

# functions inside functions nested function
def calculator(n1,n2):
    def sum(n1, n2):
        return n1+n2
    return sum(n1,n2)

cal = calculator(10,10)
print(cal)