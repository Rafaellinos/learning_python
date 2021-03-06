"""
    Tuples are immutables, so you can't update, sort, add item etc
    Usually more faster than lists.
    Tuple only has two methods: count and index, but it works with len
"""
tuple2 = (1,2,3,4)
print(3 in tuple2)

new_tuple = tuple2[1:4]
print(new_tuple)

a, b, *other = tuple2 #unpacking tuple
print(other)
print(tuple2)
print(tuple2.index(2)) #seach by value, returns the index
print(tuple2[2]) #search by index, returns the value

tuple3 = ('1','2','3','4')
print(tuple3.index('3'))


a, b, *_ = tuple3 
# underscore indicates to python that the variable will not be used.
print(a)
print(b)