from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,6,7,7]
print(Counter(li))
# out put Counter({7: 2, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1})
# its counts how may times an item appears
setence = 'bla bla bla thinking about python'
print(Counter(setence))

dict_1 = defaultdict(lambda: 5, {
    'a':1,
    'b':2
})
# defaultdict gives a calleble object to return if the key doesn't exist
print(dict_1['c'])

d = OrderedDict()
d['a'] = 1
d['b'] = 2

d2 = OrderedDict()
d2['b'] = 2
d2['a'] = 1

print(d2 == d)
"""
 OrderedDict keeps the order that the objects was stored.
 In this case, d2 is not equal to d, even though has the same items.
 By using a commom dict, the answer will be true, because they dont store
 the order.
"""
