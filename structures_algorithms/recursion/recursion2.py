"""
fibonachi numbers by using recursion
ex:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

return index
if n == 2
    return 1
if n == 8
    return 21
"""


def fibonachi(n):
    lista = [0,1]
    i = n
    while i > 0:
        lista.append(lista[-1] + lista[-2])
        i -= 1
    return lista[n]

def fibonachi1(n, n1=0, n2=1):
    if n == 0:
        return n1
    tmp = n2
    n2 = n1 + n2
    n1 = tmp
    n -= 1
    return fibonachi1(n,n1,n2)

def fibonachi2(n):
    if n < 2:
        return n
    return fibonachi2(n-1) + fibonachi2(n-2)
    


print(fibonachi(10))
print(fibonachi1(10))
print(fibonachi2(10))
    

