"""
Given an array, return the first of repeated item.
Ex:
Given an array = [2,5,1,2,3,5,1,2,4]
it should return 2

Given an array = [2,1,1,2,3,5,1,2,4]
it should return 1

Given an array = [2,3,4,5]
it should return Not found
"""


def found_occurrence(array: list):
    unique_list = list()
    index = 0
    length = array.__len__() - 1
    while index <= length:
        if array[index] not in unique_list:
            unique_list.append(array[index])
        else:
            return array[index]
        index += 1
    return None


print(found_occurrence([4, 51, 1, 21, 3, 52, 7, 2, 4])) # output 4
print(found_occurrence([2, 1, 1, 2, 3, 5, 1, 2, 4])) # output 1
print(found_occurrence([2, 3, 4, 5])) # output None
print(found_occurrence([0])) # output None
print(found_occurrence([2, 5, 5, 2])) # output 5
