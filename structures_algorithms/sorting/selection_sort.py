
def selection_sort(arr):
    new_array = []
    next_index = 0
    n = len(arr)
    for x in range(n):
        for i in range(0, n-x-1):
            if arr[x] > arr[i+x]:
                arr[x] = arr[i+x]
    return arr




lista = [8,3,1,5,4,6,9,2,7]

print(selection_sort(lista))