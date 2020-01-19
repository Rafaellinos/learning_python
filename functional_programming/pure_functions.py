"""
    Based on pure functions. 
    Rule 1: Always return the same output with an input
    Rule 2: Do not produce side effects on outside (Ex: print, touch a global variable)
"""

def multiply_by2(li=[]): 
    return [i*2 for i in li]

print(multiply_by2([1,2,3]))
