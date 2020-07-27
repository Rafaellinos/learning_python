
def selection_sort(arr):
    lenth = len(arr)
    for i in range(lenth):
        menor = arr[i]
        for j in range(i,lenth):
            if  arr[j] < menor:
                menor = arr[j]
        arr.remove(menor)
        arr.insert(i, menor)
    return arr

lista = [8,3,1,5,4,6,9,2,7]

print(selection_sort(lista))