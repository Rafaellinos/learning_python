"""
merge two arrays into one
"""

array1 = [0, 3, 4, 31]
array2 = [4, 6, 30]

def merge_arrays(array1: list, array2: list) -> list:
    if array1.__len__() == 0:
        return array2
    if array2.__len__() == 0:
        return array1

    index = 0
    while index <= array1.__len__()-1:
        array2.append(array1[index])
        index += 1

    return sorted(array2)

print(merge_arrays(array1, array2))