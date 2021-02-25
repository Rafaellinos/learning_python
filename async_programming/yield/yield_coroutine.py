
def média():
    total = 0.0
    contador = 0
    média = None
    while True:
        entrada = yield média # Trava aqui até receber o valor, precisa ser none
        total += entrada
        contador += 1
        média = total/contador


coro = média()
next(coro)  # preparação, ou priming

coro.send(10)  # 10.0
coro.send(20)  # 15.0

# vai fazendo a média enquanto envia valores