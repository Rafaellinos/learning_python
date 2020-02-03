import re

string = 'this search inside of this text please!'

pattern = re.compile('this')

# return none if no matching
# a = re.search('this', string) # <re.Match object; span=(17, 21), match='this'>
a = pattern.search(string)
b = pattern.findall(string) 
c = pattern.fullmatch(string) # return only if matchs the full string
d = pattern.match(string) # matchs the string
print(b) # ['this', 'this']
print(c)
if a:
    print(a.span())
    print(a.start())
    print(a.end())
    print(a.group()) # for multiple searchs
