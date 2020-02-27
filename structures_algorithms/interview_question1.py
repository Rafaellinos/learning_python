"""
Check each element in array to see if they added is equal to sum number

Ex:
    sum = 8
    array = [1,2,4,4]
    Should return True, because 4+4 == 8

    sum = 8
    array1 = [2,4,5,7]
    Should return False, because any of those numbers added is equal to sum
"""

sum = 8


# naive approach
def check_sum(array):

    for j in range(len(array)):
        for i in range(len(array)):
            if j == i:
                print(j, i)
                continue
            if array[j] + array[i] == sum:
                return True
    return False






print(check_sum([3, 3, 4, 7]))
