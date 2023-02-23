import asyncio
from typing import Any


async def coroutine_test(bla: Any) -> Any:
    print(bla)
    while True:
        valor = bla
        if not bla:
            print('bla is False')
            break
    print(valor)
    return valor # return the value for the exception StopIteration


async def main() -> None:
    a = coroutine_test(None)
    print(a, type(a))
    a.close()
    print(f"a is closed")

    def classic_coroutine(received):
        while True:
            produced = yield received
            print("received?", produced)
            received += 1
        return received

    t = classic_coroutine(10)
    print(t, type(t))
    t.send(None)
    b = t.send(12.5)
    print(b)
    b = t.send(13.5)
    print(b)


if __name__ == '__main__':
    asyncio.run(main())

# await keyword avoids block because it suspends the current coroutine object
# await keyword WORKS WITH AWAITABLES

# Todo async coroutine precisa rodar dentro de um event-loop.
# Event loop é o core de todas aplicações asyncio, permite ter concorrencia em uma unica thread
# basicamente esperando o OS notificar que determinada operacao foi concluida.
# Isso é util para operações I/O bound (e.g. escrever no hd, esperar retorno na operacao).
# Deleta a task para o SO e enquanto o SO n devolve a resposta, podemos partir pra outra.

# https://www.pythontutorial.net/python-concurrency/python-event-loop/


#    Use asyncio in order to adopt coroutines in your program.
#    Use asyncio in order to use the asynchronous programming paradigm.
#    Use asyncio in order to use non-blocking I/O.

# https://superfastpython.com/python-asyncio/
#A coroutine is a function that can be suspended and resumed.
#  single-threaded event loop.

# await executes the coroutine
# await blocks the current thread