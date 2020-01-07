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

my_list = [1,2,3,4,5]
num = 0
total = 0
for i in my_list:
    num +=1
    total += i
print(str(num)+'\n'+str(total))