# io_bound/eloop.py
import asyncio
import time
import aiohttp

async def download_site(session, url):
    async with session.get(url) as response:
        indicator = "J" if "jython" in url else "R"
        print(indicator, sep='', end='', flush=True)

async def download_all_sites(sites):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)

        await asyncio.gather(*tasks, return_exceptions=True)

if __name__ == '__main__':
    sites = [
        "http://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80

    print("Starting downloads")
    start = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(download_all_sites(sites))
    duration = time.time() - start
    print(f"\nDownloaded {len(sites)} sites in {duration} seconds")
