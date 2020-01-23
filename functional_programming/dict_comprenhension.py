

my_dict = {
    'a': 2,
    'b': 4,
    'c': 5
}

my_dict1 = {k:v**2 for k,v in my_dict.items() if v%2==0}
print(my_dict1) # out {'a': 4, 'b': 16}

my_dict2 = {n:n**2 for n in [1,2,3]} #create a dict with key == n and value == n*2
print(my_dict2) # out {1: 1, 2: 4, 3: 9}
