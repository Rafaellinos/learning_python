"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Example 1:

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7] 
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

Example 2:

Input: nums = [1,2,3,4,4,3,2,1], n = 4
Output: [1,4,2,3,3,2,4,1]

Example 3:

Input: nums = [1,1,2,2], n = 2
Output: [1,2,1,2]

"""


# def shuffle(nums, n):
#     nums1 = nums[:n+1]
#     nums2 = nums[n:]
#     new_list = []
#     for n1, n2 in zip(nums1, nums2):
#         new_list.append(n1)
#         new_list.append(n2)
#     return new_list

def shuffle(nums, n):
    return [n1 if n1 % 2 == 0 else n2 for n1, n2 in zip(nums[:n+1], nums[n:])]

# def shuffle(nums, n):
#     t = len(nums) / 2
#     c = 0
#     result = []
#     while c < t:
#         result.append(nums[c])
#         result.append(nums[c+n])
#         c += 1
#     return result


print(shuffle(nums=[1, 2, 3, 4, 4, 3, 2, 1], n=3))
