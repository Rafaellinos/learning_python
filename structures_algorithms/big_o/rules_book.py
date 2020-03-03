"""
Rule1 : Think about the worst case possible.
    Example: If we loop through a list to found an item, if the item is in the last
    position, that's the worst case. If the item we need is on the first position,
    for example, that's the best scenario.
"""


def get_item(lista: list):
    for i in lista:  # O(n)
        if i == 'something':  # O(n)
            print("found")  # O(n)
            break


get_item(['asd', 'asdasd', 'asdasda', '123123', 'something'])
# worst case, the item we need is the last one
"""
Rule2: Remove constants.
    Example: In Big O notation, there is no need to use O(n/2 + 3), for example,
    in this case, will be O(n). That's what drop the constants means, remove the
    constants number in the notation, just leave the N, if we had at least one.
    O(2n) -> O(n). Because the line on the graph increases linearly, not matter
    how many numbers is with (n).
"""


def someStuff(items: list):
    print(items[0])  # O(1)

    middle_index = len(items) / 2
    index = 0
    while (index < middle_index):
        print(items[index])
        index += 1

    for i in range(100):  # O(100)
        print('hi')


# O(1 + n/2 + 100) -> dropping the constants -> O(n)

"""
Rule3: Different terms of inputs.
    Example: If the function loop through 2 iterables -> O(a + b).
    In other words, everytime that the function uses for loop, for example,
    to loop though different items, you calculate by adding a letter for each
    loop in each item.
    In nested loops, we use multiplication. O(n * n) -> O(n²)
"""


def compressboxtwice(boxes, boxes2): # in this case, will be O(a + b)
    for b in boxes:
        print(b)
    for b2 in boxes2:
        print(b2)
# in this case, the functions is lopping through 2 different items
# This is not O(n), its O(a + b), a for the first list and b for the second list.

def nested_loop(boxes):
    # 1 = 1, 2, 3, 4, 5
    # 2 = 1, 2, 3, 4, 5
    for i in boxes:
        print(i)
        for x in boxes:
            print(x, end="")
        print("")
# in this case, is nested loop so we use O( a * b)
nested_loop([1, 2, 3, 4, 5])

"""
Rule4: Drop Non Dominants.
    Example: In the calculation of the Big O, drop everything and leave
    just the most important terms, in this case, x² é dominant, because
    its increases more than n + n.
"""
def print_all_numbers(numbers):
    print("these are the numbers:")
    for n in numbers: # O(n)
        print(n)

    print("these are the their sums:")
    for n in numbers: # O(n * n) because nested loop
        for x in numbers:
            print(f"{n + x}")

print_all_numbers([1, 2, 3, 4, 5])
# O(n + n²) -> leave only the dominant -> O(n²)