"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""


def check_sum(array: list, target: int):
    index = 0
    length = array.__len__() - 1

    missing_for_target = dict()

    while index <= length:
        if array[index] < target:
            sum_ = target - array[index]
            if sum_ in missing_for_target.keys():
                return [missing_for_target[sum_], index]
            else:
                missing_for_target[array[index]] = index
        index += 1
    return []


target = 0
array = [0, 4, 3, 0]  # target = 9

print(check_sum(array, target))
