some_list = ['a','b','c','d','d','m','n','n']
unique_list = []
duplicates = []
for i in some_list:
    if i not in unique_list:
        unique_list.append(i)
    else:
        duplicates.append(i)
print(some_list)
print(unique_list)
print(duplicates)

"""
    To get the duplicate values
"""
duplicates1 = []
for i in some_list:
    if some_list.count(i) > 1:
        if i not in duplicates1:
            duplicates1.append(i) #get the duplicates only
print(duplicates1)