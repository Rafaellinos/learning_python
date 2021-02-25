"""
Found a largest or smallest N item from iterator
"""

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 43, 37, 2]
print(heapq.nlargest(3, nums)) # 3 largest
print(heapq.nsmallest(3, nums)) # 3 smallest

people = [
    {"name": "rafael", "idade": 30},
    {"name": "yasmin", "idade": 22},
    {"name": "matheus", "idade": 23},
    {"name": "luiz", "idade": 54},
    {"name": "robson", "idade": 32},
]

print(heapq.nlargest(2, people, key=lambda d: d["idade"]))

print(heapq.heapify(nums)) # organiza por ordem

# se for apenas um numero, maior ou menor, use min() e max()
