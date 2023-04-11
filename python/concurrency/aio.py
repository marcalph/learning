import asyncio
from random import randint
import time
import json
import aiohttp

# odd number generator
def odds(start, stop):
    for odd in range(start, stop +1, 2):
        yield odd


async def randn():
    await asyncio.sleep(3)
    return randint(1, 100)

async def sq_odds(start, stop):
    for odd in odds(start, stop):
        await asyncio.sleep(2)
        yield odd**2

async def simple():
    odd_values = [odd for odd in odds(3,15)]
    print(odd_values)
    
    start = time.perf_counter()
    r = await randn()
    elapsed = time.perf_counter() - start
    print(f"{r} took {elapsed} secs")

    start = time.perf_counter()
    r = await asyncio.gather(*(randn() for _ in range(10)))
    elapsed = time.perf_counter() - start
    print(f"{r} took {elapsed} secs")

    start = time.perf_counter()
    async for so in sq_odds(11, 17):
        print(f"so: {so}")
    elapsed = time.perf_counter() - start
    print(f"{r} took {elapsed} secs")


async def worker(name, num, sess):
    print(f"worker-{name}")
    url: str = f"http://qrng.anu.edu.au/API/jsonI.php?length={num}&type=uint16"
    response = await sess.request(method="GET", url=url)
    value = await response.text()
    print(value)
    value = json.loads(value)
    print(value["data"])
    return sum(value["data"])
    

async def main():
    async with aiohttp.ClientSession() as session:
        sums = await asyncio.gather(*(worker(f"w{i}", n, session) for i, n in enumerate(range(2, 10))))
        print(f"response is {sums}")

if __name__ == "__main__":
    mode = ""
    if mode == "simple":
        asyncio.run(simple())
    else:
        start = time.perf_counter()
        asyncio.run(main())
        elapsed = time.perf_counter() -start
        print(f"executed in {elapsed:0.2f} seconds")