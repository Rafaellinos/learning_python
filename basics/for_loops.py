for item in (1,2,3,4):
    for x in ['a','b','c']:
        print(item, x)
"""
    output: 1 a, 1 b, 1 c, 2 a, 2 b, ...
    This happens because when starts at 1 on the tuple and then, goes to
    the list, it stays on the list until he ends and then continues to 2,3 etc.
"""
for i in 'Test': 
    # iterable is a collection of items that can be iterable, 
    # like lists, tuples, dicts, objects etc
    print(i)
users = {
    'name': 'Rafael',
    'age': 30,
    'can_wsim': False
}
for item in users.items():
    print(item) #item returns a tuble with key and value
for item in users.keys():
    print(item) #returns the keys
for item in users.values():
    print(item)# returns the values
for key, value in users.items():
    print(key, value) #used to get both key and value

for _ in range(0, 10, 2):
    # first, the starting point, second the ending point
    # third jumps, default is 1. On this case is jumping 2
    print(_)

for i in range(2):
    print(list(range(10)))
    #output is 2 lists with 0 to 9.

for i, char in enumerate('HEllooooooooooo'):
    # returns a index(i) and the element on the iterable object
    print(f"{i}:{char},,",end="")
print("")
