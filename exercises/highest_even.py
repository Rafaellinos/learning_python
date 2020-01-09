def highest_even(lista=[0]):
    max_num = 0
    for i in lista:
        if i % 2 != 0:
            lista.remove(i)
    # or just return max(lista)
    for i in lista:
        if i > max_num:
            max_num = i
    return max_num


print(highest_even([1,2,3,4,5,6,10,11,20,51,60]))
print(highest_even())
            