"""
    zip({itarables})
    params: iterables itens
    return: zip object (itarable)

    Zip the itarables together
"""
my_list = [1,2,3]
your_list = (4,5,6)
their_list = {7,8,9}

zipped = zip(my_list, your_list, their_list)
print(list(zipped)) # [(1, 4, 8), (2, 5, 9), (3, 6, 7)]