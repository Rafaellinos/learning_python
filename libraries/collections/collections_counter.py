import collections


print(collections.Counter([1, 3, 4, 1, 3]))
# out put Counter({1: 2, 3: 2, 4: 1})

list_of_words = 'I\'m SAM'

print(collections.Counter(list_of_words.split()))
# Counter({"I'm": 1, 'SAM': 1}) # work occurency