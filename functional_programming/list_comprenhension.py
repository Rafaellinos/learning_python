my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)
print([x for x in 'hello'])
print([n*2 for n in range(0,100)])
print([n**2 for n in range(0,100) if n % 2 == 0])