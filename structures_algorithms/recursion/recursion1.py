"""
factorial using recursion

5! = 5*4*3*2*1

recrusion - stop
          - recursion - stop
                      - recursion ...
"""

def find_factoryal(fact, value=1):
    value = fact * value
    if fact <=1:
        return value
    return find_factoryal(fact-1,value)

def find_factoryal_loop(fact):
    fact2 = fact - 1
    fact = fact * fact2
    while fact2 > 1:
        fact2 -= 1
        fact = fact * fact2
    return fact



print(find_factoryal_loop(5))
print(find_factoryal(5))