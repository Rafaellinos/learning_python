import asyncio
from urllib.parse import urljoin
from aiohttp import ClientSession
from requests import get



base_url = 'https://pokeapi.co/api/v2/'
pokemons = get(urljoin(base_url, 'pokemon/?limit=10')).json()['results']


async def fetch(session, url):
    async with session.get(url) as response:
        result = await response.json()
        print(result['sprites'])
        return result


async def main():
    async with ClientSession() as session:
        for pokemon in pokemons:
            url = pokemon['url']
            name = pokemon['name']
            print(name, url)
            result = await fetch(session, url)
            return result

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
