import re

# https://www.w3schools.com/python/python_regex.asp
pattern = re.compile(r'[a-zA-Z]')

string = 'Rafael Veloso'
a = pattern.search(string)
print(a)