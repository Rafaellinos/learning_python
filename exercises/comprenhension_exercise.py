some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)

"""
do the same thing as above by using comprenhension
"""
print(some_list)

duplicates = {x for x in some_list if some_list.count(x) > 1}
print(duplicates)

my_list2 = [1,'a','b',2,{},[]]
# remove the duplicate objects
my_uniq_list = []
for x in my_list2:
    if x not in my_uniq_list:
        my_uniq_list.append(x)
print(my_uniq_list)