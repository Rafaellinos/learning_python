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
if __name__ == '__main__':
    asyncio.run(main())

# await keyword avoids block because it suspends the current coroutine object
# await keyword WORKS WITH AWAITABLES
