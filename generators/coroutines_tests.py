


def coroutine_test(bla):
    print(bla)
    while True:
        valor = yield bla
        if not bla:
            print('bla is False')
            break
    print(valor)
    return valor # return the value for the exception StopIteration


c = coroutine_test(None)
next(c) # priming
res = c.send(200)
res = c.send(300)
print(res)
c.close()


