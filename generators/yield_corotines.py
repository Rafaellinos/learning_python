from coroutine_decorator import coroutine

def corrotina():
    print("start")
    valor = yield
    print(f"received", valor)


# c = corrotina()
# next(c) # could be c.send(None)
# c.send(10)

@coroutine
def média():
    total = 0.0
    contador = 0
    média = None
    while True:
        entrada = yield média # retorna a média
        total += entrada
        contador += 1
        média = total / contador


m = média()
#next(m) # priming, start the corrotine. Since we are using the decorator for priming, we dont need this line
a = m.send(10)
a = m.send(20)

print(a)
