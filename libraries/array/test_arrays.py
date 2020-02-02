"""
In python, lists are different from arrays.
lists are dynamic and arrays not, when you create an array
the memory necessary is setup.

Arrays is like a wrapper over C arrays.

Lists uses a lot more space than C arrays.

Lists and arrays can both be indexed, but can only store one type of data.
But an array can be divided by 3, and each number in the array will be
divided by 3. 
"""
from array import array

# 'i' it means that this array can hold only integers.
# to see more = https://docs.python.org/3/library/array.html
array1 = array('i',[1,2,3])
print(array1[1])


