from time import time
from random import choice, shuffle


def performance(func):
    def wrap_func(*args, **kw):
        t1 = time()
        result = func(*args, **kw)
        t2 = time()
        print(f"took {t2 - t1}s")
        return result

    return wrap_func


def random_list(lista: list) -> list:
    list_alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    random_letters = []
    for _ in range(1000):
        random_letter = "".join([choice(list_alphabet) for _ in range(6)])
        if random_letter not in random_letters:
            random_letters.append(random_letter)
    lista.extend(random_letters)
    shuffle(lista)
    print(lista)
    return lista


@performance
def find_nemo(lista: list):
    for i in lista:
        if i == 'nemo':
            print(f"found nemo at {lista.index(i)} position")
            break # including break here is good because we dont need to keep looping after we found what we need.


def get_first(lista: list):
    print(str(lista[0]))


def get_2(lista: list):
    print(str(lista[0]))
    print(str(lista[1]))


nemo = ['nemo']
list_random = random_list(nemo)
find_nemo(list_random)
# rind_nemo is O(n) --> Linear time
# in this case, we have a list with 1001 objs, each means that
# the big O is O(1001).
# the graph increases with the number of operations
# https://towardsdatascience.com/big-o-d13a8b1068c8
# O(n) is the most common.

get_first(list_random)
get_2(list_random)
# get_first() is n(1), because no matter how many items
# the list has, will always get the first item
# get2 is O(2). Is predicable and scalable, is constant time
