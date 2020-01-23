"""
almost the same as list comprenhesion
but remember that sets remove any duplicates values
"""

print({x for x in 'hello'})
print({n*2 for n in range(0,100)})
print({n**2 for n in range(0,100) if n % 2 == 0})