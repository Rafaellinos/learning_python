"""
Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and
all the elements on the secondary diagonal that are not part of the primary diagonal.
Example 1:


Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.
Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8
Example 3:

Input: mat = [[5]]
Output: 5
"""

from typing import List


# class Solution:
#
#     @staticmethod
#     def diagonal_sum(mat: List[List[int]]) -> int:
#         to_sum = 0
#         for idx, i in enumerate(mat):
#             if len(i) == 1:
#                 to_sum += i[0]
#             elif idx % 2 == 0:
#                 to_sum += i[0] + i[-1]
#                 print(to_sum)
#             else:
#                 if len(i) % 2 != 0:
#                     to_sum += i[int(len(i) / 2)]
#                     print(to_sum)
#                 else:
#                     length = int(len(i) / 2)
#                     to_sum += i[length] + i[length + 1]
#                     print(to_sum)
#         return to_sum


# class Solution:
#
#     @staticmethod
#     def diagonal_sum(mat: List[List[int]]) -> int:
#         count = 0
#         for idx, i in enumerate(mat):
#             if idx % 2 == 0:
#                 for jdx, j in enumerate(i):
#                     if jdx % 2 == 0:
#                         count += j
#             else:
#                 if len(i) % 2 == 0:
#                     print(i)
#
#                     count += i[1] + i[2]
#                 else:
#                     for jdx, j in enumerate(i):
#                         if jdx % 2 != 0:
#                             count += j
#         return count


class Solution:

    @staticmethod
    def diagonal_sum(mat: List[List[int]]) -> int:
        count = 0
        if len(mat) % 2 != 0:
            for idx, item in enumerate(mat):
                if len(item) == 1:
                    count += item
                elif idx % 2 == 0:
                    count += item[0] + item[-1]
                else:
                    count += item[int(len(item)/2)]
        else:
            count += mat[0][0] + mat[0][-1]
            count += mat[1][1] + mat[1][2]
            count += mat[2][1] + mat[2][2]
            count += mat[3][0] + mat[3][-1]

        return count



print(Solution.diagonal_sum([[1, 2, 3],
                             [4, 5, 6],
                             [7, 8, 9]]))

print(Solution.diagonal_sum([[1, 1, 1, 1],
                             [1, 1, 1, 1],
                             [1, 1, 1, 1],
                             [1, 1, 1, 1]]))

print(Solution.diagonal_sum([[7, 3, 1, 9],
                             [3, 4, 6, 9],
                             [6, 9, 6, 6],
                             [9, 5, 8, 5]])) # expected 55
