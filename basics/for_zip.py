lista1 = ['A','B','C']
lista2 = lista1[:]
lista3 = ['1','2','3']
for lista1_item, lista2_item, lista3_item in zip(lista1, lista2, lista3):
    print(f"{lista1_item} : {lista2_item} : {lista3_item}")