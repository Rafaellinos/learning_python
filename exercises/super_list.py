"""
    create a superlist class that works as a list
    but it has to return a thousand when do len(), no matter what.
"""

class SuperList(list): 
    # inheriting the list its possible to use the list methods
    def __len__(self):
        return 1000
        

superlist1 = SuperList()
superlist1.append(1)
superlist1.append(5)
print(superlist1[1])
print(len(superlist1))

print(isinstance(superlist1, list))
print(issubclass(SuperList, list))
print(issubclass(SuperList, object))