import re

# https://www.w3schools.com/python/python_regex.asp
pattern = re.compile(r"([a-zA-Z]).([a])")

"""
([a-zA-Z]).([a])

([a-zA-Z]) = matchs any letter a~z upper or lower case
. = matchs any character
([a]) = matchs a


"""

string = 'Rafael Veloso'
a = pattern.search(string)
print(a)
print(a.group(0))
print(a.group(1))
print(a.group(2))

"""

output:
afa
a
a

because 
([a-zA-Z]) found 'a'
. found '.'
'a' found 'a'

"""