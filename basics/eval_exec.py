"""
execute function inside of strings
"""

exec("print('hello world')")
a = exec("3+4")
print(a)# None

# eval can return a value
b = eval("3+4")
print(b)