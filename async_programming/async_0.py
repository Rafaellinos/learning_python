"""
Diferença entre Paralelismo e concorrência:

ConcorrênciaFazer: coisas e parar pra fazer outra ou seja, fazer pedaços de
 uma tarefa e depois voltar.

Paralelismo:


Corrotinas: Funções Assíncronas (async) ex:
    import asyncio

    async def ping_server(ip):
        pass

    @asyncio.coroutine
    def ping_server(ip):
        pass
"""
from asyncio import get_event_loop, coroutine


# ipython -i file.py
# @coroutine #<- deprecated since python 3.8, use async def
async def print_async(msg: str) -> None:
    print(f'Async: {msg}')


loop = get_event_loop()
loop.run_until_complete(print_async('oi'))
loop.close()
