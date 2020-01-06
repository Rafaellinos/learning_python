lista = [1,2,3,4]
lista.append(5)
lista2 = lista
print(lista2)
# If I try to copy the last on that way (lista2 = lista),
# any changes that I made on lista2 goes to lista aswell, because
# they are pointing to the same place in memory.
# the right way to copy a list, is lista2 = lista[:], or lista2 = lista.copy()

lista2.insert(1, 500) # insert a value on index
print(lista2)

lista2.extend(lista) #extends a list to a existing one
print(lista2)

removed_item = lista2.pop(1) #if no index given, remove the last item, also returns whatever u've removed.
print(removed_item)
print(lista2)
lista2.remove(500) #remove the first item found on parameter
print(lista2)
print(lista2.index(2)) # returns the index of the given value

print(2 in lista2) # returns True if found the item, if not, False

print(lista.count(2)) # count how much times the item appears on the list

lista2.sort() # organize the list. sorted(lista2) does the same thing, but without modify
print(lista2)

lista2.reverse() #revert the index, or can be lista[::-1] without modify the list
print(lista2)

lista2.clear() # clears the list. New in version 3.3
print(lista2)
print(lista)

print(list(range(100))) # add 0 to 99 in a list

test = " "
print(test.join(['hi','my','name','is','rafael'])) # joins each item on the list

list_unpacking = ['a','b','c','d','e','f']
a, b, c, *other, f = list_unpacking # *other unpack the rest of the items
print(type(other))
print(f"{a},{b},{c} and {other}, {f}")

#remove duplicates
list2 = [1,2,3,4,5,5]
list3 = []
for item in list2:
    if not item in list3:
        list3.append(item)
print(list2)
print(list3)
# OR can use set
print(set(list2))
list4 = list(set(list2))
print(list4)