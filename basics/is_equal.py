print(True is True)
print('1' is '1')
print([] is [])
print(10 is 10)

"""
    Is, unlike the ==, compare the memory place.
"""
a = '12'
b = '12'
print(id(a))
print(id(b))
# same output
c = [1,2,3]
d = [1,2,3]
print(id(c))
print(id(d))
print(c is d) # false, diference memory places
print(c == d) # equally the same
# list have a different space memory because they are data structure