"""
    map loop throught the itarable and calls the function for each item
    
    Also doesn't affect the outside variable, in this case, my_list still 
    the same.

    params: map({function}, {iterable})
    return: map object (iterable)
"""

my_list = [1, 2, 3]


def multiply_by2(item):
    return item * 2


map_obj = map(multiply_by2, my_list)

print(map_obj)  # <map object at 0x7f57561373d0>
# print(tuple(map_obj))
print(list(map_obj))  # [2, 4, 6]

map_string = map(lambda s: str(s).upper(), (1, 'a', 'abc'))
print(list(map_string))  # ['1', 'A', 'ABC']
