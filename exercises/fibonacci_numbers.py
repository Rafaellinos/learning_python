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
            
fib(20)
        
### by using yield
def fib2(n):
    a = 0
    b = 1
    for i in range(n):
        yield a
        #when the function has yield, is that number that the generator will return
        tmp = a
        a = b
        b = tmp + b

for x in fib2(21):
    print(x) # print the a