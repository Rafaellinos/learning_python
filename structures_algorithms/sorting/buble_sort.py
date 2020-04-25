"""
bubble Sort
"""

lista = [8,3,1,5,4,6,9,2,7]

def bubble_sorte(arr):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(bubble_sorte(lista))