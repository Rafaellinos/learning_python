"""
    filter({function}, {iterable})
    return: filter object (iterable)

    If the function returns true, add the item on iterable in a filter obj
    if not, ignore

"""

my_list = [1,2,3]

def only_odd(item):
    # checks if the item is odd or even
    # returns true if odd and false if even
    return item % 2 != 0

print(list(filter(only_odd, my_list)))

alphabets = ['a','b','c','e','i']

def filter_vowels(alphabet):
    vowels = ['a','e','i','o','u']
    if alphabet in vowels:
        return True
    return False

filtered_voewls = filter(filter_vowels, alphabets) # add only the item that the function return True
print(filtered_voewls)
print(list(filtered_voewls))