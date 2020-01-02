"""
    dict is a data structure. It looks like a json, with key and value.
    Dicts unlike of lists, has no way to order the items and has no index. 
"""
dict1 = {
    'a': [0,1,2],
    'b': 'Hello',
    'c': True
}
print(dict1)
dict2 = { 
    #dict keys must be immutable
    #keys must be unique, so if has 2 items with the same key, will be overwritten
    123: [1,2,3],
    123: 'key2',
    True: 'hello',
    'hi': 'nice',
    (1,2): 'Tuples are immutable'
}
print(dict2)
dict3 = dict(name='JohnJohn')
print(dict3)
print(dict1['b'])
print(dict2[123])
print(dict3['name'])

#get method dont give error if the item is not there, istead, return None
#or returns a default value.
print(dict2.get('hi','error')) 

#search for element in dict, returns True if found and False otherwise
print(123 in dict2.keys()) #seach for keys

print('key2' in dict2.values()) #seach for values

print((123, 'key2') in dict2.items()) #seach for the whole "line", with key and value on tuple

dict4 = dict3.copy() #copy a dict
dict3.clear() #clear the dict

print(dict2.pop(123)) #remove the item and returns his value

print(dict4)
dict4.update({'name': 'Rafael'}) #update an item
dict4.update({'age': 23})
print(dict4)

for key, value in dict4.items(): 
    # dict.items() is a list of tuples with key and value
    print(f"{key}:{value}")

for item in dict4.items():
    print(str(item))