import pdb

def add(num1, num2):
    pdb.set_trace()
    return num1 + num2

"""
> /home/rafael/Documents/gits/learning_python/libraries/pdb_debugger/pdb_test.py(5)add()
-> return num1 + num2
(Pdb) num1
4
(Pdb) num2
'hasddas'
(Pdb) help
"""
"""
commands:
w -> current line

a -> all arguments

can type an variable name

help -> show commands

next -> goes to the next step

continue -> continue the code running

"""


add(4, 'hasddas')