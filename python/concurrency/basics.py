import requests
import time
import threading
import concurrent.futures
import aiohttp
import asyncio

# sources novig 21 dys, colin scott interactivae latency
# gil realpython
# subinterpreters
# syncio real python 
# SO how does aysncio actually works + daslk + celery

thread_local = threading.local()

def get_session():
    if mode == "sync":
        return requests.Session()
    elif mode == "threads":
        if not hasattr(thread_local, "session"):
            thread_local.session = requests.Session()
        return thread_local.session
    else:
        raise TypeError("wrong execution mode")

def download_one(url):
    session = get_session()
    with session.get(url, verify=False) as response:
        indicator = "J" if "jython" in url else "R"
        print(indicator, sep="", end="", flush=True)

async def dl_one(session, url):
    async with session.get(url) as response:
        indicator = "J" if "jython" in url else "R"
        print(indicator, sep="", end="", flush=True) 

async def dl_all(urls):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        tasks = []
        for url in urls:
            task = asyncio.ensure_future(dl_one(session, url))
            tasks.append(task)

        await asyncio.gather(*tasks, return_exceptions=False)

def download_all(urls):
    if mode == "sync":
        for url in urls:
            download_one(url)
        print()
    elif mode == "threads":
        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            executor.map(download_one, urls)
    else:
        raise TypeError("wrong execution mode") 

if __name__ == "__main__":
    urls = [
        "http://www.jython.org",
        "http://olympus.realpython.org/dice"
    ] * 50
    mode="async"
    start = time.time()
    if mode=="async":
        loop = asyncio.get_event_loop()
        loop.run_until_complete(dl_all(urls))
    else:
        download_all(urls)
    duration = time.time() - start
    print(f"DLed {len(urls)} pages in {duration} secs")