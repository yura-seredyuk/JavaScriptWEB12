import time
import logging
import tracemalloc

import asyncio
from aiohttp import ClientSession, ClientResponseError


async def fetch_url(session, url):
    try:
        async with session.get(url, timeout=15) as response:
            resp = await response.read()
    except ClientResponseError as e:
        logging.warning(e.code)
    except asyncio.TimeoutError:
        logging.warning("Timeout!!!")
    except Exception as e:
        logging.warning(e)
    else:
        return resp
    return

async def fetch_all(loop, ntimes):
    URL = "https://www.google.com/"
    tasks = []
    async with ClientSession() as session:
        for i in range(ntimes):
            task = asyncio.ensure_future(fetch_url(session, URL))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
    return responses

if __name__ == "__main__":

    
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    
    tracemalloc.start()
    print("Current: %d, Peak: %d." % tracemalloc.get_traced_memory())

    
    for ntimes in [1, 10, 100, 500, 1000, 10000]:
        start = time.time()
        loop = asyncio.get_event_loop()
        future = asyncio.ensure_future(fetch_all(loop, ntimes))
        loop.run_until_complete(future)
        responses = future.result()
        logging.info(f"Fetch count {ntimes}, Time: {time.time()-start}")
    print("Current: %d, Peak: %d." % tracemalloc.get_traced_memory())


# Current: 0, Peak: 0.
# 20:44:52: Fetch count 1, Time: 0.238814115524292
# 20:44:54: Fetch count 10, Time: 2.1485793590545654
# 20:45:22: Fetch count 100, Time: 28.657430171966553
# 20:47:31: Fetch count 500, Time: 128.68104481697083
# 20:51:52: Fetch count 1000, Time: 261.29435300827026
# Current: 1 657 166, Peak: 1 796 249.

# Current: 0, Peak: 0.
# 20:54:12: Fetch count 1, Time: 0.5086781978607178
# 20:54:12: Fetch count 10, Time: 0.28859853744506836
# 20:54:14: Fetch count 100, Time: 1.1940011978149414
# 20:54:18: Fetch count 500, Time: 4.733238697052002
# 20:54:27: Fetch count 1000, Time: 8.771993398666382
# Current: 2156420, Peak: 8382371.