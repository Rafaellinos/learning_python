def highest_even(lista=[0]):
    max_num = 0
    for i in lista:
        """
            Becareful when using remove like this.
            With remove, you change its size and cause it to skip elements
        """
        if i % 2 != 0:
            lista.remove(i)
    # lista = [x for x in lista if x % 2 != 0] <- use this.
    print(lista)
    # or just return max(lista)

    for i in lista:
        if i > max_num:
            max_num = i
    return max_num

lista = [1,2023,3,4444,5,6,10,1221,20,51,60111]
lista = highest_even(lista)
print(lista)
