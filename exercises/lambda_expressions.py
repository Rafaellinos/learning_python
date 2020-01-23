"""
exercise:
1. Create a lambda that prints the squared number on list

2. a = [(0,2),(4,3),(9,9),(10,-1)] sort the list based on the second number on the tuple
"""

print(list(map(lambda n: n**2, [5,4,3])))

a = [(0,2),(4,3),(9,9),(10,-1)]

a.sort(key=lambda e: e[1])
print(a)
