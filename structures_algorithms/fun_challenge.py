
def fun_challenge(input):
    a = 10 # O(1)
    a = 50 + 3 # O(1)

    for i in range(len(input)): # O(n)
        # anotherfunc() # O(n)
        stranger = True # O(n)
        a += 1 # O(n)

    return a # O(1)

fun_challenge([1,2])

# calculation :
# 3 + n + n + n + n
# 3 O(1) and 4 O(n)
# result = O(3 + 4n) same thing as O(n)

def another_challeng(input):
    a = 5 # O(1)
    b = 10 # O(1)
    c = 50 # O(1)
    for i in range(len(input)): # O(n)
        x = i + 1 # O(n)
        y = i + 2 # O(n)
        z = i + 3 # O(n)

    for j in range(len(input)): # O(n)
        p = j * 2 # O(n)
        q = j * 2 # O(n)

    whoAmI = "I dont know" # O(1)

# Calculation:
# O(4 + 7n) same as O(n)

