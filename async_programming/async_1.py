from aiohttp import ClientSession
from asyncio import get_event_loop

"""

"""

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()

async def main():
    async with ClientSession() as session:
        html = await fetch(session, 'http://ddg.gg')
        print(html)

loop = get_event_loop()
loop.run_until_complete(main())
