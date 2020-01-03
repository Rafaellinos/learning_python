"""
    Collections of unique objects
"""

my_set = {1,2,3,4,5,5}
print(type(my_set))
print(my_set) 
#returns only UNIQUE values, if has more than one of the same, just ignore
my_set.add(100)
print(my_set)

my_list = [1,2,3,4,5,5]
# transform in set to remove duplicate
print(my_list)
print(set(my_list))

set_1 = {1,2,3,4,5}
set_2 = {4,5,6,7,8,9,10}
print(set_1.difference(set_2))
# difference returns the diference between set_1 and set_2
# in this case will return {1,2,3}, because 1,2,3 is no present in set_2
print(set_2.difference(set_1))
# on this case will return {6,7,8,9,10}, because they are no present in set_1