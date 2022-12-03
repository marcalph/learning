import asyncio
import time

async def test(i):
    await asyncio.sleep(i)
    print('test')

async def three_awaits():
    tac = time.monotonic()
    await test(2)
    await test(2)
    await test(2)
    tic = time.monotonic()
    print(f"ran in {tic-tac}")

async def tasks_three_awaits():
    tac = time.monotonic() 
    t0 =  asyncio.create_task(test(2))
    t1 =  asyncio.create_task(test(2))
    t2 =  asyncio.create_task(test(2))
    await t0
    await t1
    await t2
    tic = time.monotonic()
    print(f"ran in {tic-tac}")


async def gather_three_awaits():
    tac = time.monotonic() 
    await asyncio.gather(test(2), test(2), test(2))
    tic = time.monotonic()
    print(f"ran in {tic-tac}")



asyncio.run(three_awaits())
asyncio.run(tasks_three_awaits())
asyncio.run(gather_three_awaits())

