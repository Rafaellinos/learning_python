from coroutine_decorator import coroutine


@coroutine
def print_(string_fmt: str):
    while True:
        values = yield
        print(string_fmt.format(*values))


@coroutine
def media(printer: coroutine):
    total = 0.0
    contador = 0
    while True:
        entrada = yield
        total += entrada
        contador += 1
        printer.send((total, contador, total / contador))


formater = print_("Total: {}, Contador: {}, Média: {}")
m = media(formater)
m.send(10)
m.send(20)
m.send(30)
