"""
Given 2 arrays, create a function that let's a used know (true, false) whether
these two arrays contain any common items.
for example:
///
    array1 = ['a','b','c','x']
    array2 = ['z','y','i']
    should return false.
///
    array1 = ['a','b','c','x']
    array2 = ['z','y','x']
    should return true
"""

def check_array(array: list, array2: list) -> bool:
    super_array = array + array2
    return len(super_array) != len(set(super_array))

def check_array1(array: list, array2: list) -> bool: # bad solution, nested loops are O(n²)
    for i in range(len(array)):
        for x in range(len(array2)):
            if array[i] == array2[x]:
                return True
    return False

def check_array2(array: list, array2: list) -> bool:
    for i in array:
        if i in array2:
            return True
    return False

def check_array3(array: list, array2: list) -> bool:
    map_d = dict()
    for i in range(len(array)):
        if not map_d.get(array[i]):
            item = array[i]
            map_d[item] = True

    for j in range(len(array2)):
        if map_d.get(array2[j]):
            return True
    return False



array1 = ['a','b','c','x']
array2 = ['z','y','x']
print(check_array3(array1, array2))
array3 = ['a','b','c','x']
array4 = ['z','y','i']
print(check_array3(array3, array4))