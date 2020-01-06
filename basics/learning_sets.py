"""
    Collections of unique objects. Set theory.
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

set_1.discard(5) # 'modifie set' discart the item
print(set_1)
set_1.difference_update(set_2) # 'modifie set' remove the intersection. {4,5}
print(set_1)
print(set_1.intersection(set_2)) # returns the intersection numbers
print(set_1 & set_2) # do the same thing as above
print(set_1.union(set_2)) # join 2 sets together and remove the duplicates
print(set_1 | set_2) # do the same as the one above

set_3 = {4,5}
set_4 = {4,5,6,7,8,9,10}
print(set_3.issubset(set_4)) # returns True if the set_3 is 'inside' of set_4
print(set_3.issuperset(set_4)) # returns True if the set_3 contains set_4 inside


