from functools import reduce

my_list = [1,2,3]

def multiply_by2(item):
    return item*2

def accumulator(acc, item):
    print(acc, item)
    return acc+item

#             func          item, acc
print(reduce(accumulator, my_list, 0)) # default = 0
# output
# 0 1
# 1 2
# 3 3
# 6

sum_total = reduce((lambda x,y: x+y), [1,2,3,4], 0)
print(sum_total) #10
"""
    reduce gets the return number and store for the next iteration.
    The first number is 0, default is 0

    1. reduce((0+1), iterable, 0): returns 1
    2. reduce((1+2), iterable, 1): returns 3
    3. reduce((3+3), iterable, 3): returns 6
    4. reduce((6+4), iterable, 6): returns 10
    
"""
