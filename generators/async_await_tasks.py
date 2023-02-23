from time import sleep, time
import asyncio


async def main():
    print("started")
    task = asyncio.create_task(foo("1123"))
    print(task)
    #await task
    await asyncio.sleep(3)
    print("finished")


async def foo(text):
    await asyncio.sleep(2)
    print(text)




if __name__ == '__main__':
    # create the event loop and starts the whole thing
    s = time()
    asyncio.run(main())
    sleep(5)
    e = time()
    print(f"total time: {e - s}")


## futures in python is equal to promises in js