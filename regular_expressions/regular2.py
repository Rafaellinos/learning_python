import re
# email validation
# regex 101
pattern = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

string = 'rafael.veloso.lino@hotmail.com'

a = pattern.search(string)
print(a)

"""
exercise.
At least 8 char long
contain any sort letters, numbers and special characters
"""

pattern2 = re.compile(r"(?=.{8,})(?=.*[a-zA-Z])(?=.*\d)(?=.*\W)")

"""
^(?=.{8,})(?=.*[a-zA-Z])(?=.*\d)(?=.*\W).*$
^ # start of string
(?=.{8,}) # checks if is at least 8 characters
(?=.*[a-zA-Z]) # check if at least one letter upper case or lower case
(?=.*\d) # checks if is at least one digit
(?=.*\W) # checks if at least one special character

.*$ = 
"""

string2 = 'abcdefgfdd1@'

b = pattern2.search(string2)
print(b) # will return None if doesnt match the compile